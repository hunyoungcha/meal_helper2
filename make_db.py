#기존 엑셀의 데이터 중 원하는 걸 뽑아와 새 db에 저장하는 파일
#https://bohemihan.tistory.com/entry/Python-re-%ED%95%A8%EC%88%98-%EB%8D%B0%EC%9D%B4%ED%84%B0%ED%94%84%EB%A0%88%EC%9E%84-%EB%82%B4%EC%9A%A9%EB%B0%94%EA%BE%B8%EA%B8%B0-%EC%B9%98%ED%99%98  <--엑셀 데이터 찾기 관련 블로그


import os
import pandas as pd
import numpy as np
from pprint import pprint


path='dataset/'
file_list=os.listdir(path)

#음식명과 식재료명을 저장해 데이터프레임을 만듬


# df = pd.read_excel(f"{path+file_list[0]}", engine = "openpyxl", sheet_name=1, usecols='B,C,D')
# df=df.fillna('')


#재료 리스트 [0]번에는 음식 이름이 저장 됨, 매개변수로는 엑셀의 fillna('')가 된 데이터 프레임을 받음
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

def append_to_excel(fpath, df, sheet_name):
    with pd.ExcelWriter(fpath, mode="a") as f:
        df.to_excel(f, sheet_name=sheet_name)

#def search_menu():
#https://bohemihan.tistory.com/entry/Python-re-%ED%95%A8%EC%88%98-%EB%8D%B0%EC%9D%B4%ED%84%B0%ED%94%84%EB%A0%88%EC%9E%84-%EB%82%B4%EC%9A%A9%EB%B0%94%EA%BE%B8%EA%B8%B0-%EC%B9%98%ED%99%98  <--엑셀 데이터 찾기 관련 블로그

# def check_over(): 중복 확인 함수,
#현재 생각중인 방법: 서치를 통해 있는지 확인 하고 없으면 추가


# def insert_list(mat_list):

# a=pd.DataFrame(mat_list(df))
# append_to_excel('files/database.xlsx', a,'new')
q=''
for i in file_list:
    print(i)
    for j in range(2):
        df = pd.read_excel(f"{i}", engine = "openpyxl", sheet_name=j, usecols='B,C,D')
        df.fillna('')

    
pprint(q)