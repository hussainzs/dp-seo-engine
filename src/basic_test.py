import unittest
from data_loader import load_pdf, load_csv, load_url
import os

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

if __name__ == '__main__':
    unittest.main()