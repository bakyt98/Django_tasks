from calendar import timegm
from datetime import datetime
from rest_framework_jwt.compat import get_username_field, get_username
from rest_framework_jwt.settings import api_settings

import uuid



def get_token(user):
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)
    return token
