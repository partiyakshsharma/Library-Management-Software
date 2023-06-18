from tkinter import *
from tkinter import ttk
import tkinter as tk
from CTkMessagebox import CTkMessagebox
import customtkinter
import pymysql
from PIL import ImageTk, Image
import pymysql
customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue")  
def clear2():
    email.delete(0,END)
    paswordss.delete(0,END)

def log_us():
    if email.get()=='' or paswordss.get()=='':
            CTkMessagebox(title="Error", message="All Fields are Required", icon="warning")
    
    else:
        try:
            conn=pymysql.connect(host='localhost',user='root',password='kanc')      
            mycursor=conn.cursor()
        except:
            CTkMessagebox(title="Error", message="Connectivity issue Contact your Devloper or Try Again", icon="cancel") 
            return
           
        query='use userdata'
        mycursor.execute(query)
        query='select * from registrationdata where Email=%s and password=%s'
        mycursor.execute(query,(email.get(),paswordss.get()))
        ro=mycursor.fetchone()
        if ro==None:
            CTkMessagebox(title="Error", message="Invalid Username or password", icon="cancel") 
        else:
            CTkMessagebox(message="Thankyou for login.",
                  icon="check", option_1="Thanks") 
            clear2() 
            mainwin()
            
            


def clear():
    FULLName.delete(0,END)
    UserName.delete(0,END)
    Email.delete(0,END)
    Password.delete(0,END)
    ConfirmPassword.delete(0,END)


def connect_database():
    if FULLName.get()=='' or UserName.get()=='' or Email.get()=='' or Password.get()=='' or ConfirmPassword.get()=='':
        CTkMessagebox(title="Error", message="All Fields Are Required", icon="cancel")
    elif Password.get() != ConfirmPassword.get():
          CTkMessagebox(title="Error", message="Password Mismatch", icon="cancel")  
    else:
        try:
         conn=pymysql.connect(host='localhost',user='root',password='kanc')      
         mycursor=conn.cursor()
        except:
            CTkMessagebox(title="Error", message="Connectivity issue Contact your Devloper or Try Again", icon="cancel")       
            return
        try:    
            query='create database userdata'
            mycursor.execute(query)
            query='use userdata'
            mycursor.execute(query)   

            query='create table registrationdata(id int auto_increment primary key not null,FUllName varchar(50),UserName varchar(100),Email varchar(50),Password  varchar(20),ConfirmPassword varchar(20))'       
            mycursor.execute(query)
        except:
            query='use userdata'
            mycursor.execute(query)
            
            query='select * from registrationdata where UserName=%s'
            mycursor.execute(query,(UserName.get()))
            
            ro=mycursor.fetchone()
            if ro !=None:
                CTkMessagebox(title="Error", message="Username Already Exist", icon="warning")
            else:    
            
             query='insert into registrationdata(FUllName,UserName,Email,password,ConfirmPassword) values(%s,%s,%s,%s,%s)'    
             mycursor.execute(query,(FULLName.get(),UserName.get(),Email.get(),Password.get(),ConfirmPassword.get()))    
             conn.commit() 
             conn.close()
             CTkMessagebox(message="Registration is successfull.",
                  icon="check", option_1="Thanks")  
             clear()
             




app = customtkinter.CTk()
app.rowconfigure(0,weight=1)
app.columnconfigure(0,weight=1)
height=650
width=1240

x=(app.winfo_screenwidth()//2) -(width//2)

y=(app.winfo_screenwidth()//4) -(height//2)

app.geometry('{}x{}+{}+{}'.format(width, height, x, y))
app.title('testing')



sign_in=customtkinter.CTkFrame(app)
signup=customtkinter.CTkFrame(app)



for frames in (sign_in,signup):
    frames.grid(row=0,column=0,sticky='nsew')

def show_frame9(frame):
    frame.tkraise()
    
show_frame9(signup)



#..................................................................................................
#..................................................................................................
#................signup............................................................................

sign_in.configure(bg_color="blue")

Loginback = ImageTk.PhotoImage(file="ms.png")
bg_imageLogin =customtkinter.CTkLabel(
    sign_in,
    image=Loginback,
)
bg_imageLogin.place(x=10, y=0)

frame=customtkinter.CTkFrame(master=bg_imageLogin, width=560, height=460,corner_radius=15)
frame.place(x=450,y=100)
labe=customtkinter.CTkLabel(master=frame,text='Create new Account',font=('Century Gothic',27,'bold'))
labe.place(x=120,y=60)

FULLName=customtkinter.CTkEntry(master=frame,height=55,width=185,border_color='black',fg_color='white',text_color='black',placeholder_text_color="black",placeholder_text="Enter First Name",font=('Century Gothic',15,'bold'),corner_radius=30)
FULLName.place(x=110,y=120)


UserName=customtkinter.CTkEntry(master=frame,height=55,width=185,border_color='black',fg_color='white',text_color='black',placeholder_text_color="black",placeholder_text="Enter Last Name",font=('Century Gothic',15,'bold'),corner_radius=30)
UserName.place(x=300,y=120)


Email=customtkinter.CTkEntry(master=frame,height=55,width=370,border_color='black',fg_color='white',text_color='black',placeholder_text_color="black",placeholder_text="Enter E-mail Account",font=('Century Gothic',15,'bold'),corner_radius=30)
Email.place(x=110,y=185)


Password=customtkinter.CTkEntry(master=frame,height=55,width=185,border_color='black',fg_color='white',text_color='black',placeholder_text_color="black",placeholder_text="Password",font=('Century Gothic',15,'bold'),corner_radius=30)
Password.place(x=110,y=250)




ConfirmPassword=customtkinter.CTkEntry(master=frame,height=55,width=185,border_color='black',text_color='black',fg_color='white',placeholder_text_color="black",placeholder_text="Confirm Password",font=('Century Gothic',15,'bold'),corner_radius=30)
ConfirmPassword.place(x=300,y=250)

subbut=customtkinter.CTkButton(master=frame,text='Submit',height=55,width=185,border_color='black',fg_color='blue',font=('Century Gothic',15,'bold'),corner_radius=30,command=connect_database)
subbut.place(x=215,y=320)

labe=customtkinter.CTkLabel(master=frame,text='Already a member?',font=('Century Gothic',15,'bold'))
labe.place(x=120,y=380)


subbut=customtkinter.CTkButton(master=frame,text='Login',command=lambda:show_frame9(signup),width=15,fg_color='grey17',font=('Century Gothic',15,'bold'),text_color='blue')
subbut.place(x=390,y=380)

# app.resizable(False,False)
#............................................................
#............................................................\
#    login

signup.configure(bg_color="black")
Loginback = ImageTk.PhotoImage(file="js.png")
bg_imageLogin =customtkinter.CTkLabel(
    signup,
    image=Loginback,
)
bg_imageLogin.place(x=10, y=0)

frame=customtkinter.CTkFrame(master=bg_imageLogin, width=560, height=460, corner_radius=15,)
frame.place(x=450,y=100)

l2=customtkinter.CTkLabel(master=frame, text="Login to Continue",font=('Century Gothic',30,'bold'))
l2.place(x=120,y=60)


labe=customtkinter.CTkLabel(master=frame,text='Not a member?',font=('Century Gothic',15,'bold'))
labe.place(x=120,y=120)


subbut=customtkinter.CTkButton(master=frame,text='Sign Up',command=lambda:show_frame9(sign_in),width=15,fg_color='grey17',font=('Century Gothic',15,'bold'),text_color='blue',)
subbut.place(x=290,y=120)

email=customtkinter.CTkEntry(master=frame,height=55,width=325,border_color='black',fg_color='white',text_color='black',placeholder_text_color="black",placeholder_text="Email account",font=('Century Gothic',15,'bold'),corner_radius=30)
email.place(x=110,y=160)

def hide():
    openeye.config(file='eye.png')
    paswordss.configure(show="*")
    eyebut.config(command=show)
    
def show():
    openeye.config(file='eye2.png')
    paswordss.configure(show="") 
    eyebut.config(command=hide)    

paswordss=customtkinter.CTkEntry(master=frame,height=55,width=325,border_color='black',fg_color='white',text_color='black',placeholder_text_color="black",placeholder_text="Password",font=('Century Gothic',15,'bold'),corner_radius=30)
paswordss.place(x=110,y=230)

openeye=PhotoImage(file='eye2.png')
eyebut=Button(frame,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyebut.place(x=490,y=303)




subbut=customtkinter.CTkButton(master=frame,text='Forget Password',command=lambda: paswords(),width=15,fg_color='grey17',font=('Century Gothic',15,'bold'),text_color='blue')
subbut.place(x=120,y=290)



subbut=customtkinter.CTkButton(master=frame,text='Delete Account',width=15,command=lambda: deleteacc(),fg_color='grey17',font=('Century Gothic',15,'bold'),text_color='blue',)
subbut.place(x=300,y=290)






subbut=customtkinter.CTkButton(master=frame,text='Login',height=55,width=285,border_color='black',fg_color='blue',font=('Century Gothic',15,'bold'),corner_radius=30,command=log_us)
subbut.place(x=130,y=320)





def deleteacc():        
    def clear0(): 
        emailentry7.delete(0,END)
        passe7.delete(0,END)
        conpasse7.delete(0,END)
        
    def delete1():
            if emailentry7.get()=='' or passe7.get()==''or conpasse7.get()=='':
                 CTkMessagebox(title="Error", message="All fields are required", icon="cancel")
            else:
                try:
                   conn=pymysql.connect(host='localhost',user='root',password='kanc')      
                   mycursor=conn.cursor()
                except:
                  CTkMessagebox(title="Error", message="Connectivity issue Contact your Devloper or Try Again", icon="cancel")       
                  return 
              
                query='use userdata'
                mycursor.execute(query)
                query='delete from  registrationdata where email=%s and password=%s'
                mycursor.execute(query,(emailentry7.get(),passe7.get()))
                rom=mycursor.fetchone()
                conn.commit()
                conn.close()
                CTkMessagebox(message="Your account has been deleted.",
                  icon="check", option_1="Thanks") 
                clear0() 
                v.destroy()
                   
    v=Toplevel()    
    window_width = 550
    window_height = 550
    screen_width = v.winfo_screenwidth()
    screen_height = v.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    v.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
    v.resizable(False, False)
    img4=ImageTk.PhotoImage(Image.open('des.png'))
    l4=customtkinter.CTkLabel(master=v,image=img4)
    l4.pack()

    v.title('Library')
    v.configure(background='#272A37')
    
    la=customtkinter.CTkLabel(v,text='Delete your Account',font=("yu gothic ui semibold", 25))
    la.place(x=60,y=30)
    # ====== Email ====================
    emailentry7=customtkinter.CTkEntry(v, placeholder_text='Enter Your Email' ,font=("yu gothic ui semibold", 18),
                        width=200, height=50,corner_radius=20 )
    emailentry7.place(x=90, y=80,)
    
    
    passe7=customtkinter.CTkEntry(v, placeholder_text='Enter your Password' ,font=("yu gothic ui semibold", 18),
                        width=200, height=50,corner_radius=20 )
    passe7.place(x=90, y=150,)
    
    
    conpasse7 =customtkinter.CTkEntry(v, placeholder_text='Confirm your Password' ,font=("yu gothic ui semibold", 18),
                        width=200, height=50,corner_radius=20 )
    conpasse7.place(x=90, y=216,)

    delbutn=customtkinter.CTkButton(v,text='Delete',width=20,height=45,fg_color='blue',font=('Century Gothic',15,'bold'),text_color='white',corner_radius=20,command=delete1)
    delbutn.place(x=150,y=290)




def paswords():
    def change_password():
        if email_entry3.get()=='' or passe.get()==''or conpasse.get()=='':
                CTkMessagebox(title="Error", message="All Fields Are Required", icon="cancel")
        elif passe.get()==''!= conpasse.get()=='':
               CTkMessagebox(title="Error", message="Password and Confirm password doesn't Match", icon="warning")
        else:
            conn=pymysql.connect(host='localhost',user='root',password='kanc',database='userdata')      
            mycursor=conn.cursor()    
            query='select * from registrationdata where Email=%s'
            mycursor.execute(query,(email_entry3.get()))       
            row=mycursor.fetchone()
            if row==None:
                CTkMessagebox(title="Error", message="Invalid Email", icon="warning")
            else:
               query='update registrationdata set Password=%s , ConfirmPassword=%s where Email=%s'  
               mycursor.execute(query,(
               passe.get(),conpasse.get(),email_entry3.get())) 
               conn.commit()
               conn.close()
               CTkMessagebox(message="Password is Reset,please Login with new Password",
                icon="check", option_1="Thanks")  
               v.destroy()
            
            
    v=Toplevel()    
    window_width = 550
    window_height = 550
    screen_width = v.winfo_screenwidth()
    screen_height = v.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    v.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

    v.title('Forgot Password')
    v.configure(background='#272A37')
    v.resizable(False, False)

    la=customtkinter.CTkLabel(v,text='Forget Password',font=("yu gothic ui semibold", 25))
    la.place(x=40,y=30)
    # ====== Email ====================
    email_entry3 =customtkinter.CTkEntry(v, placeholder_text='Enter Your Email' ,font=("yu gothic ui semibold", 18),
                        width=200, height=50,corner_radius=20 )
    email_entry3.place(x=40, y=80,)
    
    passe =customtkinter.CTkEntry(v, placeholder_text='New Password' ,font=("yu gothic ui semibold", 18),
                        width=200, height=50,corner_radius=20 )
    passe.place(x=40, y=150,)
    
    
    conpasse =customtkinter.CTkEntry(v, placeholder_text='Confirm New Password' ,font=("yu gothic ui semibold", 18),
                        width=200, height=50,corner_radius=20 )
    conpasse.place(x=40, y=220,)

    subbutn=customtkinter.CTkButton(v,text='Update Password',width=15,height=45,fg_color='blue',font=('Century Gothic',15,'bold'),text_color='white',corner_radius=20,command=change_password)
    subbutn.place(x=50,y=290)



def mainwin():
            
            
    v=Toplevel()    
    window_width = 1280
    window_height = 720
    screen_width = v.winfo_screenwidth()
    screen_height = v.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    v.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
    img4=ImageTk.PhotoImage(Image.open('pattern.png'))
    l4=customtkinter.CTkLabel(master=v,image=img4)
    l4.pack()

    v.title('Library')
    v.configure(background='#272A37')
    # v.resizable(False, False)
    # la1=customtkinter.CTkLabel(v,font=('Century Gothic',60))
    # la1.place(relx=0.5, rely=0.5, )
    
    def homepage():
        def clear3():
            bookid.delete(0,END)
            stuname.delete(0,END)
            roll.delete(0,END)
            booktitle.delete(0,END)
            bookcourse.delete(0,END)
            bookiss.delete(0,END)
            gen.delete(0,END)
            due.delete(0,END)
        def isue():
            if bookid.get()=='' or stuname.get()==''or  roll.get()==''or booktitle.get()==''or bookcourse.get()==''or bookiss.get()=='' or gen.get()==''or due.get()=='':
                   CTkMessagebox(title="Error", message="All Fields Are Required", icon="cancel")
            else:
              try:
                   conn=pymysql.connect(host='localhost',user='root',password='kanc')      
                   mycursor=conn.cursor()
              except:
                  CTkMessagebox(title="Error", message="Connectivity issue Contact your Devloper or Try Again", icon="cancel")       
                  return
              try:    
                  query='create database userdata'
                  mycursor.execute(query)
                  query='use userdata'
                  mycursor.execute(query)   
                  query='create table bookis(bookid int primary key not null,studentname varchar(50) not null,Rollnumber int not null,Booktitle varchar(100) not null,course varchar(50) not null,IssueDate date not null,Gender varchar(20) not null,Duedate date)'      
                  mycursor.execute(query)
              except:
                  query='use userdata'
                  mycursor.execute(query)
                  query='select * from bookis where Rollnumber=%s'
                  mycursor.execute(query,(roll.get()))
                  ro=mycursor.fetchone()
                  if ro !=None:
                    CTkMessagebox(title="Error", message="Rollnumber Already Exist", icon="warning")
                  else:              
                    query='insert into bookis(bookid,studentname,Rollnumber,Booktitle,course,IssueDate,Gender,Duedate ) values(%s,%s,%s,%s,%s,%s,%s,%s)'    
                    mycursor.execute(query,(bookid.get(),stuname.get(),roll.get(),booktitle.get(),bookcourse.get(),bookiss.get(),gen.get(),due.get()))    
                    conn.commit() 
                    conn.close()
                    CTkMessagebox(message="book  isue  successfull.",
                  icon="check", option_1="Thanks")  
                    clear3()
        frame8=customtkinter.CTkFrame(master=frame3,width=1140,height=790,corner_radius=15)
        frame8.place(x=0,y=0)
       
        img44=ImageTk.PhotoImage(Image.open('ch2.png'))
        l44=customtkinter.CTkLabel(master=frame8,image=img44)
        l44.pack()
          
        bookisue=customtkinter.CTkLabel(master=frame8,text='Issue Books Here',font=('Century Gothic',30,'bold'),)
        bookisue.place(x=80,y=50)
       
        bookname=customtkinter.CTkLabel(master=frame8,text='Book ID',font=('Century Gothic',20,'bold'),)
        bookname.place(x=50,y=110)
        bookid=customtkinter.CTkEntry(master=frame8,placeholder_text='Enter the Id of the book',height=35)
        bookid.place(x=290,y=115)
         
        bookname=customtkinter.CTkLabel(master=frame8,text='Name',font=('Century Gothic',20,'bold'))
        bookname.place(x=50,y=160)
        stuname=customtkinter.CTkEntry(master=frame8,placeholder_text='Enter Your Name',height=35)
        stuname.place(x=290,y=165)
       
        bookname=customtkinter.CTkLabel(master=frame8,text='Roll Number',font=('Century Gothic',20,'bold'))
        bookname.place(x=50,y=210)
        roll=customtkinter.CTkEntry(master=frame8,placeholder_text='Enter your Roll Number',height=35)
        roll.place(x=290,y=210)
       
        bookname=customtkinter.CTkLabel(master=frame8,text='Book Title',font=('Century Gothic',20,'bold'))
        bookname.place(x=50,y=260)
        booktitle=customtkinter.CTkEntry(master=frame8,placeholder_text='Enter Title of the Book',height=35)
        booktitle.place(x=290,y=255)
       
        bookname=customtkinter.CTkLabel(master=frame8,text='Course',font=('Century Gothic',20,'bold'))
        bookname.place(x=50,y=310)
        bookcourse=customtkinter.CTkEntry(master=frame8,placeholder_text='Enter Course',height=35)
        bookcourse.place(x=290,y=300)
       
       
        bookname=customtkinter.CTkLabel(master=frame8,text='Issue date',font=('Century Gothic',20,'bold'))
        bookname.place(x=50,y=360)
        bookiss=customtkinter.CTkEntry(master=frame8,placeholder_text='YY-MM-DD',height=35)
        bookiss.place(x=290,y=350)
       
       
        bookname=customtkinter.CTkLabel(master=frame8,text='Gender',font=('Century Gothic',20,'bold'))
        bookname.place(x=50,y=410)
        gen=customtkinter.CTkEntry(master=frame8,placeholder_text='Enter Gender',height=35)
        gen.place(x=290,y=400)
       
       
       
        bookname=customtkinter.CTkLabel(master=frame8,text='Due date',font=('Century Gothic',20,'bold'))
        bookname.place(x=50,y=460)
        due=customtkinter.CTkEntry(master=frame8,placeholder_text='YY-MM-DD',height=35)
        due.place(x=290,y=450)
       
       
        button2 = customtkinter.CTkButton(master=frame8,width=190,height=40,text="Issue ",font=('Century Gothic',20,'bold'),corner_radius=6,command=isue)
        button2.place(x=120, y=500)
       
    def add():
       def clear5():
           bookid4.delete(0,END)
           bookttle.delete(0,END)
           auth.delete(0,END)
           edition.delete(0,END)
           price.delete(0,END) 
       def addbook():
           if bookid4.get()=='' or bookttle==''or auth.get()=='' or price.get()=='':
                 CTkMessagebox(title="Error", message="All Fields Are Required", icon="cancel")      
           else:
               try:
                   conn=pymysql.connect(host='localhost',user='root',password='kanc')      
                   mycursor=conn.cursor()
               except:
                  CTkMessagebox(title="Error", message="Connectivity issue Contact your Devloper or Try Again", icon="cancel")       
                  return
               try:
                query='use userdata'
                mycursor.execute(query)
                query='create table booklist(BookId int not null primary key,Booktitle varchar(100),Authorname varchar(100) not null,BookEdition varchar(100) not null,price int not null)'
                mycursor.execute(query)
               except:
                   query='use userdata'
                   mycursor.execute(query)
                   query='insert into booklist(BookId,Booktitle,Authorname,BookEdition,price) values(%s,%s,%s,%s,%s)' 
                   mycursor.execute(query,(bookid4.get(),bookttle.get(),auth.get(),edition.get(),price.get()))
                   conn.commit()
                   conn.close()
                   CTkMessagebox(message="Thankyou for adding Book.",
                  icon="check", option_1="Thanks")  
                   clear5()
 
                    
                       
                        
        
        
       fram=customtkinter.CTkFrame(master=frame3,width=1140,height=790,)
       fram.place(x=0,y=0)
        
       img444=ImageTk.PhotoImage(Image.open('sch.png'))
       l444=customtkinter.CTkLabel(master=fram,image=img444)
       l444.pack()
       
       
       bookname=customtkinter.CTkLabel(master=fram,text='Add Book Here',font=('Century Gothic',30,'bold'),)
       bookname.place(x=80,y=50)
       bookname=customtkinter.CTkLabel(master=fram,text='Book ID',font=('Century Gothic',20,'bold'),)
       bookname.place(x=50,y=110)
       bookid4=customtkinter.CTkEntry(master=fram,height=35)
       bookid4.place(x=290,y=115)
       
       
       bookname=customtkinter.CTkLabel(master=fram,text='Book Title',font=('Century Gothic',20,'bold'),)
       bookname.place(x=50,y=160)
       bookttle=customtkinter.CTkEntry(master=fram,placeholder_text='Enter the title of the book',height=35)
       bookttle.place(x=290,y=165)
       
       bookname=customtkinter.CTkLabel(master=fram,text='Author',font=('Century Gothic',20,'bold'))
       bookname.place(x=50,y=210)
       auth=customtkinter.CTkEntry(master=fram,placeholder_text='Enter Author name',height=35)
       auth.place(x=290,y=210)
       
       bookname=customtkinter.CTkLabel(master=fram,text='Edition',font=('Century Gothic',20,'bold'))
       bookname.place(x=50,y=260)
       edition=customtkinter.CTkEntry(master=fram,height=35)
       edition.place(x=290,y=255)
       
       bookname=customtkinter.CTkLabel(master=fram,text='Price',font=('Century Gothic',20,'bold'))
       bookname.place(x=50,y=300)
       price=customtkinter.CTkEntry(master=fram,placeholder_text='Enter price',height=35)
       price.place(x=290,y=300)
       button2 = customtkinter.CTkButton(master=fram,width=190,height=40,text="submit",font=('Century Gothic',20,'bold'),corner_radius=6,command=addbook)
       button2.place(x=120, y=360)
        
        
    def te():
       def clear4():
           bookid1.delete(0,END)
           roll1.delete(0,END)
           stuname1.delete(0,END)
           booktit.delete(0,END)
           course1.delete(0,END) 
       def delete1():
            if bookid1.get()=='' or roll1.get()=='':
                 CTkMessagebox(title="Error", message="Roll number and Bookid fields are required", icon="cancel")
            else:
                try:
                   conn=pymysql.connect(host='localhost',user='root',password='kanc')      
                   mycursor=conn.cursor()
                except:
                  CTkMessagebox(title="Error", message="Connectivity issue Contact your Devloper or Try Again", icon="cancel")       
                  return 
                query='use userdata'
                mycursor.execute(query)
                query='DELETE from bookis where bookid=%s and rollnumber=%s'
                mycursor.execute(query,(bookid1.get(),roll1.get()))
                conn.commit()
                conn.close()
                CTkMessagebox(message="Thanks for Returning Book",
                  icon="check", option_1="Thanks")
                clear4()
                
                
        
        
        
        
       fra=customtkinter.CTkFrame(master=frame3,width=1140,height=790)
       fra.place(x=0,y=0)
        
       img4444=ImageTk.PhotoImage(Image.open('ssfd.png'))
       l4444=customtkinter.CTkLabel(master=fra,image=img4444)
       l4444.pack()
       
       bookname=customtkinter.CTkLabel(master=fra,text='Book ID',font=('Century Gothic',20,'bold'),)
       bookname.place(x=580,y=110)
       bookid1=customtkinter.CTkEntry(master=fra,placeholder_text='Enter the title of the book',height=35)
       bookid1.place(x=790,y=115)
       
       bookname=customtkinter.CTkLabel(master=fra,text='Name',font=('Century Gothic',20,'bold'))
       bookname.place(x=580,y=160)
       stuname1=customtkinter.CTkEntry(master=fra,placeholder_text='Enter Your Name',height=35)
       stuname1.place(x=790,y=165)
       
       bookname=customtkinter.CTkLabel(master=fra,text='Roll Number',font=('Century Gothic',20,'bold'))
       bookname.place(x=580,y=210)
       roll1=customtkinter.CTkEntry(master=fra,placeholder_text='Enter your Roll Number',height=35)
       roll1.place(x=790,y=210)
       
       bookname=customtkinter.CTkLabel(master=fra,text='Book Title',font=('Century Gothic',20,'bold'))
       bookname.place(x=580,y=260)
       booktit=customtkinter.CTkEntry(master=fra,placeholder_text='Book Title',height=35)
       booktit.place(x=790,y=255)
       
       bookname=customtkinter.CTkLabel(master=fra,text='Course',font=('Century Gothic',20,'bold'))
       bookname.place(x=580,y=310)
       course1=customtkinter.CTkEntry(master=fra,placeholder_text='Enter Course',height=35)
       course1.place(x=790,y=300)
       
       button2 = customtkinter.CTkButton(master=fra,width=190,height=40,text="Return ",font=('Century Gothic',20,'bold'),command=delete1,corner_radius=6,)
       button2.place(x=670, y=380)
       
       def clear7():
           bookid6.delete(0,END)
           booktit2.delete(0,END)
       
       def deletebook():
            if bookid6.get()=='' or booktit2.get()=='':
                 CTkMessagebox(title="Error", message="All fields are required", icon="cancel")
            else:
                try:
                   conn=pymysql.connect(host='localhost',user='root',password='kanc')      
                   mycursor=conn.cursor()
                except:
                  CTkMessagebox(title="Error", message="Connectivity issue Contact your Devloper or Try Again", icon="cancel")       
                  return 
                query='use userdata'
                mycursor.execute(query)
                query='DELETE from booklist where BookId=%s and Booktitle=%s'
                mycursor.execute(query,(bookid6.get(),booktit2.get()))
                conn.commit()
                conn.close()
                CTkMessagebox(message="your Book has been deleted ",
                  icon="check", option_1="Thanks")
                clear7()

       #//Book deletion from database
       bookname=customtkinter.CTkLabel(master=fra,text='Book ID',font=('Century Gothic',20,'bold'),)
       bookname.place(x=580,y=470)
       bookid6=customtkinter.CTkEntry(master=fra,placeholder_text='Enter the ID of the book',height=35)
       bookid6.place(x=790,y=480)
       
       bookname=customtkinter.CTkLabel(master=fra,text='BookTitle',font=('Century Gothic',20,'bold'))
       bookname.place(x=580,y=510)
       booktit2=customtkinter.CTkEntry(master=fra,placeholder_text='Enter Book Title',height=35)
       booktit2.place(x=790,y=520)
       
       delbutton2 = customtkinter.CTkButton(master=fra,width=190,height=40,text="Delete Book",font=('Century Gothic',20,'bold'),corner_radius=6,command=deletebook)
       delbutton2.place(x=670, y=580)
        
        
    def aish():    
        frame1=customtkinter.CTkFrame(master=frame3,width=1140,height=790)
        frame1.place(x=0,y=0) 
        
        img4444=ImageTk.PhotoImage(Image.open('1.png'))
        l4444=customtkinter.CTkLabel(master=frame1,image=img4444)
        l4444.pack()     
        subbut=customtkinter.CTkButton(master=frame1,text='Show Data',height=55,width=185,border_color='black',fg_color='blue',font=('Century Gothic',20,'bold'),corner_radius=30,)
        subbut.place(x=390,y=60)
        tableframe=tk.Frame(frame1,)
        tableframe.place(x=50,y=170,height=760,width=650)
        yscroll=Scrollbar(tableframe,orient=VERTICAL)
        librarybooks=ttk.Treeview(tableframe,columns=("BookId","Book Title","Author","Edition","Price"),yscrollcommand=yscroll.set)
        
        yscroll.pack(side=RIGHT,fill=Y)
        yscroll.config(command=librarybooks.yview) 
        
        librarybooks.heading("BookId",text="Book id")
        librarybooks.heading("Book Title",text="Book Title")
        librarybooks.heading("Author",text="Author")
        librarybooks.heading("Edition",text="Edition")
        librarybooks.heading("Price",text="price")
        
        librarybooks['show']="headings"
        librarybooks.pack(fill='both',expand=1)
        
        librarybooks.column("BookId",width=100,anchor=tk.CENTER)
        librarybooks.column("Book Title",width=100,anchor=tk.CENTER)
        librarybooks.column("Author",width=100,anchor=tk.CENTER)    
        librarybooks.column("Edition",width=100,anchor=tk.CENTER)
        librarybooks.column("Price",width=100,anchor=tk.CENTER)
        
        conn=pymysql.connect(host='localhost',user='root',password='kanc')      
        mycursor=conn.cursor()
        mycursor.execute('use userdata')
        mycursor.execute('select * from booklist')
        i=0
        for ro in mycursor:
              librarybooks.insert('',i,text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4]))
              i=i+1
        
        
        
        dataframe=tk.Frame(frame1,)
        dataframe.place(x=730,y=170,height=760,width=650) 
        yscroll=Scrollbar(dataframe,orient=VERTICAL)
        studentdata=ttk.Treeview(dataframe,columns=("bookid","studentname","Rollnumber","Booktitle","course","IssueDate","Gender","Duedate"),yscrollcommand=yscroll.set)
        yscroll.pack(side=RIGHT,fill=Y)
        yscroll.config(command=studentdata.yview)
        
        studentdata.heading("bookid",text="Bookid")
        studentdata.heading("studentname",text="studentname")
        studentdata.heading("Rollnumber",text="Rollnumber")
        studentdata.heading("Booktitle",text="Booktitle")
        studentdata.heading("course",text="course")
        studentdata.heading("IssueDate",text="IssueDate")
        studentdata.heading("Gender",text="Gender")
        studentdata.heading("Duedate",text="Duedate")
        
        studentdata['show']="headings"
        studentdata.pack(fill='both',expand=1)
        
        studentdata.column("bookid",width=70,anchor=tk.CENTER)
        studentdata.column("studentname",width=70,anchor=tk.CENTER)    
        studentdata.column("Rollnumber",width=70,anchor=tk.CENTER)
        studentdata.column("Booktitle",width=70,anchor=tk.CENTER)
        studentdata.column("course",width=70,anchor=tk.CENTER)
        studentdata.column("IssueDate",width=70,anchor=tk.CENTER)
        studentdata.column("Gender",width=70,anchor=tk.CENTER)
        studentdata.column("Duedate",width=70,anchor=tk.CENTER)
        
        conn=pymysql.connect(host='localhost',user='root',password='kanc')      
        mycursor=conn.cursor()
        mycursor.execute('use userdata')
        mycursor.execute('select * from bookis')
        j=0
        for ro in mycursor:
              studentdata.insert('',i,text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7]))
              j=j+1
        
         
        
        
        
        
        
        
    def na():
        ais=customtkinter.CTkFrame(master=frame3,width=1140,height=790)
        img12=ImageTk.PhotoImage(Image.open('ss.png'))
        l12=customtkinter.CTkLabel(master=ais,image=img12)
        l12.pack()     
        ais.place(x=0,y=0)
    def ab2():
       frame8=customtkinter.CTkFrame(master=frame3,width=1140,height=790,)
       img122=ImageTk.PhotoImage(Image.open('About US.png'))
       l122=customtkinter.CTkLabel(master=frame8,image=img122)
       l122.pack()     
       frame8.place(x=0,y=0)
                                    

                         
    def delete_page():
      for frame in frame3.winfo_children():
          frame.destroy()    
    def indicate(page):
         delete_page()
         page()
         
         
         
    frame2=customtkinter.CTkFrame(v, width=320, height=800, corner_radius=15)
    frame2.place(x=10,y=20)
    
    
    button2 = customtkinter.CTkButton(master=frame2,width=190,height=40,text="Issue Book",font=('Century Gothic',20,'bold'),corner_radius=6,command=lambda:indicate(homepage))
    button2.place(x=60, y=110)
    
    button3 = customtkinter.CTkButton(master=frame2,width=190,height=40,text="Add Book",command=lambda:indicate(add),font=('Century Gothic',20,'bold'), corner_radius=6)
    button3.place(x=60, y=180)
    
    
    button3 = customtkinter.CTkButton(master=frame2,width=190,height=40,    text="Return Book",command=lambda:indicate(te),font=('Century Gothic',20,'bold'), corner_radius=6)
    button3.place(x=60, y=250)
    
    
    button4 = customtkinter.CTkButton(master=frame2,width=190,height=40,    text="view All data",command=lambda:indicate(aish),font=('Century Gothic',20,'bold'), corner_radius=6)
    button4.place(x=60, y=320)
    
    button5 = customtkinter.CTkButton(master=frame2,width=190,height=40,    text="Contact Us",command=lambda:indicate(na),font=('Century Gothic',20,'bold'), corner_radius=6)
    button5.place(x=60, y=390)
    
    button6 = customtkinter.CTkButton(master=frame2,width=190,height=40, command=lambda:indicate(ab2),   text="About Us",font=('Century Gothic',20,'bold'),corner_radius=6)
    button6.place(x=60, y=460)
    
    def ask_question():
    # get yes/no answers
     msg = CTkMessagebox(title="Exit?", message="Do you want to close the program?",
                        icon="question", option_1="Cancel", option_2="No", option_3="Yes")
     response = msg.get()
    
     if response=="Yes":
        v.destroy()       
     else:
        print("Click 'Yes' to exit!")
        
    
    button6 = customtkinter.CTkButton(master=frame2,width=190,height=40,text="Log Out",command=ask_question,font=('Century Gothic',20,'bold'), corner_radius=6)
    button6.place(x=60, y=730)
    
    frame3=customtkinter.CTkFrame(v, width=1150, height=800, corner_radius=15)
    frame3.place(x=360,y=20)
        
    img1222=ImageTk.PhotoImage(Image.open('main.png'))
    l1222=customtkinter.CTkLabel(master=frame3,image=img1222)
    l1222.pack()  


app.mainloop()    