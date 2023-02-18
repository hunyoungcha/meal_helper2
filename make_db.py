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


# #간식 파트 제거
a=np.array(df[5:])
f=[]
sw=1
for i in a:
    if '저녁' in i[0]:
        sw=1
        f.append(i[1:])
    elif '간식' in i[0]:
        sw=0
    elif sw==1:
        f.append(i[1:])

# 식재료 필터링
g=[]
for i in f:
    g.append([i[0],i[1].split(',')[0]])

#메뉴와 재료를 같은 리스트에 넣기

#현재 방법: g[1]가 ''가 아닐때의 인덱스를 추출한 다음 ''가 아닐땐 추출한 인덱스에 append해주고 그 리스트는 삭제 시킨다
for i in range(len(f)):
    if g[i][0]!='':
        indx=g[i].index()
    elif g[i][0]=='':
        g[indx].append(g[i][1])
        del g[i]
pprint(g)         

        

# for i in f:
#     print(i)









# for i in a:
#     print(pd.isna(i[0]))