import requests

r = requests.get('http://wether.livedoor.com/forecast/webservice/json/vl?city=130010')
print(r.status_code)
print(r.text[:500])
tmp = r.json()
print(tmp) #ここでエラーとなってしまいます。

'''
tmp = r.json() #このようにしてもエラーとなってしまいます。
'''
