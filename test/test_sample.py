import unittest
from src.main import main
import io
import sys


class TestMain(unittest.TestCase):
    def test_output(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        main()
        sys.stdout = sys.__stdout__
        self.assertEqual(
            captured_output.getvalue().strip(),
            "Hello from the Python Boilerplate Project!",
        )


if __name__ == "__main__":
    unittest.main()
