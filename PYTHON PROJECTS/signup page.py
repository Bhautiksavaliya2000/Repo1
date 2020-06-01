import tkinter as tk
from tkinter.messagebox import *
from tkinter import ttk

def getvalue():
    if (username_var.get() == ''):
        print(showinfo("warning", "* fields must be filled."))
    elif pass_var.get() == '':
        print(showinfo("warning", "* fields must be filled."))
    elif pass_var.get() != repass_var.get():
        print(showinfo("warning", "both password must be same."))

    else:
        name = username_var.get()
        mail = email_var.get()
        pas = pass_var.get()
        pas2 = repass_var.get()
        gender = gender_var.get()
        user_type = usertype.get()

        file = open("G:\PYTHON\GUI\signup details",'a')
        file.write(f'{name}\t{mail}\t{pas}\t{pas2}\t{gender}\t{user_type}\n')
        
        username.delete(0,tk.END)
        email.delete(0,tk.END)
        password.delete(0,tk.END)
        repass.delete(0,tk.END)

def switchstate():
    if check_btn.get() == 1:
       button.config(state = tk.ACTIVE) 
    elif check_btn.get() == 0:
        button.config(state = tk.DISABLED)             


root = tk.Tk()
root.title("sign up menu")
root.geometry("350x300")
root.config(bg='#64A6E8')

#creating labels                                 #sticky = to stick label left side.
label1 = ttk.Label(root,text='Enter username *:',background='#64A6E8')
label2 = ttk.Label(root,text='Enter email *:',background='#64A6E8')
label3 = ttk.Label(root,text='Enter password *:',background='#64A6E8')
label4 = ttk.Label(root,text='Confirm password *:',background='#64A6E8')
label5 = ttk.Label(root,text='Choose your gender *',background='#64A6E8')

#creating entry fields
username_var = tk.StringVar()
username = ttk.Entry(root,textvariable=username_var)
username.focus()

email_var = tk.StringVar()
email = ttk.Entry(root,textvariable=email_var)

pass_var = tk.StringVar()
password = ttk.Entry(root,textvariable=pass_var,show='*')

repass_var = tk.StringVar()
repass = ttk.Entry(root,textvariable=repass_var,show='*')

#creating combobox
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(root,textvariable=gender_var,width=17,state='readonly',background='#64A6E8')
gender_combobox['values'] = ('Male','Female','Others')
gender_combobox.current(0)

#creating radiobutton
usertype = tk.StringVar()                 #variable should be same to allow only one radiobutton select at a time.
radiobtn1 = ttk.Radiobutton(root,text='student',value='student',variable=usertype)
radiobtn2 = ttk.Radiobutton(root,text='graduate',value='graduate',variable=usertype)
radiobtn3 = ttk.Radiobutton(root,text='professional',value='professional',variable=usertype)

#creating cheakbox
check_btn = tk.IntVar()
checkbtn = ttk.Checkbutton(root,text='accept terms and conditions',variable=check_btn,command=switchstate)

#creating button.
button = ttk.Button(root,text='sign up',command=getvalue,state=tk.DISABLED)

#setting position of each widgit.
label1.grid(row=0,column=0,sticky=tk.W)
username.grid(row=0,column=1,padx=3,pady=3)

label2.grid(row=1,column=0,sticky=tk.W)
email.grid(row=1,column=1,padx=3,pady=3)

label3.grid(row=2,column=0,sticky=tk.W)
password.grid(row=2,column=1,padx=3,pady=3)

label4.grid(row=3,column=0,sticky=tk.W)
repass.grid(row=3,column=1,padx=3,pady=3)

label5.grid(row=4,column=0,sticky=tk.W)
gender_combobox.grid(row=4,column=1,padx=3,pady=3)

radiobtn1.grid(row=5,column=0,padx=3,pady=3)
radiobtn2.grid(row=5,column=1,padx=3,pady=3)
radiobtn3.grid(row=5,column=2,padx=3,pady=3)

checkbtn.grid(row=6,columnspan=3,sticky=tk.W,padx=3,pady=3)              # to merge three columns

button.grid(row=7,column=1,padx=3,pady=10)
root.mainloop()
