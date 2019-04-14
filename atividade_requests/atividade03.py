import requests
from bs4 import BeautifulSoup

def gerar_arquivo(url):
    arquivo = open("links.txt", "w+")
    response = requests.get(url)
    html = BeautifulSoup(response.text, "html")
    links_temp = html.find_all("a")
    links = []

    for l in links_temp:
        links.append(l.get_text().join("\n"))

    arquivo.writelines(links)
    arquivo.close()

def main():
    gerar_arquivo("http://www.google.com")

if __name__ == "__main__":
    main()