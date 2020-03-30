from bs4 import BeautifulSoup
import sys


with open(sys.argv[1]) as fp:
    html = fp.read()#.split("\n")   #

html = html.replace("\n\n","\n")

soup = BeautifulSoup(html,'html.parser')
abs = soup.findAll("ab")

hash = {}
abs_list = list(set(abs))
#print(abs)
for row in abs_list:
    rowtext = row.get_text()
    print(rowtext)
