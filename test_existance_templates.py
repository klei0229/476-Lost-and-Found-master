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
    def test_check_improve_app_templates_aboutus_html_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'improv_app',
                          'templates',
                          'aboutus.html'))
        self.assertTrue(file_exits)
    def test_check_improve_app_templates_chatroom_html_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'improv_app',
                          'templates',
                          'chatroom.html'))
        self.assertTrue(file_exits)
    def test_check_improve_app_templates_chatroom_video_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'improv_app',
                          'templates',
                          'chatroomvideo.html'))
        self.assertTrue(file_exits)
    def test_check_improve_app_templates_create_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'improv_app',
                          'templates',
                          'create_page.html'))
        self.assertTrue(file_exits)
    def test_check_improve_app_templates_index_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'improv_app',
                          'templates',
                          'index.html'))
        self.assertTrue(file_exits)
    def test_check_improve_app_templates_layout_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'improv_app',
                          'templates',
                          'layout.html'))
        self.assertTrue(file_exits)
    def test_check_improve_app_templates_login_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'improv_app',
                          'templates',
                          'login.html'))
        self.assertTrue(file_exits)
    def test_check_improve_app_templates_search_page_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'improv_app',
                          'templates',
                          'search_page.html'))
        self.assertTrue(file_exits)
    def test_check_improve_app_templates_search_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'improv_app',
                          'templates',
                          'search.html'))
        self.assertTrue(file_exits)
    def test_check_improve_app_templates_session_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'improv_app',
                          'templates',
                          'session.html'))
        self.assertTrue(file_exits)
    def test_check_improve_app_templates_signup_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'improv_app',
                          'templates',
                          'signup.html'))
        self.assertTrue(file_exits)
    def test_check_improve_app_templates_yuhao_test_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'improv_app',
                          'templates',
                          'yuhao_test.html'))
        self.assertTrue(file_exits)
