from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    # przechodzimy do strony logowania
    page.goto("https://practicetestautomation.com/practice-test-login/")
    # wprowadzenie username
    page.fill("#username","student")
    # wprowadzenie password
    page.fill("#password","Password13")
    # klikniecie przycisku Submit
    page.click("#submit")

    # Logged In Unsuccessfully
    unsuccess_message = "Your password is invalid!"
    message = page.text_content("//*[@id='error']")
    print(f"Zawartosc naglowka to {message}")

    assert unsuccess_message in message

    # sprawdzenie czy element z tekstem Log out jest widoczny na stronie
    locator_logout = page.locator("text=Log out").is_visible()
    assert locator_logout is True

    browser.close()