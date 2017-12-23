from flask.ext.testing import TestCase
from . import app
# use the flask testing build to test on each route
class MyTest(TestCase):
    def create_app(self):
        return app

class improv_test(MyTest):
    # check for route home => using index html
    def test_home_page(self):
        self.client.get('/')
        self.assert_template_used('index.html')
    # check for route signup => using signup html
    def test_signup_page(self):
        self.client.get('/signup')
        self.assert_template_used('signup.html')
    # check for route create => using create page html
    def test_create_page(self):
        self.client.get('/create')
        self.assert_template_used('create_page.html')
    # check for seach => using search html
    def test_search_page(self):
        self.client.get('/search')
        self.assert_template_used('search.html')
    # check for chatroom => chatroom  html
    def test_chat_page(self):
        self.client.get('/chatroom')
        self.assert_template_used('chatroom.html')
    # check for video page => chatroomvideo html
    def test_video_page(self):
        self.client.get('/chatroom_video')
        self.assert_template_used('chatroomvideo.html')
    # check for test page = > yuhao_test html
    def test_test_page(self):
        self.client.get('/yuhao_test')
        self.assert_template_used('yuhao_test.html')
    # check for about page => about us html.
    def test_about_page(self):
        self.client.get('/aboutus')
        self.assert_template_used('aboutus.html')
