import unittest
from extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        test = extract_title("# Hello")
        test2 = extract_title("# Whats up   ")
        self.assertEqual(test, "Hello")
        self.assertEqual(test2, "Whats up")

if __name__ == "__main__":
    unittest.main()