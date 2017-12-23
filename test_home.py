import improv_app
import unittest
from bs4 import BeautifulSoup


class TestImprovHome(unittest.TestCase):
    def setUp(self):
        improv_app.app.config['TESTING'] = True
        self.app = improv_app.app.test_client()
        self.response = self.app.get("/")
        self.soup = BeautifulSoup(self.response.data,
                                  'html.parser')
    def test_title(self):
        self.assertEqual("Improv Chatroom",
                         self.soup.title.text)
    def test_h1(self):
        self.assertEqual("Improv Chatroom App",
                         self.soup.h1.text.strip())
    def test_h2(self):
        headings2 = self.soup.find_all('h2')
        self.assertEqual("Threatre Acting",
                         headings2[1].text.strip())
        self.assertEqual("Stand-up Comedy",
                         headings2[0].text.strip())
    def test_h3(self):
        headings3 = self.soup.find_all('h3')
        self.assertEqual("Improv with other collaboratively and interactively, click about us for more information",
                         headings3[0].text.strip())
        self.assertEqual("Work on your Stand up",
                         headings3[1].text.strip())
        self.assertEqual("Perform with others",
                         headings3[2].text.strip())
    def test_h4(self):
        headings3 = self.soup.find_all('h4')
        self.assertEqual("Watch others live and join right now",
                         headings3[0].text.strip())
        self.assertEqual("Create A Session: Create a new room where others can join and perform with you collaboratively",
                         headings3[1].text.strip())
        self.assertEqual("Look Through Old Sessions",
                         headings3[2].text.strip())
        self.assertEqual("Watch Others: Interact with others by watching other user's live session, give feedback and leave comments",
                         headings3[3].text.strip())
        self.assertEqual("Create A Session: Create a new room where others can join and perform with you collaboratively",
                         headings3[4].text.strip())
        self.assertEqual("watch others live right now",
                         headings3[5].text.strip())
        self.assertEqual("Watch Others: Interact with others by watching other user's live session, give feedback and leave comments",
                         headings3[6].text.strip())
        self.assertEqual("Look Thorugh Old Sessions",
                         headings3[7].text.strip())
        self.assertEqual("Browse Archive: Look through past performances that have been archived",
                         headings3[8].text.strip())
    def test_p(self):
        p = self.soup.find_all('p')
        self.assertEqual("Prompts and topics will be randomly provided.",
                         p[0].text.strip())
        self.assertEqual("Prompts and topics will be randomly provided.",
                         p[1].text.strip())
        self.assertEqual("Prompts and topics will be randomly provided.",
                         p[2].text.strip())
        self.assertEqual("About Us",
                         p[3].text.strip())
