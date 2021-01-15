from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'username': fields.String(required=True, description='The user\'s username'),
        'password': fields.String(required=True, description='The user password '),
    })
	
class PostDto:
    api = Namespace('post', description='Post related operations')
    post_upload = api.model('post_upload', {
        'image': fields.String(required=True, description='Image'),
        'description': fields.String(required=True, description='Image Description')
    })
    post_details = api.model('post', {
		'username': fields.String(required=True, description='Post Owner'),
        'posted_on': fields.DateTime(required=True, description='Posted DateTime'),
        'image': fields.String(required=True, description='Image'),
        'description': fields.String(required=True, description='Image Description'),
        'id': fields.Integer(required=True, description='Post ID')
    })
    post_delete = api.model('post_delete', {
        'id': fields.Integer(required=True, description='Post ID')
    })