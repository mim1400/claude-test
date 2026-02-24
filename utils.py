"""Utility functions for the application."""


def greet(name: str) -> str:
    """Return a greeting string for the given name."""
    return f"Hello, {name}!"


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def is_palindrome(text: str) -> bool:
    """Return True if the given string is a palindrome (case-insensitive)."""
    normalized = text.lower().replace(" ", "")
    return normalized == normalized[::-1]
