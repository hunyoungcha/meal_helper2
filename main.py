#메인 gui 띄우는 파일

import tkinter as tk
from tkinter import filedialog


window=tk.Tk()
window.title('meals_helper')
window.geometry('800x400')



def Load_meal():
    meal_file = filedialog.askopenfilename(initialdir="/", title="Meal_File",filetypes=(("*.jpg","*.jpg"),("*.png","*.png"),("all files", "*.*")))
    meal_lab.config(text=meal_file.split('/')[-1])

def Load_snack():
    snack_file = filedialog.askopenfilename(initialdir="/", title="Snack_File",filetypes=(("*.jpg","*.jpg"),("*.png","*.png"),("all files", "*.*")))
    snack_lab.config(text=snack_file.split('/')[-1]) 










#메뉴 입력 위 라벨
lab=tk.Label(window, text='급식 메뉴', font=20)
lab.place(x=1,y=1)

#메뉴 입력 텍스트 박스
inx=tk.Text(window, width=50, height=15, font=30)
inx.place(x=1,y=30)

#급식 라벨
meal_lab=tk.Label(window,text="*업로드 된 급식 사진이 없습니다.",font=20)
meal_lab.place(x=420,y=30)
#급식 버튼
meal_button=tk.Button(window,text='급식 사진 업로드',width=50, background='gray',foreground='white',command=Load_meal)
meal_button.place(x=420,y=53)

#간식 라벨
snack_lab=tk.Label(window,text="*업로드 된 간식 사진이 없습니다.",font=20)
snack_lab.place(x=420,y=100)

#간식 버튼
snack_button=tk.Button(window,text='간식 사진 업로드',width=50, background='gray',foreground='white',command=Load_snack)
snack_button.place(x=420,y=123)

#간식 텍스트 라벨
snack_text_lab=tk.Label(window,text='간식 메뉴', font=20)
snack_text_lab.place(x=420, y=170)

#간식 텍스트 박스
snack_text=tk.Text(window,width=45,height=1,font=30)
snack_text.place(x=420,y=193)

#생성 버튼
create_btn=tk.Button(window,width=22, height=4, text='생성', background='blue',foreground='white')
create_btn.place(x=5, y=280)

#파일명 라벨
file_name_lab=tk.Label(window,text='*파일명',font=20)
file_name_lab.place(x=180,y=280)

#파일명 텍스트 박스
file_name_text=tk.Text(window,width=20,height=1,font=30)
file_name_text.place(x=180, y=300)


window.mainloop()