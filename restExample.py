import requests

print("\nGet Example")
req = requests.get('https://github.com/timeline.json')
print(req.status_code)
print(req.text)
print(req.json())

print("\nGet Example Bad URL Raise Err")
bad_req = requests.get('https://google.com')
print(bad_req.status_code)
bad_req.raise_for_status()


print("\nPost Example")
payload = {'key1': 'value1', 'key2': 'value2'}
req = requests.post("https://httpbin.org/post", params=payload)
print(req.url)
print(req.text)

print("\nPost Example with data")
req = requests.post("https://httpbin.org/post", data=payload)
print(req.text)