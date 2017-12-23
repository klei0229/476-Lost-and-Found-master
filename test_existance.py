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
