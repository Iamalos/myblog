import frontmatter
import markdown
from pathlib import Path
from typing import List, Dict, Optional
from functools import lru_cache
from datetime import datetime

POSTS_DIR = Path(__file__).parent.parent / "posts"


@lru_cache(maxsize=128)
def load_post_by_slug(slug: str) -> Optional[Dict]:
    """
    Load a single post by its slug.
    Cached for performance.

    Args:
        slug: URL-friendly post identifier (e.g., 'first-post')

    Returns:
        Dictionary with post metadata and content, or None if not found
    """
    # Try to find the post file matching the slug
    for post_file in POSTS_DIR.glob("*.md"):
        if slug in post_file.stem:  # Match slug in filename
            post = frontmatter.load(post_file)

            return {
                'slug': slug,
                'title': post.get('title', 'Untitled'),
                'date': post.get('date', datetime.now()),
                'tags': post.get('tags', []),
                'excerpt': post.get('excerpt', ''),
                'content': markdown_to_html(post.content),
                'raw_content': post.content
            }

    return None


def load_all_posts() -> List[Dict]:
    """
    Load all blog posts from the posts directory.

    Returns:
        List of dictionaries containing post metadata
    """
    posts = []

    if not POSTS_DIR.exists():
        return posts

    for post_file in POSTS_DIR.glob("*.md"):
        post = frontmatter.load(post_file)

        # Extract slug from filename
        slug = extract_slug_from_filename(post_file.name)

        posts.append({
            'slug': slug,
            'title': post.get('title', 'Untitled'),
            'date': post.get('date', datetime.now()),
            'tags': post.get('tags', []),
            'excerpt': post.get('excerpt', ''),
            'filename': post_file.name
        })

    return posts


def get_all_tags() -> List[str]:
    """
    Get a list of all unique tags across all posts.
    """
    tags = set()
    posts = load_all_posts()
    for post in posts:
        tags.update(post.get('tags', []))
    
    return sorted(list(tags))


def filter_posts(posts: List[Dict], selected_cats: List[str]) -> List[Dict]:
    """Filter posts by selected categories (AND logic)."""
    if not selected_cats: return posts
    return [p for p in posts if all(cat in p.get('tags', []) for cat in selected_cats)]


def get_enabled_tags(all_posts: List[Dict], selected_cats: List[str], all_tags: List[str]) -> List[str]:
    """
    Calculate which tags should be enabled based on current selection.
    Returns list of enabled tags.
    """
    # If no categories selected, enable all tags that appear in at least one post
    if not selected_cats:
        return [tag for tag in all_tags if any(tag in p.get('tags', []) for p in all_posts)]

    enabled_tags = set()
    for tag in all_tags:
        # Already selected tags are always enabled (for removal)
        if tag in selected_cats:
            enabled_tags.add(tag)
            continue
        
        # Check intersection: (Selected + Tag) -> must have >0 posts
        test_cats = selected_cats + [tag]
        if filter_posts(all_posts, test_cats):
            enabled_tags.add(tag)
            
    return list(enabled_tags)


def markdown_to_html(content: str) -> str:
    """
    Convert markdown content to HTML with extensions.

    Args:
        content: Raw markdown content

    Returns:
        HTML string
    """
    md = markdown.Markdown(extensions=[
        'fenced_code',      # For code blocks
        'codehilite',       # Code syntax highlighting
        'tables',           # Table support
        'toc',              # Table of contents
        'nl2br',            # Newline to <br>
    ])

    return md.convert(content)


def extract_slug_from_filename(filename: str) -> str:
    """
    Extract slug from filename.
    Expected format: YYYY-MM-DD-slug-name.md

    Args:
        filename: Post filename

    Returns:
        Slug string
    """
    stem = Path(filename).stem
    parts = stem.split('-')

    # Skip first 3 parts (year, month, day)
    if len(parts) > 3:
        return '-'.join(parts[3:])

    return stem
