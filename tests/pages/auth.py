from playwright.sync_api import Page


class SignupPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_field = page.get_by_placeholder("Email address")
        self.password_field = page.get_by_placeholder("Password")
        self.signup_button = page.get_by_role("button", name="Create your account")
        
    def complete_signup_form(self, email, password):
        self.email_field.fill(email)
        self.password_field.fill(password)
        self.signup_button.click()    
class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_field = page.get_by_placeholder("Email address")
        self.password_field = page.get_by_placeholder("Password")
        self.signup_button = page.get_by_role("button", name="Sign in")
        
        
class ConfirmationPage:
    def __init__(self, page: Page):
        self.page = page
        self.confirm_button = page.get_by_role("button")