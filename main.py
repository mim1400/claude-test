"""Main entry point for the application."""

from utils import greet, add, is_palindrome


def main():
    # Greeting
    print(greet("World"))

    # Math utility
    result = add(3, 7)
    print(f"3 + 7 = {result}")

    # String utility
    word = "racecar"
    print(f"Is '{word}' a palindrome? {is_palindrome(word)}")


if __name__ == "__main__":
    main()
