from fasthtml.common import *
from monsterui.all import *
from app.utils import load_all_posts, load_post_by_slug, get_all_tags, filter_posts, get_enabled_tags
from app.components import Layout, PostCard, PostContent, AboutContent, ContactForm, NotFoundContent, FilterSection


def setup_routes(app):
    """Setup all application routes"""

    @app.get("/")
    def homepage(category: list[str] = None):
        """Homepage listing all blog posts"""
        all_posts = load_all_posts()
        # Sort by date (newest first)
        all_posts.sort(key=lambda p: p['date'], reverse=True)

        # Normalize categories
        selected_cats = [c.lower() for c in category] if category else []
        if 'all' in selected_cats:
            selected_cats = []

        posts = filter_posts(all_posts, selected_cats)
        all_tags = get_all_tags()
        enabled_tags = get_enabled_tags(all_posts, selected_cats, all_tags)

        return Layout(
            # Hero section
            Div(
                H1("Ivan Dolgushev", cls="text-4xl font-bold mb-3 text-gray-900"),
                P("Software engineer, writer, and technology enthusiast.",
                  cls="text-xl text-gray-600 mb-8"),
                cls="mb-12"
            ),
            
            # Filter Section
            FilterSection(all_tags, selected_cats, list(enabled_tags)),

            # Blog posts section
            Div(
                H2("Recent Posts", cls="text-2xl font-bold mb-6 text-gray-900"),
                Div(
                    *[PostCard(post) for post in posts] if posts else [
                        P("No blog posts yet. Check back soon!", cls="text-gray-600 py-6")
                    ],
                    cls="divide-y divide-gray-200"
                ),
                cls="mb-12"
            ),
            title="Ivan Dolgushev - Personal Blog"
        )

    @app.get("/post/{slug}")
    def post_page(slug: str):
        """Individual blog post page"""
        post = load_post_by_slug(slug)

        if not post:
            return Layout(
                NotFoundContent(),
                title="404 - Not Found"
            ), 404

        return Layout(
            PostContent(post),
            title=f"{post['title']} - My Blog"
        )

    @app.get("/about")
    def about_page():
        """About page"""
        return Layout(
            AboutContent(),
            title="About - My Blog"
        )

    @app.get("/contact")
    def contact_page():
        """Contact page"""
        return Layout(
            ContactForm(),
            title="Contact - My Blog"
        )

    @app.post("/contact/submit")
    async def contact_submit(name: str, email: str, message: str):
        """Handle contact form submission"""
        # In a real application, you would send an email or save to a database here
        return Layout(
            Div(
                H1("Thank You!", cls="text-4xl font-bold mb-4 text-center text-success"),
                P(f"Thanks for reaching out, {name}!", cls="text-center text-lg mb-2"),
                P("Your message has been received. I'll get back to you soon!", cls="text-center text-gray-600 mb-6"),
                Div(
                    A(Button("Back to Home", cls=ButtonT.primary), href="/"),
                    cls="text-center"
                ),
                cls="py-12"
            ),
            title="Message Sent - My Blog"
        )
