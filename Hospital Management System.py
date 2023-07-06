import tkinter 
from tkinter import *
from tkinter import ttk
import mysql.connector
from tkcalendar import *

mydb = mysql.connector.connect(host='localhost',user='User',passwd='Password')
mycursor = mydb.cursor()


try :
    mycursor.execute("create database HOSPITAL")
    mycursor.execute("use HOSPITAL")
except :
    mydb = mysql.connector.connect(host='localhost',user='User',passwd='Password',database='HOSPITAL')

try :
    sql = "create table PATIENTS (First_Name varchar(30), Last_Name varchar(30), Insurance varchar(10), Address varchar(30), Phone varchar(15), P_No int(3) primary key)"
    mycursor = mydb.cursor()
    mycursor.execute(sql)
except :
    pass

try:
    mycursor.execute("create table DOCTOR (First_Name varchar(30),Last_Name varchar(30),Specialization varchar(30),Address varchar(50),Phone varchar(15),Doct_ID int(3))")
except:
    pass

try: 
    sql="create table APPOINTMENTS(a_no int(5),DOCTOR_NAME varchar(20),PATIENT_NAME varchar(20),DATE date)"
    mycursor=mydb.cursor()
    mycursor.execute(sql)
except:
    pass

root = Tk()
root.title('Hospital Management')
root.configure(background = "#4d88ff")
    
sideframe = Frame(root,height=650,width=230,bg='#1a1a1a')
sideframe.place(x=0,y=2)

frame3 = Frame(root,height=650,width=750,bg='#33ff33')
frame3.place(x=230,y=0)

frame2 = Frame(root,height=650,width=750,bg='#ff3333')
frame2.place(x=230,y=0)

frame1 = Frame(root,height=650,width=750,bg='#4d88ff')
frame1.place(x=230,y=0)


##firstlabel = Label(sideframe,height=4,width=32,bg='#404040')
##firstlabel.place(x=0,y=0)

def framechanger1(event):
    frame1.tkraise()
    dashboardlabel.tkraise()
    root.configure(background = "#4d88ff")
    iconlabel.tkraise()

def framechanger2(event):
    frame2.tkraise()
    dashboardlabel.tkraise()
    root.configure(background = "#ff3333")
    iconlabel.tkraise()
    
def framechanger3(event):
    frame3.tkraise()
    dashboardlabel.tkraise()
    root.configure(background = "#33ff33")
    iconlabel.tkraise()


#############################################################################################


patientlabel = Label(sideframe,text="PATIENTS",height=2,width=18,font=('Trebuchet MS',17),bg='#4d88ff',fg='#ffffff')
patientlabel.place(x=0,y=65)
patientlabel.bind("<Button>",framechanger1) 

doctorlabel = Label(sideframe,text="DOCTORS",height=2,width=18,font=('Trebuchet MS',17),bg='#ff3333',fg='#ffffff')
doctorlabel.place(x=0,y=130)
doctorlabel.bind("<Button>",framechanger2)

appoinlabel = Label(sideframe,text="APPOINTMENTS",height=2,width=18,font=('Trebuchet MS',17),bg='#33ff33',fg='#ffffff')
appoinlabel.place(x=0,y=195)
appoinlabel.bind("<Button>",framechanger3)

dashboardlabel = Label(root,text="DASHBOARD",height=2,width=97,font=('Bahnschrift Condensed',19),bg='#1a1a1a',fg='#ffffff')
dashboardlabel.place(x=0,y=2)

iconlabel = Label(root,text="☰",height=2,width=5,font=('Trebuchet MS',17),bg='#1a1a1a',fg='#ffffff')
iconlabel.place(x=0,y=2) 

def patient_no():
    mydb = mysql.connector.connect(host='localhost',user='root',passwd='123',database='HOSPITAL')
    mycursor = mydb.cursor()
    sql = "select p_no from PATIENTS"
    mycursor.execute(sql)
    rows = mycursor.fetchall()
    for i in rows :
        p_no = i
    try:
        return p_no[0]+1
    except:
        return int(1)
    mydb.close()

def add_patient(a,b,c,d,e):
    mydb = mysql.connector.connect(host='localhost',user='root',passwd='123',database='HOSPITAL')
    mycursor = mydb.cursor()
    First_Name = a
    Last_Name = b
    Insurance = c
    Address = d
    Phone = e
    P_No = patient_no()

    sql = "insert into PATIENTS (First_Name, Last_Name, Insurance, Address, Phone, P_No) values (%s,%s,%s,%s,%s,%s)"
    rows = [First_Name, Last_Name, Insurance, Address, Phone, P_No]
    mycursor = mydb.cursor()
    mycursor.execute(sql,rows)
    mydb.commit()
    mydb.close()

def patient_fnames():
    mydb = mysql.connector.connect(host='localhost',user='root',passwd='123',database='HOSPITAL')
    mycursor = mydb.cursor()
    sql = "select * from PATIENTS"
    mycursor.execute(sql)
    fnames = []
    rows = mycursor.fetchall()
    for i in rows :
        fnames.append(i[0])
    return fnames

def patient_lnames():
    mydb = mysql.connector.connect(host='localhost',user='root',passwd='123',database='HOSPITAL')
    mycursor = mydb.cursor()
    sql = "select * from PATIENTS"
    mycursor.execute(sql)
    lnames = []
    rows = mycursor.fetchall()
    for i in rows :
        lnames.append(i[1])
    return lnames

def patient_names():
    mydb = mysql.connector.connect(host='localhost',user='root',passwd='123',database='HOSPITAL')
    mycursor = mydb.cursor()
    sql = "select * from PATIENTS"
    mycursor.execute(sql)
    names = []
    rows = mycursor.fetchall()
    for i in rows :
        names.append(i[0]+" "+i[1])
    return names


def patient_insurances():
    mydb = mysql.connector.connect(host='localhost',user='root',passwd='123',database='HOSPITAL')
    mycursor = mydb.cursor()
    sql = "select * from PATIENTS"
    mycursor.execute(sql)
    insurances = []
    rows = mycursor.fetchall()
    for i in rows :
        insurances.append(i[2])
    return insurances

def patient_addresses():
    mydb = mysql.connector.connect(host='localhost',user='root',passwd='123',database='HOSPITAL')
    mycursor = mydb.cursor()
    sql = "select * from PATIENTS"
    mycursor.execute(sql)
    addresses = []
    rows = mycursor.fetchall()
    for i in rows :
        addresses.append(i[3])
    return addresses

def patient_phones():
    mydb = mysql.connector.connect(host='localhost',user='root',passwd='123',database='HOSPITAL')
    mycursor = mydb.cursor()
    sql = "select * from PATIENTS"
    mycursor.execute(sql)
    phones = []
    rows = mycursor.fetchall()
    for i in rows :
        phones.append(i[4])
    return phones
    

def patient_details():
    details = zip(patient_fnames(),patient_lnames(),patient_insurances(),patient_addresses(),patient_phones())
    return (list(details))


def show_patients():
    tempList = list(patient_details())
    for j in listBox.get_children():
        listBox.delete(j)

    for i, (fname,lname,insurance,address, phone) in enumerate(tempList, start=1):
        listBox.insert("", "end", values=(i, fname,lname,insurance,address, phone))


 
cols = ('S.No', 'First Name', 'Last Name','Insurance','Address', 'Phone')

listBox = ttk.Treeview(frame1,height=10, columns=cols, show='headings')
for col in cols:
    listBox.heading(col, text=col)
    
vsb = ttk.Scrollbar(frame1, orient="vertical", command=listBox.yview)
vsb.place(x=720, y=130, height=376)

listBox.configure(yscrollcommand=vsb.set)

style = ttk.Style(frame1)
style.configure('Treeview', rowheight=35,font='20')

listBox.column('#1',width=60)
listBox.column('#2',width=120)
listBox.column('#3',width=120)
listBox.column('#4',width=105)
listBox.column('#5',width=165)
listBox.column('#6',width=120)

listBox.place(x=27,y=130)

def addpatient():
    top = Toplevel()
    top.title('Add Patient')

    fpatienttext = Label(top,text="First Name ")
    fpatienttext.place(x=20,y=60)
    
    fpatientinput= Entry(top,width=30)
    fpatientinput.place(x=125,y=60)

    lpatienttext = Label(top,text="Last Name ")
    lpatienttext.place(x=20,y=85)
    
    lpatientinput= Entry(top,width=30)
    lpatientinput.place(x=125,y=85)
    
    instext = Label(top,text="Insurance ")
    instext.place(x=20,y=110)
    
    insinput= Entry(top,width=30)
    insinput.place(x=125,y=110)

    addtext = Label(top,text="Address ")
    addtext.place(x=20,y=135)
    
    addinput= Entry(top,width=30)
    addinput.place(x=125,y=135)
    
    mobtext = Label(top,text="Mobile ")
    mobtext.place(x=20,y=160)
    
    mobinput= Entry(top,width=30)
    mobinput.place(x=125,y=160)

    status = Label(top,text="Status  ")
    status.place(x=80,y=185)


    def clearer():
        fpatientinput.delete(0, END)
        lpatientinput.delete(0, END)
        insinput.delete(0, END)
        addinput.delete(0, END)
        mobinput.delete(0, END)
        
    def getdata():
        a=fpatientinput.get()
        b=lpatientinput.get()
        c=insinput.get()
        d=addinput.get()
        e=mobinput.get()
        add_patient(a,b,c,d,e)
        status.config(text="Status  : Patient Added")
        clearer()

    submit = Button(top,text="Submit",command = getdata)
    submit.place(x=100,y=210)

    def closer():
        show_patients()
        top.destroy()
        
    close = Button(top,text="Close & Refresh",command = closer)
    close.place(x=160,y=210)
        
    
    top.geometry('340x260')
    top.mainloop()

def removepatients():
    top = Toplevel()
    top.title('Add Patient')
    
    pationnotext = Label(top,text="Patient Number")
    pationnotext.place(x=20,y=60)
    
    pationnoinput= Entry(top,width=30)
    pationnoinput.place(x=125,y=60)
    
    fpatienttext = Label(top,text="First Name : ")
    fpatienttext.place(x=20,y=85)
    lpatienttext = Label(top,text="Last Name  : ")
    lpatienttext.place(x=20,y=110)        

    def checker():
        patientno = int(pationnoinput.get())-1
        fname,lname=patient_fnames()[patientno],patient_lnames()[patientno]
        fpatienttext.config(text="First Name : "+fname)
        lpatienttext.config(text="Last Name : "+lname)
        
    check = Button(top,text="Check",command = checker)
    check.place(x=100,y=210)

    def remover():
        mydb = mysql.connector.connect(host='localhost',user='root',passwd='123',database='HOSPITAL')
        mycursor = mydb.cursor()
        patientno = pationnoinput.get()
        sqlstatement = "DELETE FROM patients where p_no={0}".format(('"'+str(patientno)+'"'))
        mycursor.execute(sqlstatement)

        sql1 = "SET @rank:=0;"
        sql2 = "update patients set p_no=@rank :=@rank+1;"
        mycursor.execute(sql1)
        mycursor.execute(sql2)
        mydb.commit()
        mydb.close()
        show_patients()
        top.destroy()

        
    close = Button(top,text="Remove",command = remover)
    close.place(x=160,y=210)
    
    top.geometry('340x260')
    top.mainloop()


addpatient = Button(frame1,command = addpatient,height=2,width=13,text='Add')
addpatient.place(x=27,y=520)

removepatient = Button(frame1,height=2,command = removepatients,width=13,text='Remove')
removepatient.place(x=140,y=520)

refreshpatient = Button(frame1,height=2,command = show_patients,width=13,text='Refresh')
refreshpatient.place(x=253,y=520)
############################################################################################################

def doctor_id():
    mydb = mysql.connector.connect(host='localhost',user='root',passwd='123',database='hospital')
    mycursor = mydb.cursor()
    sql = "select Doct_ID from DOCTOR"
    mycursor.execute(sql)
    rows = mycursor.fetchall()
    for i in rows :
        d_no = i
    try :
        return d_id[0] + 1
    except :
        return int(1)
    mydb.close()

def add_doctor(a,b,c,d,e):
    mydb = mysql.connector.connect(host='localhost',user='root',passwd='123',database='hospital')
    First_Name = a
    Last_Name = b
    Specialization = c
    Address = d
    Phone = e
    Doct_ID = doctor_id()
    
    sql="insert into DOCTOR(First_Name,Last_Name,Specialization,Address,Phone,Doct_ID) values (%s,%s,%s,%s,%s,%s)"
    rows=[First_Name,Last_Name,Specialization,Address,Phone,Doct_ID]
    mycursor=mydb.cursor()
    mycursor.execute(sql,rows)
    mydb.commit()

def doctor_fnames():
    mydb = mysql.connector.connect(host='localhost',user='root',passwd='123',database='hospital')
    mycursor = mydb.cursor()
    sql = "select * from DOCTOR"
    mycursor.execute(sql)
    d_fnames = []
    rows = mycursor.fetchall()
    for i in rows :
        d_fnames.append(i[0])
    return d_fnames

def doctor_lnames():
    mydb = mysql.connector.connect(host='localhost',user='root',passwd='123',database='hospital')
    mycursor = mydb.cursor()
    sql = "select * from DOCTOR"
    mycursor.execute(sql)
    d_lnames = []
    rows = mycursor.fetchall()
    for i in rows :
        d_lnames.append(i[1])
    return d_lnames

def doctor_names():
    mydb = mysql.connector.connect(host='localhost',user='root',passwd='123',database='hospital')
    mycursor = mydb.cursor()
    sql = "select * from DOCTOR"
    mycursor.execute(sql)
    d_names = []
    rows = mycursor.fetchall()
    for i in rows :
        d_names.append(i[0]+" "+i[1])
    return d_names



def doctor_specializations():
    mydb = mysql.connector.connect(host='localhost',user='root',passwd='123',database='hospital')
    mycursor = mydb.cursor()
    sql = "select * from DOCTOR"
    mycursor.execute(sql)
    d_specializations = []
    rows = mycursor.fetchall()
    for i in rows :
        d_specializations.append(i[2])
    return d_specializations

def doctor_addresses():
    mydb = mysql.connector.connect(host='localhost',user='root',passwd='123',database='hospital')
    mycursor = mydb.cursor()
    sql = "select * from DOCTOR"
    mycursor.execute(sql)
    d_addresses = []
    rows = mycursor.fetchall()
    for i in rows :
        d_addresses.append(i[3])
    return d_addresses

def doctor_phones():
    mydb = mysql.connector.connect(host='localhost',user='root',passwd='123',database='hospital')
    mycursor = mydb.cursor()
    sql = "select * from DOCTOR"
    mycursor.execute(sql)
    d_phones = []
    rows = mycursor.fetchall()
    for i in rows :
        d_phones.append(i[4])
    return d_phones

def doctor_details():
    details = zip(doctor_fnames(),doctor_lnames(),doctor_specializations(),doctor_addresses(),doctor_phones())
    return list(details)

def show_doctors():
    tempList = list(doctor_details())
    for j in listBox2.get_children():
        listBox2.delete(j)

    for i, (fname,lname,specialization,address, phone) in enumerate(tempList, start=1):
        listBox2.insert("", "end", values=(i, fname,lname,specialization,address, phone))


 
cols2 = ('S.No', 'First Name', 'Last Name','Specialization','Address', 'Phone')

listBox2 = ttk.Treeview(frame2,height=10, columns=cols2, show='headings')

for col2 in cols2:
    listBox2.heading(col2, text=col2)
    
vsb2 = ttk.Scrollbar(frame2, orient="vertical", command=listBox2.yview)
vsb2.place(x=720, y=130, height=376)

listBox2.configure(yscrollcommand=vsb2.set)

style2 = ttk.Style(frame2)
style2.configure('Treeview', rowheight=35,font='20')

listBox2.column('#1',width=60)
listBox2.column('#2',width=120)
listBox2.column('#3',width=120)
listBox2.column('#4',width=105)
listBox2.column('#5',width=165)
listBox2.column('#6',width=120)

listBox2.place(x=27,y=130)

def adddoctor():
    top = Toplevel()
    top.title('Add Doctor')

    fdoctortext = Label(top,text="First Name")
    fdoctortext.place(x=20,y=60)
    
    fdoctorinput= Entry(top,width=30)
    fdoctorinput.place(x=125,y=60)

    ldoctortext = Label(top,text="Last Name")
    ldoctortext.place(x=20,y=85)
    
    ldoctorinput= Entry(top,width=30)
    ldoctorinput.place(x=125,y=85)
    
    spetext = Label(top,text="Specialization")
    spetext.place(x=20,y=110)
    
    speinput= Entry(top,width=30)
    speinput.place(x=125,y=110)

    daddtext = Label(top,text="Address")
    daddtext.place(x=20,y=135)
    
    daddinput= Entry(top,width=30)
    daddinput.place(x=125,y=135)
    
    dmobtext = Label(top,text="Mobile")
    dmobtext.place(x=20,y=160)
    
    dmobinput= Entry(top,width=30)
    dmobinput.place(x=125,y=160)

    dstatus = Label(top,text="Status  : ")
    dstatus.place(x=80,y=185)


    def clearer():
        fdoctorinput.delete(0, END)
        ldoctorinput.delete(0, END)
        speinput.delete(0, END)
        daddinput.delete(0, END)
        dmobinput.delete(0, END)
        
    def getdata():
        a=fdoctorinput.get()
        b=ldoctorinput.get()
        c=speinput.get()
        d=daddinput.get()
        e=dmobinput.get()
        add_doctor(a,b,c,d,e)
        dstatus.config(text="Status  : Doctor Added")
        clearer()

    submit = Button(top,text="Submit",command = getdata)
    submit.place(x=100,y=210)

    def closer():
        show_doctors()
        top.destroy()
        
    close = Button(top,text="Close & Refresh",command = closer)
    close.place(x=160,y=210)
        
    
    top.geometry('340x260')
    top.mainloop()

def removedoctor():
    top = Toplevel()
    top.title('Remove Doctor')
    
    doctornotext = Label(top,text="Doctor Number")
    doctornotext.place(x=20,y=60)
    
    doctornoinput= Entry(top,width=30)
    doctornoinput.place(x=125,y=60)
    
    fdoctortext = Label(top,text="First Name : ")
    fdoctortext.place(x=20,y=85)
    ldoctortext = Label(top,text="Last Name  : ")
    ldoctortext.place(x=20,y=110)        

    def checker():
        doctorno = int(doctornoinput.get())-1
        fname,lname=doctor_fnames()[doctorno],doctor_lnames()[doctorno]
        fdoctortext.config(text="First Name : "+fname)
        ldoctortext.config(text="Last Name : "+lname)
        
    check = Button(top,text="Check",command = checker)
    check.place(x=100,y=210)
    
    def closer():
        show_doctors()
        top.destroy()
        
    def remover():
        mydb = mysql.connector.connect(host='localhost',user='root',passwd='123',database='HOSPITAL')
        mycursor = mydb.cursor()
        doctorno = doctornoinput.get()
        sqlstatement = "DELETE FROM doctor where doct_id={0}".format(('"'+str(doctorno)+'"'))
        mycursor.execute(sqlstatement)

        sql1 = "SET @rank:=0;"
        sql2 = "update doctor set doct_id=@rank :=@rank+1;"
        mycursor.execute(sql1)
        mycursor.execute(sql2)
        mydb.commit()
        mydb.close()
        closer()
        

        
    close = Button(top,text="Remove",command = remover)
    close.place(x=160,y=210)
    
    top.geometry('340x260')
    top.mainloop()


addpatient = Button(frame2,command = adddoctor,height=2,width=13,text='Add')
addpatient.place(x=27,y=520)

removepatient = Button(frame2,height=2,command = removedoctor,width=13,text='Remove')
removepatient.place(x=140,y=520)

refreshpatient = Button(frame2,height=2,command = show_doctors,width=13,text='Refresh')
refreshpatient.place(x=253,y=520)

############################################################################################################
def getdate():
    mydb = mysql.connector.connect(host='localhost',user='root',passwd='123',database='HOSPITAL')
    mycursor = mydb.cursor()
    sql='select date from APPOINTMENTS;'
    mycursor.execute(sql)
    rows=mycursor.fetchall()
    dates=[]
    for i in rows:
        dates.append(i)
    return dates

def appoin_no():
    mydb = mysql.connector.connect(host='localhost',user='root',passwd='123',database='HOSPITAL')
    mycursor = mydb.cursor()
    sql = "select a_no from APPOINTMENTS"
    mycursor.execute(sql)
    rows = mycursor.fetchall()
    for i in rows :
        a_no = i
    try:
        return a_no[0]+1
    except:
        return int(1)
    mydb.close()

def removeappoin():
    top = Toplevel()
    top.title('Remove Doctor')
    
    apoinnotext = Label(top,text="Appoinment No : ")
    apoinnotext.place(x=20,y=60)
    
    apoinnoinput= Entry(top,width=30)
    apoinnoinput.place(x=125,y=60)
    
    fdoctortext = Label(top,text="Patient Name : ")
    fdoctortext.place(x=20,y=85)
    ldoctortext = Label(top,text="Doctor Name  : ")
    ldoctortext.place(x=20,y=110)        

    def checker():
        print(apoinnoinput.get(),type(apoinnoinput.get()))
        apoinno = int(apoinnoinput.get())-1
        fname,lname=get_doc_name()[apoinno],get_pat_name()[apoinno]
        fdoctortext.config(text="Patient Name : "+fname)
        ldoctortext.config(text="Doctor Name : "+lname)
        
    check = Button(top,text="Check",command = checker)
    check.place(x=100,y=210)

    def remover():
        mydb = mysql.connector.connect(host='localhost',user='root',passwd='123',database='HOSPITAL')
        mycursor = mydb.cursor()
        doctorno = apoinnoinput.get()
        sqlstatement = "DELETE FROM APPOINTMENTS where a_no={0}".format(('"'+str(doctorno)+'"'))
        mycursor.execute(sqlstatement)

        sql1 = "SET @rank:=0;"
        sql2 = "update APPOINTMENTS set a_no=@rank :=@rank+1;"
        mycursor.execute(sql1)
        mycursor.execute(sql2)
        mydb.commit()
        mydb.close()
        show_patients()
        top.destroy()

    close = Button(top,text="Remove",command = remover)
    close.place(x=160,y=210)
    
    top.geometry('340x260')
    top.mainloop()


def addapoin(a,b,c,d):
    x=d
    y=a
    z=b
    xx=c

    mydb = mysql.connector.connect(host='localhost',user='root',passwd='123',database='HOSPITAL')
    mycursor = mydb.cursor()
    
    sql = "insert into APPOINTMENTS (a_no, Doctor_Name, Patient_name, Date) values (%s,%s,%s,%s)"
    rows=[x,y,z,xx]
    mycursor.execute(sql,rows)
    mydb.commit()
    mydb.close()
    

    

def add_apoin():
    top = Toplevel()
    top.title('Add')

    v1=StringVar(top)
    doptions = doctor_names()
    doctortext = Label(top,text="Doctor : ")
    doctortext.place(x=20,y=60)
    
    doctorinput= OptionMenu(top,v1,(doptions))
    doctorinput.place(x=120,y=60)

    v2=StringVar(top)
    poptions = patient_names()
    patienttext = Label(top,text="Patient : ")
    patienttext.place(x=20,y=92)
    
    patientinput= OptionMenu(top,v2,(poptions))
    patientinput.place(x=120,y=92)

    def geter():
        v1value,v2value = v1.get(),v2.get()
        return v1value,v2value
        
    datetext = Label(top,text="Date : ")
    datetext.place(x=20,y=142)


    ent = DateEntry(top, width = 15,height=4
                    , background = 'black', foreground = 'white', borderwidth = 3,showweeknumbers = False)
    ent.place(x=125,y=142)

    def ent_val():
        top.date = ent.get_date()
        astatus.config(text="Status  :  Date"+str(top.date))
    

    dateinput= Button(top,text="Select Date",command = ent_val)
    dateinput.place(x=240,y=142)

    astatus = Label(top,text="Status : ")
    astatus.place(x=80,y=185)


    def getdata():
        a,b=geter()
        c=str(top.date).replace("-",".")
        d=appoin_no()

        addapoin(a,b,c,d)
        closer()

    submit = Button(top,text="Submit",command = getdata)
    submit.place(x=100,y=210)

    def closer():
        show_appoin()
        top.destroy()
        
    close = Button(top,text="Close & Refresh",command = closer)
    close.place(x=160,y=210)
        
    
    top.geometry('340x260')
    top.mainloop()
    

def appoin_details():
    adetails = zip(doctor_names(),patient_names(),getdate())
    return list(adetails)

def get_doc_name():
    mydb = mysql.connector.connect(host='localhost',user='root',passwd='123',database='hospital')
    mycursor = mydb.cursor()
    sql = "select doctor_name from APPOINTMENTS"
    mycursor.execute(sql)
    d_names = []
    rows = mycursor.fetchall()
    for i in rows :
        d_names.append(i[0])
    return d_names

def get_pat_name():
    mydb = mysql.connector.connect(host='localhost',user='root',passwd='123',database='hospital')
    mycursor = mydb.cursor()
    sql = "select patient_name from APPOINTMENTS"
    mycursor.execute(sql)
    p_names = []
    rows = mycursor.fetchall()
    for i in rows :
        p_names.append(i[0])
    return p_names

def get_appoin_details():
    details=zip(get_doc_name(),get_pat_name(),getdate())
    return details

def show_appoin():
    tempList = list(get_appoin_details())
    for j in listBox3.get_children():
        listBox3.delete(j)

    for i, (dname,pname,date) in enumerate(tempList, start=1):
        listBox3.insert("", "end", values=(i, dname,pname,date))

cols3 = ('S.No', 'Doctor Name', 'Patient Name','Date')
listBox3 = ttk.Treeview(frame3,height=10, columns=cols3, show='headings')

for col3 in cols3:
    listBox3.heading(col3, text=col3)

  
vsb3 = ttk.Scrollbar(frame1, orient="vertical", command=listBox3.yview)
vsb3.place(x=720, y=130, height=376)

listBox3.configure(yscrollcommand=vsb3.set)

style3 = ttk.Style(frame3)
style3.configure('Treeview', rowheight=35,font= '20')
listBox3.column('#1',width=80)
listBox3.column('#2',width=160)
listBox3.column('#3',width=160)
listBox3.column('#4',width=160)


listBox3.place(x=27,y=130)

addpatient = Button(frame3,command = add_apoin,height=2,width=13,text='Add')
addpatient.place(x=27,y=520)

removepatient = Button(frame3,height=2,command = removeappoin,width=13,text='Remove')
removepatient.place(x=140,y=520)

refreshpatient = Button(frame3,height=2,command = show_appoin,width=13,text='Refresh')
refreshpatient.place(x=253,y=520)

root.geometry('980x650')
root.mainloop()
