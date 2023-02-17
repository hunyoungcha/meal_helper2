#기존 엑셀의 데이터 중 원하는 걸 뽑아와 새 db에 저장하는 파일


import os
import pandas as pd
import numpy as np
from pprint import pprint


path='dataset/'
file_list=os.listdir(path)

#음식명과 식재료명을 저장해 데이터프레임을 만듬
df = pd.read_excel(f"{path+file_list[0]}", engine = "openpyxl", sheet_name="조리지시서(10월 1일~15일)", usecols='B,C,D')
df=df.fillna('')

a=np.array(df[5:])
f=np.array([])
#간식 파트 제거
######## numpy로 배열 안에 배열 모양 그대로 append하는 법 알아야 함#######
# for i in a[:5]:
f=np.shape(a)    
print(f)


# for i in range(len(a)):
#     f=np.append(f, np.array([[a[i][1:]]]))
#     # if a[i][0]=='간식' :
#         # print('True')

#재료 필터링 하기(생것,말린것,개량,양조,가루,재래,볶은것,전란,훈제,튀긴것,)

#메뉴와 재료를 같은 리스트에 넣기




# for i in a:
#     print(pd.isna(i[0]))