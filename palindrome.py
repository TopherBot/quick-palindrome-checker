#!/usr/bin/env python3
"""quick-palindrome-checker
A tiny CLI tool to determine if a string is a palindrome.

Features:
- Ignores case, whitespace, and punctuation.
- Works with arguments or piped input.
- Zero third‑party dependencies.
"""
import sys
import re

def is_palindrome(s: str) -> bool:
    """Return True if `s` is a palindrome after normalising it.
    Normalisation removes all non‑alphanumeric characters and lower‑cases the result.
    """
    cleaned = re.sub(r"[^A-Za-z0-9]", "", s).lower()
    return cleaned == cleaned[::-1]

def main() -> None:
    # Determine the source of input
    if len(sys.argv) > 1:
        # Join all arguments to allow spaces without quoting
        input_str = " ".join(sys.argv[1:])
        check_and_print(input_str)
    else:
        # Read from stdin line‑by‑line
        try:
            for line in sys.stdin:
                line = line.rstrip('\n')
                if line:
                    check_and_print(line)
        except KeyboardInterrupt:
            pass

def check_and_print(s: str) -> None:
    if is_palindrome(s):
        print(f"✅ \"{s}\" is a palindrome!")
    else:
        print(f"❌ \"{s}\" is NOT a palindrome.")

if __name__ == "__main__":
    main()
