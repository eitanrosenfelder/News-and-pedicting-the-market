
import pandas as pd
import numpy as np
import re

def subsetting_df(df, col, p):
    new_df = df[(df[col] >= p)]
    return new_df

df_1 = subsetting_df(df_try, 'max_score_Relavent', p=0.3)

years = ["2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020"]
months = ["January", "February", "March", "April", "May","June", "July", "August", "September", "October", "November", "December"]

def running_on_all(months,years):
    for year in years:
        print(year)
        for month in months:
            s = str(month+year+'.pkl')
            sub = str(month+year+'sub'+'.pkl')
            df = pd.read_pickle(r'C:\\Users\\eitan\\Downloads\\masters\\'+s, compression='xz')
            if len(df) != 0:
                new_df = subsetting_df(df, 'max_score_Relavent', p=0.3)
                print(month)
                new_df.to_pickle(r'C:\\Users\\eitan\\Downloads\\masters\\'+sub, compression='xz')
running_on_all(months,years)

months2021 = ["January", "February", "March", "April"]
year2021 = ["2021"]
running_on_all(months2021,year2021)

alphabets= "([A-Za-z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever|[$0-9])"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov)"

def split_into_sentences(text):
    text = " " + text + "  "
    text = text.replace("\n"," ")
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub(r'(\d+)\.(\d+)',r"\1_\2", text)
    text = re.sub("\s" + alphabets + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + alphabets + "[.]"," \\1<prd>",text)
    if "”" in text: text = text.replace(".”","”.")
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("<prd>",".")
    text = re.sub(r'(\d+)\_(\d+)',r"\1.\2", text)
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences

def split_articles(df):
    dfnew = pd.DataFrame(data=None,columns=['Date', 'Headline', 'max_score_Health_care_Headline',
       'mean_score_Health_care_Headline', 'max_score_Materials_Headline', 'mean_score_Materials_Headline',
       'max_score_Utilities_Headline', 'mean_score_Utilities_Headline', 'max_score_Energy_Headline',
       'mean_score_Energy_Headline', 'max_score_Consumer_discretionary_Headline',
       'mean_score_Consumer_discretionary_Headline', 'max_score_Consumer_staples_Headline',
       'mean_score_Consumer_staples_Headline', 'max_score_Financials_Headline',
       'mean_score_Financials_Headline', 'max_score_Telecommunications_Headline',
       'mean_score_Telecommunications_Headline', 'max_score_Technology_Headline',
       'mean_score_Technology_Headline', 'max_score_Real_estate_Headline',
       'mean_score_Real_estate_Headline','sentence_from_article'])

    for i in range(len(df["Article"])):
        text = df["Article"].iloc[i]
        new = split_into_sentences(text)
        for s in range(len(new)):
            dfnew.loc[s] = [df["Date"].iloc[i], df["Headline"].iloc[i], df["max_score_Health_care"].iloc[i], df["mean_score_Health_care"].iloc[i], df["max_score_Materials"].iloc[i], df["mean_score_Materials"].iloc[i], df["max_score_Utilities"].iloc[i], df["mean_score_Utilities"].iloc[i], df["max_score_Energy"].iloc[i], df["mean_score_Energy"].iloc[i], df["max_score_Consumer_discretionary"].iloc[i], df["mean_score_Consumer_discretionary"].iloc[i], df["max_score_Consumer_staples"].iloc[i], df["mean_score_Consumer_staples"].iloc[i], df["max_score_Financials"].iloc[i], df["mean_score_Financials"].iloc[i], df["max_score_Telecommunications"].iloc[i], df["mean_score_Telecommunications"].iloc[i], df["max_score_Technology"].iloc[i], df["mean_score_Technology"].iloc[i], df["max_score_Real_estate"].iloc[i], df["mean_score_Real_estate"].iloc[i], new[s]]
    return dfnew
dfnew = split_articles(df_1)

def splitting_all_articles(months,years):
    for year in years:
        print(year)
        for month in months:
            sub = str(month+year+'sub'+'.pkl')
            try:
                df = pd.read_pickle(r'C:\\Users\\eitan\\Downloads\\masters\\'+sub, compression='xz')
                if len(df) != 0:
                    dfnew = split_articles(df)
                    print(month)
                    dfnew.to_pickle(r'C:\\Users\\eitan\\Downloads\\masters\\'+sub, compression='xz')
            except FileNotFoundError:
                continue
splitting_all_articles(months,years)

splitting_all_articles(months2021,year2021)

df_s = pd.read_pickle(r'C:\\Users\\eitan\\Downloads\\masters\\January2020sub.pkl', compression='xz')