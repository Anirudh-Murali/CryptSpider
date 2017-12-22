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



# start_date = "20171001"
# end = "end=20171001"
# date = "/?start=20171001&end=20171201"

# home_page = "https://coinmarketcap.com/currencies/"
# url = str(home_page+currency+"/historical-data"+date)
# print(url)
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
    # extract_weekdata(size)
    df['weekday'] = pd.Series(f_weekday)
    # df
    # print(df)
    i = 0
    new = []
    # size = len(df)
    while i < size_df:
        if df['weekday'][i]==6:
    #         print("found")
            new.append(df.iloc[i,:])
        i+=1
    # print(new)
    sundays = pd.DataFrame(new)
    # print(sundays)
    sunday_matrix = pd.concat([sundays.Close, sundays.month], axis=1, join_axes=[sundays.Open.index])
    sunday_matrix
    # print(new)
    # sundays


    size1 = len(sunday_matrix)
    i = size1 - 1
    # print(size1)
    b = {}
    c= {}
    while i > 0:
        j = 1
        cur_month = sunday_matrix.iloc[i,1]
    #     print(cur_month)
        b = {}
        while True:
            if cur_month == sunday_matrix.iloc[i,1]:
                key = 'Week ' + str(j)
                j+=1
    #             value = sunday_matrix.loc[sunday_matrix['month'] == month_keys[k]]
    #     value = value.Open
                b[key] = sunday_matrix.iloc[i,0]
            else:
                i += 1
                break
            i-=1
        c[str(cur_month)] = b
        i -= 1
    print(c)
    # c= json.dumps(c)
    flash = pd.DataFrame(c)
    d = {}

    flash.index.name = 'week_name'

    flash['index'] = currency

    d['aisk'] = flash
    d['bitch'] = flash
    p1 = pd.Panel(data=d)
    p1.to_excel("Output/"+currency+".xls")

input_ = pd.read_csv("input.csv")
# input_[0]
# for(c in )
for c in input_:
    populate(c)
