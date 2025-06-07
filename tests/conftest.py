import os

import pytest
from django.contrib.auth import get_user_model
from django.test import Client
from playwright.sync_api import Page
from pytest_django.live_server_helper import LiveServer
from allauth.account.models import EmailAddress
from allauth.account.utils import user_email

os.environ.setdefault("DJANGO_ALLOW_ASYNC_UNSAFE", "true")

@pytest.fixture
def browser_context_args(live_server: LiveServer):
    return {"base_url": live_server.url}

@pytest.fixture
def user_data():
    return {"email": "test@example.com", "password": "test_password123"}

@pytest.fixture
def verified_user(user_data):
    User = get_user_model()
    
    user = User.objects.create_user(
        email=user_data["email"], password=user_data["password"]
    )
    
    email, created = EmailAddress.objects.get_or_create(
        user=user, email=user_email(user)
    )
    email.verified = True
    email.save()
    
    return user

@pytest.fixture
def auth_page(page: Page, verified_user, user_data):
    client = Client()
    resp = client.post(
        "/accounts/login",
        {"login": user_data["email"], "password": user_data["password"]},
    )
    
    session_id = resp.cookies["sessionid"].value
    page.context.add_cookies(
        [{"name": "sessionid", "value": session_id, "domain": "localhost", "path": "/"}]
    )
    return page