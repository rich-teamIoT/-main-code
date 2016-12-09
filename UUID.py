import uuid
from flask import Blueprint

uuid_api=Blueprint('uuid_api', __name__)
user_id=uuid.uuid4()

