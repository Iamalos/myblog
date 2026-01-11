from fasthtml.common import *
from monsterui.all import *
from datetime import datetime


def Layout(*children, title="My Blog"):
    """
    Main layout component with navigation and footer.
    Clean, minimal design inspired by modern personal blogs.
    """
    return (
        Title(title),
        # Sticky navigation bar
        Div(
            Div(
                A("Ivan Dolgushev", href="/",
                  cls="text-xl font-bold text-gray-900 hover:text-blue-600 transition-all duration-300"),
                Nav(
                    A("Home", href="/",
                      cls="nav-link px-4 py-2 text-gray-700 hover:text-blue-600 hover:scale-110 transition-all duration-300"),
                    A("About", href="/about",
                      cls="nav-link px-4 py-2 text-gray-700 hover:text-blue-600 hover:scale-110 transition-all duration-300"),
                    A("Contact", href="/contact",
                      cls="nav-link px-4 py-2 text-gray-700 hover:text-blue-600 hover:scale-110 transition-all duration-300"),
                    cls="flex gap-2 items-center"
                ),
                cls="flex justify-between items-center py-4 px-6 max-w-4xl mx-auto"
            ),
            cls="sticky top-0 z-50 bg-white/90 backdrop-blur-sm border-b border-gray-200 mb-8"
        ),

        # Main content area
        Container(
            Div(
                *children,
                cls="max-w-4xl mx-auto py-8"
            ),

            # Footer
            Footer(
                P(f"© {datetime.now().year} Ivan Dolgushev. Built with FastHTML & MonsterUI.",
                  cls="text-center text-sm text-gray-500 py-8 mt-16 border-t border-gray-200"),
            ),

            cls="min-h-screen px-4"
        )
    )


def PostCard(post: dict):
    """
    Row-style post preview inspired by modern personal blogs.
    Simple, clean design with title and date.
    """
    date_str = post['date'].strftime('%d %b %Y') if isinstance(post['date'], datetime) else str(post['date'])

    return Div(
        Div(
            A(post['title'], href=f"/post/{post['slug']}",
              cls="text-xl font-medium text-gray-900 hover:text-blue-600 transition-all duration-300 hover:translate-x-1 inline-block"),
            Span(date_str, cls="text-sm text-gray-500 ml-auto"),
            cls="flex items-baseline justify-between gap-4"
        ),
        P(post['excerpt'], cls="text-gray-600 mt-2 text-sm leading-relaxed"),
        cls="py-6 border-b border-gray-200 hover:border-blue-300 transition-all duration-300"
    )


def PostContent(post: dict):
    """
    Full post content component for individual post pages.
    """
    date_str = post['date'].strftime('%B %d, %Y') if isinstance(post['date'], datetime) else str(post['date'])

    return Article(
        Header(
            H1(post['title'], cls="text-5xl font-bold mb-4 text-gray-900"),
            P(date_str, cls="text-gray-500 mb-8"),
            cls="mb-8"
        ),

        # Post content with prose styling
        Div(
            NotStr(post['content']),  # Raw HTML from markdown
            cls="prose prose-lg max-w-none"
        ),

        Footer(
            A("← Back to Home", href="/",
              cls="inline-block px-4 py-2 border-2 border-blue-600 text-blue-600 rounded-lg hover:bg-blue-600 hover:text-white transition-colors mt-12")
        ),

        cls="py-8 bg-white shadow-lg p-8 rounded-lg"
    )


def AboutContent():
    """About page content"""
    return Div(
        H1("About Me", cls="text-4xl font-bold mb-6"),
        Div(
            P("Welcome to my blog! This is where I share my thoughts and experiences.",
              cls="mb-4 text-lg"),
            P("Built with FastHTML and MonsterUI for a modern, responsive experience.",
              cls="mb-4 text-lg"),
            P("I'm passionate about technology, programming, and sharing knowledge with the community.",
              cls="text-lg"),
            cls="prose prose-lg"
        )
    )


def ContactForm():
    """Contact form component with styled form elements"""
    return Div(
        H1("Contact Me", cls="text-4xl font-bold mb-6"),
        Form(
            Div(
                Label("Name", _for="name", cls="block text-sm font-medium text-gray-700 mb-2"),
                Input(name="name", id="name", type="text", required=True,
                      cls="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"),
                cls="mb-4"
            ),
            Div(
                Label("Email", _for="email", cls="block text-sm font-medium text-gray-700 mb-2"),
                Input(name="email", id="email", type="email", required=True,
                      cls="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"),
                cls="mb-4"
            ),
            Div(
                Label("Message", _for="message", cls="block text-sm font-medium text-gray-700 mb-2"),
                Textarea(name="message", id="message", required=True, rows=5,
                        cls="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"),
                cls="mb-4"
            ),
            Button("Send Message", type="submit",
                   cls="px-6 py-3 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 transition-colors"),

            method="post",
            action="/contact/submit",
            cls="max-w-lg bg-white shadow-lg p-8 rounded-lg"
        )
    )


def NotFoundContent():
    """404 page content"""
    return Div(
        H1("404 - Page Not Found", cls="text-4xl font-bold text-center mt-20"),
        P("The page you're looking for doesn't exist.", cls="text-center mt-4 text-lg text-gray-600"),
        Div(
            A("Go Home", href="/",
              cls="inline-block px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors mt-6"),
            cls="text-center"
        )
    )
