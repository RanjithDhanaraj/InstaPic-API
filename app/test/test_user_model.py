import unittest
from unittest.mock import patch
import datetime
import jwt
from app.main import db
from app.main.model.user import User
from app.test.base import BaseTestCase


class TestUserModel(BaseTestCase):
    def test_user_repr(self):
        new_user = User(
            username='test',
            password='test',
            registered_on=datetime.datetime.utcnow()
        )
        self.assertEqual(repr(new_user), "<User '{}'>".format(new_user.username))

    def test_encode_auth_token(self):
        user = register_user()
        auth_token = user.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))

    @patch('jwt.encode')
    def test_encode_auth_token_with_exception(self, jwt_encode):
        jwt_encode.side_effect = Exception()
        user = register_user()
        self.assertRaises(Exception, User.encode_auth_token(user.id))

    def test_decode_auth_token(self):
        user = register_user()
        auth_token = user.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))
        self.assertTrue(User.decode_auth_token(auth_token.decode("utf-8") ) == 1)
    
    @patch('jwt.decode')
    def test_decode_auth_token_with_expired_token_exception(self, jwt_decode):
        """Test for exception handling of Expired error token during decoding"""
        jwt_decode.side_effect = jwt.ExpiredSignatureError
        user = register_user()
        auth_token = user.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))
        self.assertTrue('Signature expired. Please log in again.', User.decode_auth_token(auth_token.decode("utf-8")) == 1)
    
    @patch('jwt.decode')
    def test_decode_auth_token_with_invalid_token_exception(self, jwt_decode):
        """Test for exception handling of Expired error token during decoding"""
        jwt_decode.side_effect = jwt.InvalidTokenError
        user = register_user()
        auth_token = user.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))
        self.assertTrue('Invalid token. Please log in again.', User.decode_auth_token(auth_token.decode("utf-8")) == 1)

def register_user():
    user = User(
        username='test',
        password='test',
        registered_on=datetime.datetime.utcnow()
    )
    db.session.add(user)
    db.session.commit()
    return user
	
if __name__ == '__main__':
    unittest.main()
