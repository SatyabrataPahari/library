#main file
import tkinter as tk
import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="1718",database="library_management")
mycursor=mycon.cursor()
#Checking for connection 
if mycon.is_connected:
    print("SUCCESS")

#Registering books into the database table    
def register_book():
    bname = bookname_entry.get()
    aname = author_entry.get()
    bId = bookid_entry.get()
    query1="INSERT INTO books_3(bookname,author,bookcode) VALUES (%s,%s,%s)"
    bvalues=(bname,aname,bId)
    try:
      mycursor.execute(query1,bvalues)
      mycon.commit()
      tk.Label(screen4, text = "Successfully Added", fg = "green" ,font = ("georgia", 13)).pack()
    except:
      tk.messagebox.showinfo("Error inserting","Cannot add data to Database")
      
    bookname_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)
    bookid_entry.delete(0,tk.END)
 
    

#Deleting data from the database table
def delete_book(): 
    bId_d = bookid_entry_d.get()
    query2="DELETE FROM books_3 WHERE bookcode='"+bId_d+"'"
    try:
      mycursor.execute(query2)
      mycon.commit()
      tk.Label(screen5, text = "Successfully Deleted", fg = "green" ,font = ("georgia", 13)).pack()
    except:
      tk.messagebox.showinfo("Error deleting","Cannot delete data from Database")
      
    bookname_entry_d.delete(0, tk.END)
    bookid_entry_d.delete(0,tk.END)
 
    

#Adding issue date to the database table
def issue_book():
    issue1 = issue_entry_i.get()
    bId_i = bookid_entry_i.get()
    query3= "UPDATE books_3 SET issue='"+issue1+"' WHERE bookcode='"+bId_i+"'"
    try:
      mycursor.execute(query3)
      mycon.commit()
      tk.messagebox.showinfo("Issued","Issued Successfully")
    except:
      tk.messagebox.showinfo("Error issuing","Error issuing")
      
    issue_entry_i.delete(0, tk.END)
    bookid_entry_i.delete(0,tk.END)
    bookname_entry_i.delete(0,tk.END)
 
    
    screen6.destroy()


#Adding return date to the database table
def return_book():
    return1 = return_entry_r.get()
    bId_r = bookid_entry_r.get()
    query4= "UPDATE books_3 SET returned= '"+return1+"' WHERE bookcode='"+bId_r+"'"
    try:
      mycursor.execute(query4)
      mycon.commit()
    except:
      tk.messagebox.showinfo("Error returning","Error returning")
      
    return_entry_r.delete(0, tk.END)
    bookid_entry_r.delete(0,tk.END)
    bookname_entry_r.delete(0,tk.END)
 
    tk.messagebox.showinfo("Returned","Returned Successfully")
    screen7.destroy()


#Code for displaying books
def view_books():
    global screen8
    screen8 = tk.Toplevel(screenm)
    screen8.geometry("600x500")
    screen8.title("Issue")
    labelFrame = tk.Frame(screen8,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
        
    headingFrame1 = tk.Frame(screen8,bg="#333945",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingFrame2 = tk.Frame(headingFrame1,bg="#EAF0F1")
    headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)
        
    headingLabel = tk.Label(headingFrame2, text="VIEW BOOKs", fg='black')
    headingLabel.place(relx=0.25,rely=0.15, relwidth=0.5, relheight=0.5)   
    
    y = 0.25
    
    tk.Label(labelFrame, text="%-30s%-30s%-10s%-20s%-20s"%('Title','Author','BID','Issue','Return'),bg='black',fg='white').place(relx=0.07,rely=0.1)
    tk.Label(labelFrame, text="----------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)
    getBooks = ("select * from books_3")
    try:
        mycursor.execute(getBooks)
        data3=mycursor.fetchall()
        mycon.commit()
        for i in data3:
            tk.Label(labelFrame, text="%-30s%-30s%-10s%-20s%-20s"%(i[0],i[1],i[2],i[3],i[4]),bg='black',fg='white').place(relx=0.07,rely=y)
            y += 0.1
    except:
        tk.messagebox.showinfo("Bad Format","Can't fetch files from database")

# Code for returning books
def return_books():
    global screen7
    global book_id_r
    global book_name_r
    global return_r
    global return_entry_r
    global bookname_entry_r
    global bookid_entry_r
    screen7 = tk.Toplevel(screenm)
    screen7.geometry("400x400")
    screen7.title("Issue")
    tk.Label(screen7,text = "Global", bg = "lightblue", width = "300", height = "2", font = ("Gerogia", 13)).pack()
    tk.Label(screen7,text = "Tasks", bg = "lightblue", width = "300", height = "2", font = ("Georgia", 13)).pack()
    tk.Label(screen7,text = "").pack()
    book_name_r=tk.StringVar()
    book_id_r=tk.StringVar()
    return_r=tk.StringVar()
    tk.Label(screen7, text = "Book Name").pack()
    bookname_entry_r = tk.Entry(screen7, textvariable = book_name_r)
    bookname_entry_r.pack()
    tk.Label(screen7, text = "Book ID").pack()
    bookid_entry_r =  tk.Entry(screen7, textvariable = book_id_r)
    bookid_entry_r.pack()
    tk.Label(screen7, text = "Return Date yyyy-mm-dd").pack()
    return_entry_r =  tk.Entry(screen7, textvariable = return_r)
    return_entry_r.pack()
    tk.Label(screen7, text = "").pack()
    tk.Button(screen7, text = "Return", width = 10, height = 1,command = return_book).pack()
        
#Code for issuing books    
def issue_books():
    global screen6
    global book_id_i
    global book_name_i
    global issue_i
    global issue_entry_i
    global bookname_entry_i
    global bookid_entry_i
    screen6 = tk.Toplevel(screenm)
    screen6.geometry("400x400")
    screen6.title("Issue")
    tk.Label(screen6,text = "Global", bg = "lightblue", width = "300", height = "2", font = ("Gerogia", 13)).pack()
    tk.Label(screen6,text = "Tasks", bg = "lightblue", width = "300", height = "2", font = ("Georgia", 13)).pack()
    tk.Label(screen6,text = "").pack()
    book_name_i=tk.StringVar()
    book_id_i=tk.StringVar()
    issue_i=tk.StringVar()
    tk.Label(screen6, text = "Book Name").pack()
    bookname_entry_i = tk.Entry(screen6, textvariable = book_name_i)
    bookname_entry_i.pack()
    tk.Label(screen6, text = "Book ID").pack()
    bookid_entry_i =  tk.Entry(screen6, textvariable = book_id_i)
    bookid_entry_i.pack()
    tk.Label(screen6, text = "Issue Date yyyy-mm-dd").pack()
    issue_entry_i =  tk.Entry(screen6, textvariable = issue_i)
    issue_entry_i.pack()
    tk.Label(screen6, text = "").pack()
    tk.Button(screen6, text = "Issue", width = 10, height = 1,command = issue_book).pack()
    
    
#Code for deleting books    
def delete_books():
    global screen5
    global book_id_d
    global book_name_d
    global bookname_entry_d
    global bookid_entry_d
    screen5 = tk.Toplevel(screenm)
    screen5.geometry("400x400")
    screen5.title("Deletion")
    tk.Label(screen5,text = "Global", bg = "lightblue", width = "300", height = "2", font = ("Gerogia", 13)).pack()
    tk.Label(screen5,text = "Tasks", bg = "lightblue", width = "300", height = "2", font = ("Georgia", 13)).pack()
    tk.Label(screen5,text = "").pack()
    book_name_d=tk.StringVar()
    book_id_d=tk.StringVar()
    tk.Label(screen5, text = "Book Name").pack()
    bookname_entry_d = tk.Entry(screen5, textvariable = book_name_d)
    bookname_entry_d.pack()
    tk.Label(screen5, text = "Book ID").pack()
    bookid_entry_d =  tk.Entry(screen5, textvariable = book_id_d)
    bookid_entry_d.pack()
    tk.Label(screen5, text = "").pack()
    tk.Button(screen5, text = "Delete", width = 10, height = 1,command = delete_book).pack()
    
# Code for adding books        
def add_books():
    global screen4
    global book_id
    global author_name
    global book_name
    global bookname_entry
    global author_entry
    global bookid_entry
    screen4 = tk.Toplevel(screenm)
    screen4.geometry("400x400")
    screen4.title("Utilities")
    tk.Label(screen4,text = "Global", bg = "lightblue", width = "300", height = "2", font = ("Gerogia", 13)).pack()
    tk.Label(screen4,text = "Tasks", bg = "lightblue", width = "300", height = "2", font = ("Georgia", 13)).pack()
    tk.Label(screen4,text = "").pack()
    book_name=tk.StringVar()
    author_name=tk.StringVar()
    book_id=tk.StringVar()
    tk.Label(screen4, text = "Book Name").pack()
    bookname_entry = tk.Entry(screen4, textvariable = book_name)
    bookname_entry.pack()
    tk.Label(screen4, text = "Author").pack()
    author_entry = tk.Entry(screen4, textvariable = author_name)
    author_entry.pack()
    tk.Label(screen4, text = "Book ID").pack()
    bookid_entry =  tk.Entry(screen4, textvariable = book_id)
    bookid_entry.pack()
    tk.Label(screen4, text = "").pack()
    tk.Button(screen4, text = "Register", width = 10, height = 1,command = register_book).pack()
mycursor.execute("SELECT * FROM books_3")

myresult1 = mycursor.fetchall()
for x in myresult1:
    print (x)    
    
#Page to provide task options
def options():
    global screen3
    screen3 = tk.Toplevel(screenm)
    screen3.geometry("500x750")
    screen3.title("Utilities")
    tk.Label(screen3,text = "Global", bg = "lightblue", width = "300", height = "2", font = ("Gerogia", 13)).pack()
    tk.Label(screen3,text = "Tasks", bg = "lightblue", width = "300", height = "2", font = ("Georgia", 13)).pack()
    tk.Label(screen3,text = "").pack()
    tk.Button(screen3,text = "Add Books", height = "2", width = "30", command=add_books).pack()
    tk.Label(screen3,text = "").pack()
    tk.Button(screen3,text = "Delete Books",height = "2", width = "30", command = delete_books).pack()
    tk.Label(screen3,text = "").pack()
    tk.Button(screen3,text = "Issue Books", height = "2", width = "30", command=issue_books).pack()
    tk.Label(screen3,text = "").pack()
    tk.Button(screen3,text = "Return Books",height = "2", width = "30", command = return_books).pack()
    tk.Label(screen3,text = "").pack()
    tk.Button(screen3,text = "View Books",height = "2", width = "30", command = view_books).pack()

#Saving credentials in the database table        
def register_user():
 
  username_info = username.get()
  password_info = password.get()
  empid_info = empid.get()
 
  user_entry_code="INSERT INTO users_1 VALUES (%s,%s,%s)"
  user_entry=(username_info,password_info,empid_info)
  try:
      mycursor.execute(user_entry_code,user_entry)
      mycon.commit()
      tk.Label(screen1, text = "Registration Sucess", fg = "green" ,font = ("georgia", 13)).pack()
  except:
      tk.messagebox.showinfo("Error inserting","Cannot add data to Database")
 
  username_entry.delete(0, tk.END)
  password_entry.delete(0, tk.END)
  empid_entry.delete(0,tk.END) 
  

mycursor.execute("SELECT * FROM users_1")

myresult = mycursor.fetchall()
for x in myresult:
    print (x)

# Verifying whether username and password exist and match    
def verifylogin():
    name = username_verify.get()
    password1 = password_verify.get()
    sqluser = "select user from users_1 where passwd='"+password1+"'"
    sqlpasswd = "select passwd from users_1 where passwd='"+password1+"'"

    try:
        mycursor.execute(sqluser)
        for i in mycursor:
            getuser = i[0]
        mycursor.execute(sqlpasswd)
        for i in mycursor:
            getpasswd = i[0]
        if(getuser == name and getpasswd == password1):
            tk.messagebox.showinfo("SUCCESS","You have successfully logged in")
            screen2.destroy()
            options()
        else:
            tk.messagebox.showerror("Failure","Can't log in, check your credentials")
    except:
        tk.messagebox.showinfo("FAILURE","Invalid credentials")

# Registration function    
def register():
  global screen1
  screen1 = tk.Toplevel(screenm)
  screen1.title("Register")
  screen1.geometry("300x250")
   
  global username
  global password
  global empid
  global username_entry
  global password_entry
  global empid_entry
  username = tk.StringVar()
  password = tk.StringVar()
  empid= tk.StringVar()
 
  tk.Label(screen1, text = "Please enter details below").pack()
  tk.Label(screen1, text = "").pack()
  tk.Label(screen1, text = "Username * ").pack()
  username_entry = tk.Entry(screen1, textvariable = username)
  username_entry.pack()
  tk.Label(screen1, text = "Password * ").pack()
  password_entry =  tk.Entry(screen1, textvariable = password)
  password_entry.pack()
  tk.Label(screen1, text = "Employee ID * ").pack()
  empid_entry =  tk.Entry(screen1, textvariable = empid)
  empid_entry.pack()
  tk.Label(screen1, text = "").pack()
  tk.Button(screen1, text = "Register", width = 10, height = 1,command = register_user).pack()
  screen1.destroy()

#Login Function
def login():
  global screen2
  screen2 = tk.Toplevel(screenm)
  screen2.title("Login")
  screen2.geometry("300x250")
  tk.Label(screen2, text = "Please enter login details").pack()
  tk.Label(screen2, text = "").pack()
 
  global username_verify
  global password_verify
   
  username_verify = tk.StringVar()
  password_verify = tk.StringVar()
 
  global username_entry1
  global password_entry1
   
  tk.Label(screen2, text = "Username  ").pack()
  username_entry1 = tk.Entry(screen2, textvariable = username_verify)
  username_entry1.pack()
  tk.Label(screen2, text = "").pack()
  tk.Label(screen2, text = "Password  ").pack()
  password_entry1 = tk.Entry(screen2, textvariable = password_verify)
  password_entry1.pack()
  tk.Label(screen2, text = "").pack()
  tk.Button(screen2, text = "Login", width = 10, height = 1,command=verifylogin).pack()

# First screen that appears 
def main_screen():
  global screenm
  screenm = tk.Tk()
  screenm.geometry("500x750")
  screenm.title("Title Screen")
  tk.Label(text = "Global", bg = "lightblue", width = "300", height = "2", font = ("Gerogia", 13)).pack()
  tk.Label(text = "Library management", bg = "lightblue", width = "300", height = "2", font = ("Georgia", 13)).pack()
  tk.Label(text = "").pack()
  tk.Button(text = "Login", height = "2", width = "30", command=login).pack()
  tk.Label(text = "").pack()
  tk.Button(text = "Register",height = "2", width = "30", command = register).pack()
 
  screenm.mainloop()
 
main_screen()

