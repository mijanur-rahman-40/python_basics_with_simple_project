import unittest
import cap

# inheritene unittest


class TestCap(unittest.TestCase):
    def testOneWord(self):
        text = 'python'
        result = cap.capitalText(text)
        self.assertEqual(result, 'Python')

    def testMultipleWords(self):
        text = 'Multi python'
        result = cap.capitalText(text)
        self.assertEqual(result, 'Multi python')


if __name__ == "__main__":
    unittest.main()
