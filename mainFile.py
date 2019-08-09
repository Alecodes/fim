from tkinter import *
from tkinter import messagebox
import random
import sqlite3
root = Tk()
root.geometry("1000x620")
root.resizable(0, 0)
root.title(" Freelancer's Invoice Manager")

#the database
from peewee import *
from os import path
njia_yetu = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(njia_yetu, "invoiceManager.db"))

class Writer(Model):
    firstName = CharField()
    secondName = CharField()
    phone = CharField(unique=True)
    email = CharField(unique=True)
    class Meta:
        database = db
class OrderDetails(Model):
    owner = ForeignKeyField(Writer, related_name ="persons")
    fName = CharField()
    orderID = CharField(unique=True)
    pageNumbers=IntegerField()
    CPP =IntegerField()
    description=CharField()
    class Meta:
        database = db

Writer.create_table(fail_silently = True)
OrderDetails.create_table(fail_silently = True)



#operatingFunctions
'''
def savebtnmsgbx():
    MsgBox = messagebox.askquestion('Confirmation Box', 'Are you sure you want to save order' + " "+ orderVar.get(),icon='warning')
    if MsgBox == 'yes':
        OrderDetails.create(owner="1", fName=fnamevar.get(), orderID="57557", pageNumbers=phonevar.get(), CPP=emailvar.get(),description=descVar.get())
        ourLister.append([fnamevar.get(), lnamevar.get(), phonevar.get(), emailvar.get()])
        set_select()
        ourLister.append([textvar.get(), lnamevar.get(), phonevar.get()])
        set_select()
    else:
        messagebox.showinfo('Return', 'You will now return to the application screen') 
'''

#Menu function and code
def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)
root.config(menu=menubar)

#New Order Section
l10=Label(root, text="Invoice Manager" , bg="grey", fg="white").place(x=10, y=10, width= 980,height=45)
l11=Label(root, text="NEW ORDER ENTRY SECTION", bg="grey", fg="white").place(x=10, y=60,width= 320, height=25)
l12=Label(root, text="PAYMENT DETAILS SECTION", bg="grey", fg="white").place(x=340, y=60,width= 320, height=25)
l13=Label(root, text="NEW WRITER SECTION", bg="grey", fg="white").place(x=670, y=60,width= 320, height=25)
l14=Label(root, text="Input New Order Details", fg="black").place(x=10, y=90,width= 320, height=20)
l15=Label(root, text="Select Writer to View Invoice", fg="black").place(x=340, y=90,width= 320, height=20)
l16=Label(root, text="Input New Writer Details", fg="black").place(x=670, y=90,width= 320, height=20)
nn=Label(root, text="", bg="grey").place(x=334, y=50,width= 1, height=620)
nn1=Label(root, text="", bg="grey").place(x=664.5, y=50,width= 1, height=380)


#Input Section

global orderVar, pageVar,costVar, descVar
l8=Label(root, text="ACCOUNT Name", fg="black").place(x=10, y=120,width=95, height=25)
variable = StringVar(root)
accVar=StringVar()
variable.set("select") # default value
y = OptionMenu(root, variable, "Writerbay", "FWC","Uvocorp","Writers Cafe'").place(x=140, y=120,width=190, height=28)
l4=Label(root, text="WRITER Name", fg="black").place(x=10, y=150,width=80, height=25)
variable = StringVar(root)
writeVar=StringVar()
variable.set("select") # default value
k = OptionMenu(root, variable,"Kiongozi 1", "Kiongozi 2", "Kiongozi 1", "Kiongozi 1", "Kiongozi 1", "Kiongozi 1"
    , "Kiongozi 1", "Kiongozi 1", "Kiongozi 1", "Kiongozi 1", "Kiongozi 1", "Kiongozi 1")
k.place(x=140, y=148,width=190, height=28)


l2=Label(root, text="ORDER Number", fg="black").place(x=10, y=180,width=100, height=25)
variable = StringVar(root)
writeVar=StringVar()
orderVar=StringVar()
myViongozi=StringVar()
textentry=Entry(root, bg="white", textvariable=orderVar).place(x=140, y=180,width=190, height=25)
l3=Label(root, text="No of PAGES", fg="black").place(x=10, y=210,width=85, height=25)
pageVar=StringVar()
w = Spinbox(root, from_ = 0, to = 100, textvariable=pageVar).place(x=140, y=210,width=190, height=25)
l4=Label(root, text="CPP", fg="black").place(x=10, y=240,width=40, height=25)
variable = StringVar(root)
costVar=StringVar()
variable.set("select") # default value
z = OptionMenu(root, variable, "100", "150","200","250","300","350","400","450","500","other:").place(x=140, y=237,width=190, height=28)
l5=Label(root, text="other >>", fg="grey").place(x=140, y=270,width=80, height=25)
textentry1=Entry(root, bg="white").place(x=210, y=270,width=120, height=25)
l6=Label(root, text="Description", fg="black").place(x=10, y=300,width=80, height=25)
descVar=StringVar()
textentry5=Text(root, width=75, height=6, wrap=WORD, background="white").place(x=140, y=310,width=190, height=100)
b2 = Button(root, bg="forestgreen", text='Save',command="").place(x=50, y=435,width=110, height=25)
b2 = Button(root, bg="forestgreen", text='Refresh',command="").place(x=170, y=435,width=110, height=25)
l7=Label(root, text="SELECT WRITER TO VIEW PAYMENT DETAILS", bg="grey", fg="white").place(x=340, y=435,width=650, height=25)


#AddUserSection
ourLister = [[" ", " ", " "]]


def which_selected():
    print("At {0}".format(select.curselection()))
    return int(select.curselection()[0])


def add_entry():
    global Writer
    MsgBox = messagebox.showinfo('Confirmation Message', 'Are you sure you want to add '+ fnamevar.get() + " " + lnamevar.get() + " to the system?", icon='warning')
    if MsgBox == 'yes':
        Writer.create(firstName=fnamevar.get(), secondName=lnamevar.get(), phone=phonevar.get(), email=emailvar.get())

        '''
        ourLister.append([fnamevar.get(), lnamevar.get(), XXX()])
        set_select()
        MsgBox.showinfo(fnamevar.get() + " " + lnamevar.get() + " " + "successful")'''
    else:
        messagebox.showinfo('Return', 'You will now return to the application screen')


def clicked(self, event):
    text = self.entry_id.get()  # get the text from entry
    reply = self.label.set(format(text))  # format the text on the invisible label you created above
    return reply


def update_entry():
    ourLister[which_selected()] = [fnamevar.get(),
                                   lnamevar.get(),
                                   phonevar.get()]


def delete_entry():
    del ourLister[which_selected()]
    set_select()




def load_entry():
    fname, lname, phone = ourLister[which_selected()]
    fnamevar.set(fname)
    lnamevar.set(lname)
    phonevar.set(phone)


def make_window():
    global fnamevar, lnamevar, phonevar, emailvar, select
    frame1 = Frame(root)
    frame1.place(x=670, y=120,width= 320, height=80)

    Label(frame1, text="First Name").grid(row=0, column=0, sticky=W)
    fnamevar = StringVar()
    fname = Entry(frame1, textvariable=fnamevar, width=60)
    fname.grid(row=0, column=1, sticky=W)

    Label(frame1, text="Last Name").grid(row=1, column=0, sticky=W)
    lnamevar = StringVar()
    lname = Entry(frame1, textvariable=lnamevar, width=60)
    lname.grid(row=1, column=1, sticky=W)

    Label(frame1, text="Phone").grid(row=2, column=0, sticky=W)
    phonevar = StringVar()
    phone = Entry(frame1, textvariable=phonevar, width=60)
    phone.grid(row=2, column=1, sticky=W)

    Label(frame1, text="Email").grid(row=3, column=0, sticky=W)
    emailvar = StringVar()
    email = Entry(frame1, textvariable=emailvar, width=60)
    email.grid(row=3, column=1, sticky=W)

    frame2 = Frame(root)       # Row of buttons
    frame2.place(x=670, y=205,width= 320, height=25)
    b1 = Button(frame2, text=" Add  ", command=add_entry, width=8)
    b2 = Button(frame2, text="Update", command=update_entry, width=8)
    b3 = Button(frame2, text="Delete", command=delete_entry, width=8)
    b4 = Button(frame2, text="Load  ", command=load_entry, width=8)
    b5 = Button(frame2, text="Refresh", command=set_select, width=8)
    b1.pack(side=LEFT)
    b2.pack(side=LEFT)
    b3.pack(side=LEFT)
    b4.pack(side=LEFT)
    b5.pack(side=LEFT)

    frame3 = Frame(root)       # select of names
    frame3.place(x=670, y=230,width= 320, height=200)
    scroll = Scrollbar(frame3, orient=VERTICAL)
    select = Listbox(frame3, yscrollcommand=scroll.set, height=10)
    scroll.config(command=select.yview)
    scroll.pack(side=RIGHT, fill=Y)
    select.pack(side=LEFT, fill=BOTH, expand=1)
    return root


def set_select():
    ourLister.sort(key=lambda record: record[1])
    select.delete(0, END)
    for fname, lname, phone in ourLister:
        select.insert(END, "{0}, {1}".format(lname, fname))


win = make_window()
set_select()


"""
#labels and buttons that adjust with number of users
colours = ['red','green','orange','white','yellow','blue']

r = 0
for c in colours:
    Label(text=c, relief=RIDGE,width=15).grid(row=r,column=0)
    Entry(bg=c, relief=SUNKEN,width=10).grid(row=r,column=1)
    r = r + 1


#Message
msg = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
msg = Message(root, text = msg)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.place(x=800, y=60,width=180, height=25)

#New writer registration

fields = 'First Name', 'Last Name', 'Email Address', 'Phone Number'

def fetch(entries):
   for entry in entries:
      field = entry[0]
      text  = entry[1].get()
      print('%s: "%s"' % (field, text))

def makeform(root, fields):
   entries = []
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=15, text=field, anchor='w')
      ent = Entry(row)
      row.place(x=10, y=150,width=180, height=25)
      lab.place(x=10, y=150,width=180, height=25)
      ent.place(x=10, y=150,width=180, height=25)
      entries.append((field, ent))
   return entries

if __name__ == '__main__':
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e=ents: fetch(e)))
   b1 = Button(root, text='Show',
          command=(lambda e=ents: fetch(e)))
   b1.pack(side=LEFT, padx=5, pady=5)
   b2 = Button(root, text='Quit', command=root.quit)
   b2.pack(side=LEFT, padx=5, pady=5)
"""
#Using place for positioning
# width x height + x_offset + y_offset:


writers = ['Kiongozi 1', 'Kiongozi 2', 'Kiongozi 3', 'Kiongozi 4', 'Kiongozi 5', 'Kiongozi 6', 'Kiongozi 7'
    , 'Kiongozi 8', 'Kiongozi 9', 'Kiongozi 10', 'Kiongozi 11', 'Kiongozi 12', 'Kiongozi 13', 'Kiongozi 14',
           'Kiongozi 15', 'Kiongozi 16']
Buttons = range(16)
for i in range(16):
    ct = [random.randrange(256) for x in range(3)]
    brightness = int(round(0.299 * ct[0] + 0.587 * ct[1] + 0.114 * ct[2]))
    ct_hex = "%02x%02x%02x" % tuple(ct)
    bg_colour = '#' + "".join(ct_hex)
    l = Button(root,
               text=writers[i],
               fg='White' if brightness < 120 else 'Black',
               bg=bg_colour)
    l.place(x=340, y=115 + i * 19.5,width=160, height=18)


#The show invoice Frame
frame4 = Frame(root)
frame4.place(x=340, y=465,width= 650, height=150)
scroll = Scrollbar(frame4, orient=VERTICAL)
select = Listbox(frame4, yscrollcommand=scroll.set, height=10)
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)



mainloop()