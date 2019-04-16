import requests
import re, urllib
from bs4 import BeautifulSoup

class Search:
    def __init__(self):
        pass

    def search(self, url, keyword, deep = 0):
        words_list = []
        response = requests.get(url)
        content = BeautifulSoup(response.text, "html5lib").text
        words = re.findall(  '\w*.{0,10}' + str(keyword) + '.{0,10}\w*' , content, re.IGNORECASE)
        links = self.extract_links(response, url)

        for w in words:
            words_list.append(w)

        if len(words_list) == 0:
            return "Nenhum resultado Encontrado"

        if deep > 0:
            for l in links:
                self.search(l, keyword, deep - 1)
        
        return words_list

    def extract_links(self, response, url):
        links_list = []

        soup = BeautifulSoup(response.text, 'html5lib')
        links = soup.findAll('a', attrs={re.compile('(?<=href=["\'])https?://.+?(?=["\'])')})

        for l in links:
            if 'href' in l.attrs:
                if 'http' in l['href']:
                    links_list.append(l['href'])

        return links_list

def main():
    # TESTE URL: https://wiki.archlinux.org/
    # KEYWORD: main page
    url = input("URL: ")
    keyword = input("Palavra : ")
    deep = int(input("Profundidade: "))
    search = Search()
    print(search.search(url, keyword, deep))

if __name__ == "__main__":
    main()
