# !pip install transformers
# !pip install wrapt
# !pip install torch==1.7.0
# !pip install finbert-embedding

import pandas as pd
from transformers import BertTokenizer, BertForSequenceClassification, AutoModelForSequenceClassification, BertTokenizerFast
from tqdm import tqdm
import torch
from torch.nn.functional import softmax
import os

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('C:/Users/eitan/PycharmProjects/masters/pytorch_model.bin' , config='C:/Users/eitan/PycharmProjects/masters/tokenizer_config.json',num_labels=3)

device = torch.device('cpu')
base_path= r'C:/Users/eitan/PycharmProjects/masters/'

def get_finbert_esg_sentiments_batch(sents, model, tokenizer,  batch_size=50):
    labels = { 0: 'positive', 1: 'negative', 2: 'neutral'}
    scores = {'neutral': 0, 'positive': 1 , 'negative':-1}
    progress_bar = tqdm(total=(len(sents) // batch_size), position=0, leave=True)
    preds = []
    confidence = []
    sentiment=[]
    for batch_of_sents in chunk_list(sents, batch_size):
        inputs = tokenizer.batch_encode_plus(batch_of_sents, return_tensors='pt', padding=True, truncation=True)
        preds_probs = model(inputs['input_ids'].to(device), token_type_ids=None, attention_mask=inputs['attention_mask'].to(device))[0]
        # torch.cuda.empty_cache()
        for pp in preds_probs:
            pp = softmax(pp, dim=0)
            top = pp.topk(1)
            idxs = top.indices.tolist()
            wts = top.values.tolist()
            preds.append(labels[idxs[0]])
            confidence.append(wts[0])
            sentiment.append(scores.get(labels[idxs[0]]))
        progress_bar.update()
    return sentiment, confidence

def load_transformer_model(model_dir):
    torch.set_grad_enabled(False)
    model = BertForSequenceClassification.from_pretrained('C:/Users/eitan/PycharmProjects/masters/pytorch_model.bin',
                                                          config='C:/Users/eitan/PycharmProjects/masters/tokenizer_config.json',
                                                          num_labels=3)

    model.to(device)
    model.eval()
    tokenizer = BertTokenizerFast.from_pretrained(model_dir)
    return model, tokenizer

def chunk_list(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]



def finBert_sentiment_score(text):
    model, tokenizer = load_transformer_model(base_path)
    sentiment_list, confidence_list = get_finbert_esg_sentiments_batch(text, model, tokenizer)
    clean_sentiment = []
    confidence = 0
    for i in range(len(sentiment_list)):
        if (sentiment_list[i] !=0) and (confidence_list[i]>0.5):
            clean_sentiment.append(sentiment_list[i])
            confidence = confidence_list[i]
    negatives = clean_sentiment.count(-1)
    positives = clean_sentiment.count(1)
    sa = (positives-negatives)/(positives+negatives+0.000001)
    return sa

years = ["2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020"]
months = ["January", "February", "March", "April", "May","June", "July", "August", "September", "October", "November", "December"]

def running_on_all(months,years):
      for year in years:
          print(year)
          for month in months:
              #+'sub'
              sub = str(month+year+'sub.pkl')
              result = str(month+year+'finbert_score.pkl')
              try:
                  df = pd.read_pickle(r'C:/Users/eitan/Downloads/masters/'+sub, compression='xz')
                  if len(df) != 0:
                      if os.stat('C:/Users/eitan/Downloads/masters/'+sub).st_size > 0:
                            df['finbert_score'] = df['sentence_from_article'].apply(lambda x : finBert_sentiment_score([x]))
                            print(month)
                            df.to_pickle(r'C:/Users/eitan/Downloads/masters/'+result, compression='xz')
              except FileNotFoundError:
                  continue
              except EOFError:
                  continue

running_on_all(months,years)

year21 = ["2021"]
months21 = ["January", "February", "March", "April"]
running_on_all(months21,year21)