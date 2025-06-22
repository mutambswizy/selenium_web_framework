import time
from datetime import datetime
from pages.user_list_page import UserListPage
from test_data.data_loader import load_test_users


def get_unique_username(base_username):
    # Add timestamp to make username unique
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"{base_username}_{timestamp}"





def test_add_multiple_users(browser):
    # Init page object
    page = UserListPage(browser)

    # Load page
    page.load()
    assert page.is_user_list_page(), "Not on User List Table Page"

    # Track added users
    added_usernames = []

    test_users = load_test_users()

    for user in test_users:
        # Prepare user data with unique username
        current_user = user.copy()
        current_user["username"] = get_unique_username(user["username"])
        added_usernames.append(current_user["username"])

        # Add new user
        page.click_add_user()
        page.add_user(**current_user)

        time.sleep(2)  # Wait for UI update

        # Verify user was added
        assert page.is_user_in_list(current_user['username']), \
            f"User {current_user['username']} not found in the user list"