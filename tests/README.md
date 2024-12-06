# BSON Fuzzing Tests

This directory contains fuzzing tests for the BSON binary format parser.

## Running Fuzzing Tests

1. Install requirements:
   ```bash
   pip install python-afl
   ```

2. Run the fuzzer:
   ```bash
   py-afl-fuzz -i tests/fuzz/fuzz_inputs -o fuzz_outputs -- python tests/fuzz/fuzz_bson.py
   ```

## Test Structure
- `fuzz_bson.py`: Main fuzzing script
- `fuzz_inputs/`: Directory containing seed inputs
- `fuzz_outputs/`: Directory for AFL output (crashes, hangs, etc.)

## Adding New Tests
Add new seed inputs to `fuzz_inputs/` following these guidelines:
1. Keep files small and focused
2. Cover different BSON types
3. Include edge cases
