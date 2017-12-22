import pandas as pd
import requests
import json
from bs4 import BeautifulSoup
from nltk.tokenize import RegexpTokenizer
import datetime
import calendar

def extract_weekdata(size,df):
    i = 0
    f_weekday = []
    # size = len(df)
    while i < size:
        weekday = calendar.weekday(df['year'][i], df['month'][i], df['day'][i])
        f_weekday.append(weekday)
        i += 1
    return f_weekday
currency = "lisk"

def populate(currency):
    res = requests.get("https://coinmarketcap.com/currencies/"+currency+"/historical-data/?start=20170101&end=20171231")
    soup = BeautifulSoup(res.content,'lxml')
    table = soup.find_all('table')[0]
    df = pd.read_html(str(table))
    final = df[0].to_json(orient='records')
    type(final)
    final = json.loads(final)

    data = json.dumps(final)
    df = pd.read_json(data)

    df['day'] = [d.day for d in df['Date']]
    df['month'] = [d.month for d in df['Date']]
    df['year'] = [d.year for d in df['Date']]
    size_df = len(df)
    f_weekday=extract_weekdata(size_df,df)
    df['weekday'] = pd.Series(f_weekday)
    i = 0
    new = []
    while i < size_df:
        if df['weekday'][i]==6:
            new.append(df.iloc[i,:])
        i+=1
    sundays = pd.DataFrame(new)
    sunday_matrix = pd.concat([sundays.Close, sundays.month], axis=1, join_axes=[sundays.Open.index])
    sunday_matrix

    size1 = len(sunday_matrix)
    i = size1 - 1
    b = {}
    c= {}
    while i > 0:
        j = 1
        cur_month = sunday_matrix.iloc[i,1]
        b = {}
        while True:
            if cur_month == sunday_matrix.iloc[i,1]:
                key = 'Week ' + str(j)
                j+=1
                b[key] = sunday_matrix.iloc[i,0]
            else:
                i += 1
                break
            i-=1
        c[str(cur_month)] = b
        i -= 1
    print(c)
    flash = pd.DataFrame(c)
    d = {}

    flash.index.name = 'week_name'

    flash['index'] = currency

    d['aisk'] = flash
    d['bitch'] = flash
    p1 = pd.Panel(data=d)
    p1.to_excel("Output/"+folder_name+"/"+currency+".xls")


input_ = pd.read_csv("input.csv")
folder_name = "test"                                           #Name of the directory you wanna store the results to. Note you can only pass existing directories
i = 0
for c in input_:
    print("-----------------------------------"+str(c)+"------------------------------------------------")
    populate(c)
