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

elements = driver.find_elements_by_xpath('//*[@id="layBodyWrap"]/div/div/div[2]/div[2]/section[1]/ul/li')
 
print( '상품 개수: {}'.format( len(elements) ) )
for el in elements:
	el_title = el.find_element_by_xpath('div/div[2]/div/div[1]')
	try:
		el_price = el.find_element_by_xpath('div/div[2]/div/div[3]')
	except:
		el_price = el.find_element_by_xpath('div/div[2]/div/div[2]')
 
	tagName = el_title.tag_name
	className = el_title.get_attribute('class')
	title = el_title.text
	price = el_price.text
    
	print( '='*50 )
	print( 'tagName: {}'.format( tagName ) )
	print( 'className: {}'.format( className ) )
	print( 'title: {}'.format( title ) )
	print( 'price: {}'.format( price ) )
