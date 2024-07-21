import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import PhotoImage
import mysql.connector
import  string


admin_option = ['Add item', 'Delete item', 'edit info', 'check report','Exit']
user_option = ['check menu', 'make order', 'view history', 'Exit']


# ENTERING ITEM DATA INTO DATABASE


def enter():

    connection = mysql.connector.connect(host='localhost', user='root', database='venderDB')
    cursor = connection.cursor()

    # cursor.execute("CREATE DATABASE venderDB")

    # dbs = cursor.execute("create table Products(name varchar(20) not null,id int(20) not null primary key, price float not null, quantity int not null)")

    sql = "insert into Products(id,name,price,quantity) values(%s,%s,%s,%s)"

    val = [(itemid_entry.get(), itemname_entry .get(), itemprice_entry.get(), itemquantity_entry.get())]

    cursor.executemany(sql, val)
    connection.commit()


# ADMIN PANEL SETUPS
def admin_choices():
    def enter():
        connection = mysql.connector.connect(host='localhost', user='root', database='venderDB')
        cursor = connection.cursor()
        # cursor.execute("CREATE DATABASE venderDB")

        # dbs = cursor.execute("create table Products(name varchar(20) not null,id int(20) not null primary key, price float not null, quantity int not null)")

        sql = "insert into Products(id,name,price,quantity) values(%s,%s,%s,%s)"

        val = [(itemid_entry.get(), itemname_entry.get(), itemprice_entry.get(), itemquantity_entry.get())]

        cursor.executemany(sql, val)
        connection.commit()

    # ENTERING ITEM FRAME PART
    if x.get() == 0:

        global addframeborder

        addframeborder = Frame(admin_window, width=430, height=350, bg='red')
        addframeborder.place(x=300, y=100)
        addframe = Frame(addframeborder, width=430, height=350, bg='white')
        addframe.pack(padx=10, pady=10)

        # LABELS FOR ENTERING ITEMS

        itemid_label = Label(addframeborder, text="Item ID:", font=('arial', 13), bg="white")
        itemid_label.place(x=20, y=50)

        itemid_label = Label(addframeborder, text="Name:", font=('arial', 13), bg="white")
        itemid_label.place(x=20, y=100)

        itemid_label = Label(addframeborder, text="Price:", font=('arial', 13), bg="white")
        itemid_label.place(x=20, y=150)

        itemid_label = Label(addframeborder, text="Quantity:", font=('arial', 13), bg="white")
        itemid_label.place(x=20, y=200)

        # ENTRY FOR ENTERING ITEMS
        itemid_entry = Entry(addframeborder, width=20, font=('arial', 13), bd=2)
        itemid_entry.place(x=100, y=50)

        itemname_entry = Entry(addframeborder, width=20, font=('arial', 13), bd=2)
        itemname_entry.place(x=100, y=100)

        itemprice_entry = Entry(addframeborder, width=20, font=('arial', 13), bd=2)
        itemprice_entry.place(x=100, y=150)

        itemquantity_entry = Entry(addframeborder, width=20, font=('arial', 13), bd=2)
        itemquantity_entry.place(x=100, y=200)

        enterbutton = Button(addframeborder, text='Add', font=("bold", 15), bg='blue', command=enter)
        enterbutton.place(x=150, y=250)

        exitbutton = Button(addframeborder, text='Exit', font=("bold", 15), bg='red', command=addframeborder.destroy)
        exitbutton.place(x=250, y=250)


# DELETING ITEM FROM THE DATABASE SECTION
    elif x.get() == 1:

       # addframeborder.destroy()
        global deleteframeborder

        connection = mysql.connector.connect(host='localhost', user='root', database='venderDB')
        cursor = connection.cursor()

        cursor.execute('select id,name,price,quantity from Products order by id')
        result = cursor.fetchall()

        # FRAME FOR THE CHECKING REPORT IN THE DELETE SECTION IN THE ADIMIN WINDOW

        reportframeborder = Frame(admin_window, width=200, height=300, bg='red')
        reportframeborder.place(x=300, y=100)
        reportframe = Frame(reportframeborder, width=200, height=300, bg='white')
        reportframe.pack(padx=10, pady=10)

        mytree = ttk.Treeview(reportframe)
        mytree['columns'] = ('id', 'name', 'price', 'quantity')

        mytree.column("#0", width=10, minwidth=2)
        mytree.column("id", anchor=CENTER, width=100)
        mytree.column("name", anchor=W, width=100)
        mytree.column("price", anchor=CENTER, width=100)
        mytree.column("quantity", anchor=CENTER, width=100)

        # headings

        mytree.heading("#0", text="", anchor=W)
        mytree.heading("id", text="id", anchor=CENTER)
        mytree.heading('name', text="Name", anchor=W)
        mytree.heading("price", text="Price", anchor=CENTER)
        mytree.heading("quantity", text="Quantity", anchor=CENTER)

        count = 0

        for row in result:  # GOING THROUGH THE DATABASE AND DISPLAYING EVERYTHING
            mytree.insert(parent='', index='end', iid=count, text='', values=(row[0], row[1], row[2], row[3]))

            count += 1

        mytree.pack()

        deleteframeborder = Frame(admin_window, width=416, height=100, bg='red')
        deleteframeborder.place(x=300, y=350)

        deleteframe = Frame(deleteframeborder, width=416, height=100, bg='white')
        deleteframe.pack(pady=10, padx=10)

        def delete():
            delete_id = deleteitem_entry.get()
            print(delete_id)
            cursor.execute(f"delete from Products where id={delete_id}")
            connection.commit()

        # cursor.execute("delete from Employee where id=127")
        # cursor.execute("delete from Products where id=deleteite.entry.get()")

        # DELETING LABEL AND ENTRY
        Label(deleteframe, text="Enter item id to delete", font=("bold", 15), bg='white').place(y=5, x=80)

        deleteitem_label = Label(deleteframe, text='ID:', font=("bold", 13), bg="white")
        deleteitem_label.place(y=40, x=10)
        deleteitem_entry = Entry(deleteframe, width=25, bd=2, font=('arial', 13))
        deleteitem_entry.place(y=40, x=60)

        deletebutton = Button(deleteframe, text="Delete", bg='red', height=1, width=6, command=delete)
        deletebutton.place(y=38, x=308)

        def framedestroy():
            deleteframeborder.destroy()
            reportframeborder.destroy()

        exitbutton = Button(deleteframe, text="exit", bg='red', height=1, width=6, command=framedestroy)
        exitbutton.place(y=38, x=350)

# ITEM EDITING WINDOW SECTION
    elif x.get() == 2:

        def enter():

            id_to_edit = editentry.get()


            connection = mysql.connector.connect(host='localhost', user='root', database='venderDB')
            cursor = connection.cursor()

            cursor.execute('select id,name,price,quantity from Products order by id')
            result = cursor.fetchall()

            datalist=[]

            for row in result:
                data=row[0]
                datalist.append(data)


            if int(id_to_edit) in datalist:

                def edit():
                    id_to_edit1= int(id_to_edit)
                    print(id_to_edit1)

                    connection = mysql.connector.connect(host='localhost', user='root', database='venderDB')
                    cursor = connection.cursor()

                    # cursor.execute('select id,name,price,quantity from Products order by id')

                    update_query = "UPDATE Products SET name = %s, price = %s , quantity= %s WHERE id = %s"

                    # Executing the update query
                    cursor.execute(update_query, (newname_entry.get(), newprice_entry.get(), newquantity_entry.get(), id_to_edit1))

                    connection.commit()

                Label(editframe, text="Enter new item information", bg='white', font=("bold", 16)).place(x=70, y=90)

                Label(editframe, text='New name:', font=("bold", 13), bg="white").place(x=10, y=140)
                newname_entry = Entry(editframe, width=20, font=('arial', 13), bd=2)
                newname_entry.place(x=110, y=140)

                Label(editframe, text='New price:', font=("bold", 13), bg="white").place(x=10, y=180)
                newprice_entry = Entry(editframe, width=20, font=('arial', 13), bd=2)
                newprice_entry.place(x=110, y=180)

                Label(editframe, text='New quantity:', font=("bold", 13), bg="white").place(x=10, y=220)
                newquantity_entry = Entry(editframe, width=20, font=('arial', 13), bd=2)
                newquantity_entry.place(x=110, y=220)
                # CLEAR FUNCTION

                def clear():
                    newquantity_entry.delete(0, END)
                    newprice_entry.delete(0, END)
                    newname_entry.delete(0, END)

                Button(editframe, text="Edit", bg="blue", command=edit).place(x=130, y=250)
                Button(editframe, text="clear", bg="green", command=clear).place(x=160, y=250)
                Button(editframe, text="Exit", bg="red", command=editframeborder.destroy).place(x=190, y=250)

                print("exist")
            else:
                messagebox.showerror('error', f'{id_to_edit} does not exist in database')





        editframeborder = Frame(admin_window, width=400, height=360, bg='red')
        editframeborder.place(x=300, y=100)
        editframe = Frame(editframeborder, width=400, height=360, bg='white')
        editframe.pack(padx=10, pady=10)

        Label(editframe, text="Enter item id to edit", bg='white', font=("bold", 16)).place(x=100, y=8)

        Label(editframe, text='ID:', bg='white', font=("bold", 15)).place(x=10, y=45)

        editentry = Entry(editframe, width=20, font=("arial", 15), bd=2)
        editentry.place(x=50, y=45)

        Button(editframe, text="Enter", bg='red', command=enter).place(x=280, y=45)
        Button(editframe, text="Exit", bg="red", command=editframeborder.destroy).place(x=310, y=45)


# THE CHECK INFORMATION SECTION
    elif x.get() == 3:

        # addframeborder.destroy()
        # deleteframeborder.destroy()

        connection = mysql.connector.connect(host='localhost', user='root', database='venderDB')
        cursor = connection.cursor()

        cursor.execute('select id,name,price,quantity from Products order by id')
        result = cursor.fetchall()
        print(result)

        # FRAME FOR THE CHECKING REPORT SECTION IN THE ADIMIN WINDOW

        reportframeborder = Frame(admin_window, width=300, height=400, bg='red')
        reportframeborder.place(x=300, y=100)
        reportframe = Frame(reportframeborder, width=300, height=400, bg='white')
        reportframe.pack(padx=10, pady=10)
        Button(reportframeborder, text='Exit', bg='blue', width=6, command=reportframeborder.destroy).place(x=10,y=208)

        # VIEW TABLE IN THE ADMIN WINDOW
        mytree = ttk.Treeview(reportframe)
        mytree['columns'] = ('id', 'name', 'price', 'quantity')

        mytree.column("#0", width=10, minwidth=2)
        mytree.column("id", anchor=CENTER, width=100)
        mytree.column("name", anchor=W, width=100)
        mytree.column("price", anchor=CENTER, width=100)
        mytree.column("quantity", anchor=CENTER, width=100)

        # headings

        mytree.heading("#0", text="", anchor=W)
        mytree.heading("id", text="id", anchor=CENTER)
        mytree.heading('name', text="Name", anchor=W)
        mytree.heading("price", text="Price", anchor=CENTER)
        mytree.heading("quantity", text="Quantity", anchor=CENTER)

        count = 0

        for row in result:  # GOING THROUGH THE DATABASE AND DISPLAYING EVERYTHING
            mytree.insert(parent='', index='end', iid=count, text='', values=(row[0], row[1], row[2], row[3]))

            count += 1

        mytree.pack()

# ADMIN WINDOW EXIT
    elif x.get() == 4:
        admin_window.destroy()


# USER MENU

def user_selection():
    # FRAME FOR THE CHECKING MENU  IN THE USER WINDOW
    if xu.get() == 0:
        #history_frame_border.destroy()
        global menuframeborder


        connection = mysql.connector.connect(host='localhost', user='root', database='venderDB')
        cursor = connection.cursor()

        cursor.execute('select id,name,price,quantity from Products order by id')
        result = cursor.fetchall()

        # FRAME FOR THE CHECKING MENU  IN THE USER WINDOW

        menuframeborder = Frame(user_window, width=400, height=400, bg='red')
        menuframeborder.place(x=280, y=80)
        menuframe = Frame(menuframeborder, width=400, height=400, bg='white')
        menuframe.pack(padx=10, pady=10)
        menuframe1 = Frame(menuframeborder, width=461, height=50, bg='sky blue')
        menuframe1.place(x=10, y=325)
        Button(menuframe1, text='EXIT', bg='red', font=('bold', 13), width=8, command=menuframeborder.destroy).place(x=150, y=10)

        # VIEW MENU TABLE IN THE USER WINDOW
        mytree = ttk.Treeview(menuframe, height=17)
        mytree['columns'] = ('id', 'name', 'price')

        mytree.column("#0", width=10, minwidth=2)
        mytree.column("id", anchor=CENTER, width=150)
        mytree.column("name", anchor=W, width=150)
        mytree.column("price", anchor=CENTER, width=150)

        # headings

        mytree.heading("#0", text="", anchor=W)
        mytree.heading("id", text="id", anchor=CENTER)
        mytree.heading('name', text="Name", anchor=W)
        mytree.heading("price", text="Price", anchor=CENTER)

        count = 0

        for row in result:  # GOING THROUGH THE DATABASE AND DISPLAYING EVERYTHING
            mytree.insert(parent='', index='end', iid=count, text='', values=(row[0], row[1], row[2]))

            count += 1
        mytree.pack()


        # FRAME FOR MAKING ORDER
        # FRAME FOR THE CHECKING MENU  IN THE USER WINDOW
    elif xu.get() == 1:

        connection = mysql.connector.connect(host='localhost', user='root', database='venderDB')
        cursor = connection.cursor()

        cursor.execute('select id,name,price,quantity from Products order by id')
        result = cursor.fetchall()

        # FRAME FOR THE CHECKING MENU  IN THE USER WINDOW

        menuframeborder = Frame(user_window, width=150, height=250, bg='red')
        menuframeborder.place(x=270, y=70)
        menuframe = Frame(menuframeborder, width=150, height=250, bg='white')
        menuframe.pack(padx=10, pady=10)
        menuframe2 = Frame(menuframeborder, width=251, height=50, bg='sky blue')
        menuframe2.place(x=10, y=326)
        def destroy():
            menuframeborder.destroy()
            costframe.destroy()
            costframe1border.destroy()
            #costframe1.destroy()
            orderframeborder.destroy()
            costframe1border.destroy()


        Button(menuframe2, text='EXIT', bg='red', font=('bold', 14), command=destroy).place(x=30, y=10)

        # VIEW MENU TABLE IN THE USER WINDOW PLACING ORDER SECTION

        mytree = ttk.Treeview(menuframe, selectmode=tkinter.EXTENDED, height=17)
        mytree['columns'] = ('id', 'name', 'price')

        mytree.column("#0", width=10, minwidth=2)
        mytree.column("id", anchor=CENTER, width=80)
        mytree.column("name", anchor=W, width=80)
        mytree.column("price", anchor=CENTER, width=80)

        # headings

        mytree.heading("#0", text="", anchor=W)
        mytree.heading("id", text="id", anchor=CENTER)
        mytree.heading('name', text="Name", anchor=W)
        mytree.heading("price", text="Price", anchor=CENTER)

        count = 0

        for row in result:  # GOING THROUGH THE DATABASE AND DISPLAYING EVERYTHING
            mytree.insert(parent='', index='end', iid=count, text='', values=(row[0], row[1], row[2]))

            count += 1

        total = 0

        my_list = []
        item_list = []



        def on_item_click():
            global costframe1border
            global costframe1

            cost = 0
            item = mytree.selection()  # Get the ID of the selected item
            details = mytree.item(item)
            productname = details.get("values")[1]
            total = details.get("values")[2]
            my_list.append(total)
            my_item = details.get('values')
            item_list.append(my_item)
            print(item_list)

            for i in my_list:
                num = float(i)
                cost += num

    # label displaying item on the order list
            Label(orderframe, width=25, text=productname, bg='white').pack()

            # TOTAL COST SECTION
            #costframe1border.destroy()

            costframe1border = Frame(user_window, bg='black', height=50, width=200)
            costframe1border.place(x=550, y=70)
            costframe1 = Frame(costframe1border, bg="black", height=50, width=200)
            costframe1.pack(padx=5, pady=5)
            Label(costframe1, width=23, text=f'TOTAL : KSH {cost}', bg='yellow', font=('impact', 15)).pack(pady=5, padx=5)


        # mytree.bind("<Button-1>", on_item_click)
        Button(menuframe2, text="Place order", bg='green', font=('bold', 14), command=on_item_click).place(x=110, y=10)

        mytree.pack()
        global costframe
        global orderframeborder

        orderframeborder = Frame(user_window, bg='black')
        orderframeborder.place(x=550, y=110)
        orderframe = Frame(orderframeborder, bg='white')
        orderframe.pack(padx=10, pady=10)
        Label(orderframe, width=20, bg='white', text='product list', font=('impact', 17)).pack()
        costframe = Frame(user_window, bg="sky blue", height=40, width=242)
        costframe.place(x=550, y=70)
        Label(costframe, text='TOTAL COST', font=('bold', 15), bg='sky blue', fg='white').place(x=50, y=10)

# USER OPTION HISTORY FRAME
    elif xu.get() == 2:
        global history_frame_border

        menuframeborder.destroy()
        menuframeborder.destroy()
        costframe.destroy()
        #costframe1border.destroy()
        orderframeborder.destroy()

        history_frame_border = Frame(user_window, height=200, width=400, bg='blue')
        history_frame_border.place(x=270, y=70)

        history_frame = Frame(history_frame_border, height=200, width=400, bg='white')
        history_frame.pack(pady=10, padx=10)

    elif xu.get() == 3:
        user_window.destroy()

# ADMIN PANEL SETUPS
def admin():

    global x
    global admin_window
    global  admin_frame

    # admin_option=['Add item','Delete', 'edit info', 'check report']
    admin_window = Toplevel(root)
    canvas = Canvas(admin_window)
    admin_window_image = PhotoImage(file=r'C:\Users\User\Downloads\vendor6.png')
    Label(admin_window, image=admin_window_image).place(x=0, y=0)

    x = IntVar()

    admin_window.geometry("800x500")
    admin_window.resizable(False, False)

    Label(admin_window, text="Admin window", font=("bold", 30)).pack()

    # FRAME IN THE ADMIN PANEL WITH THE RADIOBUTTON
    frameborder = Frame(admin_window, width=200, height=300, bg="red")
    frameborder.place(x=10, y=100)

    admin_frame = Frame(frameborder, width=200, height=300, bg='white')
    admin_frame.pack(padx=10, pady=10)

# drawing line on the admin panel  using canvas
    canvas.create_line(1, 25, 200, 25, width=10)
    canvas.pack()

    # CREATING RADIOBUTTON FOR ADMIN PANEL SECTION

    for i in range(len(admin_option)):
        optionbutton = Radiobutton(admin_frame, text=admin_option[i], variable=x, value=i,
                                   indicatoron=0, width=25, height=2, font=('impact', 15),
                                   command=admin_choices)
        optionbutton.pack()

    admin_window.mainloop()

# LOG IN SECTION SETUPS

def login():

    user = username.get()
    passcode = password.get()

    if user == "root" and passcode == "1234":
        admin()

    # FLOW IF DETAILS ARE CORRECT
    # USER WINDOW

    elif user == "user" and passcode == "1234":
        global xu
        global user_window
        global useroptionframe

        xu = IntVar()
# USER WINDOW
        user_window = Toplevel(root)
        user_window.geometry("800x500")
        user_window.resizable(False, False)
        Label(user_window, text="User window", font=("bold", 20)).pack()
        user_window_image = PhotoImage(file=r'C:\Users\User\Downloads\vendor4.png')
        Label(user_window, image=user_window_image).place(x=0, y=0)
        Label(user_window,text="WELCOME AGAIN TO OUR PLATFORM", font=('impact', 18)).place(x=200,y=6)

        useroptionframeborder = Frame(user_window, width=200, height=300, bg='red')
        useroptionframeborder.place(x=20, y=80)

        useroptionframe = Frame(useroptionframeborder, width=200, height=300, bg='white')
        useroptionframe.pack(pady=10, padx=10)

        for i in range(len(user_option)):
            useroptionbutton = Radiobutton(useroptionframe, text=user_option[i], variable=xu, value=i, width=20, height=3,
                                         indicatoron=0, font=("impact", 16), command=user_selection)
            useroptionbutton.pack()


        user_window.mainloop()

    # FOLLOWS THIS SECTION IF THE LOG IN DETAILS ARE WRONG

    elif user == "" and passcode == "":
        messagebox.showerror("invalid", "User name and password required")

    elif user == "":
        messagebox.showerror("invalid", "username required")
    elif passcode == "":
        messagebox.showerror("invalid", "Password required")

    elif user != 'root' or user != " user" or passcode != "1234":
        messagebox.showerror("invalid", "wrong details")

# THE MAIN SECTION OF THE SCREEN
def main():
    global root
    global username
    global password


# window for main log in screen
    root = Tk()
    root.geometry("900x620+100+80")
    root.resizable(False, False)
    root.config(bg='yellow')
    #link=Image.open(r'C:\Users\User\OneDrive\Desktop\vendor.png')
    image = PhotoImage(file= r'C:\Users\User\Downloads\vendor3.png')
    Label(root, image=image ).place(x=0, y=0)

    Label(root, text='VENDOR MANAGEMENT SYSTEM', font=('impact', 20), bg='black', fg='white').pack()

    borderframe = Frame(root, bg='black', height=400, width=800, relief=RAISED)
    borderframe.pack()

    rootframe = Frame(borderframe, bg='sky blue', height=400, width=800)
    rootframe.pack(padx=10, pady=10)
    frameimage = PhotoImage(file=r'C:\Users\User\Downloads\vendor6.png')
    Label(rootframe, image=frameimage).place(x=0, y=0)

    username = StringVar()
    password = StringVar()
# FOR LABEL& ENTRY IN THE LOG IN SCREEN SECTION
    username_label = Label(rootframe, text="Username:", font=("bold", 20))
    username_label.place(x=100, y=50)

    password_label = Label(rootframe, text="password:", font=('bold', 20))
    password_label.place(x=100, y=100)

    username_entry = Entry(rootframe, width=25, bd=2, textvariable=username, font=('arial', 20))
    username_entry.place(x=300, y=50)

    password_entry = Entry(rootframe, width=25, bd=2, textvariable=password, show="*", font=("arial", 20))
    password_entry.place(x=300, y=100)

#    FOR CLEARING ENTERED VALUES IN THE LOG IN SECTION
    def clear():
        username_entry.delete(0, END)
        password_entry.delete(0, END)

# BUTTON ON THE LOG IN SCREEN

    submit_button = Button(rootframe, text="log in", height=2, width=10, bg='blue', command=login)
    submit_button.place(x=300, y=200)
    clear_button = Button(rootframe, text="clear", height=2, width=10, command=clear)
    clear_button.place(x=450, y=200)
    exit_button = Button(rootframe, text="exit", height=2, width=10, bg='red', command=root.destroy)
    exit_button.place(x=600, y=200)

    root.mainloop()

main()
