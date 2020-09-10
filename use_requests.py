import requests

url = "https://detik.com"
try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Success ! Response = {response.status_code}')
    else:
        print('Ups, ada error ni')
except Exception as e:
    print(f'There is an error {e}')
print('Program ended')