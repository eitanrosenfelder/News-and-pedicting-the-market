# News-and-pedicting-the-market
Can I decide if to invest or not based on the news of the month before?

In this project, we (Netnael Tavisal, Ayelet Taub and me) worked on the goal of predicting good or bad months.
This question of can we time the market is an open question we tackled here.

We did this by using sentiment analysis of the news in the CNBC (a big economic news outlet in the US, based on these results we concluded if we should invest in the coming month or not. 

At first I took the data which was stored as a dictionary in a huge json file, constructing from that a dataframe by searching and extracting the articles and their metadata.
Here is the function I wrote:
def extracting_placments(string):
    lst_dates = [(i) for i in findall('Publish_Date', string)]
    lst_head = [(i) for i in findall("', 'Headline", string)]
    lst_headline_end = [(i) for i in findall(", 'Author'", string)]
    lst_articles_start = [(i) for i in findall("Article_Text", string)]
    lst_articles_end = [(i) for i in findall("}, 'https", string)]
    lst_articles_miss = [(i) for i in findall("Don't miss:", string)]
    return lst_dates, lst_head, lst_headline_end, lst_articles_start, lst_articles_end, lst_articles_miss
   
More about that stage of work and how the files were stored can be in the file:
https://github.com/eitanrosenfelder/News-and-pedicting-the-market/blob/main/news%20to%20data%20-%20for%20git.py

The next step I did was splitting the articles to sentences, this was needed since the amount of data is huge, we wanted to select the relevant sentences and ignore the rest so we can save computing time, which is an issue with huge amounts of data, especially when using heavy models like sentiment analysis. In order to not bore the readers, I will just mention I used regex library to do so, those who want to dive deeper can see how it was done in the file and those who want can read it:
https://github.com/eitanrosenfelder/News-and-pedicting-the-market/blob/main/news%20-%20splitting%20senteces%20-%20for%20git.py

Next stage was subsetting the data by checking similarity between the headline and/or sentence to sentences which to our (mainly Ayelet, with some help of Netanel and Me) feeling represent the speciphic market sector.
Market Sector = companies from a set field, there are 11 different market sectors.
We split them to differenet sectors since we realised (I am not american;-)) in a similiar project that Netanel Tavisal led (with Ayelet Taub and Lee Assuri)
with using economic indicators that bad or good months vary between sectors and can not be predicted on the whole market at once.

This was done by selection of sentences by hand and then using cosine similarity, with using these code parts:
def prep_similarities(template_sen,name_sector):
    template_sen_embeddings = model.encode(template_sen)
    return template_sen_embeddings

def get_scores(template_sen_embeddings, df,col,name_sector):
    headlines_list = df[col].tolist()
    sen_list_embeddings = model.encode(headlines_list)
    cosine_scores = util.pytorch_cos_sim(template_sen_embeddings, sen_list_embeddings)
    
More can be seen in the file:
https://github.com/eitanrosenfelder/News-and-pedicting-the-market/blob/main/news%20-%20simarity%20of%20senteces%20and%20headline%20to%20sectors%20-%20for%20git.py


Then we (Netanel and me) applied the FinBert sentiment analysis in order to give a score for each sentence with the following rates:
scores = {'neutral': 0, 'positive': 1 , 'negative':-1}

The functions and the scoring is presented in the following code file:
https://github.com/eitanrosenfelder/News-and-pedicting-the-market/blob/main/news%20-%20FinBERT%20scoring%20-%20for%20git.py

After that, I set a threshold for the minimal similarity between the sentences to the sentences we selected to represent the sectors (or the most similiar sentence), this threshold cuts the amount of the sentences we observe, and then took an average of the finbert score. the subsetting function was very simple:
def subsetting_df(df, col, p):
    new_df = df[(df[col] >= p)]
    return new_df
The code file of theis stage of the project is over here:
https://github.com/eitanrosenfelder/News-and-pedicting-the-market/blob/main/calculating_scores_for_all.py


Here I got to forming the Y data, using ETFs as different sectors, Collecting the financial information from yfinance library with following code:
import yfinance as yf
sectors = ["XLE","XLB","XLI","XLY","XLP","XLV","XLF","XLK","VOX","XLU","VNQ"]
for s in range(0,len(sectors)):
    sector = str(sectors[s])
    df_sector = pd.DataFrame(yf.download(tickers=sector, start=start, end=end, interval="1d"))
    df_sector = df_sector.groupby(pd.Grouper(freq="M")).nth(0)
    df_sector = df_sector["Adj Close"]
    df_sector = pd.DataFrame(df_sector.pct_change().shift(-1))
    
More information can be seen in the code file:
https://github.com/eitanrosenfelder/News-and-pedicting-the-market/blob/main/news%20-%20coverting%20scores%20to%20x%20and%20-%20for%20git.py

At last, I used a few different models (Logistic Regression, Ridge Regression, ElasticNet Regression, XGBoost and Random Forest to classify the coming month if we expect it to be a good month (possitive returns) or not, using Cross Validation with some of the models for setting the best hyperparameters.
After that I evaluated the models on the test data (2012-2014) with selecting the best ones,
based on trying to balance the misclassification of each type for each sector.
The code can be observed here:
https://github.com/eitanrosenfelder/News-and-pedicting-the-market/blob/main/news%20-%20prediction%20and%20checking%20accuracy%20-%20for%20git.py

At last I chose those models and implemented them on the validation data (2015-2019+) 
and achieved returns a bit higher then the "spy" or "rsp" for the same time zone:)
