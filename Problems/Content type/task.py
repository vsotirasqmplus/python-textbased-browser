import requests


def get_content_type(url):
    response = requests.get(url).headers
    return response['Content-Type']  # + '; ' + response['Content-Encoding']

# print(get_content_type('http://google.com'))
# print(get_content_type('http://github.com'))
