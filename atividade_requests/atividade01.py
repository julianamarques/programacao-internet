import requests

def request(url):
    response = requests.get(url)

    print(response.status_code)
    print(response.headers["content-length"])
    print(response.text)

def main():
    url = input("Insira uma URL: ")
    request(url)

if __name__ == "__main__":
    main()