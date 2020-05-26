import requests
res = requests.get("https://en-gb.facebook.com/login/")
print (res.status_code)
#print res.text
#print res.headers
print res.encoding
print res.is_redirect
print res.elapsed
print res.url
print res.history
print res.content
print res.json()