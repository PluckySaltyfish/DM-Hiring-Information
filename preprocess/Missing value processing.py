import pandas as pd
import numpy as np
from scipy import stats
def pre_preprocess(df):
    df = df.replace(' ', np.NaN)
    df['s_min'] = df['s_min'].replace('面议 ', np.NaN)
    df['s_min'] = df['s_min'].replace('1000元/月以下 ', 1)
    df['s_min'] = df['s_min'].replace('100000元/月以上 ', 100)
    df['s_max'] = df['s_max'].replace('面议 ', np.NaN)
    df['s_max'] = df['s_max'].replace('1000元/月以下 ', 1)
    df['s_max'] = df['s_max'].replace('100000元/月以上 ', 100)
    df['vacancies'] = df['vacancies'].replace('若干', np.NaN)
    print(df.shape[0])
    print(df.isnull().sum())
    return df

def Missing_value_processing(df,column_name):
    for index, row in df.iterrows():
        if row[column_name] is np.NaN:
            flag = 0
            df1 = df.loc[df['c_name'] == row['c_name']]
            for index1, row1 in df1.iterrows():
                if row1[column_name] is np.NaN:
                    continue
                else:
                    df.at[index, column_name] = row1[column_name]
                    flag = 1
                    break
            if flag == 0:
                df.at[index, column_name] = df[column_name].value_counts().index[0]
    return df

def preprocess1(df):
    df = df.dropna(subset=['c_name'])
    df['w_field'] = df['w_field'].fillna(df['w_field'].value_counts().index[0])
    df['s_min'] = pd.to_numeric(df['s_min'], errors='coerce')
    df['s_min'] = df['s_min'].fillna(stats.mode(df['s_min'])[0][0])
    df['s_max'] = pd.to_numeric(df['s_max'], errors='coerce')
    df['s_max'] = df['s_max'].fillna(stats.mode(df['s_max'])[0][0])
    df['vacancies'] = pd.to_numeric(df['vacancies'], errors='coerce')
    df['vacancies'] = df['vacancies'].fillna(stats.mode(df['vacancies'])[0][0])
    for index, row in df.iterrows():
        if row['description'] is np.NaN:
            df.at[index, 'description'] = row['j_name']
    print(df.isnull().sum())
    print(df.info())
    return df

def preprocess2(df):
    b = df['c_scale'].value_counts().index[0]
    df['c_scale'] = df['c_scale'].replace('5年', b)
    df['c_scale'] = df['c_scale'].replace('3年', b)
    df['c_scale'] = df['c_scale'].replace('10年', b)
    df['c_scale'] = df['c_scale'].replace('以下', b)
    df['c_scale'] = df['c_scale'].replace('验', b)
    df=Missing_value_processing(df,'c_nature')
    df=Missing_value_processing(df,'c_scale')
    df=Missing_value_processing(df,'welfare')
    return df

if __name__ == '__main__':
    print(1)
    path = 'D:\\BIT\\Course\\数据挖掘\\大作业\\process\\3.csv'
    f = open(path, encoding='UTF-8')
    df = pd.read_csv(f)
    print(df.head())
    df=pre_preprocess(df)
    df=preprocess1(df)
    df=preprocess2(df)
    df.to_csv('Missing_value_processed_data.csv',encoding='utf-8',index=None)
