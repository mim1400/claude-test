"""Tests for utils module."""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import greet, add, is_palindrome


def test_greet():
    assert greet("World") == "Hello, World!"
    assert greet("Alice") == "Hello, Alice!"


def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0.5, 0.5) == 1.0


def test_is_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("A man a plan a canal Panama".replace(" ", "")) is True
    assert is_palindrome("hello") is False
