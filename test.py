import os
import pandas as pd
import numpy as np
from pprint import pprint
import time

path='dataset/'
file_list=os.listdir(path)

#음식명과 식재료명을 저장해 데이터프레임을 만듬
df = pd.read_excel(f"{path+file_list[0]}", engine = "openpyxl", sheet_name="조리지시서(10월 1일~15일)", usecols='B,C,D')
df=df.fillna('')

def mat_list(dataframe):
    a=np.array(dataframe[5:])
    mat_list=[]
    tmp=[]
    for i in a:
        if '저녁' in i[0]:
            sw=1
            tmp.append(i[1])
            tmp.append(i[2].split(',')[0])
        elif '간식' in i[0]:
            sw=0
            mat_list.append(['end'])
            tmp=[]
        elif sw==1:
            if i[1]=='':
                tmp.append(i[2].split(',')[0])
            elif i[1]!='':
                tmp=list(dict.fromkeys(tmp)) #dict의 key는 중복을 허용 안하기 때문에 fromkey로 key값으로 바꾼다음 다시 리스트화 시킴으로써 중복을 제거 함
                mat_list.append(tmp)
                tmp=[]
                tmp.append(i[1])
                tmp.append(i[2].split(',')[0])
    return mat_list

start_time = time.time()
mat_list(df)
print("--- %s seconds ---" % (time.time() - start_time))