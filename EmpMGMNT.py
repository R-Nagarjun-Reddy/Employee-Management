import tkinter as tk
import sqlite3
connection=sqlite3.connect("test1.db")
cur=connection.cursor()
try:
    cur.execute('''
    CREATE TABLE test1 (Name Text,Salary INTEGER,Designation Text,DateOfJoining Text)
    ''')
except :
    pass

def AddEmp() :

    addwin=tk.Tk()
    addwin.configure(bg='grey')
    label2 = tk.Label(master=addwin, text="Add an Employee", fg="white", bg="black", height=3, font=25)
    name_var = tk.StringVar(addwin)
    sal = tk.StringVar(addwin)
    des = tk.StringVar(addwin)
    doj = tk.StringVar(addwin)
    label2.grid(row=0,pady=10)
    name_label=tk.Label(addwin, text = 'Employee Name',pady=10,padx=10, font=('calibre',10, 'bold')).grid(row=2,column=0,pady=10,padx=10)
    name_Entry=tk.Entry(addwin,textvariable = name_var, font=('calibre',10,'normal')).grid(row=2,column=1,pady=10)
    sal_label = tk.Label(addwin, text='Salary', pady=10, padx=10, font=('calibre', 10, 'bold')).grid(row=3,column=0,pady=10,padx=10)
    sal_Entry = tk.Entry(addwin, textvariable=sal, font=('calibre', 10, 'normal')).grid(row=3, column=1,pady=10)
    des_label = tk.Label(addwin, text='Designation', pady=10, padx=10, font=('calibre', 10, 'bold')).grid(row=4,column=0,pady=10,padx=10)
    des_Entry = tk.Entry(addwin, textvariable=des, font=('calibre', 10, 'normal')).grid(row=4, column=1,pady=10)
    doj_label = tk.Label(addwin, text='Date ofJoining', pady=10, padx=10, font=('calibre', 10, 'bold')).grid(row=5,column=0,pady=10,padx=10)
    doj_Entry = tk.Entry(addwin, textvariable=doj, font=('calibre', 10, 'normal')).grid(row=5, column=1,pady=10)
    sub_btn = tk.Button(addwin, text='Submit', command= lambda :submit(name_var.get(),sal.get(),des.get(),doj.get(),addwin)).grid(row=7,column=1,pady=10)
    addwin.mainloop()


def SearchEmp() :
    addwin=tk.Tk()
    label2 = tk.Label(master=addwin, text="Search an Employee", fg="white", bg="black", height=2, font=14)
    label2.grid(row=0,pady=6)
    name_var = tk.StringVar(addwin)
    name_label=tk.Label(addwin, text = 'Enter the Employee Name',pady=10,padx=10, font=('calibre',10, 'bold')).grid(row=2,column=0,pady=10,padx=10)
    name_Entry=tk.Entry(addwin,textvariable = name_var, font=('calibre',10,'normal')).grid(row=2,column=1,pady=10)
    sub_btn = tk.Button(addwin, text='Submit', command= lambda :submit_search(name_var.get(),addwin)).grid(row=4,column=1,pady=10)


    addwin.mainloop()
def DelEmp() :
    addwin=tk.Tk()
    label2 = tk.Label(master=addwin, text="Delete an Employee", fg="white", bg="black", height=2, font=14)
    label2.grid(row=0,pady=5)
    name_var = tk.StringVar(addwin)
    name_label=tk.Label(addwin, text = 'Enter the Employee Name',pady=10,padx=10, font=('calibre',10, 'bold')).grid(row=2,column=0,pady=10,padx=10)
    name_Entry=tk.Entry(addwin,textvariable = name_var, font=('calibre',10,'normal')).grid(row=2,column=1,pady=10)
    sub_btn = tk.Button(addwin, text='Submit', command= lambda :submit_delete(name_var.get(),addwin)).grid(row=4,column=1,pady=10)


    addwin.mainloop()
def PrintEmp() :
    addwin=tk.Tk()
    label2 = tk.Label(master=addwin, text=" Employee list", fg="white", bg="black", height=2, font=14)
    label2.grid(row=0,pady=6)
    rows = cur.execute(''' SELECT Name, Salary,Designation,DateOfJoining FROM test1  ''').fetchall()
    print(rows)
    
    
    
   
    row_number=2
    for row in rows:
        names,salary,designation,doj=row[0],row[1],row[2],row[3]

        employee_details=tk.Label(addwin,text=' Name: '+ names+'\t Salary: '+str(salary)+'\t Designation: '+designation+' \t Date Of Joining: '+doj,pady=10,padx=10, font=('calibre',10, 'bold')).grid(row=row_number)
        row_number+=1

    addwin.mainloop()
def submit(name,sal,des,doj,addwin):
    print(name + sal)
    cur.execute('''INSERT INTO test1 VALUES (?,?,?,?) ''',(name,sal,des,doj))
    connection.commit()
    rows = cur.execute(''' SELECT Name, Salary,Designation,DateOfJoining FROM test1  ''').fetchall()
    print(rows)
    
    addwin.destroy()
   # sub_win=tk.Tk()
   
    #row_number=0
   # for row in rows:
      #  names,salary,designation,DOJ=row[0],row[1],row[2],row[3]

       # employee_details=tk.Label(sub_win,text=' Name: '+ names+'\t Salary: '+str(salary)+'\t Designation: '+designation+' \t Date Of Joining: '+doj,pady=10,padx=10, font=('calibre',10, 'bold')).grid(row=row_number)
       # row_number+=1

def submit_search(name,addwin):
    details = cur.execute(''' SELECT Name,Salary,Designation,DateOfJoining From test1 WHERE Name = (?)  ''',(name,)).fetchall()
    print(details)
    addwin.destroy()
def submit_delete(name,addwin):
    cur.execute(''' DELETE From test1 WHERE Name = (?)  ''',(name,))
    #print(details)
    connection.commit()
    addwin.destroy()    





window = tk.Tk()
window.geometry=("400x200")
window.configure(bg='grey')
# label=tk.Label(text="Employee management",fg="red",bg="black",width=2,height=2)
label = tk.Label(master=window,text="Employee Management System", fg="white", bg="black",height=3,font=("Times New Roman",25,'bold'))
label.pack()
b1=tk.Button(window,text="Add an employee",command=AddEmp,fg="red", bg="black",height=1,font=14 , pady=0,padx=0,activebackground='yellow')
b1.pack(pady=5)
b2=tk.Button(window,text="Search an employee",command=SearchEmp,fg="red", bg="black",height=1,font=14 , pady=0,padx=0,activebackground='yellow')
b2.pack(pady=5)
b3=tk.Button(window,text="Delete an employee",command=DelEmp,fg="red", bg="black",height=1,font=14 , pady=0,padx=0,activebackground='yellow')
b3.pack(pady=5)
b4=tk.Button(window,text="view all employees",command=PrintEmp,fg="red", bg="black",height=1,font=14 , pady=0,padx=0,activebackground='yellow')
b4.pack(pady=5)


window.mainloop()
