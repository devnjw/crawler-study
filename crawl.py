from crawler import SeleniumRequest
from crawler.parser import st11_parser
from pprint import pprint
 
targets = {
    "11st": {
        "url": 'https://searchn.11st.co.kr/pc/price-compare?kwd=%25EC%258B%25A0%25EB%25B0%259C&tabId=PRICE_COMPARE&pageNo=1'
        , "parser": "st11_parser"
    }
}

request = SeleniumRequest( driver_path='./crawler/drivers/chromedriver' )

def run_target(target):
    info = targets[target]

    url = info['url']
    callback = eval(info["parser"])

    data = request.get( url, callback=callback )

    pprint( data )

def run():
    for key in targets.keys():
        run_target(key)

if __name__ == "__main__":
   run()