import requests
import tkinter
import sqlite3

try:
    connection = sqlite3.connect("./app.sqlite")
    print("Connection to SQLite DB successful")
except sqlite3.Error as e:
    print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")


create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT NOT NULL,
  password TEXT NOT NULL
);
"""
execute_query(connection, create_users_table)

def createHabit():
    global usernameEntry
    global passwordEntry
    url=f"https://pixe.la/v1/users/{usernameEntry.get()}/graphs"
    if habitDrop.get()=="Reading":
        unit="Page"
    elif habitDrop.get()=="Cycling":
        unit="Km"
    else:
        unit=""
    params={
        "id":"212829",
        "name":habitDrop.get(),
        "unit":unit,
        "type":"float",
        "color":colorDrop.get()
    }
    headers={
        "X-USER-TOKEN":passwordEntry.get()
    }
    response=requests.post(url=url,json=params,headers=headers)
    print(response)

def setup():
    global habitLabel
    global habitDrop
    global habitOptions
    global habitClicked
    global habitOptions
    global colorClicked
    global colorDrop
    global habitButton
    lbl1.config(text="Enter habit details")
    lbl1.grid(row=0,column=1,columnspan=2)
    habitLabel=tkinter.Label(window,text="Select a habit")
    habitOptions=["Reading","Cycling", "Art"]
    habitClicked=tkinter.StringVar()
    habitClicked.set("Reading")
    habitDrop=tkinter.OptionMenu(window,habitClicked,*habitOptions)
    habitLabel.grid(row=1,column=1)
    habitDrop.grid(row=1,column=1)
    colorOptions=["shibafu","momiji","sora","ichou","ajisai","kuro"]
    colorClicked=tkinter.StringVar()
    colorClicked.set("shibafu")
    colorLabel=tkinter.Label(window,text="Select a color")
    colorDrop=tkinter.OptionMenu(window,colorClicked,*colorOptions)
    habitButton=tkinter.Button(
        window,
        text="Create Habit",
        width=20,
        height=3,
        font=("Montserrat", 15),
        command=createHabit
        )
    colorLabel.grid(row=2,column=1)
    colorDrop.grid(row=2,column=1)
    habitButton.grid(row=3,column=1,columnspan=2)



def afterSignup():
    global usernameEntry
    global passwordEntry
    global usernameLabel
    global passwordLabel
    global signupButton
    lbl1.config(text="Signup Successful")
    usernameEntry.destroy()
    usernameLabel.destroy()
    passwordEntry.destroy()
    passwordLabel.destroy()
    signupButton.destroy()
    setup()

def afterLogin():
    lbl1.config(text="Login Successful")
    usernameEntry.destroy()
    usernameLabel.destroy()
    passwordEntry.destroy()
    passwordLabel.destroy()
    loginButton.destroy()

def Login():
    global usernameEntry
    global passwordEntry
    find_user = f"""
    SELECT users.username,users.password FROM users WHERE users.username='{usernameEntry.get()}'
    """
    status = execute_read_query(connection, find_user)
    if status[0][0]==usernameEntry.get() and status[0][1]==passwordEntry.get():
        afterLogin()


def Signup():
    global usernameEntry
    global passwordEntry
    url = "https://pixe.la/v1/users"
    params = {
        "token": passwordEntry.get(),
        "username": usernameEntry.get(),
        "agreeTermsOfService": "yes",
        "notminor": "yes",
    }

    response = requests.post(url, json=params)
    print(response.status_code)
    if response.status_code == 200:
        create_users = f"""
        INSERT INTO 
            users (username, password)
        VALUES 
            ('{params["username"]}','{params["token"]}')
            """
        execute_query(connection, create_users)
    afterSignup()


def onClickLogin():
    global usernameEntry
    global passwordEntry
    global usernameLabel
    global passwordLabel
    global loginButton
    btn1.destroy()
    btn2.destroy()
    lbl1.config(text="Login")
    lbl1.grid(columnspan=2)
    usernameLabel = tkinter.Label(window, text="Username :", font=("Montserrat", 15))
    usernameEntry = tkinter.Entry(window, font=("Montserrat", 15))
    usernameLabel.grid(row=1, column=1, pady=20)
    usernameEntry.grid(row=1, column=2, pady=20)
    passwordLabel = tkinter.Label(window, text="Password :", font=("Montserrat", 15))
    passwordEntry = tkinter.Entry(window, font=("Montserrat", 15))
    passwordLabel.grid(row=2, column=1, pady=20)
    passwordEntry.grid(row=2, column=2, pady=20)
    loginButton = tkinter.Button(
        window,
        text="Login",
        width=20,
        height=3,
        font=("Montserrat", 15),
        command=Login,
    )
    loginButton.grid(row=3, column=2, columnspan=2, pady=20)


def onClickSignup():
    global usernameEntry
    global passwordEntry
    global passwordLabel
    global usernameLabel
    global usernameEntry
    global signupButton
    btn1.destroy()
    btn2.destroy()
    lbl1.config(text="Signup")
    lbl1.grid(columnspan=2)
    usernameLabel = tkinter.Label(window, text="Username :", font=("Montserrat", 15))
    usernameEntry = tkinter.Entry(window, font=("Montserrat", 15))
    usernameLabel.grid(row=1, column=1, pady=20)
    usernameEntry.grid(row=1, column=2, pady=20)
    passwordLabel = tkinter.Label(window, text="Password :", font=("Montserrat", 15))
    passwordEntry = tkinter.Entry(window, font=("Montserrat", 15))
    passwordLabel.grid(row=2, column=1, pady=20)
    passwordEntry.grid(row=2, column=2, pady=20)
    signupButton = tkinter.Button(
        window,
        text="Signup",
        width=20,
        height=3,
        font=("Montserrat", 15),
        command=Signup,
    )
    signupButton.grid(row=3, column=1, columnspan=2, pady=20)

window = tkinter.Tk()
window.title("Habit Tracker")

# Create label
lbl1 = tkinter.Label(
    window,
    text="Welcome to Habit Tracker",
    width=50,
    height=10,
    font=("Helvetica", 30),
)
lbl1.grid(row=0, column=1)

# Create buttons

btn1 = tkinter.Button(
    window,
    text="Login",
    width=20,
    height=3,
    font=("Montserrat", 15),
    command=onClickLogin,
)
btn2 = tkinter.Button(
    window,
    text="Signup",
    width=20,
    height=3,
    font=("Montserrat", 15),
    command=onClickSignup,
)
btn1.grid(row=1, column=1, pady=20)
btn2.grid(row=2, column=1, pady=20)


window.mainloop()
