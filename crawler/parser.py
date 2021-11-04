import re

def st11_parser( response=None ):
    datas = list()
 
    elements = response.find_elements_by_xpath('//*[@id="layBodyWrap"]/div/div/div[2]/div[2]/section[1]/ul/li')
    
    for idx, el in enumerate(elements):
        el_title = el.find_element_by_xpath('div/div[2]/div/div[1]')
        try:
            el_price = el.find_element_by_xpath('div/div[2]/div/div[3]')
        except:
            el_price = el.find_element_by_xpath('div/div[2]/div/div[2]')
        el_img_url = el.find_element_by_xpath('div/div[1]')
        el_link = el.find_element_by_xpath('div/div[2]/div/div[1]/a')
 
        title = el_title.text.strip()
        price = re.sub(r'[^0-9]', '', el_price.text.strip())
        link = el_link.get_attribute('href')
    
        data = {
            "no": idx+1
            , "title": title
            , "price": price
            , "link": link
        }
 
        datas.append( data )
 
    return datas
