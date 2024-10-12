import unittest
from data_loader import load_pdf, load_csv, load_url
import os, re

class TestDataLoader(unittest.TestCase):

    def test_load_pdf(self):
        '''
        Test basic functionality of load_pdf function. Checks if it outputs the correct number of documents from the PDF files.
        '''
        
        pdf_list = [
            'files/34_Style.pdf',
            'files/All_Style.pdf',
            'files/DEI_Style.pdf',
            'files/Sports_Style.pdf'
        ]
        pdfs_list = load_pdf(pdf_list)
        self.assertEqual(len(pdfs_list), 89, "Expected 89 documents from PDF files")

    def test_load_csv(self):
        '''
        Test basic functionality of load_csv function. Checks if it outputs the correct number of documents from the CSV file.
        '''

        os.environ['USER_AGENT'] = 'myagent'
        csv_data = load_csv("files/organic_search.csv")
        self.assertEqual(len(csv_data), 1573, "Expected 1573 rows from CSV file")

    def test_load_url(self):
        '''
        Test basic functionality of load_url function. Checks if it outputs the correct number of documents from the URLs.
        '''

        urls = ['https://yoast.com/slug/', 'https://www.webfx.com/seo/learn/email-marketing-tips-to-improve-seo/']
        docs_list = load_url(urls)
        self.assertEqual(len(docs_list), 2, "Expected 2 documents from URLs")

# test the regex pattern for tag cleaning
class TestRegexPattern(unittest.TestCase):

    def setUp(self):
        self.pattern = re.compile(r'\d+[/-]\d+|\d+\.\d+')
        self.true_strings = ['12.5.2013', '3.28.2012', '4-16-15', '04-21-2', '10/15/2014', '02-25-', '02/25/16']
        self.false_strings = ['34st-Ego', 'top 10']

    def test_true_strings(self):
        for string in self.true_strings:
            with self.subTest(string=string):
                self.assertIsNotNone(self.pattern.search(string), f"Error: {string} should match the pattern.")

    def test_false_strings(self):
        for string in self.false_strings:
            with self.subTest(string=string):
                self.assertIsNone(self.pattern.search(string), f"Error: {string} should not match the pattern.")


if __name__ == '__main__':
    unittest.main()