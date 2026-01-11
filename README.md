# My Personal Blog

A modern personal blog built with FastHTML and MonsterUI (Tailwind CSS + DaisyUI).

## Features

- Homepage with blog post listings
- Individual post pages with full content
- Markdown support with frontmatter metadata
- About and Contact pages
- Responsive design with MonsterUI
- No database required - posts stored as Markdown files

## Tech Stack

- **FastHTML**: Python web framework
- **MonsterUI**: Tailwind CSS + DaisyUI components
- **Markdown**: For writing blog posts
- **Python Frontmatter**: Parse YAML metadata from posts

## Getting Started

### Prerequisites

- Python 3.12 or higher
- pip (Python package manager)

### Installation

1. Clone or navigate to this repository:
```bash
cd /Users/ivandolgushev/nbs/myblog
```

2. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
# Or on Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Blog

Start the development server:

```bash
python -m app.main
```

Or with uvicorn directly:

```bash
uvicorn app.main:app --reload --port 8000
```

The blog will be available at: http://localhost:8000

## Project Structure

```
myblog/
├── app/
│   ├── __init__.py         # Package marker
│   ├── main.py             # Application entry point
│   ├── routes.py           # Route handlers
│   ├── components.py       # Reusable UI components
│   └── utils.py            # Utility functions
├── posts/
│   └── *.md                # Blog posts (Markdown files)
├── static/
│   ├── css/
│   │   └── custom.css      # Custom styles
│   └── images/             # Blog images
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Writing Blog Posts

Create a new Markdown file in the `posts/` directory with this naming convention:

```
YYYY-MM-DD-slug-name.md
```

### Post Format

```markdown
---
title: "Your Post Title"
date: 2026-01-03
excerpt: "A brief description of your post for the homepage preview"
---

# Your Post Content

Write your post content here using **Markdown** syntax.

## Subheadings

- Lists
- Code blocks
- Tables
- And more!
```

### Example

See the sample posts in the `posts/` directory:
- `2026-01-03-welcome-to-my-blog.md`
- `2026-01-05-python-decorators-explained.md`
- `2026-01-08-building-with-fasthtml.md`

## Available Pages

- `/` - Homepage with all blog posts
- `/post/{slug}` - Individual blog post
- `/about` - About page
- `/contact` - Contact form

## Customization

### Styling

Edit `static/css/custom.css` to customize the appearance.

The blog uses:
- Tailwind CSS for utility classes
- DaisyUI for component styling
- Custom prose styles for blog content

### Components

Modify `app/components.py` to customize:
- `Layout()` - Page layout, navigation, footer
- `PostCard()` - Blog post preview cards
- `PostContent()` - Full post rendering
- `AboutContent()` - About page content
- `ContactForm()` - Contact form

### Routes

Add or modify routes in `app/routes.py` to create new pages or functionality.

## Development

The application uses hot-reload, so changes to Python files will automatically restart the server.

To add new features:
1. Edit the relevant files in `app/`
2. Save your changes
3. The server will automatically reload
4. Refresh your browser

## Production Deployment

For production deployment, consider:

1. Using a production ASGI server (Gunicorn with uvicorn workers)
2. Setting up a reverse proxy (Nginx or Caddy)
3. Using environment variables for configuration
4. Implementing proper error logging
5. Adding analytics and SEO optimization

## License

MIT License - feel free to use this for your own blog!

## Credits

Built with:
- [FastHTML](https://fastht.ml/) by Answer.AI
- [MonsterUI](https://github.com/AnswerDotAI/MonsterUI) by Answer.AI
- [Tailwind CSS](https://tailwindcss.com/)
- [DaisyUI](https://daisyui.com/)
