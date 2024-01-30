from tkinter import *
from tkinter import ttk
import random
import datetime
import time
from tkinter import messagebox
import mysql.connector


class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management")
        self.root.geometry("1540x800+0+0")

        lbtitle=Label(self.root,bd=28,text="Hospital Management",fg="Red",bg="white",font=("times new roman",20,"bold"),relief=RIDGE)
        lbtitle.pack(side=TOP,fill=X)
        
        # ==========dataframe================
     
        dataframe=Frame(self.root,bd=20,relief=RIDGE)
        dataframe.place (x=0,y=130,width=1530,height=300)
         
         # ==================Left====================
        
        self.NameOfTablet = StringVar()
        self.ref = StringVar()
        self.dose = StringVar()
        self.NoOfTablets = StringVar()
        self.lot = StringVar()
        self.issueDate = StringVar()
        self.expDate = StringVar()
        self.dailydose = StringVar()
        self.bp = StringVar()
        self.storage = StringVar()
        self.medicine = StringVar()
        self.pid = StringVar()
        self.nhsnumber = StringVar()
        self.pname = StringVar()
        self.dob = StringVar()
        self.address = StringVar()
       
        
        
        

        dataframeLeft=LabelFrame(dataframe,bd=10,relief=RIDGE,padx=20,font=("times new roman",20,"bold"),text="Patient Information")
        dataframeLeft.place (x=2,y=5,width=850,height=350)

        lblnameTablet=Label(dataframeLeft,bd=10,padx=2,pady=6,font=("times new roman",10),text="Name of Tablet")
        lblnameTablet.grid(row=0,column=0)

        TabletName=ttk.Combobox(dataframeLeft,textvariable=self.NameOfTablet,font=("times new roman",10),width=33)

        TabletName["values"]=('Medixol', 'PainAway', 'CiproGuard', 'HeartEase', 'MoodBliss')
        TabletName.current(0)
        TabletName.grid(row=0,column=1)

        ref=Label(dataframeLeft,font=("times new roman",10),padx=1,text="Refrence Number")
        ref.grid(row=1,column=0,sticky=W)
        txtref=Entry(dataframeLeft,font=("times new roman",10),textvariable=self.ref,width=33)
        txtref.grid(row=1,column=1)

        dose=Label(dataframeLeft,font=("times new roman",10),padx=1,text="Dose",pady=4)
        dose.grid(row=2,column=0,sticky=W)
        txtdose=Entry(dataframeLeft,font=("times new roman",10),textvariable=self.dose,width=33)
        txtdose.grid(row=2,column=1)

        NoOfTablets=Label(dataframeLeft,font=("times new roman",10),padx=1,text="No Of Tablets",pady=4)
        NoOfTablets.grid(row=3,column=0,sticky=W)
        txtNoOfTablets=Entry(dataframeLeft,font=("times new roman",10),width=33,textvariable=self.NoOfTablets)
        txtNoOfTablets.grid(row=3,column=1)

        lot=Label(dataframeLeft,font=("times new roman",10),padx=1,text="lot",pady=4)
        lot.grid(row=4,column=0,sticky=W)
        txtlot=Entry(dataframeLeft,font=("times new roman",10),textvariable=self.lot,width=33)
        txtlot.grid(row=4,column=1)
             

        IssueDate=Label(dataframeLeft,font=("times new roman",10),padx=1,text="Issue Date",pady=4)
        IssueDate.grid(row=5,column=0,sticky=W)
        txtIssueDate=Entry(dataframeLeft,font=("times new roman",10),textvariable=self.issueDate,width=33)
        txtIssueDate.grid(row=5,column=1)

        ExpDate=Label(dataframeLeft,font=("times new roman",10),padx=1,text="Expiry Date",pady=4)
        ExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(dataframeLeft,font=("times new roman",10),textvariable=self.expDate,width=33)
        txtExpDate.grid(row=6,column=1)

        DailyDose=Label(dataframeLeft,font=("times new roman",10),padx=1,text="Daily Dose",pady=4)
        DailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(dataframeLeft,font=("times new roman",10),textvariable=self.dailydose,width=33)
        txtDailyDose.grid(row=7,column=1)

        # SideEffects=Label(dataframeLeft,font=("times new roman",10),padx=1,text="Side Effects",pady=4)
        # SideEffects.grid(row=8,column=0,sticky=W)
        # txtSideEffects=Entry(dataframeLeft,font=("times new roman",10),textvariable=self.sideeffects,width=33)
        # txtSideEffects.grid(row=8,column=1)

        # FurtherInfo=Label(dataframeLeft,font=("times new roman",10),padx=1,text="FurtherInfo",pady=4)
        # FurtherInfo.grid(row=9,column=0,sticky=W)
        # txtFurtherInfo=Entry(dataframeLeft,font=("times new roman",10),textvariable=self.furtherinfo,width=33)
        # txtFurtherInfo.grid(row=9,column=1)

        BloodPressure=Label(dataframeLeft,font=("times new roman",10),padx=1,text="Blood Pressure",pady=4)
        BloodPressure.grid(row=0,column=3,sticky=W)
        txtBloodPressure=Entry(dataframeLeft,font=("times new roman",10),textvariable=self.bp,width=33)
        txtBloodPressure.grid(row=0,column=4)


        Storage=Label(dataframeLeft,font=("times new roman",10),padx=1,text="Storage",pady=4)
        Storage.grid(row=1,column=3,sticky=W)
        txtStorage=Entry(dataframeLeft,font=("times new roman",10),textvariable=self.storage,width=33)
        txtStorage.grid(row=1,column=4)

        Medicine=Label(dataframeLeft,font=("times new roman",10),padx=1,text="Medicine",pady=4)
        Medicine.grid(row=2,column=3,sticky=W)
        txtMedicine=Entry(dataframeLeft,font=("times new roman",10),textvariable=self.medicine,width=33)
        txtMedicine.grid(row=2,column=4)


        PatientID=Label(dataframeLeft,font=("times new roman",10),padx=1,text="Patient ID",pady=4)
        PatientID.grid(row=3,column=3,sticky=W)
        txtPatientID=Entry(dataframeLeft,font=("times new roman",10),textvariable=self.pid,width=33)
        txtPatientID.grid(row=3,column=4)


        NHSNumber=Label(dataframeLeft,font=("times new roman",10),padx=1,text="NHS Number",pady=4)
        NHSNumber.grid(row=4,column=3,sticky=W)
        txtNHSNumber=Entry(dataframeLeft,font=("times new roman",10),textvariable=self.nhsnumber,width=33)
        txtNHSNumber.grid(row=4,column=4)


        PatientName=Label(dataframeLeft,font=("times new roman",10),padx=1,text="Patient Name",pady=4)
        PatientName.grid(row=5,column=3,sticky=W)
        txtPatientName=Entry(dataframeLeft,font=("times new roman",10),textvariable=self.pname,width=33)
        txtPatientName.grid(row=5,column=4)

        DOB=Label(dataframeLeft,font=("times new roman",10),padx=1,text="Date of Birth",pady=4)
        DOB.grid(row=6,column=3,sticky=W)
        txtDOB=Entry(dataframeLeft,font=("times new roman",10),textvariable=self.dob,width=33)
        txtDOB.grid(row=6,column=4)

        Address=Label(dataframeLeft,font=("times new roman",10),padx=1,text="Patient Address",pady=4)
        Address.grid(row=7,column=3,sticky=W)
        txtAddress=Entry(dataframeLeft,font=("times new roman",10),textvariable=self.address,width=33)
        txtAddress.grid(row=7,column=4)

            #  =================right=======================

        dataframeRight=LabelFrame(dataframe,bd=10,relief=RIDGE,padx=20,font=("times new roman",20,"bold"),text="Prescription")
        dataframeRight.place (x=860,y=5,width=450,height=350)

        self.txtprescription=Text(dataframeRight,font=("times new roman",10),height=16,width=65,padx=2,pady=4)
        self.txtprescription.grid(row=0,column=0)

        # ===============button frame================
        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place (x=0,y=450,width=1530,height=70)

        btnPrescription=Button(Buttonframe,text="Prescription",font=("times new roman",10,"bold"),height=1,width=30,padx=2,pady=2,fg="red")
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData=Button(Buttonframe,text="Prescription Data",font=("times new roman",10,"bold"),height=1,width=30,padx=10,pady=4,fg="red")
        btnPrescriptionData.grid(row=0,column=1)

        btnUpdate=Button(Buttonframe,text="Update",font=("times new roman",10,"bold"),height=1,width=23,padx=30,pady=4,fg="red")
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(Buttonframe,text="Delete",font=("times new roman",10,"bold"),height=1,width=23,padx=30,pady=4,fg="red")
        btnDelete.grid(row=0,column=3)
        
        btnclear=Button(Buttonframe,text="Clear",font=("times new roman",10,"bold"),height=1,width=23,padx=30,pady=4,fg="red")
        btnclear.grid(row=0,column=4)

        btnExit=Button(Buttonframe,text="Exit",font=("times new roman",10,"bold"),height=1,width=23,padx=30,pady=4,fg="red")
        btnExit.grid(row=0,column=5)

    

        # ===============Details frame================
        Detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=500, width=1530, height=400)  # Decrease the height


        # ================Table====================
        # ================scrollbar================
        scrollbar_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scrollbar_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)

        self.hospital_table = ttk.Treeview(
        Detailsframe,
        columns=("NameOfTablet", "ref", "dose", "NoOfTablets", "lot", "issueDate", "expDate", "dailydose", "storage", "nhsnumber", "pname", "dob", "address"),
        xscrollcommand=scrollbar_x.set,
        yscrollcommand=scrollbar_y.set,
        height=15  # Adjust this height as needed
    )

        scrollbar_x.pack(side=BOTTOM, fill=X)
        scrollbar_y.pack(side=RIGHT, fill=Y)

        scrollbar_x.config(command=self.hospital_table.xview)
        scrollbar_y.config(command=self.hospital_table.yview)


        self.hospital_table.heading("NameOfTablet",text="Name of Tablet")
        self.hospital_table.heading("ref",text="Refrence")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("NoOfTablets",text="number of Tablets")
        self.hospital_table.heading("lot",text="lot")
        self.hospital_table.heading("issueDate",text="Issue Date")
        self.hospital_table.heading("expDate",text="Expiry Date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("pname",text="patient Name")
        self.hospital_table.heading("dob",text="Date of Birth")
        self.hospital_table.heading("address",text="Address")


        self.hospital_table["show"]="headings"


        self.hospital_table.column("NameOfTablet",width=40)
        self.hospital_table.column("ref",width=40)
        self.hospital_table.column("dose",width=40)
        self.hospital_table.column("NoOfTablets",width=40)
        self.hospital_table.column("lot",width=40)
        self.hospital_table.column("issueDate",width=40)
        self.hospital_table.column("expDate",width=40)
        self.hospital_table.column("dailydose",width=40)
        self.hospital_table.column("storage",width=40)
        self.hospital_table.column("nhsnumber",width=40)
        self.hospital_table.column("pname",width=40)
        self.hospital_table.column("dob",width=40)
        self.hospital_table.column("address",width=45)



        self.hospital_table.pack(fill=BOTH,expand=1)
       

        # ==============Functionality==========
        def iprescriptionData(self):
            if self.NameOfTablet.get=="" or  self.ref=="":
                messagebox.showerror("Error","All Fields required")






    


root=Tk()
hospital=Hospital(root)
root.mainloop()