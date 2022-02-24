from tkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3

studentName, susn, phone, dept, sem= "", "", 0, "", 0
susn, compId, comp, eligib, r1, r2, r3, r4, r5, sal = "", 0, "", 9, 9,9,9,9,9, 0
enteredName = ""
currentFrameOpen = ""

def connect():
  conn = sqlite3.connect('database.db')
  c = conn.cursor()
  c.execute("""CREATE TABLE IF NOT EXISTS `student_details`(sname varchar(20), usn varchar(20) NOT NULL PRIMARY KEY, sphone integer, department varchar(5), semester integer)""")
  c.execute("""CREATE TABLE IF NOT EXISTS `recruitment_details`(usn varchar(20), cid integer, company varchar(20), eligibility integer, round_1 integer, round_2 integer, round_3 integer, round_4 integer, round_5 integer, salary integer)""")
  conn.commit()

def insertStudentDetails():
  global currentFrameOpen
  currentFrameOpen = "studentDetails"

  studentName, susn, phone, dept, sem= "", "", 0, "", 0

  frame = Frame(root, padx=10, pady=10)
  frame.pack(padx = 10, pady = 10)

  Label(frame, text="student name").grid(row = 0, column = 0)
  studentName = Entry(frame, width= 40)
  studentName.focus_set()
  studentName.grid(row = 0, column=1)

  Label(frame, text="usn").grid(row = 1, column = 0)
  susn = Entry(frame, width= 40)
  susn.focus_set()
  susn.grid(row = 1, column=1)

  Label(frame, text="Phone number").grid(row = 2, column = 0)
  phone = Entry(frame, width= 40)
  phone.focus_set()
  phone.grid(row = 2, column=1)

  Label(frame, text="department").grid(row = 3, column = 0)
  dept = Entry(frame, width= 40)
  dept.focus_set()
  dept.grid(row = 3, column=1)

  Label(frame, text="semester").grid(row = 4, column = 0)
  sem = Entry(frame, width= 40)
  sem.focus_set()
  sem.grid(row = 4, column=1)

  def submitStudentDetails():
    sphone, semester = IntVar(), IntVar()
    sname = studentName.get()
    usn = susn.get()
    sphone = phone.get()
    department = dept.get()
    semester = sem.get()

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("""INSERT INTO `student_details`(sname, usn, sphone, department, semester) VALUES (?,?,?,?,?)""", (sname, usn, sphone, department, semester))
    conn.commit()

  def closeStudentDetails():
    frame.destroy()

  submitStudentDetailsBtn = ttk.Button(frame, text="Submit Student Details", command=submitStudentDetails).grid(row=20, column=1)
  closeStudentDetailsBtn = ttk.Button(frame,text="close", command=closeStudentDetails).grid(row=22, column=1)

def insertRecruitmentDetails():
  susn, compId, comp, eligib, r1, r2, r3, r4, r5, sal = "", 0, "", 9, 9,9,9,9,9, 0
  recruitmentFrame = Frame(root, padx = 10, pady = 10)
  recruitmentFrame.pack(padx = 10, pady = 10)

  Label(recruitmentFrame, text="USN").grid(row = 0, column = 0)
  susn = Entry(recruitmentFrame, width= 40)
  susn.focus_set()
  susn.grid(row = 0, column=1)

  Label(recruitmentFrame, text="Company ID").grid(row = 1, column = 0)
  compId = Entry(recruitmentFrame, width= 40)
  compId.focus_set()
  compId.grid(row = 1, column=1)

  Label(recruitmentFrame, text="Company").grid(row = 2, column = 0)
  comp = Entry(recruitmentFrame, width= 40)
  comp.focus_set()
  comp.grid(row = 2, column=1)

  Label(recruitmentFrame, text="Eligibility").grid(row = 3, column = 0)
  eligib = Entry(recruitmentFrame, width= 40)
  eligib.focus_set()
  eligib.grid(row = 3, column=1)

  Label(recruitmentFrame, text="Round 1").grid(row = 4, column = 0)
  r1 = Entry(recruitmentFrame, width= 40)
  r1.focus_set()
  r1.grid(row = 4, column=1)

  Label(recruitmentFrame, text="Round 2").grid(row = 5, column = 0)
  r2 = Entry(recruitmentFrame, width= 40)
  r2.focus_set()
  r2.grid(row = 5, column=1)

  Label(recruitmentFrame, text="Round 3").grid(row = 6, column = 0)
  r3 = Entry(recruitmentFrame, width= 40)
  r3.focus_set()
  r3.grid(row = 6, column=1)

  Label(recruitmentFrame, text="Round 4").grid(row = 7, column = 0)
  r4 = Entry(recruitmentFrame, width= 40)
  r4.focus_set()
  r4.grid(row = 7, column=1)

  Label(recruitmentFrame, text="Round 5").grid(row = 8, column = 0)
  r5 = Entry(recruitmentFrame, width= 40)
  r5.focus_set()
  r5.grid(row = 8, column=1)

  Label(recruitmentFrame, text="Salary").grid(row = 9, column = 0)
  sal = Entry(recruitmentFrame, width= 40)
  sal.focus_set()
  sal.grid(row = 9, column=1)

  def submitRecruitmentDetails():
    # database attributes > usn, cid, company, eligibility, round_1, round_2, round_3, round_4, round_5, salary
    # code equivalents > susn, compId, comp, eligib, r1, r2, r3 r4, r5, sal

    cid, eligibility, round_1, round_2, round_3, round_4, round_4, round_5, salary = IntVar(), IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(), IntVar()
    usn = susn.get()
    cid = compId.get()
    company = comp.get()
    eligibility = eligib.get()
    round_1 = r1.get()
    round_2 = r2.get()
    round_3 = r3.get()
    round_4 = r4.get()
    round_5 = r5.get()
    salary = sal.get()

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("""INSERT INTO `recruitment_details`(usn, cid, company, eligibility, round_1, round_2, round_3, round_4, round_5, salary) VALUES (?,?,?,?,?,?,?,?,?,?)""", (usn, cid, company, eligibility, round_1, round_2, round_3, round_4, round_5, salary))
    conn.commit()

  def closeRecruitmentDetails():
    recruitmentFrame.destroy()
  button = ttk.Button(recruitmentFrame, text="Submit Recruitment Details", command=submitRecruitmentDetails).grid(row=30, column=1)
  closeRecruitmentDetailsBtn = ttk.Button(recruitmentFrame, text="close", command=closeRecruitmentDetails).grid(row=33, column=1)

def queries():
  queriesFrame= Frame(root, padx = 10, pady = 10)
  queriesFrame.pack(padx = 10, pady = 10)  

  def displayAllStudentDetails():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute(""" SELECT * FROM `student_details` """)
    details = c.fetchall()

    tree = ttk.Treeview(root, column=("sname", "usn", "sphone", "department", "semester"), show='headings')
    tree['columns'] = ('sname', 'usn', 'sphone', 'department', 'semester')
    tree.column("#0", width = 50, anchor=W)
    tree.column("sname", width = 100, anchor=W)
    tree.column("usn", width = 100, anchor=E)
    tree.column("sphone", width = 100, anchor=W)
    tree.column("department", width = 100, anchor=W)
    tree.column("semester", width = 60, anchor=E)

    tree.heading("#0", text="label", anchor=W)
    tree.heading("sname", text="Student Name", anchor=W)
    tree.heading("usn", text="USN", anchor=E)
    tree.heading("sphone", text="Student Phone", anchor=W)
    tree.heading("department",text="Department", anchor=W)
    tree.heading("semester", text="Semester", anchor=E)
    tree.pack()


    for row in details:
      print(row)
      tree.insert("", tk.END, values=row)
    conn.close()


  def displayRecruitmentDetails():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute(""" SELECT * FROM `recruitment_details` """)
    details = c.fetchall()

    tree = ttk.Treeview(root, column=("usn", "cid", "company", "eligibility", "round 1", "round 2", "round 3", "round 4", "round 5", "salary"), show='headings')
    tree['columns'] = ("usn", "cid", "company", "eligibility", "round 1", "round 2", "round 3", "round 4", "round 5", "salary")
    tree.column("#0", width = 50, anchor=W)
    tree.column("usn", width = 80, anchor=W)
    tree.column("cid", width = 60, anchor=E)
    tree.column("company", width = 60, anchor=W)
    tree.column("eligibility", width = 60, anchor=W)
    tree.column("round 1", width = 60, anchor=E)
    tree.column("round 2", width = 60, anchor=E)
    tree.column("round 3", width = 60, anchor=E)
    tree.column("round 4", width = 60, anchor=E)
    tree.column("round 5", width = 60, anchor=E)
    tree.column("salary", width = 60, anchor=E)

    tree.heading("#0", text="label", anchor=W)
    tree.heading("usn", text="USN", anchor=W)
    tree.heading("cid", text="CID", anchor=E)
    tree.heading("company", text="Company", anchor=W)
    tree.heading("eligibility",text="Eligibility", anchor=W)
    tree.heading("round 1", text="Eligibility", anchor=E)
    tree.heading("round 2", text="round 2", anchor=E)
    tree.heading("round 3", text="round 3", anchor=E)
    tree.heading("round 4", text="round 4", anchor=E)
    tree.heading("round 5", text="round 5", anchor=E)
    tree.heading("salary", text="salary", anchor=E)
    tree.pack()

    for row in details:
      print(row)
      tree.insert("", tk.END, values=row)
    conn.close()

  def displaySpecificStudentDetail():
    # accepts user input and calls findName function when button is clicked
    nameEntry = StringVar()

    Label(queriesFrame, text="Enter student name").grid(row=30, column=0)
    nameEntry = Entry(queriesFrame, width= 40)
    nameEntry.focus_set()
    nameEntry.grid(row = 35, column=0)

    def findName(): # to find the specific name and displaying details when submit button is clicked
      enteredName = nameEntry.get()
      conn = sqlite3.connect('database.db')
      c = conn.cursor()
      print(f"entered into findname function and name is {enteredName}")

      c.execute(""" SELECT * FROM `student_details` WHERE sname = (?)""", (enteredName,))
      details = c.fetchall()
      print(details)

      tree = ttk.Treeview(queriesFrame, column=("name", "usn", "phoneno", "dept", "semester"))
      tree['columns'] = ("name", "usn", "phoneno", "department", "semester")
      tree.column("#0", width = 50, anchor=W)
      tree.column("name", width = 50, anchor=W)
      tree.column("usn", width = 50, anchor=W)
      tree.column("phoneno", width = 50, anchor=W)
      tree.column("department", width = 50, anchor=W)
      tree.column("semester", width = 50, anchor=W)
      
      tree.heading("#0", text="label", anchor=E)
      tree.heading("name", text="name", anchor=E)
      tree.heading("usn", text="usn", anchor=E)
      tree.heading("phoneno", text="phoneno", anchor=E)
      tree.heading("department", text="department", anchor=E)
      tree.heading("semester", text="semester", anchor=E)
      tree.grid(row=30, column=0)

      for row in details:
        print(row)
        tree.insert("", tk.END, values=row)

    ttk.Button(queriesFrame, text="Submit", command=findName).grid(row=40, column=0)
    
  var1 = IntVar()

  def displaySpecificRecruitmentDetail():
    # accepts user input and calls findName function when button is clicked
    nameEntry = StringVar()

    Label(queriesFrame, text="Enter student usn").grid(row=30, column=0)
    usnEntry = Entry(queriesFrame, width= 40)
    usnEntry.focus_set()
    usnEntry.grid(row = 35, column=0)

    def findUsn(): # to find the specific name and displaying details when submit button is clicked
      enteredUsn = usnEntry.get()
      conn = sqlite3.connect('database.db')
      c = conn.cursor()
      print(f"entered into findname function and name is {enteredUsn}")

      c.execute(""" SELECT * FROM `recruitment_details` WHERE usn = (?)""", (enteredUsn,))
      details = c.fetchall()
      print(details)

      tree = ttk.Treeview(queriesFrame, column=("usn", "cid", "company", "eligibility", "round 1", "round 2", "round 3", "round 4", "round 5", "salary"))
      tree['columns'] = ("usn", "cid", "company", "eligibility", "round 1", "round 2", "round 3", "round 4", "round 5", "salary")
      tree.column("#0", width = 0, anchor=W)
      tree.column("usn", width = 80, anchor=W)
      tree.column("cid", width = 50, anchor=E)
      tree.column("company", width = 80, anchor=W)
      tree.column("eligibility", width = 50, anchor=W)
      tree.column("round 1", width = 50, anchor=E)
      tree.column("round 2", width = 50, anchor=E)
      tree.column("round 3", width = 50, anchor=E)
      tree.column("round 4", width = 50, anchor=E)
      tree.column("round 5", width = 50, anchor=E)
      tree.column("salary", width = 50, anchor=E)
      
      tree.heading("#0", text="l", anchor=E)
      tree.heading("usn", text="usn", anchor=E)
      tree.heading("cid", text="cid", anchor=E)
      tree.heading("company", text="company", anchor=E)
      tree.heading("eligibility", text="eligibility", anchor=E)
      tree.heading("round 1", text="round 1", anchor=E)
      tree.heading("round 2", text="round 2", anchor=E)
      tree.heading("round 3", text="round 3", anchor=E)
      tree.heading("round 4", text="round 4", anchor=E)
      tree.heading("round 5", text="round 5", anchor=E)
      tree.heading("salary", text="salary", anchor=E)
      tree.grid(row=30, column=0)

      for row in details:
        print(row)
        tree.insert("", tk.END, values=row)

    ttk.Button(queriesFrame, text="Submit", command=findUsn).grid(row=40, column=0)
    
  var1 = IntVar()

  def closeQueries():
    queriesFrame.destroy()

  q1 = Radiobutton(queriesFrame, text="Show Students Details table", variable=var1, value=1, command=displayAllStudentDetails).grid(row=20, column=0)
  q2 = Radiobutton(queriesFrame, text="Show Specific Student Details", variable=var1, value=2, command=displaySpecificStudentDetail).grid(row=21, column=0)
  q3 = Radiobutton(queriesFrame, text="Show Recruitment Details", variable=var1, value=3, command=displayRecruitmentDetails).grid(row=22, column=0)
  q4 = Radiobutton(queriesFrame, text="Show Specific Recruitment Details table", variable=var1, value=4, command=displaySpecificRecruitmentDetail).grid(row=23, column=0)
  closeQueriesBtn = ttk.Button(queriesFrame, text="close", command=closeQueries).grid(row=40, column=0)

connect()

root = Tk()
root.geometry('700x700')
root.title("Placement Tracking and Analysis")
var = IntVar()
Label(root, text = "Choose from the given options").pack()
R1 = Radiobutton(root, text="Insert Student Details", variable=var, value=1, command=insertStudentDetails).pack(anchor="w")
R2 = Radiobutton(root, text="Insert Recruitment Details", variable=var, value=2,command=insertRecruitmentDetails).pack(anchor="w")
R3 = Radiobutton(root, text="Queries", variable=var, value=3,command=queries).pack(anchor="w")
label = Label(root, text="").pack()

root.mainloop()
