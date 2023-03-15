#기존 엑셀의 데이터 중 원하는 걸 뽑아와 새 db에 저장하는 파일
#https://bohemihan.tistory.com/entry/Python-re-%ED%95%A8%EC%88%98-%EB%8D%B0%EC%9D%B4%ED%84%B0%ED%94%84%EB%A0%88%EC%9E%84-%EB%82%B4%EC%9A%A9%EB%B0%94%EA%BE%B8%EA%B8%B0-%EC%B9%98%ED%99%98  <--엑셀 데이터 찾기 관련 블로그


import os
import pandas as pd
import numpy as np
from openpyxl import load_workbook
from pprint import pprint

path='dataset/'
file_list=os.listdir(path)

#음식명과 식재료명을 저장해 데이터프레임을 만듬





#재료 딕셔너리,key에 메뉴이름 value에 재료가 저장됨, 매개변수로는 엑셀의 fillna('')가 된 데이터 프레임을 받음
def mat_list(dataframe):
    a=np.array(dataframe[5:])
    mat_list={}
    key=''
    value=[]
    sw=None
    for i in a:
        if '점심' in i[0]:
            sw=1
            key=i[1]
            value.append(i[2].split(',')[0])
        elif '간식' in i[0]:
            sw=0
            key=''
            value=[]
        elif sw==1:
            if i[1]=='':
                value.append(i[2].split(',')[0])
            elif i[1]!='':
                value=','.join(set(value))
                mat_list[key]=value
                key=''
                value=[]
                key=i[1]
                value.append(i[2].split(',')[0])
    return mat_list

#def search_menu():
#https://bohemihan.tistory.com/entry/Python-re-%ED%95%A8%EC%88%98-%EB%8D%B0%EC%9D%B4%ED%84%B0%ED%94%84%EB%A0%88%EC%9E%84-%EB%82%B4%EC%9A%A9%EB%B0%94%EA%BE%B8%EA%B8%B0-%EC%B9%98%ED%99%98  <--엑셀 데이터 찾기 관련 블로그

def make_db():
    fin_dict={}
    for file in file_list:
        for sheet in range(2):
            df=pd.read_excel(f"{path+file}", engine = "openpyxl", sheet_name=sheet, usecols='B,C,D')
            df=df.fillna('')
            fin_dict.update(mat_list(df))


    wb=load_workbook('files/database.xlsx')
    ws=wb['database']

    for row,(key,value) in enumerate(fin_dict.items()):
        ws.cell(row=row+1,column=1,value=key)
        ws.cell(row=row+1,column=2,value=value)
    wb.save('files/database.xlsx')

make_db()