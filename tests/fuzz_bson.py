#!/usr/bin/env python3
"""
Fuzzing script for BSON binary format parsing.
Focuses on security-critical functions:
- Document size validation (_get_object_size)
- Binary data handling (_get_binary)
- String processing (_get_string)
"""

import sys
import os
import afl
from bson import decode, InvalidBSON, InvalidStringData

def fuzz_bson(data):
    """Process potentially malformed BSON data."""
    try:
        decoded = decode(data)
        if isinstance(decoded, dict):
            for key in decoded:
                str(key)
            for value in decoded.values():
                if hasattr(value, 'subtype'):
                    value.subtype
                    bytes(value)
    except (InvalidBSON, InvalidStringData, ValueError, TypeError):
        pass
    except Exception:
        raise

def main():
    """Main fuzzing loop using AFL persistent mode."""
    # Initialize AFL
    afl.init()

    while afl.loop(1000):  # Use persistent mode with 1000 iterations
        try:
            # Read input from stdin (AFL will provide input)
            data = sys.stdin.buffer.read()
            fuzz_bson(data)
        except Exception as e:
            # Only raise exceptions that aren't expected
            raise

if __name__ == "__main__":
    main()
