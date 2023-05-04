from tkinter import *
root = Tk()
root.geometry("260x195")
file= open("dog_age.txt","a")

#ฟังก์ชันเคลียร์ข้อมูลในกล่องข้อความ
def deletetext():
    et_name.delete(0,END)
    et_tel.delete(0,END)
    et_age_dog_year.delete(0,END)
    labelResult_age.configure(text="")

#ฟังชันคำนวณอายุสุนัข
def calculate():
    if float(et_age_dog_year.get()) <= 2:
        result = float(et_age_dog_year.get())*10.5
    elif float(et_age_dog_year.get()) > 2:
        result = (float(et_age_dog_year.get())*4)+13
    labelResult_age.configure(text=result)
    return result

#ฟังก์ชันบันทึกข้อมูลลงในไฟล์ text
def save_data():
    f=open("dog_age.txt","a",encoding="utf8")
    f.write(f"ชื่อ-สกุล เจ้าของสุนัข : {et_name.get()} \nเบอร์โทร : {et_tel.get()} \nอายุสุนัข : {et_age_dog_year.get()} ปี \nอายุสุนัขเทียบกับคน : {calculate()} ปี \n")
    f.write("\n")
    f.close()

root.title("โปรแกรมคำนวณอายุสุนัข")
Label(text="ข้อมูลเจ้าของสุนัข").grid(row=0, column=1)
Label(text="ชื่อ-สกุล").grid(row=1)
Label(text="เบอร์ติดต่อ").grid(row=2)

et_name = Entry()
et_name.grid(row=1, column=1)
et_tel = Entry()
et_tel.grid(row=2, column=1)

Label(root,text="ข้อมูลสุนัข").grid(row=3, column=1)
Label(root,text="อายุสุนัข").grid(row=4, column=0)
Label(root,text="ปี").grid(row=4, column=2)

et_age_dog_year = Entry()
et_age_dog_year.grid(row=4, column=1)

cle_button = Button(text="ล้างข้อมุล", command=deletetext).grid(row=10, column=1,sticky=E)
cal_button = Button(text="คำนวณ", command=calculate).grid(row=10, column=1, sticky=W)
save_button = Button(text="บันทึกข้อมูล", command=save_data).grid(row=12, column=1)


label_age = Label(root,text="อายุสุนัขเทียบกับอายุคน")
label_age.grid(row=11,column=0)

labelResult_age = Label(width=17,bg='Slategray1')
labelResult_age.grid(row=11,column=1)
Label(root,text="ปี").grid(row=11, column=2)

root.mainloop()

