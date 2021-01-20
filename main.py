from tkinter import *
import mysql.connector
from tkinter import messagebox
from datetime import *

mydb = mysql.connector.connect(user ="lifechoices", password = "@Lifechoices1234",
                               host = "localhost", database = "lifechoicesonline",
                               auth_plugin = "mysql_native_password")

mycursor = mydb.cursor()


window = Tk()
window.title("Lifechoices Online")
window.geometry("450x450")
window.configure(background = "light green")

# DATETIME
now = datetime.now()
add_date = now.strftime("%d %B %Y")
today_date = now.strftime("%H: %M %p")
datetime = add_date+"\n"+today_date

lbd = Label(window, text = "", bg = "light green")
lbd['text'] = datetime
lbd.place(x = 180, y = 300)

# WINDOW LABELS
headlb = Label(window, text = "LifeChoices Online", font=("bold", 20))
headlb.configure(background = "green")
headlb.place(x = 100, y = 10)

userlb = Label(window, text = "Username")
userlb.place(x = 100, y = 100)

passlb = Label(window, text = "Password")
passlb.place(x = 100, y = 150)

pass_ent = Entry(window, show = "*")
pass_ent.place(x = 200, y = 150)

employ_ent = Entry(window)
employ_ent.place(x = 200, y = 100)



def login():
    user_name = employ_ent.get()
    pass_word = pass_ent.get()
    sql = "select * from logins where username = %s and password = %s"
    mycursor.execute(sql, [(user_name), (pass_word)])
    results = mycursor.fetchall()
    if results:
        for i in results:
            logged()
            break
    else:
        failed()

def logged():
    window2 = Tk()
    window2.title("Cellphone Number")
    window2.geometry("300x100")
    window2.configure(background = "light green")

    mobilb = Label(window2, text = "Cellnumber")
    mobilb.place(x = 10, y = 10)
    mobi_ent = Entry(window2)
    mobi_ent.place(x = 100, y = 10)

    messagebox.showinfo("Login Successful", "Enjoy You Day")
    def logout():
        window2.destroy()

    logout_btn = Button(window2, text = "Logout", command = logout)
    logout_btn.place(x = 20, y = 20)


def failed():
    messagebox.showerror("Login Unsuccessful","incorrect username or password.")

# LOGIN BUTTON
log_btn = Button(window,text = "Login", width = 10, command = login)
log_btn.place(x = 50, y = 250)


# REGISTER INTERFACE
def register():
    print("you hit return")

    window3 = Tk()
    window3.title("Register")
    window3.geometry("450x450")
    window3.configure(background = "light green")

    mydb = mysql.connector.connect(user ="lifechoices", password = "@Lifechoices1234",
                                   host = "localhost", database = "lifechoicesonline",
                                   auth_plugin = "mysql_native_password")

    mycursor = mydb.cursor()

    # WINDOW3 LABELS REGISTRATION
    full_lb = Label(window3, text = "Fullname")
    full_lb.place(x = 100, y = 50)
    user_name = Label(window3, text = "Username")
    user_name.place(x = 100, y = 100)
    user_pass = Label(window3, text = "Password")
    user_pass.place(x = 100, y = 150)

    # WINDOW3 ENTRIES REGISTRATION
    full_ent = Entry(window3)
    full_ent.place(x = 200, y = 50)
    user_ent = Entry(window3)
    user_ent.place(x = 200, y = 100)
    pass_user = Entry(window3, show = "*")
    pass_user.place(x = 200, y = 150)

    # SIGN UP FUNCTION FOR INSERT BUTTON

    def sign_up():
        fname = full_ent.get()
        nameuser = user_ent.get()
        passname = pass_user.get()


        try:
            secsql = "insert into users(full_name,username,password) values(%s, %s, %s)"
            mycursor.execute(secsql,[(fname), (nameuser),(passname)])
            mydb.commit()
            messagebox.showinfo("successful", "You Register")
        except ValueError:
            print("Couldn't sign up")


    insert = Button(window3, text = "Sign up", command = sign_up, width = 25)
    insert.configure(background = "light blue")
    insert.place(x = 100, y = 250)

    # EXIT FUNCTION AND BUTTON
    def quit(): #Will make the function go back to the main screen
        window3.destroy()

    exit_btn = Button(window3, text = "Quit", command = quit, width = 25)
    exit_btn.configure(background = "red")
    exit_btn.place(x = 100,y = 300)


keyspressed = 0
def admin():
    mydb = mysql.connector.connect(user ="lifechoices", password = "@Lifechoices1234",
                               host = "localhost", database = "lifechoicesonline",
                               auth_plugin = "mysql_native_password")

    mycursor = mydb.cursor()


    window.withdraw()
    global keyspressed
    admin_gui = Tk()
    admin_gui.title("Admin Login")
    admin_gui.geometry("550x500")
    admin_gui.configure(background = "light green")

    # ADMIN LABEL
    idlb = Label(admin_gui, text = "Id")
    idlb.place(x = 100, y = 10)
    full_lb = Label(admin_gui, text = "Fullname")
    full_lb.place(x = 100, y = 50)
    user_name = Label(admin_gui, text = "Username")
    user_name.place(x = 100, y = 100)
    user_pass = Label(admin_gui, text = "Password")
    user_pass.place(x = 100, y = 150)

    # ADMIN_GUI ENTRIES REGISTRATION
    id_ent = Entry(admin_gui)
    id_ent.place(x = 200, y = 10)
    full_ent = Entry(admin_gui)
    full_ent.place(x = 200, y = 50)
    user_ent = Entry(admin_gui)
    user_ent.place(x = 200, y = 100)
    pass_user = Entry(admin_gui, show = "*")
    pass_user.place(x = 200, y = 150)

    loginlb = Label(admin_gui, text = "")
    loginlb.place(x = 10, y = 10)

    def add():
        id_no = id_ent.get()
        login_ent = full_ent.get()
        nameuser = user_ent.get()
        passname = pass_user.get()


        try:
            insert4logins = "insert into logins(loginId,full_name, username,password) values(%s, %s, %s, %s)"
            mycursor.execute(insert4logins,[(id_no),(login_ent), (nameuser),(passname)])
            mydb.commit()
        except ValueError:
            print("Couldn't sign up")

        finally:
            print("THe data might've gone through or not")


    # ADD BUTTON
    add_btn = Button(admin_gui, text = "Add Record", command = add)
    add_btn.place(x = 10, y = 300)

    def remove():
        nameuser = user_ent.get()
        delete = "delete from logins where username = %s"
        mycursor.execute(delete,[(nameuser)])
        mydb.commit()




    # REMOVE BUTTON
    remove_data = Button(admin_gui, text = "Delete Record",command = remove)
    remove_data.place(x = 120, y = 300)

    def check():

        secsql = mycursor.execute("select * from logins")
        for i in mycursor:
            print(i)
            logdata = str(i)
            logdata = re.sub(',',':',logdata)
            loginlb['text'] += "People logged in" + "\n" + logdata + "\n"

    # Check Button
    check_data = Button(admin_gui, text = "Check Record", command = check)
    check_data.place(x = 250, y = 300)

    def grant():
        pass

    # GRANT PRIVILAGES BUTTON
    grant_btn = Button(admin_gui, text = "Grant Privilages")
    grant_btn.place(x = 380, y = 300)




window.bind("<Control-a>", lambda x: admin())
label = Label(window)
label.place(x=0,y=0)

# REGISTER BUTTON CONNECT TO def register
sign_btn = Button(window, text = "Register" ,width = 10, command = register)
sign_btn.place(x = 300, y = 250)



window.mainloop()
