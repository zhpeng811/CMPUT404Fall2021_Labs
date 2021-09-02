import requests

print(requests.__version__)

google_response = requests.get("http://google.com")
print(google_response.status_code)

# URL obtained by clicking the 'Raw' button on github
github_response = requests.get("https://raw.githubusercontent.com/zhpeng811/CMPUT404Fall2021_Lab1/main/cmput404_lab1_zhpeng.py")
print(github_response.text)