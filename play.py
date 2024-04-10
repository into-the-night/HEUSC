from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager

options = webdriver.EdgeOptions()
options.use_chromium = True
# options.add_argument("--headless")
# options.add_argument('--user-data-dir=C:\\Users\\abhay\\AppData\\Local\\Microsoft\\Edge\\User Data\\')
# options.add_argument("profile-directory=Default")
options.add_argument("--enable-chrome-browser-cloud-management")
options.add_experimental_option("detach", True)
driver = webdriver.Edge(options=options, service=Service(EdgeChromiumDriverManager().install()))



def play_music(songname):
    link = 'https://music.youtube.com/search?q='+'+'.join(songname)
    driver.get(link)
    button = driver.find_element(By.XPATH, value="//yt-icon[@class='icon style-scope ytmusic-play-button-renderer']")
    button.click()








