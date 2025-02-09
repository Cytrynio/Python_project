from playwright.sync_api import sync_playwright

with open("password.txt","r") as password:
    password_text = password.read()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    # przechodzimy do strony logowania
    page.goto("https://practicetestautomation.com/practice-test-login/")
    # wprowadzenie username
    page.fill("#username","student")
    # wprowadzenie password
    page.fill("#password",password_text)
    # klikniecie przycisku Submit
    page.click("#submit")
    # czekamy na przekierowanie do strony
    page.wait_for_url("**/logged-in-successfully/") # czekamy aż URL zawiera logged-in-sccuessfully

    # Logged In Successfully
    success_message = "Logged In Successfully"
    message = page.text_content("h1")
    print(f"Zawartosc naglowka to {message}")

    assert success_message in message

    # sprawdzenie czy element z tekstem Log out jest widoczny na stronie
    locator_logout = page.locator("text=Log out").is_visible()
    assert locator_logout is True

    browser.close()