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


#재료 리스트 [0]번에는 음식 이름이 저장 됨, 매개변수로는 엑셀의 fillna('')가 된 데이터 프레임을 받음
def mat_list(dataframe):
    # #간식 파트 제거
    a=np.array(dataframe[5:])
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
    for i in range(len(g)):
        if g[i][0]!='':
            indx=i
        elif g[i][0]=='':
            if g[i][1] not in g[indx]:
                g[indx].append(g[i][1])

    #메뉴와 재료 매칭 안된 재료들은 삭제
    mat_list=[]
    for i in g:
        if i[0]!='':
            mat_list.append(i)

    return mat_list

def insert_data(m_list):
    