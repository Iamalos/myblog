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
            'excerpt': post.get('excerpt', ''),
            'filename': post_file.name
        })

    return posts


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
