import improv_app
import unittest
import os.path as op
import os

class Test_exstance_template (unittest.TestCase):
    def setUp(self):
        improv_app.app.config['TESTING'] = True
        self.app = improv_app.app.test_client()
        self.dir = os.path.dirname(
                    os.path.abspath(__file__))
    def test_check_improve_app_css_aboutus_css_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'improv_app',
                          'static',
                          'css',
                          'aboutus.css'))
        self.assertTrue(file_exits)
    def test_check_improve_app_css_chatroom_css_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'improv_app',
                          'static',
                          'css',
                          'chatroom.css'))
        self.assertTrue(file_exits)
    def test_check_improve_app_css_create_css_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'improv_app',
                          'static',
                          'css',
                          'create.css'))
        self.assertTrue(file_exits)
    def test_check_improve_app_css_home_css_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'improv_app',
                          'static',
                          'css',
                          'home.css'))
        self.assertTrue(file_exits)
    def test_check_improve_app_css_layout_css_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'improv_app',
                          'static',
                          'css',
                          'layout.css'))
        self.assertTrue(file_exits)
    def test_check_improve_app_css_login_css_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'improv_app',
                          'static',
                          'css',
                          'login.css'))
        self.assertTrue(file_exits)
    def test_check_improve_app_css_search_page_css_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'improv_app',
                          'static',
                          'css',
                          'search_page.css'))
        self.assertTrue(file_exits)
    def test_check_improve_app_css_search_css_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'improv_app',
                          'static',
                          'css',
                          'search.css'))
        self.assertTrue(file_exits)
    def test_check_improve_app_css_signup_css_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'improv_app',
                          'static',
                          'css',
                          'signup.css'))
        self.assertTrue(file_exits)
