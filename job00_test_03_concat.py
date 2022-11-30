import pandas as pd
import glob
import datetime

data_path = glob.glob('./crawling_data_2/*.csv')
print(data_path)
df = pd.DataFrame()
for path in data_path[:-4]:
    df_temp = pd.read_csv(path, index_col=0)
    df = pd.concat([df, df_temp], ignore_index=True)
#df.drop_duplicates(inplace=True) #중복데이터 제거
#df.reset_index(inplace=True) #중복데이터 제거
multi_categorys = ['판타지 액션', '아동 일상', '이세계 판타지', '판타지 아동', '액션 아동', '판타지 개그', '개그 로맨스', '액션 개그']
print(df.head(30))
df.dropna(inplace=True)
df.reset_index(inplace=True, drop=True)
#del df['index'] # 중복데이터 제거 후 index 생겨서 index 삭제

df = df[df['multi_category'].isin(multi_categorys)]
print(df.head())
print(df.multi_category.value_counts())
df.info()
df.to_csv('./crawling_data_2/laftel_crawling_data_{}.csv'.format(
    datetime.datetime.now().strftime('%Y%m%d')), index=False)