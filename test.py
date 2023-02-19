from openpyxl import Workbook
from openpyxl import load_workbook

wb=load_workbook('dataset/1월 조리지시서 지역아동센터(만 6_11세-점심(저녁) 및 간식).xlsx')
ws=wb['조리지시서(1월 2일~14일)']

