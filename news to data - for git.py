# importing libraries
import json
import pandas as pd
import numpy as np
import re

json_file_path = "C:\\Users\\eitan\\Downloads\\masters\\cnbc_news.json"

with open(json_file_path, 'r', encoding="utf8") as j:
    cnbc_news = json.loads(j.read())


def findall(p, s):
    '''Yields all the positions of
    the pattern p in the string s.'''
    i = s.find(p)
    while i != -1:
        yield i
        i = s.find(p, i + 1)


def extracting_placments(string):
    lst_dates = [(i) for i in findall('Publish_Date', string)]
    lst_head = [(i) for i in findall("', 'Headline", string)]
    lst_headline_end = [(i) for i in findall(", 'Author'", string)]
    lst_articles_start = [(i) for i in findall("Article_Text", string)]
    lst_articles_end = [(i) for i in findall("}, 'https", string)]
    lst_articles_miss = [(i) for i in findall("Don't miss:", string)]
    return lst_dates, lst_head, lst_headline_end, lst_articles_start, lst_articles_end, lst_articles_miss


def making_data_frames(news, lst_dates, lst_head, lst_headline_end, lst_articles_start, lst_articles_end):
    date = []
    head = []
    article = []
    l = len(lst_articles_end)
    for k in range(0, l):
        date.append(news[lst_dates[k] + 12:lst_head[k]])
        head.append(news[lst_head[k] + 12:lst_headline_end[k]])
        if k == l:
            article.append(news[lst_articles_start[k] + 12:])
        else:
            article.append(news[lst_articles_start[k] + 12:lst_articles_end[k]])

    df = pd.DataFrame(zip(date, head, article), columns=["Date", "Headline", "Article"])
    return df


new_df = making_data_frames(this, lst_dates, lst_head, lst_headline_end, lst_articles_start, lst_articles_end)

years = ["2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018",
         "2019", "2020"]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December"]


def running_on_all(cnbc_news, months, years):
    for year in years:
        print(year)
        for month in months:
            news = str(cnbc_news[year][month])
            # news = news.strip('\', "")
            news = news.replace("/", "")
            lst_dates, lst_head, lst_headline_end, lst_articles_start, lst_articles_end, lst_articles_miss = extracting_placments(
                news)
            new_df = making_data_frames(news, lst_dates, lst_head, lst_headline_end, lst_articles_start,
                                        lst_articles_end)
            s = str(month + year + '.pkl')
            print(month)
            new_df.to_pickle(r'C:\\Users\\eitan\\Downloads\\masters\\' + s, compression='xz')


running_on_all(cnbc_news, months, years)

months2021 = ["January", "February", "March", "April", "May"]
year2021 = ["2021"]
running_on_all(cnbc_news, months2021, year2021)

reading = pd.read_pickle('C:\\Users\\eitan\\Downloads\\masters\\September2020.pkl', compression='xz',
                         storage_options=None)