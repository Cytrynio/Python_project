from playwright.sync_api import sync_playwright

LOGIN_URL = "https://practicetestautomation.com/practice-test-login/"
SUCCESS_URL = "**/logged-in-successfully/"
SUCCESS_MESSAGE = "Logged In Successfully"
INVALID_CREDENTIALS_MESSAGE = "Your username is invalid!"
INVALID_PASSWORD_MESSAGE = "Your password is invalid!"


def login_test(username: str, password: str, expected_url: str, expected_message: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(LOGIN_URL)
        page.fill("#username", username)
        page.fill("#password", password)
        page.click("#submit")

        # Sprawdzenie przekierowania (dla happy path) lub błędnego komunikatu (dla negatywnych przypadków)
        if expected_url:
            page.wait_for_url(expected_url)
            message = page.text_content("h1")
            assert expected_message in message, f"Expected '{expected_message}', got '{message}'"
            assert page.locator("text=Log out").is_visible(), "Log out button not found!"
        else:
            error_message = page.text_content("#error")
            assert expected_message in error_message, f"Expected '{expected_message}', got '{error_message}'"

        browser.close()


# Testy:
def test_happy_path():
    with open("password.txt", "r") as password_file:
        password_text = password_file.read().strip()
    login_test("student", password_text, SUCCESS_URL, SUCCESS_MESSAGE)


def test_invalid_username():
    with open("password.txt", "r") as password_file:
        password_text = password_file.read().strip()
    login_test("wrong_user", password_text, None, INVALID_CREDENTIALS_MESSAGE)


def test_invalid_password():
    login_test("student", "wrong_password", None, INVALID_PASSWORD_MESSAGE)


# Wykonanie testów
test_happy_path()
test_invalid_username()
test_invalid_password()
