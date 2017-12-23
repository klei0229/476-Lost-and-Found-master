import improv_app
import unittest
import os.path as op
import os
# testing the existance of non-html and css files (14
class Test_exstance (unittest.TestCase):
    # set up
    def setUp(self):
        improv_app.app.config['TESTING'] = True
        self.app = improv_app.app.test_client()
        self.dir = os.path.dirname(
                    os.path.abspath(__file__))
    # test the application
    def test_check_application_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'application.py'))
        self.assertTrue(file_exits)
    # test procfile for heroku
    def test_check_procfile_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'Procfile'))
        self.assertTrue(file_exits)
    # test for .gitignore
    def test_check_gitignore_file(self):
        file_exits = op.exists(op.join(self.dir,
                          '.gitignore'))
        self.assertTrue(file_exits)
    # test for readme
    def test_check_readme_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'README.MD'))
        self.assertTrue(file_exits)
    # test for requirements
    def test_check_requirements_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'requirements.txt'))
        self.assertTrue(file_exits)
    # test for test python of home
    def test_check_test_home_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'test_home.py'))
        self.assertTrue(file_exits)
    def test_check_improve_app_test_html_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'test_existance_templates.py'))
        self.assertTrue(file_exits)
    def test_check_improve_app_test_css_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'test_exsitance_css.py'))
        self.assertTrue(file_exits)

    # outside is done
    # inside of improv_app
    # test for init python
    def test_check_improve_app_init_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'improv_app',
                          '__init__.py'))
        self.assertTrue(file_exits)
    # test for chatroom_manager
    def test_check_improve_app_chatroom_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'improv_app',
                          'chatroom_manager.py'))
        self.assertTrue(file_exits)
    # test forms py
    def test_check_improve_app_forms_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'improv_app',
                          'forms.py'))
        self.assertTrue(file_exits)
    # test for models
    def test_check_improve_app_models_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'improv_app',
                          'models.py'))
        self.assertTrue(file_exits)
    # test for routes
    def test_check_improve_app_route_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'improv_app',
                          'routes.py'))
        self.assertTrue(file_exits)
    # test for test file of routes
    def test_check_improve_app_test_routes_file(self):
        file_exits = op.exists(op.join(self.dir,
                          'improv_app',
                          'test_routes.py'))
        self.assertTrue(file_exits)
