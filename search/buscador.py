import requests
import re
from bs4 import BeautifulSoup

class Search:
    @staticmethod
    def recursive_search(url, deep, keyword):
        links = []
        links_list = []

        if deep == 0:
            return search(url, keyword)

        response = requests.get(url)

        if response is not None:
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                links = soup.find_all("a")

                for l in a:
                    try:
                        if (str(l['href']).startswith("http")):
                            if l["href"] not in links_list:
                                links_list.append(l["href"])
                                search(l["href"], keyword)
                    except:
                        pass

                if deep > 0:
                    extract_links(links, deep - 1, keyword)

                return links


    @staticmethod
    def extract_links(links, deep, keyword):
        for l in links:
            links.append(recursive_search(l, deep, keyword))

        return links


    @staticmethod
    def search(url, keyword):
        words_list = []
        response = requests.get(url)

        text = BeautifulSoup(response.text, "html.parser").text

        words = re.findall('\w*.{0,10}' + keyword + '.{0,10}\w*', text, re.IGNORECASE)

        for w in words:
            words_list.append(w)

        return words_list


def main():
    url = input("URL: ")
    keyword = input("Keyword : ")
    deep = int(input("Profundidade: "))

    print(recursive_search(url, deep, keyword))
    
    if __name__ == '__main__':
        main()
