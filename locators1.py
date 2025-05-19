from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://dev-hideprint.minhhoangjsc.io/login')

    # cssSelector - id - #, class - ., attribute tagname[attribute = "value"]
    # text - //tagname[text()="text"]
    # id using
    emailtxtbox = page.wait_for_selector('#email')
    emailtxtbox.type('owner@gmail.com')
    passwordtxtbox = page.wait_for_selector('#password')
    passwordtxtbox.type('123123')
    loginbtn = page.wait_for_selector('//*[@id="formAuthentication"]/button')
    loginbtn.click()
    page.wait_for_timeout(3000)

    # contains
    # attribute - //tagname[contains(@attribute,"value"]
    # //input[contains(@placeholder,"User")]
    # text - //tagname[contains(text(),"Forgot your)]
    # //label[contains(text(), "Username")]

    # dynamic - kimkim123, kimkim1345, kimkim789
    # starts-with - //tagname[starts-with(@id, 'kimkim')]
    # ends-with

    #family
    # parent - //tagname[@id = "xy"]/parent::input[]
    # child - //tagname[@id = "xy"]/child::input[]
    # ancestor
    # sibling - //td[text()="Microsoft"]//following-sibling::td[2]

