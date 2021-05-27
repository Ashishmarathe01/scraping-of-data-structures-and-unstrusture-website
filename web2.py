from bs4 import BeautifulSoup
import requests
import csv
import  pandas as pd
 # Dtabase Creation
import sqlite3
conn=sqlite3.connect('Test2.db')
c=conn.cursor()
conn=sqlite3.connect('Test2.db')
c=conn.cursor()

d_day=[]
d_month=[]
url=[]
desc=[]
image=[]
allUrl=[]
tittle=[]
page=list(range(0,1))
req=requests.get("https://www.naadyogacouncil.com/en/events/").text
# print(req)

# getting data of day
soup=BeautifulSoup(req,"html.parser")
day=soup.find_all('div',class_="day",limit=10)
for i in range(len(day)):
    d_day.append(day[i].text)
    len(d_day)
# print("day",d_day)


# getting data of month
month=soup.find_all('div',class_="month",limit=10)
# print('iam',month)
for i in range(len(month)):
    d_month.append(month[i].text)
    len(d_month)
# print('month',d_month)

# getting data of description
desc1=soup.find_all("p",limit=10)

for i in range(len(desc1)):
    desc.append(desc1[i].text)
    len(desc)
# print('desc',desc)

# getting data of image
im=soup.find_all("img",class_="attachment-post-small-2 size-post-small-2 wp-post-image",limit=10)
for i in ((im)):
    image.append(i['src'])
    len(image)
# print('imag',image)

# getting data of url
ur=soup.find_all("a",class_ ="button button-border accent1 hover-accent1",limit=10)
# print("urrrrrrrrrrrrrrrrr",ur)
for i in (ur):
    url.append(i['href'])
    j=len(url)
# print('I m url ',url)

# getting data of allurls and filter it with intersted url
aur=soup.find_all("a")
for i in (aur):
    if (i.get('href') !=  '#'):
        if (i.get('href') != '#main'):
            if (i.get('href') != url):
                 allUrl.append(i['href']) # non intesring url

    j=len(url)

# getting data of tittle
tit=soup.find_all("a",class_ ="url",limit=10)
# print(tit)
for i in (tit):
    tittle.append(i['title'])
    j=len(url)

print("print I m Titile",tittle,len(tittle))
print("print I m url",url,len(url))
print("print I m image",image,len(image))
print("print I m desc",desc,len(desc))
print("print I m d_month",d_month,len(d_month))
print("print I m d_day",d_day,len(d_day))






# converting in Csv of event 2 website
df={'Title':tittle,'URL':url,'Image':image,'Description':desc,'Month':d_month,'day':d_day}
dataset=pd.DataFrame(data=df)

print('data',dataset)
dataset.to_csv('event1.csv')
df1=pd.read_csv('event1.csv')
df1.shape


# intersting url into csv

df={'Interesting_url':url}
Iu=pd.DataFrame(data=df)
print('data',Iu)
Iu.to_csv('Intersting_url.csv')
df2=pd.read_csv('Intersting_url.csv')
df2.shape



# storing no intersted url
df={'Nonintersting_url':allUrl}
Nu=pd.DataFrame(data=df)
print('data',Nu)
Nu.to_csv('NonIntersting_url.csv')
df3=pd.read_csv('NonIntersting_url.csv')
df3.shape


# storing data in data base for  event
print("storind data in data base for event*****************")
c.execute('CREATE TABLE IF NOT EXISTS event2 (Title, Url, Images, Description, Months, day)')
conn.commit()

df1.to_sql('event1', conn, if_exists='replace' ,index=False)

c.execute('''SELECT * FROM event1''')
for row in c.fetchall():
    print(row)

# storing data in data base for Intersting_url
print("storind data in data base for Intersting_url *****************")
c.execute('CREATE TABLE IF NOT EXISTS Intersting_url (Intersting_url)')
conn.commit()

df2.to_sql('Intersting_url', conn, if_exists='replace' ,index=False)

c.execute('''SELECT * FROM Intersting_url''')
for row in c.fetchall():
    print(row)


# storing data in data base for NonIntersting_url
print("storind data in data base for NonIntersting_url*****************")
c.execute('CREATE TABLE IF NOT EXISTS NonIntersting_url (NonIntersting_url)')
conn.commit()

df3.to_sql('NonIntersting_url', conn, if_exists='replace' ,index=False)

c.execute('''SELECT * FROM NonIntersting_url''')
for row in c.fetchall():
    print(row)










