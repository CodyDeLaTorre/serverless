from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        if "country" in dic:
            url = "https://restcountries.com/v3.1/name/"
            r = requests.get(url + dic["country"])
            data = r.json()
            definitions = []
            for country_data in data:
                definition = country_data["capital"][0]
                name = country_data["name"]["common"]
                definitions.append(definition)
                definitions.append(name)
            message = f'The capital of {definitions[1]} is {definitions[0]}'

        else:
            message = "Give me a country to define please"

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        self.wfile.write(message.encode())

        return