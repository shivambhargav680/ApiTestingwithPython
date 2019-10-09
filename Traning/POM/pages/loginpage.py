class loginpage():

    def __init__(self,driver):
        self.driver = driver


        self.username_textbox_id = "txtUsername"
        self.password_textbox_id = "txtPassword"
        self.login_button_id     = "btnLogin"

    def enter_username(self,username):
        self.driver.find