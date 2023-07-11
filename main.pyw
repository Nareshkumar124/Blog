from customtkinter import *
from PIL import Image
import tkinter
from tkinter import messagebox
import psycopg2
import threading
import io
from smtplib import SMTP_SSL
from email.message import EmailMessage
from validate_email import validate_email
from random import shuffle
# scaling-------------------------------------------------------------------------
# set_default_color_theme('green')
check=False
def scaling(scalingValue):
        scalingValueFloat = int(scalingValue.replace("%", "")) / 100
        set_widget_scaling(scalingValueFloat)

# window theme color------------------------------------------------------------------
def setTheme(value):
    if value=="Dark":
        nameButton.configure(text_color='white')
        set_appearance_mode('dark')     
    else:
        nameButton.configure(text_color='black')
        set_appearance_mode('light')
# Databse connection -----------------------------------------------------------------
def Database(q,send=False):
    conn=None
    cur=None
    try:
        conn=psycopg2.connect(
            database="exam",
            user='postgres',
            password="Naresh@123",
            host="localhost",
            port=5432
        )
        cur=conn.cursor()
        # fetch data----------------
        cur.execute(q)
        if send:
            conn.commit()
            return True
        else: 
            data=cur.fetchall()
            return data

    except Exception as e:
        print(e)
        messagebox.showerror("Database",e)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

# submit Button functionality-----------------------------------------------------------------
def submit(uid,password):
    try:
        uid=int(uid.get())
    except:
        messagebox.showwarning('Warning','AUID format is not valid.')
        return
    exUidPassword=Database(f'SELECT auid , password FROM student WHERE auid = {uid}')
    # print(exUidPassword)
    if exUidPassword is None:
        return
    else:
        if len(exUidPassword)==0:
            messagebox.showinfo("Databse",'No data available in database.')
        elif exUidPassword[0][1]==password.get():
            loginFrame.place_forget()
            win.unbind('<Return>')
            mainWindow(uid)
        else:
            messagebox.showerror("Error",'Password is not correct.')

# login page gui----------------------------------------------------------------------------
def loginGui():
    #Placeholder function-----------------------------------------
    def onEntry(e):
        if uidValue.get()=="UID":
            uid.delete(0,END)
    def onLeave(e):
        if uidValue.get()=='':
            uid.insert(0,"UID")
    def onEntry1(e):
        password.configure(show="*")
        if passwordValue.get()=="Password":
            password.delete(0,END)
    def onLeave1(e):
        if passwordValue.get()=='':
            password.configure(show='')
            password.insert(0,"Password")
    #---------------------------------------------------------------
    uidValue=StringVar()
    passwordValue=StringVar()
    image=CTkImage(light_image=Image.open('photo\img3.png'),dark_image=Image.open('photo/img3.png'),size=(300,300))
    img=CTkLabel(loginFrame,image=image,text='').grid(row=0,column=0,pady=90,padx=40)
    entryFrame=CTkFrame(loginFrame,width=300,height=400)
    loginText=CTkLabel(entryFrame,text="Login",font=('Roboto',50)).pack(pady=10,padx=80)
    uid=CTkEntry(entryFrame,width=300,height=50,font=('Roboto',20),textvariable=uidValue)
    uid.insert(0,"UID")
    uid.bind('<FocusIn>',onEntry)
    uid.bind('<FocusOut>',onLeave)
    uid.pack(pady=10,padx=10)
    password=CTkEntry(entryFrame,width=300,height=50,font=('Roboto',20),textvariable=passwordValue)
    password.insert(0,"Password")
    password.bind('<FocusIn>',onEntry1)
    password.bind('<FocusOut>',onLeave1)
    password.pack(pady=10,padx=10) #textvariable=password
    submitButton=CTkButton(entryFrame,text='Submit',width=300,height=50,font=('Roboto',25),command=lambda:submit(uidValue,passwordValue))
    submitButton.pack(pady=10,padx=10)
    win.bind("<Return>",lambda X:submit(uidValue,passwordValue))
    entryFrame.grid(row=0,column=1,padx=60)
    loginFrame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
def optionFrameGui(uid):
    exStudentName=Database(f"SELECT firstname || ' ' || lastname FROM student WHERE auid={uid};")
    studentNameFrame=CTkFrame(optionFrame,height=200)
    UserImage=CTkImage(light_image=Image.open('photo/user1.png'),dark_image=Image.open('photo/user.png'),size=(25,25))
    global nameButton
    nameButton=CTkButton(studentNameFrame,text=exStudentName[0][0].title(),font=("Roboto", 20 ,"bold"),command=lambda:studentInformationGui(uid),height=50,image=UserImage,fg_color='transparent',text_color='white')
    nameButton.grid(row=0,column=0,pady=5,padx=10)
    studentNameFrame.grid(row=0,column=0,padx=10,pady=20)
    # name text_color----------------------------------- 
    if get_appearance_mode()=="Light":
        nameButton.configure(text_color='black')
    #Image-----------------------------------------------
    homeImage=CTkImage(light_image=Image.open('photo/home.png'),dark_image=Image.open('photo/home.png'),size=(20,20))
    resultImage=CTkImage(light_image=Image.open('photo/result.png'),dark_image=Image.open('photo/result.png'),size=(20,20))
    aboutImage=CTkImage(light_image=Image.open('photo/about.png'),dark_image=Image.open('photo/about.png'),size=(20,20))
    #Button----------------------------------------------
    homeButton=CTkButton(optionFrame,text="Home",height=40,font=("Roboto", 20),image=homeImage,command=home)
    homeButton.grid(row=2,column=0,pady=10,padx=10)
    resultButton=CTkButton(optionFrame,text="Result",height=40,font=("Roboto", 20),image=resultImage,command=lambda:resultGui(uid))
    resultButton.grid(row=3,column=0,pady=10,padx=10) 
    AboutButton=CTkButton(optionFrame,text="About",height=40,font=("Roboto", 20),image=aboutImage,command=aboutGui)
    AboutButton.grid(row=4,column=0,pady=10,padx=10)    
    themeButton=CTkOptionMenu(optionFrame,values=["Dark","Light"],font=("Roboto", 20),height=40,command=setTheme)
    themeButton.set('Theme')
    themeButton.grid(row=5,column=0,padx=10,pady=10)
    scaleButton=CTkOptionMenu(optionFrame,values=["100%","95%","90%","85%"],command=scaling,font=("Roboto", 20),height=40)
    scaleButton.set('Scaling')
    scaleButton.grid(row=6,column=0,padx=10,pady=10)
    optionFrame.pack(side='left',fill=Y)

def textFrameGui():
    # header=CTkImage(dark_image=Image.open("photo/h.png"),light_image=Image.open("photo/h.png"),size=(750,200))
    # headerLabel=CTkLabel(textFrame,image=header,text="")
    # headerLabel.pack(padx=2,pady=2)
    textFrame.pack(side='top',fill=X,pady=5,padx=5)

def subjectFrameGui(uid):
    exSubject=Database(f'''SELECT title,subject_id,start_date,end_date,image FROM student
    JOIN course_subject USING(course_id)
    JOIN subject USING (subject_id) LEFT JOIN timimg USING(subject_id)
    WHERE auid={uid};''')
    # subject button in loop--------------------------------------------------
    for i in exSubject:
        if i[4]!=None:
            bookImage=CTkImage(light_image=Image.open(io.BytesIO(i[4])),dark_image=Image.open(io.BytesIO(i[4])),size=(150,150))
        else:
            bookImage=CTkImage(light_image=Image.open('photo/book.png'),dark_image=Image.open('photo/book.png'),size=(150,150))
        # button of subject---------------------------------
        def buttonValue(subject_id=i[1]):
            questionGui(uid,subject_id)
        #---------------------------------------------------
        singleSubjectFrame=CTkFrame(subjectFrame,border_width=1)
        subjectImage=CTkLabel(singleSubjectFrame,image=bookImage,text="")
        subjectImage.grid(row=0,column=0,rowspan=4,padx=10,pady=10)

        subjectName=CTkLabel(singleSubjectFrame,text=f"{i[0]}",font=("Roboto",40))
        subjectName.grid(row=0,column=1,pady=5,padx=30,sticky = W)
        if i[2]!=None:
            subjectst=CTkLabel(singleSubjectFrame,text=f"Start Time: {i[2].strftime('%c')}",font=("Roboto",20))
            subjectst.grid(row=1,column=1,pady=5,padx=30,sticky = W)

            subjectet=CTkLabel(singleSubjectFrame,text=f"End Time: {i[3].strftime('%c')}",font=("Roboto",20))
            subjectet.grid(row=2,column=1,pady=5,padx=30,sticky = W)
        else:
            subjectst=CTkLabel(singleSubjectFrame,text="Start Time: Not Scheduled",font=("Roboto",20))
            subjectst.grid(row=1,column=1,pady=5,padx=30,sticky = W)

            subjectet=CTkLabel(singleSubjectFrame,text="End Time: Not Scheduled",font=("Roboto",20))
            subjectet.grid(row=2,column=1,pady=5,padx=30,sticky = W)

        subjectButton=CTkButton(singleSubjectFrame,text=f"Attempt",width=300,font=("Roboto",30),command=buttonValue)
        subjectButton.grid(row=3,column=1,padx=30,pady=5,sticky = W)

        singleSubjectFrame.pack(padx=5,pady=5,fill=X,expand=True)  
    subjectFrame.pack(fill='both',expand=True,padx=5,pady=5)

def examTime(subject_id):
    examTimeSE=Database(f"SELECT start_date,end_date FROM timimg WHERE subject_id={subject_id}")
    examTimeN=Database("SELECT NOW()::TIMESTAMP")
    if len(examTimeSE)==0:
        messagebox.showinfo("Eaxm","Exam is not scheduled.")
        return False
    if ((v1:=examTimeSE[0][0]<=examTimeN[0][0]) and (v2:=examTimeSE[0][1]>=examTimeN[0][0])):
        return True
    else:
        if not v1:
            messagebox.showinfo('Exam',f"Exam will start at {examTimeSE[0][0]}")
        else:
            messagebox.showinfo("Exam","Exam Time is out.")
        return False
    
def questionGui(uid,subject_id):
    examTimeValue=True
    submitorNot=Database(f'''SELECT * FROM submit WHERE auid={uid} and subject_id = {subject_id};''')
    if  len(submitorNot)==0: #(examTimeValue:=examTime(subject_id)) and
        global check
        check=True
        subjectFrame.pack_forget()
        # questionFrame-----------------------------------------
        exQus=Database(f'''SELECT question_id,question,option_1,option_2,option_3,option_4 FROM student
                        JOIN course_subject USING(course_id)
                        JOIN question USING(subject_id)
                        WHERE auid={uid} and subject_id={subject_id};''')
        if len(exQus)==0:
            subjectFrame.pack(fill='both',expand=True,padx=5,pady=5)
            messagebox.showinfo("Question",'Question are not available.')
            check=False
            return
        # questionOptionFrame-------------------------------------
        var=[]
        qId=[]
        for i in range(len(exQus)):
            var.append(StringVar())
            qId.append(exQus[i][0])
        # timeFrame--------------------------------------------
        # duration=Database(f"SELECT duration FROM timimg WHERE subject_id={subject_id}")[0][0]
        duration=100
        # --------------------------------------------------------
        subName=Database(f'SELECT title FROM subject WHERE subject_id={subject_id}')
        print(subName)
        timeFrame=CTkFrame(questionFrame,height=50)
        durationFrame=CTkLabel(timeFrame,text=f'Time:- {00} : {00} : {00}',font=("Roboto",40))
        durationFrame.pack(side="right",padx=20)
        subLabel=CTkLabel(timeFrame,text=subName[0][0],font=("Roboto",40))
        subLabel.pack(side="left",padx=20)
        timeFunction(duration,durationFrame,var,uid,qId,subject_id)
        timeFrame.pack(padx=5,pady=5,fill=X)
        # --------------------------------------------------------------
        questionOptionFrame=CTkScrollableFrame(questionFrame)
        for index,ques in enumerate(exQus):
            suffOption=list(ques[2:6])
            shuffle(suffOption)

            singleQuestionFrame=CTkFrame(questionOptionFrame)
            # questionBox----------------------------------------------
            questionLabel=CTkLabel(singleQuestionFrame,text=f"Qus.{index+1} {ques[1]}",font=("Roboto",25),wraplength=700,justify="left")
            questionLabel.grid(row=0,column=0,padx=10,pady=5,sticky=W)
            for i,text in enumerate(suffOption): #ques[2:6]
                option=CTkRadioButton(singleQuestionFrame,text=f'{text}',font=("Roboto",25),value=text,variable=var[index])
                option.grid(row=i+1,column=0,sticky=W,padx=10,pady=5)

            clearButton=CTkButton(singleQuestionFrame,text="Clear",width=300,command=option.deselect)
            clearButton.grid(row=5,column=0,sticky=W,pady=5,padx=10)
            
            # ---------------------------------------------------------------
            singleQuestionFrame.pack(padx=5,pady=5,fill=X)
        win.protocol("WM_DELETE_WINDOW",lambda:ansSubmit(var,uid,qId,subject_id,win_destroy=True))
        questionOptionFrame.pack(padx=5,pady=5,fill="both",expand=True)
        ansSubmitButton=CTkButton(questionFrame,text="Submit",width=300,height=35,command=lambda:ansSubmit(var,uid,qId,subject_id))
        ansSubmitButton.pack(side="right",padx=10,pady=(0,5))
        questionFrame.pack(fill='both',expand=True,padx=5,pady=(0,5))
    
    elif examTimeValue:
        messagebox.showinfo('submit','Test is already submit.')
        return

def ansSubmit(var,uid,qId,sId,permission=False,win_destroy=False):
    # senddata-----------------------------------
    if not permission:
        per=messagebox.askquestion("Submit",'You want to submit these question.')
        if per!='yes':
            return
        else:
            permission=True

    if permission:
        for i,anss in enumerate(var):
            if anss.get()=='':
                ans='NOT'
            else:
                ans=anss.get()
            Database(f'''INSERT INTO answer VALUES({int(uid)},{qId[i]},'{ans}');''',send=True)
        Database(f'''INSERT INTO submit VALUES({int(uid)},{int(sId)});''',send=True)
        global check
        check=False
        for wig in questionFrame.winfo_children():
            wig.destroy()
        questionFrame.pack_forget()
        textFrame.pack_forget()
        packFrame.clear()
        home()

        #protocall
        if win_destroy:
            win.destroy()
        else:
            win.protocol("WM_DELETE_WINDOW",win.destroy)

def timeFunction(duration,durationFrame,var,uid,qId,subject_id):
        seconds=duration%60
        minutes=(duration//60)%60
        hours=duration//3600
        durationFrame.configure(text=f"Time:- {hours:02} : {minutes:02} : {seconds:02}")
        duration=duration-1
        if duration==-1:
            messagebox.showinfo("Submit","Time up, Submit these question.")
            ansSubmit(var,uid,qId,subject_id,permission=True)
            return
        durationFrame.after(1000,lambda:timeFunction(duration,durationFrame,var,uid,qId,subject_id))

def studentInformationGui(uid):
    textFrame.pack_forget()
    subjectFrame.pack_forget()
    resultFrame.pack_forget()
    aboutFrame.pack_forget()
    questionFrame.pack_forget()
    if "studentInformationFrame" not in packFrame:
        for widget in studentInformationFrame.winfo_children(): #destroy old widget--
            widget.destroy()
        packFrame.clear()
        packFrame.append("studentInformationFrame")
        # Query---------------------
        exInformation=Database(f'''SELECT auid,firstname||' '|| lastname,email,course.name,sem,department.name
                                FROM student
                                JOIN course USING(course_id)
                                JOIN department USING(dept_id)
                                WHERE auid={uid}''')

        # ----------------------------------------------------------------------------------------------------------------
        editProfileFrame=CTkFrame(studentInformationFrame,fg_color='transparent')
        editImage=CTkImage(dark_image=Image.open('photo/edit.png'),light_image=Image.open('photo/edit.png'),size=(25,25))
        button1=CTkButton(editProfileFrame,text="Edit Profile",font=('Roboto',20),height=40,image=editImage,command=lambda:editProfile(uid))
        button1.pack(side="right",padx=20,pady=(10,0))
        editProfileFrame.pack(padx=10,pady=10,fill=X)
        profileImageLode=CTkImage(dark_image=Image.open("photo/profile.png"),light_image=Image.open("photo/profile1.png"),size=(300,300))
        profileImageLabel=CTkLabel(studentInformationFrame,text='',image=profileImageLode)
        profileImageLabel.pack()
        nameLabel=CTkLabel(studentInformationFrame,text=f'{exInformation[0][1].title()}',font=('Roboto',50))
        nameLabel.pack(padx=5)
        uidLabel=CTkLabel(studentInformationFrame,text=f"UID: {exInformation[0][0]}",font=('Roboto',30))
        uidLabel.pack()

        subInformationFarme=CTkFrame(studentInformationFrame,border_width=2)

        couresLabel=CTkLabel(subInformationFarme,text=f"Course:",font=('Roboto',30),justify="left")
        couresLabel.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        couresLabel2=CTkLabel(subInformationFarme,text=f"{exInformation[0][3]}, {exInformation[0][4]} SEM",font=('Roboto',30),justify="left")
        couresLabel2.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        emailLabel=CTkLabel(subInformationFarme,text=f"Email:",font=('Roboto',30))
        emailLabel.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        emailLabel2=CTkLabel(subInformationFarme,text=f"{exInformation[0][2]}",font=('Roboto',30))
        emailLabel2.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        deptLabel=CTkLabel(subInformationFarme,text=f"Department:",font=('Roboto',30))
        deptLabel.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        deptLabel2=CTkLabel(subInformationFarme,text=f"{exInformation[0][5]}",font=('Roboto',30))
        deptLabel2.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        subInformationFarme.pack(padx=10,pady=30)

        # ---------------------------------------------------------------------------------------------------------------------
        studentInformationFrame.pack(pady=5,padx=5,fill="both",expand=True)
        print(packFrame)

def editProfile(uid):
    for widget in studentInformationFrame.winfo_children(): #destroy old widget--
            widget.destroy()
    packFrame.clear()
    data=Database(f"SELECT firstname,lastname,email,password FROM student WHERE auid= {uid}")
    name1=StringVar()
    name2=StringVar()
    email=StringVar()
    password=StringVar()

    editFarme=CTkFrame(studentInformationFrame,border_width=2)
    l1=CTkLabel(editFarme,text="Update Information",font=("Roboto",30))
    l1.grid(row=0,column=0,pady=(5,10),padx=10)


    name1Label=CTkLabel(editFarme,text="First Name:",font=("Roboto",20))
    name1Label.grid(row=1,column=0,pady=(0,5),padx=40,sticky=W)
    name1Entry=CTkEntry(editFarme,font=("Roboto",20),width=500,height=40,textvariable=name1)
    name1Entry.grid(row=2,column=0,pady=(0,10),padx=40,sticky=W)
    name1Entry.insert(0,data[0][0])

    name2Label=CTkLabel(editFarme,text="Last Name:",font=("Roboto",20))
    name2Label.grid(row=3,column=0,pady=(20,5),padx=40,sticky=W)
    name2Entry=CTkEntry(editFarme,font=("Roboto",20),width=500,height=40,textvariable=name2)
    name2Entry.grid(row=4,column=0,pady=(0,10),padx=40,sticky=W)
    name2Entry.insert(0,data[0][1])

    emailLabel=CTkLabel(editFarme,text="Email:",font=("Roboto",20))
    emailLabel.grid(row=5,column=0,pady=(20,5),padx=40,sticky=W)
    emailEntry=CTkEntry(editFarme,font=("Roboto",20),width=500,height=40,textvariable=email)
    emailEntry.grid(row=6,column=0,pady=(0,10),padx=40,sticky=W)
    emailEntry.insert(0,data[0][2])

    passwordLabel=CTkLabel(editFarme,text="Password:",font=("Roboto",20))
    passwordLabel.grid(row=7,column=0,pady=(20,5),padx=40,sticky=W)
    passwordEntry=CTkEntry(editFarme,font=("Roboto",20),width=500,height=40,textvariable=password)
    passwordEntry.grid(row=8,column=0,pady=(0,10),padx=40,sticky=W)
    passwordEntry.insert(0,data[0][3])

    s_button=CTkButton(editFarme,text="Submit",font=("Roboto",20),command=lambda:profileSubmit(name1,name2,email,password,uid))
    s_button.grid(row=9,column=0,padx=40,pady=(5,20))

    editFarme.pack(pady=(100,0),padx=10)
    

def profileSubmit(name1,name2,email,password,uid):
    name1=name1.get()
    name2=name2.get()
    email=email.get()
    password=password.get()
    if len(name1)>50 or len(name2)>50:
        messagebox.showinfo("Submit","Choose a short name.")
        return
    if len(name1)<3 or len(name2)<3:
        messagebox.showinfo("Submit","Choose a long name.")
        return
    if not validate_email(email):
        messagebox.showinfo("Sunmit","Email is not valid.")
        return
    if len(password)>50:
        messagebox.showinfo('submit',"Choose a short password.")
        return
    if len(password)<6:
        messagebox.showinfo('Submit',"Choose a long password.")
        return
    check=Database(f'''UPDATE student 
                SET firstname='{name1}',lastname='{name2}',email='{email}',password='{password}'
                WHERE auid={uid};''',send=True)
    if check:
        messagebox.showinfo('Submit','Your information has been updated.')
        studentInformationGui(uid)
        nameButton.configure(text=f"{name1} {name2}".title())

    
    
    

def home():
    studentInformationFrame.pack_forget()
    resultFrame.pack_forget()
    aboutFrame.pack_forget()
    if "subjectFrame" not in packFrame:
        packFrame.clear()
        packFrame.append('subjectFrame')
        textFrame.pack(side='top',fill=X,pady=5,padx=5)
        if check:
            questionFrame.pack(fill='both',expand=True,padx=5,pady=5)
        else:
            subjectFrame.pack(fill='both',expand=True,padx=5,pady=5)
        print(packFrame)
    
def resultGui(uid):
    textFrame.pack_forget()
    subjectFrame.pack_forget()
    aboutFrame.pack_forget()
    studentInformationFrame.pack_forget()
    questionFrame.pack_forget()
    if "resultFrame" not in packFrame:
        packFrame.clear()
        packFrame.append("resultFrame")
        for widget in resultFrame.winfo_children(): #destroy old widget--
            widget.destroy()
        
        # RESULT GUI-----------------------------------------------------
        
        exSubject=Database(f'''SELECT title,subject_id,image FROM student
        JOIN course_subject USING(course_id)
        JOIN subject USING (subject_id) LEFT JOIN timimg USING(subject_id)
        WHERE auid={uid};''')

        #resualt mail Frame-------------------------------------------------------
        resmailFrame=CTkFrame(resultFrame)
        resultButtonImage=CTkImage(dark_image=Image.open('photo/exam-results.png'),light_image=Image.open('photo/exam-results.png'),size=(20,20))
        resultButton=CTkButton(resmailFrame,text="Result",height=40,font=("Roboto",20),image=resultButtonImage,command=lambda:resultInApp(uid))
        resultButton.pack(padx=10,pady=5,side="left")
        mailButtonImage=CTkImage(dark_image=Image.open('photo/mail.png'),light_image=Image.open('photo/mail.png'),size=(25,25))
        mailButton=CTkButton(resmailFrame,text="Mail",height=40,font=("Roboto",20),image=mailButtonImage,command=lambda:threading.Thread(target=resultMail,args=(uid,)).start())
        mailButton.pack(padx=10,pady=5,side="right")
        resmailFrame.pack(padx=5,pady=5,fill=X) 

    # subject button in loop--------------------------------------------------
        for i in exSubject:
            if i[2]!=None:
                bookImage=CTkImage(light_image=Image.open(io.BytesIO(i[2])),dark_image=Image.open(io.BytesIO(i[2])),size=(150,150))
            else:
                bookImage=CTkImage(light_image=Image.open('photo/book.png'),dark_image=Image.open('photo/book.png'),size=(150,150))
            # button of subject---------------------------------
            def buttonValue(subject_id=i[1]):
                studentResult(uid,subject_id)
                # questionGui(uid,subject_id)
            #---------------------------------------------------
            singleSubjectFrame=CTkFrame(resultFrame,border_width=1)
            subjectImage=CTkLabel(singleSubjectFrame,image=bookImage,text="")
            subjectImage.grid(row=0,column=0,rowspan=3,padx=10,pady=10)

            subjectName=CTkLabel(singleSubjectFrame,text=f"{i[0]}",font=("Roboto",40))
            subjectName.grid(row=0,column=1,pady=5,padx=30,sticky = W)
            des=CTkLabel(singleSubjectFrame,text=f"Check answer with question:",font=("Roboto",20))
            des.grid(row=1,column=1,pady=(5,1),padx=30,sticky = W)

            subjectButton=CTkButton(singleSubjectFrame,text=f"Check",width=300,height=40,font=("Roboto",30),command=buttonValue)
            subjectButton.grid(row=2,column=1,padx=30,pady=5,sticky = W)

            singleSubjectFrame.pack(padx=5,pady=5,fill=X,expand=True)
        resultFrame.pack(pady=5,padx=5,fill="both",expand=True)
        print(packFrame)

def studentResult(uid,subject_id):
    exSubmitorNot=Database(f"SELECT * FROM submit WHERE auid = {uid} and subject_id={subject_id};")
    print(exSubmitorNot)
    if len(exSubmitorNot)==0:
        messagebox.showinfo("Result","Result is not available.")
        return
    else:
        exQuestionAnsansRight=Database(f"SELECT question,answer,student_answer FROM answer JOIN question USING(question_id) WHERE auid={uid} and subject_id = {subject_id};")
        for widget in resultFrame.winfo_children(): #destroy old widget--
                widget.destroy()
        packFrame.clear()
        backButtonFrame=CTkFrame(resultFrame)
        backImage=CTkImage(dark_image=Image.open('photo/back.png'),light_image=Image.open('photo/back.png'),size=(20,20))
        backButton=CTkButton(backButtonFrame,text="Back",command=lambda:resultGui(uid),image=backImage,height=40,font=("Roboto",20))
        backButton.pack(padx=10,pady=5,side="left")

        resultButtonImage=CTkImage(dark_image=Image.open('photo/exam-results.png'),light_image=Image.open('photo/exam-results.png'),size=(20,20))
        resultButton=CTkButton(backButtonFrame,text="Result",height=40,font=("Roboto",20),image=resultButtonImage,command=lambda:resultInApp(uid))
        resultButton.pack(padx=10,pady=5,side="right")

        mailButtonImage=CTkImage(dark_image=Image.open('photo/mail.png'),light_image=Image.open('photo/mail.png'),size=(25,25))
        mailButton=CTkButton(backButtonFrame,text="Mail",height=40,font=("Roboto",20),image=mailButtonImage,command=lambda:threading.Thread(target=resultMail,args=(uid,)).start())
        mailButton.pack(padx=10,pady=5,side="right")
        backButtonFrame.pack(padx=5,pady=5,fill=X)


        for index,i in enumerate(exQuestionAnsansRight):
            # Now pack resualt--------------------------------------------------
            singleQuestionFrame=CTkFrame(resultFrame,border_width=1)
            # questionBox----------------------------------------------
            questionLabel=CTkLabel(singleQuestionFrame,text=f"Qus.{index+1} {i[0]}",font=("Roboto",25),wraplength=700,justify="left")
            questionLabel.grid(row=0,column=0,padx=10,pady=5,sticky=W)
            answer=CTkLabel(singleQuestionFrame,text=f"Right Answer: {i[1]}",font=("Roboto",20))
            answer.grid(row=1,column=0,padx=10,pady=5,sticky=W)
            studenAnswer=CTkLabel(singleQuestionFrame,text=f"Your answer: {i[2]}",font=("Roboto",20))
            studenAnswer.grid(row=2,column=0,padx=10,sticky=W)
            if i[2]==i[1]:
                rightwrong=CTkLabel(singleQuestionFrame,text="Your answer is right.",font=("Roboto",13),text_color='#4b6043')
            elif i[2]=="NOT":
                rightwrong=CTkLabel(singleQuestionFrame,text="Not Attempted",text_color='#4b6043',font=("Roboto",13))
            else:
                rightwrong=CTkLabel(singleQuestionFrame,text="Your answer is wrong.",text_color='#EF5350',font=("Roboto",13))
            rightwrong.grid(row=3,column=0,padx=10,pady=2.5,sticky=W)
            # ---------------------------------------------------------------
            singleQuestionFrame.pack(padx=5,pady=5,fill=X)
            
                          
def aboutGui():
    import json
    with open("photo/about.json",'r')as f:
        data=f.read()
    data2=json.loads(data)
    textFrame.pack_forget()
    subjectFrame.pack_forget()
    resultFrame.pack_forget()
    questionFrame.pack_forget()
    studentInformationFrame.pack_forget()
    if "aboutFrame" not in packFrame:
        packFrame.clear()
        packFrame.append("aboutFrame")
        for widget in aboutFrame.winfo_children(): #destroy old widget--
            widget.destroy()
        aboutText=CTkLabel(aboutFrame,text="About",font=("Roboto",50,"bold"))
        aboutText.pack(pady=(20,5))
        text=CTkScrollableFrame(aboutFrame,width=805)
        text1=CTkLabel(text,text=data2["about"],font=("Roboto",25),wraplength=800,justify="left")
        text1.pack(padx=5,pady=5)
        text.pack(pady=10,fill=Y,expand=True)
        aboutFrame.pack(pady=5,padx=5,fill="both",expand=True)
        print(packFrame)

def table(root,data,totalNumber):
    row=len(data)
    column=len(data[0])
    i=0
    for j in range(column):
        cell=CTkLabel(root,text=f"{data[i][j]}",wraplength=150,font=("Roboto",20,"bold"),fg_color='#1f6aa5',corner_radius=5)
        cell.grid(row=i,column=j,padx=10,pady=10,ipadx=5,ipady=5)

    for i in range(1,row):
        for j in range(column):
            cell=CTkLabel(root,text=f"{data[i][j]}",wraplength=150,font=("Roboto",20))
            cell.grid(row=i,column=j,padx=10,pady=10)
    row=row+1
    cell=CTkLabel(root,text=f"Total Marks",font=("Roboto",30,'bold'))
    cell.grid(row=row,column=0,padx=10,pady=30,columnspan=5)
    cell=CTkLabel(root,text=f"{totalNumber}",wraplength=150,font=("Roboto",30,'bold'))
    cell.grid(row=row,column=5,padx=10,pady=30,ipadx=10,ipady=10)
        
def resultInApp(uid):
    packFrame.clear()
    for widget in resultFrame.winfo_children(): #destroy old widget--
                widget.destroy()
    Label=CTkLabel(resultFrame,text="Student Result",font=("Roboto",40,"bold"))
    Label.pack(padx=10,pady=10)
    resFrame=CTkFrame(resultFrame,border_width=2)
    resData1=resultQueries(uid)
    resData2=[]
    totalNumber=0
    for res in resData1:
        resData2.append(list(res))
    for i,res in enumerate(resData2):
        x=(res[1]*4)+(res[2]*(-1))
        res.append(x)
        totalNumber+=x

    resData2.insert(0,("Subject",'Right Answer','Wrong Answer','Not Attempted',"Total Question",'Marks'))
    table(resFrame,resData2,totalNumber)

    resFrame.pack(padx=20,pady=20,fill=Y,expand=True)
    

def resultQueries(uid):

    exSubject=Database(f'''
    SELECT subject.subject_id,title from student
    JOIN course_subject USING(course_id)
    JOIN subject USING(subject_id)  JOIN submit USING(subject_id,auid) 
    WHERE student.auid={uid};
    ''')
    resultList=[]
    for i in exSubject:
        subjectNumber=Database(f'''
        SELECT 
        count(*) FILTER(WHERE question.answer=answer.student_answer) as right,
        count(*) FILTER(WHERE question.answer!=answer.student_answer and answer.student_answer!='NOT' ) as wrong,
        count(*) FILTER(WHERE answer.student_answer='NOT') as Not_attepted,
        count(*) as Total 
        FROM answer
        JOIN question USING(question_id)
        WHERE auid={uid} and subject_id = {i[0]};
        ''')
        resultList.append((i[1],subjectNumber[0][0],subjectNumber[0][1],subjectNumber[0][2],subjectNumber[0][3]))
    return resultList

def resultMail(uid):
    bar.start()
    SENDER_EMAIL='Mtemp2534@gmail.com'
    MAIL_PASSWORD='xwboxfpobtyhfzrm'
    RECEIVER_EMAIL=Database(f"SELECT email from student Where auid={uid}")[0][0]
    # Quries ------------------------------------------------------------------------
    studentName=Database(f"SELECT firstname||' '|| lastname from student WHERE auid={uid}")[0][0]
    resultList=resultQueries(uid)
    subBody=""
    totalNumber=0
    for res in resultList:
        rightNumber=res[1]*4
        wrongNumber=res[2]*(-1)
        total=rightNumber+wrongNumber
        totalNumber+=total
        # presentage=(total/(res[4]*4))*100
 
        # mail Table content-----------------------------------
        subBody+=f'''
    			<tr>
					<td class="subject">{res[0]}</td>
					<td class="marks">{total}</td>
				</tr>
                '''
    subBody+=f'''
    			<tr>
					<td class="subject">Total</td>
					<td class="marks">{totalNumber}</td>
				</tr>
                '''
    # --------------------------------------------------------------------------------
    
    mail_body=f"""
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>Student Result</title>
	<style>
		body {{
			background-color: #F5F5F5;
			font-family: Arial, sans-serif;
			font-size: 16px;
			line-height: 1.5;
		}}
		.container {{
			max-width: 600px;
			margin: 0 auto;
			background-color: #FFFFFF;
			padding: 20px;
			box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
			border-radius: 10px;
		}}
		h1 {{
			text-align: center;
			font-size: 36px;
			color: #444444;
			margin-bottom: 20px;
		}}
		p {{
			color: #666666;
			margin-bottom: 10px;
		}}
		table {{
			width: 100%;
			border-collapse: collapse;
			margin-bottom: 20px;
		}}
		th, td {{
			padding: 10px;
			text-align: left;
			border-bottom: 1px solid #DDDDDD;
		}}
		th {{
			font-size: 20px;
			font-weight: bold;
			color: #444444;
			background-color: #F2F2F2;
			border-top: 1px solid #DDDDDD;
			border-left: 1px solid #DDDDDD;
			border-right: 1px solid #DDDDDD;
		}}
		td {{
			font-size: 20px;
			color: #666666;
			border-left: 1px solid #DDDDDD;
			border-right: 1px solid #DDDDDD;
		}}
		.subject {{
			font-weight: bold;
			color: #0066CC;
		}}
		.marks {{
			font-weight: bold;
			color: #00CC66;
		}}
	</style>
</head>
<body>
	<div class="container">
		<h1>Student Result</h1>
		<h2>Dear {studentName},</h2>
		<p>We are pleased to inform you that your recent examination results have been released:</p>
		<table>
			<thead>
				<tr>
					<th>Subject</th>
					<th>Marks</th>
				</tr>
			</thead>
			<tbody>
				{subBody}
			</tbody>
		</table>
		<p>If you have any questions about your marks or would like to discuss your progress, please don't hesitate to contact your teacher or academic advisor.</p>
		<p>Best regards,</p>
		<p>Akal University</p>
	</div>
</body>
</html>
    """
    subject="Exam Result"
    sendMail(SENDER_EMAIL,RECEIVER_EMAIL,MAIL_PASSWORD,subject,mail_body)

def sendMail(SENDER_EMAIL,RECEIVER_EMAIL,MAIL_PASSWORD,subject,mail_body):
    msg=EmailMessage()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg['Subject'] = subject
    msg.add_alternative(mail_body,subtype="html")
    try:
        with SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(SENDER_EMAIL, MAIL_PASSWORD) 
            smtp.send_message(msg)
            smtp.close()
    except Exception as e:
        bar.stop()
        bar.set(0)
        messagebox.showinfo('Mail',e)
    else:
        bar.stop()
        bar.set(0)
        messagebox.showinfo('Mail',"Your mail has been sent.")

def mainWindow(uid):
    optionFrameGui(uid)
    textFrameGui()
    subjectFrameGui(uid)
    packFrame.append("subjectFrame")
    win.geometry('1300x730+100+100')
    win.state("zoomed")
    print(packFrame)

packFrame=[] #information about frame pack
win=CTk()
# window configration--------------------------------------------------------------------------
s_width=win.winfo_screenwidth()
s_height=win.winfo_screenheight()
w_width=900
w_height=510
x=(s_width/2)-(w_width/2)
y=(s_height/2)-(w_height/2)
print(x,y)
win.geometry(f'{w_width}x{w_height}+{int(x)}+{int(y)}')

win.title('Exam')
# Frame----------------------------------------------------------------------------------------
bar=CTkProgressBar(win,corner_radius=0,determinate_speed=2)
bar.pack(side='bottom',fill=X)
bar.set(0)
loginFrame=CTkFrame(win,width=880,height=480)
optionFrame=CTkFrame(win,width=200,corner_radius=0)
textFrame=CTkFrame(win,height=150)
subjectFrame=CTkScrollableFrame(win)
studentInformationFrame=CTkScrollableFrame(win)
resultFrame=CTkScrollableFrame(win)
aboutFrame=CTkFrame(win)
questionFrame=CTkFrame(win)
topwin=None

loginGui()
# mainWindow(222706013)
win.mainloop()

