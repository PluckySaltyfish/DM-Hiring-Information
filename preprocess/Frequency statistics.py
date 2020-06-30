import pandas as pd
import numpy as np
def pre_preprocess(df):
    b = df['c_scale'].value_counts().index[0]
    df['c_scale'] = df['c_scale'].replace('5年', b)
    df['c_scale'] = df['c_scale'].replace('3年', b)
    df['c_scale'] = df['c_scale'].replace('10年', b)
    df['c_scale'] = df['c_scale'].replace('以下', b)
    df['c_scale'] = df['c_scale'].replace('验', b)
    df['s_min'] = df['s_min'].replace('1000元/月以下 ', 1)
    df['s_min'] = df['s_min'].replace('100000元/月以上 ', 100)
    df['s_max'] = df['s_max'].replace('1000元/月以下 ', 1)
    df['s_max'] = df['s_max'].replace('100000元/月以上 ', 100)
    return df

# 缺失值处理前频数统计
def Frequency_statistics(df):
    # c_nature
    c_nature_counts = df['c_nature'].value_counts()
    df_c_nature = pd.DataFrame({"c_nature": c_nature_counts.index, "frequency": c_nature_counts.values})
    df_c_nature = df_c_nature.append([{"c_nature": 'Nan', "frequency": df['c_nature'].isnull().sum()}],
                                     ignore_index=True)
    df_c_nature = df_c_nature.sort_values(by='frequency', ascending=False)
    df_c_nature.to_csv('df_c_nature.csv', encoding='utf-8', index=None)
    # c_scale
    c_scale_counts = df['c_scale'].value_counts()
    df_c_scale = pd.DataFrame({"c_scale": c_scale_counts.index, "frequency": c_scale_counts.values})
    df_c_scale = df_c_scale.append([{"c_scale": 'Nan', "frequency": df['c_scale'].isnull().sum()}], ignore_index=True)
    df_c_scale = df_c_scale.sort_values(by='frequency', ascending=False)
    df_c_scale.to_csv('df_c_scale.csv', encoding='utf-8', index=None)
    # w_experience
    w_experience_counts = df['w_experience'].value_counts()
    df_w_experience = pd.DataFrame({"w_experience": w_experience_counts.index, "frequency": w_experience_counts.values})
    df_w_experience_order = ["w_experience", "frequency"]
    df_w_experience = df_w_experience[df_w_experience_order]
    df_w_experience.to_csv('df_w_experience.csv', encoding='utf-8', index=None)
    # education
    education_counts = df['education'].value_counts()
    df_education = pd.DataFrame({"education": education_counts.index, "frequency": education_counts.values})
    df_education.to_csv('df_education.csv', encoding='utf-8', index=None)
    # s_min
    s_min_counts = df['s_min'].value_counts()
    df_s_min = pd.DataFrame({"s_min": s_min_counts.index, "frequency": s_min_counts.values})
    df_s_min_order = ["s_min", "frequency"]
    df_s_min = df_s_min[df_s_min_order]
    df_s_min = df_s_min.append([{"s_min": 'Nan', "frequency": df['s_min'].isnull().sum()}], ignore_index=True)
    df_s_min = df_s_min.sort_values(by='frequency', ascending=False)
    df_s_min.to_csv('df_s_min.csv', encoding='utf-8', index=None)
    # s_max
    s_max_counts = df['s_max'].value_counts()
    df_s_max = pd.DataFrame({"s_max": s_max_counts.index, "frequency": s_max_counts.values})
    df_s_max_order = ["s_max", "frequency"]
    df_s_max = df_s_max[df_s_max_order]
    df_s_max = df_s_max.append([{"s_max": 'Nan', "frequency": df['s_max'].isnull().sum()}], ignore_index=True)
    df_s_max = df_s_max.sort_values(by='frequency', ascending=False)
    df_s_max.to_csv('df_s_max.csv', encoding='utf-8', index=None)
    # vacancies
    vacancies_counts = df['vacancies'].value_counts()
    df_vacancies = pd.DataFrame({"vacancies": vacancies_counts.index, "frequency": vacancies_counts.values})
    df_vacancies_order = ["vacancies", "frequency"]
    df_vacancies = df_vacancies[df_vacancies_order]
    df_vacancies = df_vacancies.append([{"vacancies": 'Nan', "frequency": df['vacancies'].isnull().sum()}],
                                       ignore_index=True)
    df_vacancies = df_vacancies.sort_values(by='frequency', ascending=False)
    df_vacancies.to_csv('df_vacancies.csv', encoding='utf-8', index=None)

def Frequency_statistics1(df):
    # 缺失值处理后频数统计
    # c_nature
    c_nature_counts1 = df1['c_nature'].value_counts()
    df_c_nature1 = pd.DataFrame({"c_nature": c_nature_counts1.index, "frequency": c_nature_counts1.values})
    df_c_nature1.to_csv('df_c_nature1.csv', encoding='utf-8', index=None)
    # c_scale
    c_scale_counts1 = df1['c_scale'].value_counts()
    df_c_scale1 = pd.DataFrame({"c_scale": c_scale_counts1.index, "frequency": c_scale_counts1.values})
    df_c_scale1.to_csv('df_c_scale1.csv', encoding='utf-8', index=None)
    # w_experience
    w_experience_counts1 = df1['w_experience'].value_counts()
    df_w_experience1 = pd.DataFrame(
        {"w_experience": w_experience_counts1.index, "frequency": w_experience_counts1.values})
    df_w_experience_order1 = ["w_experience", "frequency"]
    df_w_experience1 = df_w_experience1[df_w_experience_order1]
    df_w_experience1.to_csv('df_w_experience1.csv', encoding='utf-8', index=None)
    # education
    education_counts1 = df1['education'].value_counts()
    df_education1 = pd.DataFrame({"education": education_counts1.index, "frequency": education_counts1.values})
    df_education1.to_csv('df_education1.csv', encoding='utf-8', index=None)
    # s_min
    s_min_counts1 = df1['s_min'].value_counts()
    df_s_min1 = pd.DataFrame({"s_min": s_min_counts1.index, "frequency": s_min_counts1.values})
    df_s_min_order1 = ["s_min", "frequency"]
    df_s_min1 = df_s_min1[df_s_min_order1]
    df_s_min1.to_csv('df_s_min1.csv', encoding='utf-8', index=None)
    # s_max
    s_max_counts1 = df1['s_max'].value_counts()
    df_s_max1 = pd.DataFrame({"s_max": s_max_counts1.index, "frequency": s_max_counts1.values})
    df_s_max_order1 = ["s_max", "frequency"]
    df_s_max1 = df_s_max1[df_s_max_order1]
    df_s_max1.to_csv('df_s_max1.csv', encoding='utf-8', index=None)
    # vacancies
    vacancies_counts1 = df1['vacancies'].value_counts()
    df_vacancies1 = pd.DataFrame({"vacancies": vacancies_counts1.index, "frequency": vacancies_counts1.values})
    df_vacancies_order1 = ["vacancies", "frequency"]
    df_vacancies1 = df_vacancies1[df_vacancies_order1]
    df_vacancies1.to_csv('df_vacancies1.csv', encoding='utf-8', index=None)


if __name__ == '__main__':
    path = 'D:\\BIT\\Course\\数据挖掘\\大作业\\process\\3.csv'
    f = open(path, encoding='UTF-8')
    df = pd.read_csv(f)
    df = df.replace(' ', np.NaN)
    df=pre_preprocess(df)
    Frequency_statistics(df)
    path1 = 'D:\\BIT\\Course\\数据挖掘\\大作业\\process\\5.csv'
    f1 = open(path1, encoding='UTF-8')
    df1 = pd.read_csv(f1)
    Frequency_statistics1(df1)
