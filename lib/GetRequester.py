import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        return_list = []
        data = json.loads(self.get_response_body())
        for stuff in data:
            return_list.append(stuff)
        
        return return_list