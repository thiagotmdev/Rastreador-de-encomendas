import requests
from bs4 import BeautifulSoup
from sms import sms


def rastrear(cod_r, n_cel):
    url_base = f'https://www.linkcorreios.com.br/?id={cod_r}'
    r_url = requests.get(url_base)
    html_url = r_url.text
    soup_url = BeautifulSoup(html_url, 'html.parser')
    find_url = soup_url.find("ul", class_="linha_status m-0")
    sms(find_url.text, n_cel, cod_r)
