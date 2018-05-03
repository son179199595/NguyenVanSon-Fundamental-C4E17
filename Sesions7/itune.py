from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "https://www.apple.com/itunes/charts/songs/"
connection = urlopen(url)
raw_data= connection.read()
text = raw_data.decode('utf8')
soup = BeautifulSoup(text,"html.parser")
div  = soup.find("div","main")
section = div.find("section","section chart-grid")
div1 = section.find("div","section-content")
ul   = div1.find("ul")
li_list   = ul.find_all("li")

list_item =[]
for li in li_list:
    a = li.h3.a
    b = li.h4.a
    namesong = lia.string
    singer   = b.string
    item = {

        "Singer":singer

    }
    list_item.append(item)
print(list_item)
pyexcel.save_as(records=list_item,dest_file_name="test2.xlsx")
