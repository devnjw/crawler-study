from selenium import webdriver
from selenium.webdriver.chrome.options import Options 

URL = 'https://searchn.11st.co.kr/pc/price-compare?kwd=%25EC%258B%25A0%25EB%25B0%259C&tabId=PRICE_COMPARE&pageNo=1'
DRIVER_PATH = 'drivers/chromedriver'

chrome_options = Options()
chrome_options.add_argument( '--headless' )
chrome_options.add_argument( '--log-level=3' )
chrome_options.add_argument( '--disable-logging' )
chrome_options.add_argument( '--no-sandbox' )
chrome_options.add_argument( '--disable-gpu' )

driver = webdriver.Chrome( executable_path=DRIVER_PATH, chrome_options=chrome_options )
driver.get( URL )

print( driver.page_source )

