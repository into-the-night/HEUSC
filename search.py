from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--window-size=1024x768")
chrome_options.add_argument("--headless")
driver = webdriver.Chrome()

def ask_google(query):
    query = query.replace(' ', '+')
    driver.get('http://www.google.com/search?q=' + query)
    answer = driver.execute_script("return document.elementFromPoint(arguments[0], arguments[1]);", 350, 230).text
    return answer

