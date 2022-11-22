from api.app import create_app, Module
from api.tokens import tokens
from api.users import users
from api.posts import posts
from api.errors import errors
from api.fake import fake
from api import models

app = create_app(
    models=models,
    modules=[
        Module(tokens),
        Module(users),
        Module(posts),
        Module(errors, indexed=False),
        Module(fake, indexed=False),
    ],
)
