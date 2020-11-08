from requests import Session
from json_parser import JsonParser
import json

session = Session()

# HEAD requests ask for *just* the headers, which is all you need to grab the
# session cookie

#jak to nie zadziala uzyj ciezkiej artylerii 
#https://pypi.org/project/selenium-wire/

nursery_endpoint_url:str = 'https://rejestrzlobkow.mpips.gov.pl:8443/lista/data'
nursery_website_url:str = 'https://empatia.mpips.gov.pl/dla-swiadczeniobiorcow/rodzina/d3/rejestr-zlobkow-i-klubow' 

session.head(nursery_website_url) #head request to empatia.mpips.gov to get cookie
response = session.post(
    url=nursery_endpoint_url,    
    
    json={"rodzaj":"","woj":"","pow":"","gmina":"","slowo":"","niep":"NIE","page_type":"zk","page_layout":"1","start_from":49,"pob_godz_od":"","pob_godz_do":"","pob_mies_od":"","pob_mies_do":"","wyz_dzien_od":"","wyz_dzien_do":"","wyz_mies_od":"","wyz_mies_do":""},
    headers={
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Content-Length': '255',
        'Content-Type': 'application/json; charset=UTF-8',
        'Host': 'rejestrzlobkow.mpips.gov.pl:8443',
        'Origin': 'https://rejestrzlobkow.mpips.gov.pl:8443',
        'RequestResponseContentType': 'application/json',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Referer': 'https://rejestrzlobkow.mpips.gov.pl:8443/lista/zk?&',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
    }
)

json_parser = JsonParser(response.text)
aa = json_parser.get_parsed_nursery_json()
print(aa)





    

#TODO jakas lekka baza danych żeby te dane wciagnac

#TODO jakis sposob zeby wszystko wciagnac
#sqlite!

#print (response.text)
#print(response)