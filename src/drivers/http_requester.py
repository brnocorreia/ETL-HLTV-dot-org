from typing import Dict
import requests


class HttpRequester:

    def __init__(self) -> None:
        self.__url = 'https://www.vlr.gg/team/6961/loud'
    
    def request_from_page(self) -> Dict[int, str]:
        response = requests.get(self.__url, timeout=100)
        return {
            "status_code": response.status_code,
            "html": response.text.encode('utf-8')
        }
        