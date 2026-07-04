import requests
variable = requests.get("http://books.toscrape.com")
print(variable.status_code)

