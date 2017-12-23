import improv_app
import unittest
import os.path as op
import os
# testing of existance of css files (9)
class Test_exstance_template (unittest.TestCase):
    # we set it up first
    def setUp(self):
        improv_app.app.config['TESTING'] = True
        self.app = improv_app.app.test_client()
        self.dir = os.path.dirname(
                    os.path.abspath(__file__))
    # we check about us css
    def test_check_improve_app_css_aboutus_css_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'improv_app',
                          'static',
                          'css',
                          'aboutus.css'))
        self.assertTrue(file_exits)
    # check chatroom css
    def test_check_improve_app_css_chatroom_css_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'improv_app',
                          'static',
                          'css',
                          'chatroom.css'))
        self.assertTrue(file_exits)
    # check create css
    def test_check_improve_app_css_create_css_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'improv_app',
                          'static',
                          'css',
                          'create.css'))
        self.assertTrue(file_exits)
    # check home css
    def test_check_improve_app_css_home_css_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'improv_app',
                          'static',
                          'css',
                          'home.css'))
        self.assertTrue(file_exits)
    # check layout css
    def test_check_improve_app_css_layout_css_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'improv_app',
                          'static',
                          'css',
                          'layout.css'))
        self.assertTrue(file_exits)
    # check login css
    def test_check_improve_app_css_login_css_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'improv_app',
                          'static',
                          'css',
                          'login.css'))
        self.assertTrue(file_exits)
    # check search page
    def test_check_improve_app_css_search_page_css_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'improv_app',
                          'static',
                          'css',
                          'search_page.css'))
        self.assertTrue(file_exits)
    # check search
    def test_check_improve_app_css_search_css_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'improv_app',
                          'static',
                          'css',
                          'search.css'))
        self.assertTrue(file_exits)
    # check sign up css
    def test_check_improve_app_css_signup_css_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'improv_app',
                          'static',
                          'css',
                          'signup.css'))
        self.assertTrue(file_exits)
