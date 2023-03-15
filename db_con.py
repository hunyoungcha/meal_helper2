#새로 만든 db에서 원하는 데이터를 뽑아 내기 위한 작업을 하는 파일

import pandas as pd


#데이터프레임에서 내가 원하는거 가져오는 함수 찾아야함


df=pd.read_excel('files/database.xlsx',sheet_name='database')

print(df['0'])