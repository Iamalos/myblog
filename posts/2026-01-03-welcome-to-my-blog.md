---
title: "Welcome to My Blog"
date: 2026-01-03
excerpt: "This is my first blog post using FastHTML and MonsterUI. Learn about why I chose these technologies and what to expect from this blog."
---

# Welcome to My Blog

This is my **first blog post** built with FastHTML and MonsterUI!

## Why FastHTML?

FastHTML is an amazing Python framework that lets you build web applications with:

- Pure Python (no separate template language)
- HTMX for dynamic interactions
- Fast development workflow
- Clean, readable code

## Code Example

Here's a simple FastHTML route:

```python
@app.get("/hello/{name}")
def hello(name: str):
    return Div(
        H1(f"Hello, {name}!"),
        P("Welcome to my blog")
    )
```

## What's Next?

Stay tuned for more posts about:

1. Python programming tips
2. Web development best practices
3. FastHTML tutorials
4. Personal projects and experiments

Thanks for reading!
