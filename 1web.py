from bs4 import BeautifulSoup as bs
import requests
import re
import csv
import  pandas as pd

# made data base
import sqlite3
conn=sqlite3.connect('Test1.db')
c=conn.cursor()
conn=sqlite3.connect('Test1.db')
c=conn.cursor()



newevent=[]
allLinks=[]
intersting_url=[]
not_intersted_url=[]

N_name=[]
T_type=[]
Dt=[]
# C_cost=[]
D_des=[]
I_im=[]
baseurl="https://insider.in"

r = requests.get("https://insider.in/all-digital-events-in-online?priceFilter=free")
soup = bs(r.content, "lxml")
for li in soup.find_all('a'):
    allLinks.append(baseurl+li['href'])
# print("I m all links ot website**********************************",allLinks) # all website links



event=soup.find_all('li',class_='card-list-item',limit=10)
# print(event)
evnetlinlks=[]
for item in event:
    for link in item.find_all('a',href=True):
        # print(link['href'])
        evnetlinlks.append(baseurl+link['href'])
        # print(evnetlinlks)
# print(len(evnetlinlks))



#event data getting :

for link in  evnetlinlks:
    r=requests.get(link)
    soup1 = bs(r.content, "lxml")
    name=soup1.find('h1',class_="css-1izdngw").text.strip() # for Tittle
    N_name.append(name)

    type=soup1.find('p',class_="css-hc3kyf").text.strip() # for Type
    T_type.append(type)


    dt=soup1.find('p',class_="css-8hlgow").text.strip() #for Date and Time
    Dt.append(dt)

    # try:
    # cost=soup1.find('p',class_="css-q525hq").text.strip() # for Cost
    # C_cost.append(cost)
    # except:
    #     cost ="no define"
    #     C_cost.append(cost)

    desc=soup1.find('section',class_="text text-left css-1rzyjn1").text # for description
    D_des.append(desc)


    img = soup1.find('div', class_="css-79elbk") # for Img

    for i in img.find_all('img'):

            img1=(i.get('src'))
            I_im.append(img1)


    # print(newevent)
    for i in allLinks:
        if(i != evnetlinlks):
                not_intersted_url.append(i)
print(not_intersted_url)# intetresting url

print("Hii I M tittle :",N_name)
print("Hii I M Images  :",I_im)
print("Hii I M Description :",D_des)
print("Hii I M Date and Time :",Dt)
print("Hii I M Type :",T_type)
# print("Hii I M Cost :",cost)
print("Hii I M Interested_url :",evnetlinlks)


# made event file to csv
print("made event to csv***************************************************************************")
df={'Title':N_name,'Image':I_im,'Description':D_des,'Date and Time':Dt,'Type':T_type,'Interested_url':evnetlinlks}
dataset=pd.DataFrame(data=df)


print('data',dataset)

dataset.to_csv('event2.csv')
df1=pd.read_csv('event2.csv')
df1.shape

# storing intersting and non intersting url into csv format


print("made Interested url  to csv***************************************************************************")
df={'Intersting_url':evnetlinlks}
Iu=pd.DataFrame(data=df)


print('data',Iu)

Iu.to_csv('intersting_url.csv')
df2=pd.read_csv('intersting_url.csv')
df2.shape


print("made Non intersted  to csv***************************************************************************")

# non intersting url converting in to csv
df={'NonIntersting_url':not_intersted_url}
Nu=pd.DataFrame(data=df)


print('data',Nu)

Nu.to_csv('not_intersted_url.csv')
df3=pd.read_csv('not_intersted_url.csv')
df3.shape



# database creation for evnet2
print("data base for All event database ******************************************************************************************")

c.execute('CREATE TABLE IF NOT EXISTS event2 (Title, Image, Description, Date_Time, Cost, Type, Interested_url)')
conn.commit()

df1.to_sql('event2', conn, if_exists='replace' ,index=False)

c.execute('''SELECT * FROM event2''')
for row in c.fetchall():
    print(row)




# database creation for Interested url
print("data base for  intested url ****************************************************************************************************************")


c.execute('CREATE TABLE IF NOT EXISTS event2 ( Interested_url)')
conn.commit()
df2.to_sql('Interested_url', conn, if_exists='replace' ,index=False)

c.execute('''SELECT * FROM Interested_url''')
for row in c.fetchall():
    print(row)


# database creation for Not Interested url
print("data base for Non intested url **********************************************************************************************")

c.execute('CREATE TABLE IF NOT EXISTS not_intersted_url (Non_Intersted_Url)')
conn.commit()
df3.to_sql('not_intersted_url',conn,if_exists='replace',index=False)

c.execute('''SELECT * FROM not_intersted_url''')
for row in c.fetchall():
    print(row)










