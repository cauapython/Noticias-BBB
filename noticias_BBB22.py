from requests import get
from bs4 import BeautifulSoup

site = get("https://www.purepeople.com.br/famosos/bbb-22_p554532/noticias/1")
soup = BeautifulSoup(site.content, "html.parser")
noticias = soup.find_all("div", {"class": "c-article-flux__content u-clearfix"})
for noticia in noticias:
    titulo = noticia.find("a", {"class": "c-article-flux__title u-hover-color u-global-link"}).get_text()
    subtitulo = noticia.find("div", {"class": "c-article-flux__chapo u-visible@tablet"}).get_text()
    link = 'https://www.purepeople.com.br' + noticia.find("a", {"class": "c-article-flux__title u-hover-color u-global-link"})["href"]
    data = noticia.find("span", {"class": "c-article-flux__date-day"}).get_text()
    horario = noticia.find("span", {"class": "c-article-flux__date-hour"}).get_text()
    print("-" * 150)
    print(f"titulo: {titulo}")
    print(f"subtitulo: {subtitulo}")
    print(f"link: {link}")
    print(f"Data: {data}", end = " ")
    print(f"às {horario}")