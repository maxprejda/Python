import requests
from bs4 import BeautifulSoup

import xlwt

book = xlwt.Workbook()

n = 0

def addToTable(cislo, hrac, pozice, haze, vyska, vaha, rok, n, sh):
    sh.write(n, 0, cislo)
    sh.write(n, 1, hrac)
    sh.write(n, 2, pozice)
    sh.write(n, 3, haze)
    sh.write(n, 4, vyska)
    sh.write(n, 5, vaha)
    sh.write(n, 6, rok)

def collect(URL, n):
    r = requests.get(URL)

    sh = book.add_sheet("Hráči " + str(n))

    data = BeautifulSoup(r.content, 'html.parser')
    tabulka = data.find('tbody')
    radky = tabulka.find_all('tr')

    for i in range(len(radky)):
        info = radky[i].find_all('td')

        cislo = info[0].text
        hrac = info[1].find('a').text
        pozice = info[2].text
        haze = info[3].text
        vyska = info[4].text
        vaha = info[5].text
        rok = info[6].text

        addToTable(cislo, hrac, pozice, haze, vyska, vaha, rok, i, sh)
        print(f'Číslo: {cislo} | Hráč: {hrac} | Pozice: {pozice} | Háže/Pálí: {haze} | Výška: {vyska} | Váha: {vaha} | Rok Narození: {rok}')

collect("https://stats.baseball.cz/cs/events/2023-nadstavba-o-extraligu/teams/27061", n)
n+=1

collect("https://stats.baseball.cz/cs/events/2023-nadstavba-o-extraligu/teams/27059", n)
n+=1

collect("https://stats.baseball.cz/cs/events/2023-nadstavba-o-extraligu/teams/27062", n)
n+=1

collect("https://stats.baseball.cz/cs/events/2023-nadstavba-o-extraligu/teams/27060", n)
n+=1

collect("https://stats.baseball.cz/cs/events/2023-nadstavba-o-extraligu/teams/27063", n)
n+=1

collect("https://stats.baseball.cz/cs/events/2023-nadstavba-o-extraligu/teams/27064", n)
n+=1

book.save("tabulka.xls")
print("done!")