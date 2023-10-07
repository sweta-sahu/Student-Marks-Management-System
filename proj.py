from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from PIL import Image, ImageDraw, ImageTk, ImageFont
import io
import base64
from winsound import *

encoded = base64.b64encode(open("edu.png", "rb").read())
BASE64_BACKGROUND = encoded

root = Tk()
root.title("S. M. S.")
root.geometry("1200x750+150+20")
root.iconbitmap('de.ico')

image_file = io.BytesIO(base64.b64decode(BASE64_BACKGROUND))
image = Image.open(image_file)
photoimage = ImageTk.PhotoImage(image)
Label(root, image=photoimage).place(x=0, y=0)

# _____________________________________ add window _______________________________________________


def f1():
    Beep(2000, 20)
    root.withdraw()
    addst.deiconify()


def f2():
    Beep(2000, 20)
    addst.withdraw()
    root.deiconify()

# _______________________________________________ view window _______________________________________


def f3():
    Beep(2000, 20)
    root.withdraw()
    viewst.deiconify()

    stData.delete(1.0, END)
    import cx_Oracle

    con = None
    cursor = None

    try:
        con = cx_Oracle.connect("system/23swetasahu")
        cursor = con.cursor()
        sql = "select rno, name, marks from students_marks"
        cursor.execute(sql)
        data = cursor.fetchall()
        data.sort()
        msg = ""
        for d in data:
            msg = msg + " r: " + str(d[0]) + " n: " + \
                d[1] + " m: " + str(d[2]) + "\n"
        stData.insert(INSERT, msg)
    except cx_Oracle.DatabaseError as e:
        messagebox.showerror("Some Issue", e)
    finally:
        if cursor is not None:
            cursor.close()
        if con is not None:
            con.close()


def f4():
    Beep(2000, 20)
    viewst.withdraw()
    root.deiconify()

# ______________________________________________ Update window ___________________________________________


def f5():
    Beep(2000, 20)
    root.withdraw()
    updatest.deiconify()


def f6():
    Beep(2000, 20)
    updatest.withdraw()
    root.deiconify()

# ______________________________________________ delete window ___________________________________________


def f7():
    Beep(2000, 20)
    root.withdraw()
    deletest.deiconify()


def f8():
    Beep(2000, 20)
    deletest.withdraw()
    root.deiconify()

# ______________________________________________ Add entry _____________________________________________


def f9():
    Beep(2000, 20)
    import cx_Oracle

    con = None
    cursor = None

    try:
        con = cx_Oracle.connect("system/23swetasahu@localhost")
        rno = int(entRno.get())
        name = entName.get()
        marks = int(entMarks.get())
        if rno < 0:
            messagebox.showerror("Error", "Roll no. should be a +ve inetger")
            entRno.delete(0, END)
            entRno.focus()
        elif len(name) < 2 or not (name.isalpha()):
            messagebox.showerror("Error", "min len 2 or should be a character")
            entName.delete(0, END)
            entName.focus()
        elif marks > 100 or marks < 0:
            messagebox.showerror("Error", "Enter marks between 0-100")
            entMarks.delete(0, END)
            entMarks.focus()
        else:
            cursor = con.cursor()
            sql = "insert into students_marks values('%d', '%s', '%d')"
            args = (rno, name, marks)
            cursor.execute(sql % args)
            con.commit()
            msg = str(cursor.rowcount) + " record inserted "
            messagebox.showinfo("Info Inserted", msg)
            entRno.delete(0, END)
            entName.delete(0, END)
            entMarks.delete(0, END)
            entRno.focus()
    except cx_Oracle.DatabaseError as e:
        messagebox.showerror("Some Issue", e)
        con.rollback()
        entRno.delete(0, END)
        entRno.focus()
    except ValueError:
        messagebox.showerror(
            "Error", "Enter only integer in place of roll no. and marks")
        entRno.delete(0, END)
        entMarks.delete(0, END)
        entRno.focus()
    finally:
        if cursor is not None:
            cursor.close()
        if con is not None:
            con.close()
# _______________________________________________ update entry __________________________________________


def f10():
    Beep(2000, 20)
    import cx_Oracle

    con = None
    cursor = None

    try:
        con = cx_Oracle.connect("system/23swetasahu")
        rno = int(entRno1.get())
        name = entName1.get()
        marks = int(entMarks1.get())
        cursor = con.cursor()
        sql = "select * from students_marks"
        cursor.execute(sql)
        data = cursor.fetchall()
        rn = []
        for d in data:
            rn.append(d[0])
        c = None
        for r in rn:
            if r == rno:
                c = 'yes'
        if c == None:
            messagebox.showerror("Alert!", "Record does not exsist")
        if rno < 0:
            messagebox.showerror("Error", "Roll no. should be a +ve inetger")
            entRno1.delete(0, END)
            entRno1.focus()
        elif len(name) < 2 or not (name.isalpha()):
            messagebox.showerror("Error", "min len 2 or should be a character")
            entName.delete(0, END)
            entName.focus()
        elif marks > 100 or marks < 0:
            messagebox.showerror("Error", "Enter marks between 0-100")
            entMarks1.delete(0, END)
            entMarks1.focus()
        else:
            cursor = con.cursor()
            sql = "update students_marks set name='%s', marks='%d' where rno='%d'"
            args = (name, marks, rno)
            cursor.execute(sql % args)
            con.commit()
            msg = str(cursor.rowcount) + " record updated "
            messagebox.showinfo("Info Updated", msg)
            entRno1.delete(0, END)
            entName1.delete(0, END)
            entMarks1.delete(0, END)
            entRno1.focus()
    except cx_Oracle.DatabaseError as e:
        messagebox.showerror("Some Issue", e)
        entRno1.delete(0, END)
        entRno1.focus()
    except ValueError:
        messagebox.showerror(
            "Error", "Enter only integer in place of roll no. and marks")
        entRno1.delete(0, END)
        entMarks1.delete(0, END)
        entRno1.focus()
    finally:
        if cursor is not None:
            cursor.close()
        if con is not None:
            con.close()

# _____________________________________________ delete entry __________________________________________


def f11():
    Beep(2000, 20)
    import cx_Oracle

    con = None
    cursor = None

    try:
        con = cx_Oracle.connect("system/23swetasahu")
        rno = int(entRno2.get())
        cursor = con.cursor()
        sql = "select * from students_marks"
        cursor.execute(sql)
        data = cursor.fetchall()
        rn = []
        for d in data:
            rn.append(d[0])
        c = None
        for r in rn:
            if r == rno:
                c = 'yes'
        if c == None:
            messagebox.showerror("Alert!", "Record does not exsist")
        if rno < 0:
            messagebox.showerror("Error", "Roll no. should be a +ve inetger")
        else:
            cursor = con.cursor()
            sql = "delete from students_marks where rno='%d'"
            args = (rno)
            cursor.execute(sql % args)
            con.commit()
            msg = str(cursor.rowcount) + " record deleted "
            messagebox.showinfo("Info Deleted", msg)
        entRno2.delete(0, END)
        entRno2.focus()
    except cx_Oracle.DatabaseError as e:
        messagebox.showerror("Some Issue", e)
        entRno2.delete(0, END)
        entRno2.focus()
    except ValueError:
        messagebox.showerror(
            "Error", "Enter only integer in place of roll no.")
        entRno2.delete(0, END)
        entRno2.focus()
    finally:
        if cursor is not None:
            cursor.close()
        if con is not None:
            con.close()

# ______________________________________________ graph ____________________________________________


def f12():
    Beep(2000, 20)
    import matplotlib.pyplot as plt
    import numpy as np
    import cx_Oracle

    con = None
    cursor = None

    try:
        con = cx_Oracle.connect("system/23swetasahu")
        cursor = con.cursor()
        sql = "select rno, name, marks from students_marks"
        cursor.execute(sql)
        data = cursor.fetchall()
        name_st = []
        marks_st = []
        for d in data:
            name_st.append(d[1])
            marks_st.append(d[2])

        plt.bar(name_st, marks_st, width=0.50, color='g')

        plt.xticks(name_st, fontsize=10, rotation=30)
        plt.title('Students Result')
        plt.xlabel('Names')
        plt.ylabel('Marks')

        plt.grid()
        plt.show()
    except cx_Oracle.DatabaseError as e:
        messagebox.showerror("Some Issue", e)
    finally:
        if cursor is not None:
            cursor.close()
        if con is not None:
            con.close()

# ______________________________________________ QOTD _________________________________________________


def f13():
    import bs4
    import requests
    try:
        res = requests.get(
            "https://www.brainyquote.com/quotes_of_the_day.html")
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        quote = soup.find('img', {"class": "p-qotd"})
        if res.status_code == 200:
            text = quote['alt']
        else:
            text = "Have a nice day"
    except requests.exceptions.ConnectionError:
        messagebox.showerror("No Network", "No Internet Connection")
    return text

# ___________________________________________ TEMP ____________________________________________________


def f14():
    import socket
    import requests

    try:
        city = 'Mumbai'
        socket.create_connection(("www.google.com", 80))
        a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
        a2 = "&q=" + city
        a3 = "&appid=c6e315d09197cec231495138183954bd"
        api_address = a1 + a2 + a3
        res1 = requests.get(api_address)
        data = res1.json()
        main = data['main']
        temp = main['temp']
    except OSError as e:
        messagebox.showerror("Some Issue", e)
    except requests.exceptions.ConnectionError:
        messagebox.showerror("No Network", "No Connection to Internet")
    return str(temp)+"\u00B0"+"C"

# _____________________________________________ Main Window ____________________________________________


img = ImageTk.PhotoImage(Image.open("degrees1.png"))
panel = Label(root, image=img)
lblTitle = Label(root, text=" XYZ Acadmey ", font=(
    "Comic Sans MS", 40, "bold"), width=30, bg='yellow')
btnAdd = Button(root, text="Add", font=(
    "Georgia", 18, "bold"), width=10, command=f1)
btnView = Button(root, text="View", font=(
    "Georgia", 18, "bold"), width=10, command=f3)
btnUpdate = Button(root, text="Update", font=(
    "Georgia", 18, "bold"), width=10, command=f5)
btnDelete = Button(root, text="Delete", font=(
    "Georgia", 18, "bold"), width=10, command=f7)
btnGraph = Button(root, text="Graph", font=(
    "Georgia", 18, "bold"), width=10, command=f12)
lblQotd = Label(root, text="QOTd: ", font=(
    "Gabriola", 22, "bold"), width=7, bg='light steel blue')
entQotd = Entry(root, bd=5, font=("Gabriola", 20, "bold"),
                width=70, state="readonly")
lblTemp = Label(root, text="Temp: ", font=(
    "Gabriola", 22, "bold"), width=7, bg='light steel blue')
entTemp = Entry(root, bd=5, font=("Gabriola", 20, "bold"),
                width=70, state="readonly")

entQotd.config(state=NORMAL)
entQotd.delete(0, END)
entQotd.insert(0, f13())
entQotd.config(state="readonly")

entTemp.config(state=NORMAL)
entTemp.delete(0, END)
entTemp.insert(0, f14())
entTemp.config(state="readonly")

panel.grid(pady=10, row=0, column=0)
lblTitle.grid(pady=10, row=0, column=1)
btnAdd.grid(pady=10, row=1, column=1)
btnView.grid(pady=10, row=2, column=1)
btnUpdate.grid(pady=10, row=3, column=1)
btnDelete.grid(pady=10, row=4, column=1)
btnGraph.grid(pady=10, row=5, column=1)
lblQotd.grid(pady=10, row=6, column=0)
entQotd.grid(pady=10, row=6, column=1)
lblTemp.grid(pady=10, row=7, column=0)
entTemp.grid(pady=10, row=7, column=1)

# _______________________________________________ Add Window ____________________________________________

encoded1 = base64.b64encode(open("page.png", "rb").read())
BASE64_BACKGROUND = encoded1
addst = Toplevel(root)
addst.title("Add S")
addst.iconbitmap('de.ico')
image_file1 = io.BytesIO(base64.b64decode(BASE64_BACKGROUND))
image1 = Image.open(image_file1)
width, height = image1.size
addst.resizable(width=False, height=False)
addst.geometry("%sx%s" % (width, height))
photoimage1 = ImageTk.PhotoImage(image1)
Label(addst, image=photoimage1).place(x=0, y=0)
addst.withdraw()

lblAddTitle = Label(addst, text=" Add Record ", font=(
    "Comic Sans MS", 22, "bold"), width=20, bg='salmon2')
lblRno = Label(addst, text="Enter Roll no.", font=(
    "Georgia", 18, "bold"), bg='medium orchid')
entRno = Entry(addst, bd=5, font=("Georgia", 18, "bold"))
lblName = Label(addst, text="Enter Name", font=(
    "Georgia", 18, "bold"), bg='medium orchid')
entName = Entry(addst, bd=5, font=("Georgia", 18, "bold"))
lblMarks = Label(addst, text="Enter Marks", font=(
    "Georgia", 18, "bold"), bg='medium orchid')
entMarks = Entry(addst, bd=5, font=("Georgia", 18, "bold"))
btnAddSave = Button(addst, text="Save", font=(
    "Georgia", 18, "bold"), width=10, command=f9)
btnAddBack = Button(addst, text="Back", font=(
    "Georgia", 18, "bold"), width=10, command=f2)

lblAddTitle.pack(pady=35)
lblRno.pack(pady=5)
entRno.pack(pady=5)
lblName.pack(pady=5)
entName.pack(pady=5)
lblMarks.pack(pady=5)
entMarks.pack(pady=5)
btnAddSave.pack(pady=20)
btnAddBack.pack(pady=10)

# _______________________________________________ View Window _______________________________________________

viewst = Toplevel(root)
viewst.title("View S")
viewst.iconbitmap('de.ico')
viewst.resizable(width=False, height=False)
viewst.geometry("%sx%s" % (width, height))
Label(viewst, image=photoimage1).place(x=0, y=0)
viewst.withdraw()

lblViewTitle = Label(viewst, text=" View Record ", font=(
    "Comic Sans MS", 22, "bold"), width=20, bg='salmon2')
stData = scrolledtext.ScrolledText(viewst, width=40, height=25)
btnViewBack = Button(viewst, text="Back", font=(
    "Georgia", 18, "bold"), width=10, command=f4)

lblViewTitle.pack(pady=35)
stData.pack(pady=10)
btnViewBack.pack(pady=15)

# _____________________________________________ Update Window ______________________________________________

updatest = Toplevel(root)
updatest.title("Update S")
updatest.iconbitmap('de.ico')
updatest.resizable(width=False, height=False)
updatest.geometry("%sx%s" % (width, height))
Label(updatest, image=photoimage1).place(x=0, y=0)
updatest.withdraw()

lblUpdateTitle = Label(updatest, text=" Update Record ", font=(
    "Comic Sans MS", 22, "bold"), width=20, bg='salmon2')
lblRno1 = Label(updatest, text="Enter Roll no.", font=(
    "Georgia", 18, "bold"), bg='CadetBlue3')
entRno1 = Entry(updatest, bd=5, font=("Georgia", 18, "bold"))
lblName1 = Label(updatest, text="Enter Name", font=(
    "Georgia", 18, "bold"), bg='CadetBlue3')
entName1 = Entry(updatest, bd=5, font=("Georgia", 18, "bold"))
lblMarks1 = Label(updatest, text="Enter Marks", font=(
    "Georgia", 18, "bold"), bg='CadetBlue3')
entMarks1 = Entry(updatest, bd=5, font=("Georgia", 18, "bold"))
btnUpdateSave = Button(updatest, text="Save", font=(
    "Georgia", 18, "bold"), width=10, command=f10)
btnUpdateBack = Button(updatest, text="Back", font=(
    "Georgia", 18, "bold"), width=10, command=f6)

lblUpdateTitle.pack(pady=35)
lblRno1.pack(pady=5)
entRno1.pack(pady=5)
lblName1.pack(pady=5)
entName1.pack(pady=5)
lblMarks1.pack(pady=5)
entMarks1.pack(pady=5)
btnUpdateSave.pack(pady=20)
btnUpdateBack.pack(pady=10)

# ____________________________________________ Delete Window ___________________________________________

deletest = Toplevel(root)
deletest.title("Delete S")
deletest.iconbitmap('de.ico')
deletest.resizable(width=False, height=False)
deletest.geometry("%sx%s" % (width, height))
Label(deletest, image=photoimage1).place(x=0, y=0)
deletest.withdraw()

lblDeleteTitle = Label(deletest, text=" Delete Record ", font=(
    "Comic Sans MS", 22, "bold"), width=20, bg='salmon2')
lblRno2 = Label(deletest, text="Enter Roll no.",
                font=("Georgia", 18, "bold"), bg='orchid3')
entRno2 = Entry(deletest, bd=5, font=("Georgia", 18, "bold"))
btnDeleteSave = Button(deletest, text="Save", font=(
    "Georgia", 18, "bold"), width=10, command=f11)
btnDeleteBack = Button(deletest, text="Back", font=(
    "Georgia", 18, "bold"), width=10, command=f8)

lblDeleteTitle.pack(pady=35)
lblRno2.pack(pady=5)
entRno2.pack(pady=5)
btnDeleteSave.pack(pady=20)
btnDeleteBack.pack(pady=10)


root.mainloop()
