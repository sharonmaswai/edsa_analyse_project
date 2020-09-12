import pandas as pd
import numpy as np

def dictionary_of_metrics(items):
    key=['mean', 'median', 'var', 'std', 'min', 'max']
    value=[np.mean(items),np.median(items), np.var(items, ddof=1), np.std(items, ddof=1), np.min(items),np.max(items)]
    values=[]
    for i in value:
        val=round(i, 2)
        values.append(val)
    zipped=zip(key, values)
    column_metrics=dict(zipped)
    
    return column_metrics

def five_num_summary(items):
    key=['max', 'median', 'min', 'q1', 'q3']
    value=[np.max(items),np.median(items), np.min(items),np.quantile(items, 0.25), np.quantile(items, 0.75)]
    values=[]
    for x in value:
        val=round(x, 2)
        values.append(val)
    zipped=zip(key, values)
    summary=dict(zipped)
    
    return summary
def date_parser(dates):
    date=[]
    for x in dates:
      new_date=x[0:10]
      date.append(new_date)
    return date 
def extract_municipality_hashtags(df):
    muni = df['Tweets'].astype(object).to_list()
    mun=[]
    hash=[[]]
    for x in muni:
        if x in mun_dict.keys():
        mun.append(x)
        else:
        mun.append(np.nan)  
    df['municipality']=mun
    df['Tweets']=  df['Tweets'].astype('str')
    df['hashtags']=  df['Tweets'].apply(lambda x: " ".join(x for x in x.split() if x.startswith('#')))
    df['hashtags']=df['hashtags'].replace([''],np.nan)
    return df       
def number_of_tweets_per_day(df):
    df['Date']=date_parser(dates)

    df['Date']=pd.to_datetime(df['Date']) 
    df=pd.DataFrame(df.groupby('Date')['Tweets'].count())
    return df        
def word_splitter(df):
    split=[]
    for i in df['Tweets']:
        lower=i.lower()
        string=str(lower).split()
        split.append(string)
    df['split tweets']=split  
    return df    
def stop_words_remover(df):
    word_splitter(df)
    # stop=[]
    # split=df['split tweets'].to_list()
    stop=stop_words_dict.get('stopwords')
    df['split tweets']=  df['split tweets'].astype('str')
    df['Without Stop Words']=  df['split tweets'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))
    
    return df    