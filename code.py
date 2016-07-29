from bs4 import BeautifulSoup
from requests import Session


s = Session()
data = {'username':#my user-name,
        'password':#my password
}
url = 'http://ec2-23-23-194-201.compute-1.amazonaws.com/'
website = s.post(url, data, cookies = data).text

mycontent = s.get(url+'contentlist.php').text
soup = BeautifulSoup(mycontent, 'html.parser')

man = (soup.find_all('tr'))
x = []
y = []

for i in man:
        x.append(i.find_all('td')[5].string)
        y.append(i.find_all('td')[1].string)
m = 0
for i in range(len(x)):
        if x[i] == 'Vaibhav':
                print(y[i])

