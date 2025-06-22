import time
from datetime import datetime
import allure
from pages.user_list_page import UserListPage


def get_unique_username(base_username):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"{base_username}_{timestamp}"


test_users = [
    {
        "first_name": "FName1",
        "last_name": "LName1",
        "username": "User1",  # Will be made unique during test
        "password": "Pass1",
        "customer": "Company AAA",
        "role": "Admin",
        "email": "admin@mail.com",
        "phone": "082555"
    },
    {
        "first_name": "FName2",
        "last_name": "LName2",
        "username": "User2",  # Will be made unique during test
        "password": "Pass2",
        "customer": "Company BBB",
        "role": "Customer",
        "email": "customer@mail.com",
        "phone": "083444"
    }
]


@allure.epic("User Management")
@allure.feature("User Creation")
@allure.story("Multiple Users Creation")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_multiple_users(browser):
    page = UserListPage(browser)

    with allure.step("Load User List Page"):
        page.load()
        assert page.is_user_list_page(), "Not on User List Table Page"

    added_usernames = []  # Keep track of added usernames

    for user in test_users:
        current_user = user.copy()
        current_user["username"] = get_unique_username(user["username"])
        added_usernames.append(current_user["username"])

        with allure.step(f"Add new user: {current_user['username']}"):
            allure.attach(
                str(current_user),
                name="User Data",
                attachment_type=allure.attachment_type.TEXT
            )

            with allure.step("Click Add User button"):
                page.click_add_user()

            with allure.step("Fill user form"):
                page.add_user(**current_user)

            time.sleep(2)  # Add a small delay if needed between additions

            with allure.step(f"Verify user {current_user['username']} appears in list"):
                assert page.is_user_in_list(current_user['username']), \
                    f"User {current_user['username']} not found in the user list"
