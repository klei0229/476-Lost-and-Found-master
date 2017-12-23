import improv_app
import unittest
import os.path as op
import os

class Test_exstance (unittest.TestCase):
    def setUp(self):
        improv_app.app.config['TESTING'] = True
        self.app = improv_app.app.test_client()
        self.dir = os.path.dirname(
                    os.path.abspath(__file__))
    def test_check_application_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'application.py'))
        self.assertTrue(file_exits)

    def test_check_procfile_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'Procfile'))
        self.assertTrue(file_exits)
    def test_check_gitignore_file(self):
        file_exits = op.exists(op.join(self.dir,
                          '.gitignore'))
        self.assertTrue(file_exits)
    def test_check_readme_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'README.MD'))
        self.assertTrue(file_exits)
    def test_check_requirements_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'requirements.txt'))
        self.assertTrue(file_exits)
    def test_check_test_home_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'test_home.py'))
        self.assertTrue(file_exits)
    def test_check_improve_app_init_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'improv_app',
                          '__init__.py'))
        self.assertTrue(file_exits)

    def test_check_improve_app_chatroom_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'improv_app',
                          'chatroom_manager.py'))
        self.assertTrue(file_exits)
    def test_check_improve_app_forms_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'improv_app',
                          'forms.py'))
        self.assertTrue(file_exits)
    def test_check_improve_app_models_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'improv_app',
                          'models.py'))
        self.assertTrue(file_exits)
    def test_check_improve_app_route_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'improv_app',
                          'routes.py'))
        self.assertTrue(file_exits)
    def test_check_improve_app_test_routes_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'improv_app',
                          'test_routes.py'))
        self.assertTrue(file_exits)

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
