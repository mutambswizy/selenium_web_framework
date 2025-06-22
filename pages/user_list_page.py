from selenium.webdriver.common.by import By



class UserListPage:
    URL = "http://www.way2automation.com/angularjs-protractor/webtables/"

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

        #Validate that you are on the User List Table page
        expected_title = "Protractor practice website - WebTables"
        assert expected_title in self.driver.title, (
            f"Unexpected title, expected: '{expected_title}' actual: '{self.driver.title}'"
        )

    def is_user_list_page(self):
        return "WebTables" in self.driver.title

    def click_add_user(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[ng-click='pop()']").click()

    def add_user(self, first_name, last_name, username, password, customer, role, email, phone):

        # Last Name
        first_name_element = self.driver.find_element(By.NAME, "FirstName")
        first_name_element.clear()
        first_name_element.send_keys(first_name)

        # Last Name
        last_name_element = self.driver.find_element(By.NAME, "LastName")
        last_name_element.clear()
        last_name_element.send_keys(last_name)

        # Username
        username_element = self.driver.find_element(By.NAME, "UserName")
        username_element.clear()
        username_element.send_keys(username)

        # Password
        password_element = self.driver.find_element(By.NAME, "Password")
        password_element.clear()
        password_element.send_keys(password)

        # Select customer radio
        if customer.lower() == 'company aaa':
            self.driver.find_element(By.CSS_SELECTOR, "input[value='15']").click()
        else:
            self.driver.find_element(By.CSS_SELECTOR, "input[value='16']").click()

        # Select role
        role_dropdown = self.driver.find_element(By.NAME, "RoleId")
        for option in role_dropdown.find_elements(By.TAG_NAME, 'option'):
            if option.text == role:
                option.click()
                break

                # Email
            email_element = self.driver.find_element(By.NAME, "Email")
            email_element.clear()
            email_element.send_keys(email)

            # Phone
            phone_element = self.driver.find_element(By.NAME, "Mobilephone")
            phone_element.clear()
            phone_element.send_keys(phone)

        # Click Save
        self.driver.find_element(By.CSS_SELECTOR, "button[ng-click='save(user)']").click()

    def get_user_row(self, username):
        """Find a user row in the table by username"""
        rows = self.driver.find_elements(By.CSS_SELECTOR, "tbody tr")
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) > 2 and username in cells[2].text:  # Username is in the 3rd column
                return row
        return None

    def is_user_in_list(self, username):
        """Check if a user exists in the table"""
        return self.get_user_row(username) is not None