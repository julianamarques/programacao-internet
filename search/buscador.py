import requests
import re
from bs4 import BeautifulSoup

class Search:
    def __init__(self):
        pass

    def search(self, url, keyword, deep = 0):
        words_list = []
        response = requests.get(url)
        content = BeautifulSoup(response.text, "html5lib").text
        words = re.findall(  '\w*.{0,10}' + str(keyword) + '.{0,10}\w*' , content, re.IGNORECASE)
        links = self.extract_links(response)

        for w in words:
            words_list.append(w)

        if len(words_list) == 0:
            return "Nenhum resultado Encontrado"

        if deep > 0:
            for l in links:
                self.search(l, keyword, deep - 1)
        
        return words_list

    def extract_links(self, response):
        soup = BeautifulSoup(response.text, 'html5lib')
        links = soup.find_all('a')
        links_list = []

        for l in links:
       		links_list.append(l["href"])

        return links

def main():
    url = input("URL: ")
    keyword = input("Palavra : ")
    deep = int(input("Profundidade: "))
    search = Search()
    print(search.search(url, keyword, deep))

if __name__ == "__main__":
    main()
