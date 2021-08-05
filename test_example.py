from selenium import webdriver

browser = webdriver.Firefox()

browser.get('https://github.com/durmus-pala')

assert browser.page_source.find('durmus')
