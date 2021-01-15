import datetime
from app.main import db
from app.main.model.user import User
from app.main.service.post_service import upload_new_post
from app.test.test_images_base64 import image1, image2, image3, image4

def save(data):
    db.session.add(data)
    db.session.commit()

def add_users_and_posts():
    db.drop_all()
    db.create_all()
    db.session.commit()

    """User 1 and Post 1"""
    user1 = User(
        username='Doggo',
        password='cutedoggoretreiver',
        registered_on=datetime.datetime.utcnow()
    )
    save(user1)
    
    post1 = upload_new_post(dict(
        image=image1,
        description='Cute Golden Retreiver'
    ), current_user=user1)

    
    """User 2 and Post 2"""
    user2 = User(
        username='Catto',
        password='meower',
        registered_on=datetime.datetime.utcnow()
    )
    save(user2)
    
    post2 = upload_new_post(dict(
        image=image2,
        description='Meow meow!'
    ), current_user=user2)

    """User 3 and Post 3"""
    user3 = User(
        username='Reddie',
        password='IAmPanda',
        registered_on=datetime.datetime.utcnow()
    )
    save(user3)
    
    post3 = upload_new_post(dict(
        image=image1,
        description='I am Panda-Man'
    ), current_user=user3)

