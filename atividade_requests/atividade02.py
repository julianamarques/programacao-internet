import requests

def baixar_arquivo(url):
    response = requests.get(url)
    arquivo = open("arquivo."+response.headers["content-type"][(response.headers["content-type"].find("/"))+1:], "w+")
    arquivo.write(response.text)
    arquivo.close()


def main():
    #url = "https://abrilexame.files.wordpress.com/2016/09/size_960_16_9_20151020-25144-9f3b5r.jpg"
    url = "https://raw.githubusercontent.com/julianamarques/programacao-internet/master/README.md"
    baixar_arquivo(url)

if __name__ == "__main__":
    main()