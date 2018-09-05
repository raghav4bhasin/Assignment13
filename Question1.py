import requests
response = requests.get("https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=text")

print('Status: ',response.status_code)
print(' ')
print(response.content)
