import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        """Send GET request and return the raw response body"""
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        """Send GET request and return response converted to Python dict/list"""
        response = requests.get(self.url)
        return response.json()


# Test code to run when executing the file directly
if __name__ == "__main__":
    url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
    requester = GetRequester(url)
    print("Raw response body:\n")
    print(requester.get_response_body())
    print("\nJSON response:\n")
    print(json.dumps(requester.load_json(), indent=2))
