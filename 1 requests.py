import requests as web

r = web.get('http://google.com')
print(type(r.text))
print(r.encoding)


