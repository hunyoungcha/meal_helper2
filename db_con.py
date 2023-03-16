#새로 만든 db에서 원하는 데이터를 뽑아 내기 위한 작업을 하는 파일

import pandas as pd
import numpy as np

df=pd.read_excel('files/database.xlsx',sheet_name='database')

#순서 상관 있는 버전(속도 느림)

#meal_dict에 dict형태로 메뉴 저장
meal_dict={}
df_list=np.array(df)
for i in df_list:
    meal_dict[i[0]]=i[1]

def search_menu(menu):
    try:
        return meal_dict[menu]
    except:
        return 0



#순서 상관 없는 버전 (속도 빠름)
# is_menu=(df['menu']=='양송이스프') | (df['menu']=='동그랑땡')
# menu=np.array(df[is_menu]['mat'])
# print(menu)