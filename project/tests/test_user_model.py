# project/tests/test_user_model.py


from project import db
from project.api.models import User
from project.tests.base import BaseTestCase
from sqlalchemy.exc import IntegrityError
from project.tests.utils import add_user
from project import bcrypt


class TestUserModel(BaseTestCase):

    def test_add_user(self):
        user = add_user('justatest', 'test@test.com', 'test')
        self.assertTrue(user.id)
        self.assertEqual(user.username, 'justatest')
        self.assertEqual(user.email, 'test@test.com')
        # self.assertEqual(bcrypt.generate_password_hash(
        #     user.password).decode(), bcrypt.generate_password_hash('test').decode())
        self.assertTrue(user.active)
        self.assertTrue(user.created_at)

    def test_add_user_duplicate_username(self):
        add_user('justatest', 'test@test.com', 'test')
        duplicate_user = User(
            username='justatest',
            email='test@test2.com',
            password='test',
        )
        db.session.add(duplicate_user)
        self.assertRaises(IntegrityError, db.session.commit)

    def test_add_user_duplicate_email(self):
        add_user('justatest', 'test@test.com', 'test')
        duplicate_user = User(
            username='justatest2',
            email='test@test.com',
            password='test',
        )
        db.session.add(duplicate_user)
        self.assertRaises(IntegrityError, db.session.commit)

    def test_passwords_are_random(self):
        user_one = add_user('justatest', 'test@test.com', 'test')
        user_two = add_user('justatest2', 'test@test2.com', 'test2')
        self.assertNotEqual(user_one.password, user_two.password)
