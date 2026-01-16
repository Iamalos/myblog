---
title: "Understanding Python Decorators"
date: 2026-01-05
tags: ["engineering", "python"]
excerpt: "A deep dive into Python decorators, how they work, and practical examples for your code. Master this powerful Python feature."
---

# Understanding Python Decorators

Decorators are one of Python's most powerful features. They allow you to modify or enhance functions and classes in a clean, readable way.

## What is a Decorator?

A decorator is a function that takes another function and extends its behavior without explicitly modifying it.

## Basic Example

```python
def my_decorator(func):
    def wrapper():
        print("Something before the function")
        func()
        print("Something after the function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

Output:
```
Something before the function
Hello!
Something after the function
```

## Practical Use Cases

### 1. Timing Functions

```python
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.2f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(2)
    return "Done"
```

### 2. Logging

```python
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper
```

## Key Takeaways

- Decorators are functions that modify other functions
- Use `@decorator_name` syntax for clean code
- They're perfect for cross-cutting concerns like logging, timing, and authentication
- Remember to use `*args` and `**kwargs` for flexible decorators

Happy coding!
