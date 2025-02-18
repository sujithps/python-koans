#!/usr/bin/env python3

import unittest
import sys
import os


# ANSI color codes
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class ColoredTestRunner(unittest.TextTestRunner):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self, test):
        result = _ColoredTestResult(self.stream, self.descriptions, self.verbosity)
        test(result)
        result.printErrors()
        return result


class _ColoredTestResult(unittest.TestResult):
    def __init__(self, stream, descriptions, verbosity):
        super().__init__(stream, descriptions, verbosity)
        self.stream = stream
        self.verbosity = verbosity
        self.successes = []

    def startTest(self, test):
        self.stream.write(f"{Colors.BLUE}Running: {test}{Colors.ENDC}\n")
        super().startTest(test)

    def addSuccess(self, test):
        super().addSuccess(test)
        self.successes.append(test)
        self.stream.write(f"{Colors.GREEN}✓ OK: {test}{Colors.ENDC}\n")

    def addError(self, test, err):
        super().addError(test, err)
        self.stream.write(f"{Colors.RED}✗ ERROR: {test}{Colors.ENDC}\n")
        self.stream.write(f"{Colors.RED}{self._exc_info_to_string(err, test)}{Colors.ENDC}\n")

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.stream.write(f"{Colors.RED}✗ FAIL: {test}{Colors.ENDC}\n")
        self.stream.write(f"{Colors.RED}{self._exc_info_to_string(err, test)}{Colors.ENDC}\n")

    def addSkip(self, test, reason):
        super().addSkip(test, reason)
        self.stream.write(f"{Colors.YELLOW}⚠ SKIP: {test} ({reason}){Colors.ENDC}\n")


def run_colored_tests(test_file):
    # Load tests from file
    loader = unittest.TestLoader()
    tests = loader.discover(start_dir=os.path.dirname(test_file),
                            pattern=os.path.basename(test_file))

    # Run with colored output
    runner = ColoredTestRunner(verbosity=2)
    result = runner.run(tests)

    # Print summary
    print("\n" + "=" * 70)
    print(f"{Colors.BOLD}Test Summary:{Colors.ENDC}")
    print(f"{Colors.GREEN}Passed: {len(result.successes)}{Colors.ENDC}")
    print(f"{Colors.RED}Failed: {len(result.failures)}{Colors.ENDC}")
    print(f"{Colors.RED}Errors: {len(result.errors)}{Colors.ENDC}")
    print(f"{Colors.YELLOW}Skipped: {len(result.skipped)}{Colors.ENDC}")

    return len(result.failures) + len(result.errors) == 0


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f"{Colors.RED}Please provide a test file name{Colors.ENDC}")
        sys.exit(1)

    success = run_colored_tests(sys.argv[1])
    sys.exit(0 if success else 1)