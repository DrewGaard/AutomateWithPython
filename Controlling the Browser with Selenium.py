from selenium import webdriver

browser = webdriver.Safari()
browser.get('https://automatetheboringstuff.com')

elem = browser.find_element_by_css_selector('body > div.main > ul:nth-child(16) > li:nth-child(1) > a')
elem.click()

browser.quit()
