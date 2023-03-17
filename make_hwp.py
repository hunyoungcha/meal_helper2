#한글 파일 만드는 파일
#https://www.codingnow.co.kr/python/?bmode=view&idx=6494279&back_url=&t=board&page= <-- 한글 자동화 참고 하면 좋을 블로그 #보안 팝업 7:05 부터
#https://www.hancom.com/board/devmanualList.do?artcl_seq=3934 <-- 한글 개발 문서

import shutil
import win32com.client as win32
from db_con import search_menu



hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")
hwp.RegisterModule("FilePathCheckDLL", "FilePathCheckerModule")



def make_hwp(file_name,change=None):
    shutil.copyfile(r'files/급식일지.hwp',rf'./{file_name}.hwp')
    hwp.Open(rf'C:\Users\차훈영\Desktop\python\meal_helper2\files\{file_name}.hwp')
make_hwp('2037010')


#meal_img,snack_img,menu,snack,