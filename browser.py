from selenium import webdriver

BROWSER = None

def start_browser():
    browser = webdriver.Chrome(executable_path="chromedriver.exe")

    return browser

def get_browser():
    global BROWSER
    
    if BROWSER is None:
        BROWSER = start_browser()

    return BROWSER


