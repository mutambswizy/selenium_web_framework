from selenium.webdriver.common.by import By


class UserListPage:
    # Base URL for the web application
    URL = "http://www.way2automation.com/angularjs-protractor/webtables/"

    def __init__(self, driver):
        # Initialize with WebDriver instance
        self.driver = driver

    def load(self):
        # Navigate to the page and verify title
        self.driver.get(self.URL)

        expected_title = "Protractor practice website - WebTables"
        assert expected_title in self.driver.title, (
            f"Unexpected title, expected: '{expected_title}' actual: '{self.driver.title}'"
        )

    def is_user_list_page(self):
        # Check if we're on the correct page
        return "WebTables" in self.driver.title

    def click_add_user(self):
        # Click the button to open add user form
        self.driver.find_element(By.CSS_SELECTOR, "button[ng-click='pop()']").click()

    def add_user(self, first_name, last_name, username, password, customer, role, email, phone):
        # Fill out the user creation form
        
        # Handle first name field
        first_name_element = self.driver.find_element(By.NAME, "FirstName")
        first_name_element.clear()
        first_name_element.send_keys(first_name)

        # Handle last name field
        last_name_element = self.driver.find_element(By.NAME, "LastName")
        last_name_element.clear()
        last_name_element.send_keys(last_name)

        # Handle username field
        username_element = self.driver.find_element(By.NAME, "UserName")
        username_element.clear()
        username_element.send_keys(username)

        # Handle password field
        password_element = self.driver.find_element(By.NAME, "Password")
        password_element.clear()
        password_element.send_keys(password)

        # Select customer radio button based on company name
        if customer.lower() == 'company aaa':
            self.driver.find_element(By.CSS_SELECTOR, "input[value='15']").click()
        else:
            self.driver.find_element(By.CSS_SELECTOR, "input[value='16']").click()

        # Select role from dropdown
        role_dropdown = self.driver.find_element(By.NAME, "RoleId")
        for option in role_dropdown.find_elements(By.TAG_NAME, 'option'):
            if option.text == role:
                option.click()
                break

                # Handle email field
            email_element = self.driver.find_element(By.NAME, "Email")
            email_element.clear()
            email_element.send_keys(email)

            # Handle phone field
            phone_element = self.driver.find_element(By.NAME, "Mobilephone")
            phone_element.clear()
            phone_element.send_keys(phone)

        # Submit the form
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