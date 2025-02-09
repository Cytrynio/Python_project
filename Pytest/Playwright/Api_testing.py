from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    requests_content = p.request.new_context()

    response = requests_content.get('https://jsonplaceholder.typicode.com/users/1')


    data = response.json()['name']

    print(data)


    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})  # Przykładowy rozmiar dla dużego ekranu

    # przechodzimy do strony logowania
    page.goto("https://google.com")
    # wprowadzenie username
    page.click("#W0wltc > div")
    page.fill("#APjFqb", data)
    # wprowadzenie password
    # klikniecie przycisku Submit
    page.click("body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf.emcav > div.UUbT9.EyBRub > div.aajZCb > div.lJ9FBc > center > input.gNO89b")
    # czekamy na przekierowanie do strony
    page.wait_for_selector("body > div:nth-child(1) > div > b")  # czekamy aż URL zawiera logged-in-sccuessfully

    # new_post = {"userId": 101,
    # "id": 101,
    # "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
    # "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut"}
    #
    # response = requests_content.post("https://jsonplaceholder.typicode.com/posts", data = new_post)
    #
    # status = response.status
    #
    # print("Status odpowiedzi:", status)
    # assert status == 201
    #
    # result = response.json()
    # print(result)
    #
    #
    # assert result["userId"] == new_post['userId']
    # assert result["title"] == 'ea molestias quasi exercitationem repellat qui ipsa sit aut'