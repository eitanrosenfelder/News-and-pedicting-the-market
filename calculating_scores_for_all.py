import pandas as pd

def subsetting_df(df, col, p):
    new_df = df[(df[col] >= p)]
    return new_df
col_names = ['max_score_Health_care_Headline',
       'mean_score_Health_care_Headline', 'max_score_Materials_Headline',
       'mean_score_Materials_Headline', 'max_score_Utilities_Headline',
       'mean_score_Utilities_Headline', 'max_score_Energy_Headline',
       'mean_score_Energy_Headline',
       'max_score_Consumer_discretionary_Headline',
       'mean_score_Consumer_discretionary_Headline',
       'max_score_Consumer_staples_Headline',
       'mean_score_Consumer_staples_Headline', 'max_score_Financials_Headline',
       'mean_score_Financials_Headline',
       'max_score_Telecommunications_Headline',
       'mean_score_Telecommunications_Headline',
       'max_score_Technology_Headline', 'mean_score_Technology_Headline',
       'max_score_Real_estate_Headline', 'mean_score_Real_estate_Headline',
       'max_score_Consumer_staples',
       'mean_score_Consumer_staples', 'max_score_Technology',
       'mean_score_Technology', 'max_score_Consumer_discretionary',
       'mean_score_Consumer_discretionary', 'max_score_Health_care',
       'mean_score_Health_care', 'max_score_Energy',
       'mean_score_Energy', 'max_score_Financials', 'mean_score_Financials',
       'max_score_Real_estate', 'mean_score_Real_estate',
       'max_score_Materials', 'mean_score_Materials', 'max_score_Industrials',
       'mean_score_Industrials', 'max_score_Utilities', 'mean_score_Utilities',
       'max_score_Telecommunications', 'mean_score_Telecommunications',
       'max_score_Relavent', 'mean_score_Relavent']

P = (0.1, 0.2, 0.3, 0.4)

def running_on_all(months,years):
       means_df = pd.DataFrame(columns=('max_score_Health_care_Headline01',
                                        'mean_score_Health_care_Headline01', 'max_score_Materials_Headline01',
                                        'mean_score_Materials_Headline01', 'max_score_Utilities_Headline01',
                                        'mean_score_Utilities_Headline01', 'max_score_Energy_Headline01',
                                        'mean_score_Energy_Headline01',
                                        'max_score_Consumer_discretionary_Headline01',
                                        'mean_score_Consumer_discretionary_Headline01',
                                        'max_score_Consumer_staples_Headline01',
                                        'mean_score_Consumer_staples_Headline01', 'max_score_Financials_Headline01',
                                        'mean_score_Financials_Headline01',
                                        'max_score_Telecommunications_Headline01',
                                        'mean_score_Telecommunications_Headline01',
                                        'max_score_Technology_Headline01', 'mean_score_Technology_Headline01',
                                        'max_score_Real_estate_Headline01', 'mean_score_Real_estate_Headline01',
                                        'max_score_Consumer_staples01',
                                        'mean_score_Consumer_staples01', 'max_score_Technology01',
                                        'mean_score_Technology01', 'max_score_Consumer_discretionary01',
                                        'mean_score_Consumer_discretionary01', 'max_score_Health_care01',
                                        'mean_score_Health_care01', 'max_score_Energy01',
                                        'mean_score_Energy01', 'max_score_Financials01', 'mean_score_Financials01',
                                        'max_score_Real_estate01', 'mean_score_Real_estate01',
                                        'max_score_Materials01', 'mean_score_Materials01', 'max_score_Industrials01',
                                        'mean_score_Industrials01', 'max_score_Utilities01', 'mean_score_Utilities01',
                                        'max_score_Telecommunications01', 'mean_score_Telecommunications01',
                                        'max_score_Relavent01', 'mean_score_Relavent01',
                                        'max_score_Health_care_Headline02',
                                        'mean_score_Health_care_Headline02', 'max_score_Materials_Headline02',
                                        'mean_score_Materials_Headline02', 'max_score_Utilities_Headline02',
                                        'mean_score_Utilities_Headline02', 'max_score_Energy_Headline02',
                                        'mean_score_Energy_Headline02',
                                        'max_score_Consumer_discretionary_Headline02',
                                        'mean_score_Consumer_discretionary_Headline02',
                                        'max_score_Consumer_staples_Headline02',
                                        'mean_score_Consumer_staples_Headline02', 'max_score_Financials_Headline02',
                                        'mean_score_Financials_Headline02',
                                        'max_score_Telecommunications_Headline02',
                                        'mean_score_Telecommunications_Headline02',
                                        'max_score_Technology_Headline02', 'mean_score_Technology_Headline02',
                                        'max_score_Real_estate_Headline02', 'mean_score_Real_estate_Headline02',
                                        'max_score_Consumer_staples02',
                                        'mean_score_Consumer_staples02', 'max_score_Technology02',
                                        'mean_score_Technology02', 'max_score_Consumer_discretionary02',
                                        'mean_score_Consumer_discretionary02', 'max_score_Health_care02',
                                        'mean_score_Health_care02', 'max_score_Energy02',
                                        'mean_score_Energy02', 'max_score_Financials02', 'mean_score_Financials02',
                                        'max_score_Real_estate02', 'mean_score_Real_estate02',
                                        'max_score_Materials02', 'mean_score_Materials02', 'max_score_Industrials02',
                                        'mean_score_Industrials02', 'max_score_Utilities02', 'mean_score_Utilities02',
                                        'max_score_Telecommunications02', 'mean_score_Telecommunications02',
                                        'max_score_Relavent02', 'mean_score_Relavent02',
                                        'max_score_Health_care_Headline03',
                                        'mean_score_Health_care_Headline03', 'max_score_Materials_Headline03',
                                        'mean_score_Materials_Headline03', 'max_score_Utilities_Headline03',
                                        'mean_score_Utilities_Headline03', 'max_score_Energy_Headline03',
                                        'mean_score_Energy_Headline03',
                                        'max_score_Consumer_discretionary_Headline03',
                                        'mean_score_Consumer_discretionary_Headline03',
                                        'max_score_Consumer_staples_Headline03',
                                        'mean_score_Consumer_staples_Headline03', 'max_score_Financials_Headline03',
                                        'mean_score_Financials_Headline03',
                                        'max_score_Telecommunications_Headline03',
                                        'mean_score_Telecommunications_Headline03',
                                        'max_score_Technology_Headline03', 'mean_score_Technology_Headline03',
                                        'max_score_Real_estate_Headline03', 'mean_score_Real_estate_Headline03',
                                        'max_score_Consumer_staples03',
                                        'mean_score_Consumer_staples03', 'max_score_Technology03',
                                        'mean_score_Technology03', 'max_score_Consumer_discretionary03',
                                        'mean_score_Consumer_discretionary03', 'max_score_Health_care03',
                                        'mean_score_Health_care03', 'max_score_Energy03',
                                        'mean_score_Energy03', 'max_score_Financials03', 'mean_score_Financials03',
                                        'max_score_Real_estate03', 'mean_score_Real_estate03',
                                        'max_score_Materials03', 'mean_score_Materials03', 'max_score_Industrials03',
                                        'mean_score_Industrials03', 'max_score_Utilities03', 'mean_score_Utilities03',
                                        'max_score_Telecommunications03', 'mean_score_Telecommunications03',
                                        'max_score_Relavent03', 'mean_score_Relavent03',
                                        'max_score_Health_care_Headline04',
                                        'mean_score_Health_care_Headline04', 'max_score_Materials_Headline04',
                                        'mean_score_Materials_Headline04', 'max_score_Utilities_Headline04',
                                        'mean_score_Utilities_Headline04', 'max_score_Energy_Headline04',
                                        'mean_score_Energy_Headline04',
                                        'max_score_Consumer_discretionary_Headline04',
                                        'mean_score_Consumer_discretionary_Headline04',
                                        'max_score_Consumer_staples_Headline04',
                                        'mean_score_Consumer_staples_Headline04', 'max_score_Financials_Headline04',
                                        'mean_score_Financials_Headline04',
                                        'max_score_Telecommunications_Headline04',
                                        'mean_score_Telecommunications_Headline04',
                                        'max_score_Technology_Headline04', 'mean_score_Technology_Headline04',
                                        'max_score_Real_estate_Headline04', 'mean_score_Real_estate_Headline04',
                                        'max_score_Consumer_staples04',
                                        'mean_score_Consumer_staples04', 'max_score_Technology04',
                                        'mean_score_Technology04', 'max_score_Consumer_discretionary04',
                                        'mean_score_Consumer_discretionary04', 'max_score_Health_care04',
                                        'mean_score_Health_care04', 'max_score_Energy04',
                                        'mean_score_Energy04', 'max_score_Financials04', 'mean_score_Financials04',
                                        'max_score_Real_estate04', 'mean_score_Real_estate04',
                                        'max_score_Materials04', 'mean_score_Materials04', 'max_score_Industrials04',
                                        'mean_score_Industrials04', 'max_score_Utilities04', 'mean_score_Utilities04',
                                        'max_score_Telecommunications04', 'mean_score_Telecommunications04',
                                        'max_score_Relavent04', 'mean_score_Relavent04'))

       row_count = -1
       for year in years:
            print(year)
            for month in months:
                date = str(month+year)
                sub = str(month+year+'finbert_score.pkl')
                try:
                    row = []
                    df = pd.read_pickle(r'C:\\Users\\eitan\\Downloads\\masters\\'+sub, compression='xz')
                    row_count += 1
                    if len(df) != 0:
                           for k in P:
                               for j in col_names:
                                   J = str(j)
                                   df2 = subsetting_df(df, col=J, p=k)
                                   row.append(df2["finbert_score"].mean())
                    means_df.loc[date] = row


                    print(month)
                except FileNotFoundError:
                    continue
                except EOFError:
                    continue
       means_df.to_pickle(r'C:\\Users\\eitan\\Downloads\\masters\\scores_for_all_try.pkl', compression='xz')

years = ["2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2014","2015","2016","2017","2018","2019","2020","2021"]
months = ["January", "February", "March", "April", "May","June", "July", "August", "September", "October", "November", "December"]
running_on_all(months,years)

