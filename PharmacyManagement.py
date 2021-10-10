from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import sys



class PMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1330x750+0+0")

        self.addmed_var = StringVar()
        self.refmed_var=StringVar()


        self.refno_var=StringVar() 
        #self.compname_var=StringVar()
        self.medicinetype_var=StringVar()
        self.medicinename_var=StringVar()
        self.lotno_var=StringVar()
        self.issuedate_var=StringVar()
        self.expdate_var=StringVar()
        self.uses_var=StringVar()
        #self.sideeffects_var=StringVar()
        self.referno_var=StringVar()
        self.cmpname_var=StringVar()
        self.cmpowner_var=StringVar()
        self.cmpaddress_var=StringVar()
        self.dosage_var=StringVar()
        self.tabletprice_var=StringVar()




        self.hospitalname_var=StringVar()
        self.hospitaladdress_var=StringVar()
        self.doctorname_var=StringVar()
        self.hospvarno_var=StringVar()

        self.hospdata_var=StringVar()
        self.hospselect_var=StringVar()

        


        labeltitle=Label(self.root,text="Pharmacy Management System",bd=12,font=('times new roman',25),relief=RIDGE,bg='white'
                        ,fg='black',padx=1,pady=2)

        labeltitle.pack(side=TOP,fill=X)

        DataFramer = Frame(self.root,bd=15,relief=RIDGE,padx=5)
        DataFramer.place(x=0,y=70,width=1350,height=500)

        DataFramerLeft = LabelFrame(DataFramer,bd=5,relief=RIDGE,padx=10,text="Medicine Info"
                        ,fg="black",font=500)

        DataFramerLeft.place(x=0,y=5,width=780,height=430)

        DataFramerRight = LabelFrame(DataFramer,bd=5,relief=RIDGE,padx=10,text="Add Medicines"
                        ,fg="black",font=500)

        DataFramerRight.place(x=800,y=5,width=510,height=430)


        ButtonFrame=Frame(self.root,bd=13,relief=RIDGE,padx=20)
        ButtonFrame.place(x=0,y=520,width=1350,height=95)


        

        

        #===========Search By========
        lblSearch=Label(ButtonFrame, font=("arial",13,"bold"),text="Search By", padx=2, bg="black", fg="white")
        lblSearch.grid(row=0,column=5,sticky=W)

        self.search_var=StringVar()
        


        search_combo=ttk.Combobox(ButtonFrame,textvariable=self.search_var, width=12, font=("arial",17,"bold"),state="readonly")
        search_combo["values"]=("ref_no","med_name","lot_no")
        search_combo.grid(row=0,column=6)
        search_combo.current(0)

        self.searchtext_var=StringVar()
        txtSearch=Entry(ButtonFrame,textvariable=self.searchtext_var, bd=3,relief=RIDGE, width=12,font=("arial",17,"bold"))
        txtSearch.grid(row=0,column=7)


        searchButton=Button(ButtonFrame,command=self.searchdata,text="SEARCH",font=("arial",13,"bold"),width=13,bg="black",fg="white")
        searchButton.grid(row=0,column=8)

        showAll = Button(ButtonFrame,command=self.showall,text="SHOW ALL", font=("arial",13,"bold"),width=13, bg="black",fg="white")
        showAll.grid(row=0,column=9)

        # =====================Label And Entry========================
        lblref_no=Label(DataFramerLeft, font=("arial",12,"bold"),text="Reference no", padx=2)
        lblref_no.grid(row=0,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="Pr@141001",database="dbms_project")
        my_cursor=conn.cursor()
        my_cursor.execute("select ref from pharma")
        reqRef = my_cursor.fetchall()

        ref_combo=ttk.Combobox(DataFramerLeft,textvariable=self.refno_var, width=15, font=("arial",14,"bold"),state="readonly")
        ref_combo["values"]=reqRef
        ref_combo.grid(row=0,column=1)
        ref_combo.current(0)
        #===============Add Medicine===============


        



        lblrefeno=Label(DataFramerLeft, font=("arial",12,"bold"),text="Type Of Medicine:", padx=2)
        lblrefeno.grid(row=2,column=0,sticky=W)


        refno_combo=ttk.Combobox(DataFramerLeft,textvariable=self.medicinetype_var, width=15, font=("arial",14,"bold"),state="readonly")
        refno_combo["values"]=("Tablet","Liquid","Drops","Injection","Capsule","Inhales")
        refno_combo.grid(row=2,column=1)
        refno_combo.current(0)

        conn=mysql.connector.connect(host="localhost",username="root",password="Pr@141001",database="dbms_project")
        my_cursor=conn.cursor()
        my_cursor.execute("select medname from pharma")
        reqMedName=my_cursor.fetchall()

        lblMedicineName=Label(DataFramerLeft,font=("arial",12,"bold"),text="Medicine Name:",padx=2,pady=6)
        lblMedicineName.grid(row=3,column=0,sticky=W)

        comMedicineName=ttk.Combobox(DataFramerLeft,textvariable=self.medicinename_var,state="readonly",font=("arial",14,"bold"),width=15)
        comMedicineName['values']=reqMedName
        comMedicineName.current(0)
        comMedicineName.grid(row=3,column=1)


        lblLotNo=Label(DataFramerLeft,font=("arial",12,"bold"),text="Lot No:",padx=1,pady=3)
        lblLotNo.grid(row=4,column=0,sticky=W)
        txtLotNo=Entry(DataFramerLeft,textvariable=self.lotno_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtLotNo.grid(row=4,column=1)

        lblIssueDate=Label(DataFramerLeft,font=("arial",12,"bold"),text="Issue Date:",padx=1,pady=3)
        lblIssueDate.grid(row=5,column=0,sticky=W)
        txtIssueDate=Entry(DataFramerLeft,textvariable=self.issuedate_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtIssueDate.grid(row=5,column=1)

        lblExDate=Label(DataFramerLeft,font=("arial",12,"bold"),text="Exp Date:",padx=1,pady=3)
        lblExDate.grid(row=6,column=0,sticky=W)
        txtExDate=Entry(DataFramerLeft,textvariable=self.expdate_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtExDate.grid(row=6,column=1)

        lblUses=Label(DataFramerLeft,font=("arial",12,"bold"),text="Uses:",padx=1,pady=2)
        lblUses.grid(row=7,column=0,sticky=W)
        txtUses=Entry(DataFramerLeft,textvariable=self.uses_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtUses.grid(row=7,column=1)

        

        

        lblDosage=Label(DataFramerLeft,font=("arial",12,"bold"),text="Dosage:",padx=1,pady=1)
        lblDosage.grid(row=9,column=0,sticky=W)
        txtDosage=Entry(DataFramerLeft,textvariable=self.dosage_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtDosage.grid(row=9,column=1)

        lblPrice=Label(DataFramerLeft,font=("arial",12,"bold"),text="Price:",padx=1,pady=1)
        lblPrice.grid(row=10,column=0,sticky=W)
        txtPrice=Entry(DataFramerLeft,textvariable=self.tabletprice_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtPrice.grid(row=10,column=1)
        #===========================================doctor-section======================================
        
        lblPres=Label(DataFramerLeft, font=("arial",10,"bold"),text="Prescription-Section", padx=2, bg="green", fg="white")
        lblPres.place(x=340,y=150)

        lbldoct_no=Label(DataFramerLeft, font=("arial",10,"bold"),text="Ref No:", padx=1)
        lbldoct_no.place(x=340,y=180)

       # self.hospitalname_var=StringVar()
      #  self.hospitaladdress_var=StringVar()
       # self.doctorname_var=StringVar()
      #  self.hospvarno_var=StringVar()


        refdoct_nocombo=ttk.Combobox(DataFramerLeft,textvariable=self.hospvarno_var, width=4, font=("arial",10,"bold"),state="readonly")
        refdoct_nocombo["values"]=reqRef
        refdoct_nocombo.place(x=390,y=180)
        refdoct_nocombo.current(0)


        lblhospital_name=Label(DataFramerLeft,font=("arial",10,"bold"),text="Hospital Name:",padx=15,pady=6)
        lblhospital_name.place(x=450,y=180)
        txthospital_name=Entry(DataFramerLeft,textvariable=self.hospitalname_var,font=("arial",10,"bold"),bg="white",bd=2,relief=RIDGE,width=12)
        txthospital_name.place(x=570,y=180)


        lblhospital_address=Label(DataFramerLeft,font=("arial",10,"bold"),text="Hospital Address:",padx=1,pady=6)
        lblhospital_address.place(x=340,y=210)
        txthospital_address=Entry(DataFramerLeft,textvariable=self.hospitaladdress_var,font=("arial",10,"bold"),bg="white",bd=2,relief=RIDGE,width=12)
        txthospital_address.place(x=460,y=210)


        lbldoctor_name=Label(DataFramerLeft,font=("arial",10,"bold"),text="Doctor Name:",padx=15,pady=6)
        lbldoctor_name.place(x=550,y=210)
        txtdoctor_name=Entry(DataFramerLeft,textvariable=self.doctorname_var,font=("arial",10,"bold"),bg="white",bd=2,relief=RIDGE,width=12)
        txtdoctor_name.place(x=660,y=210)
  
        btnDoctor = Button(text="Update Credentials",command=self.updateCredentials,font=("arial",9,"bold"),fg="white",bg="black")
        btnDoctor.place(x=370,y=350)

        lblsearchHospital=Label(DataFramerLeft, font=("arial",10,"bold"),text="Search By", bg="black", fg="white")
        lblsearchHospital.place(x=335,y=270)


        #self.hospdata_var=StringVar()
        #self.hospselect_var=StringVar()

        searchHospital_combo=ttk.Combobox(DataFramerLeft,textvariable=self.hospselect_var,width=15, font=("arial",10,"bold"),state="readonly")
        searchHospital_combo["values"]=("hospital_name","doctor_name")
        searchHospital_combo.place(x=405,y=270)
        searchHospital_combo.current(0)



        txtSearcHosp=Entry(DataFramerLeft,textvariable=self.hospdata_var, bd=2,relief=RIDGE, width=15,font=("arial",10,"bold"))
        txtSearcHosp.place(x=530,y=270)


        btnSearcHosp = Button(DataFramerLeft,command=self.updatehospinfo,text="Search Info",font=("arial",7,"bold"),width=20,bg="black",fg="white",pady=4)
        btnSearcHosp.place(x=630,y=270)


        Framedeatils=Frame(self.root,bd=3,relief=RIDGE)
        Framedeatils.place(x=0,y=0,width=0,height=0)


        Table_frame1=Frame(self.root,bd=15,relief=RIDGE)
        Table_frame1.place(x=330,y=415,width=400,height=100)

        scroll_x=ttk.Scrollbar(Table_frame1,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(Table_frame1,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)


        self.comp_table1=ttk.Treeview(Table_frame1,column=("RefNo","HospitalName","DoctorName","HospitalAddress"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.comp_table1.xview)
        scroll_y.config(command=self.comp_table1.yview)
        self.comp_table1["show"]="headings"
        self.comp_table1.heading("RefNo",text="Reference No")
        
        
        self.comp_table1.heading("HospitalName",text="Hospital Name")
        self.comp_table1.heading("DoctorName",text="Doctor Name")
        self.comp_table1.heading("HospitalAddress",text="Hospital Address")
        
        
        
        self.comp_table1.pack(fill=BOTH,expand=1)

        self.comp_table1.column("RefNo",width=100)
        
        self.comp_table1.column("HospitalName",width=100)
        self.comp_table1.column("DoctorName",width=100)
        self.comp_table1.column("HospitalAddress",width=100)
        


        #=============================================boibo==========
        


        
        btnUpdate = Button(text="Update Stock",command=self.fitch_dataMed,font=12,fg="white",bg="black")
        btnUpdate.place(x=490,y=100)

        side_frame = Frame(DataFramerLeft,bd = 4,relief = RIDGE,bg="white")
        side_frame.place(x=450,y=20,width=250,height = 120)
        
        sc_x = ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y = ttk.Scrollbar(side_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)

        

        self.update_table = ttk.Treeview(side_frame,column=("ref_no","med_avail"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)

        sc_x.config(command=self.update_table.xview)
        sc_y.config(command=self.update_table.yview)

        self.update_table.heading("ref_no",text="Ref No")
        self.update_table.heading("med_avail",text="Stock Available")

        self.update_table["show"]="headings"
        self.update_table.pack(fill=BOTH,expand=1)

        self.update_table.column("ref_no",width=100)
        self.update_table.column("med_avail",width=100)



        #=================== ADD-BUTTONS ===============
        

        
        btnAddData = Button(ButtonFrame,command=self.Add_Data,text="Add-Medicine",font=12,fg="white",bg="black")
        btnAddData.grid(row=0,column=0)

        btnAddData = Button(ButtonFrame,command=self.Update,text="Update",font=12,fg="white",bg="black")
        btnAddData.grid(row=0,column=1)

        btnAddData = Button(ButtonFrame,command=self.delete,text="Delete",font=12,fg="white",bg="black")
        btnAddData.grid(row=0,column=2)


        btnAddData = Button(ButtonFrame,command=self.reset,text="Reset",font=12,fg="white",bg="black")
        btnAddData.grid(row=0,column=3)

        btnAddData = Button(ButtonFrame,command=self.exit_program,text="Exit",font=12,fg="white",bg="black")
        btnAddData.grid(row=0,column=4)
        
       
        


        #================== DataFramerRight =========================
        lblrefno=Label(DataFramerRight,font=("arial",12,"bold"),text="Reference No:",padx=15,pady=6)
        lblrefno.place(x=0,y=20)
        txtrefno=Entry(DataFramerRight,textvariable=self.refmed_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtrefno.place(x=135,y=20)


        lblmedname=Label(DataFramerRight,font=("arial",12,"bold"),text="Medicine Name:",padx=15,pady=6)
        lblmedname.place(x=0,y=50)
        txtmedname=Entry(DataFramerRight,textvariable=self.addmed_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtmedname.place(x=140,y=50)
        

        side_frame = Frame(DataFramerRight,bd = 4,relief = RIDGE,bg="white")
        side_frame.place(x=0,y=80,width=220,height = 120)
        
        sc_x = ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y = ttk.Scrollbar(side_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)

        

        self.medicine_table = ttk.Treeview(side_frame,column=("ref","medname"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)

        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("ref",text="Ref")
        self.medicine_table.heading("medname",text="Medicine Name")

        self.medicine_table["show"]="headings"
        self.medicine_table.pack(fill=BOTH,expand=1)

        self.medicine_table.column("ref",width=70)
        self.medicine_table.column("medname",width=70)

        self.medicine_table.bind("<ButtonRelease-1>",self.Medget_cursor)
        #====================== Medicine Add  Buttons=========================
        down_frame = Frame(DataFramerRight,bd=4,relief=RIDGE,bg="black")
        down_frame.place(x=260,y=80,height=110)

        btnAddmed = Button(down_frame,command=self.AddMed,text="ADD",font=("arial",7,"bold"),width=12,bg="black",fg="white",pady=4)
        btnAddmed.grid(row=0,column=0)

        btnUpdatemed = Button(down_frame,command=self.UpdateMed,text="UPDATE",font=("arial",7,"bold"),width=12,bg="black",fg="white",pady=4)
        btnUpdatemed.grid(row=1,column=0)


        btnDeletemed = Button(down_frame,command=self.DeleteMed,text="DELETE",font=("arial",7,"bold"),width=12,bg="black",fg="white",pady=4)
        btnDeletemed.grid(row=2,column=0)


        btnClearmed = Button(down_frame,command=self.ClearMed,text="CLEAR",font=("arial",7,"bold"),width=12,bg="black",fg="white",pady=4)
        btnClearmed.grid(row=3,column=0)

        #============================================company-details====================================
        lblCompany=Label(DataFramerRight, font=("arial",10,"bold"),text="Company-Details", padx=2, bg="green", fg="white")
        lblCompany.place(x=250,y=195)
        
        lblref_cmp_no=Label(DataFramerRight, font=("arial",10,"bold"),text="Ref No:", padx=2)
        lblref_cmp_no.place(x=0,y=220)


        ref_cmp_no_combo=ttk.Combobox(DataFramerRight,textvariable=self.referno_var, width=4, font=("arial",10,"bold"),state="readonly")
        ref_cmp_no_combo["values"]=reqRef
        ref_cmp_no_combo.place(x=50,y=220)
        ref_cmp_no_combo.current(0)


        lblcmp_name=Label(DataFramerRight,font=("arial",9,"bold"),text="Company Name:",padx=15,pady=6)
        lblcmp_name.place(x=110,y=220)
        txtcmp_name=Entry(DataFramerRight,textvariable=self.cmpname_var,font=("arial",9,"bold"),bg="white",bd=2,relief=RIDGE,width=12)
        txtcmp_name.place(x=220,y=220)


        lblcmp_owner=Label(DataFramerRight,font=("arial",9,"bold"),text="Company Owner:",padx=15,pady=6)
        lblcmp_owner.place(x=290,y=220)
        txtcmp_owner=Entry(DataFramerRight,textvariable=self.cmpowner_var,font=("arial",9,"bold"),bg="white",bd=2,relief=RIDGE,width=10)
        txtcmp_owner.place(x=410,y=220)

        lblcmp_address=Label(DataFramerRight,font=("arial",9,"bold"),text="Company Address:",padx=2,pady=6)
        lblcmp_address.place(x=0,y=250)
        txtcmp_address=Entry(DataFramerRight,textvariable=self.cmpaddress_var,font=("arial",9,"bold"),bg="white",bd=2,relief=RIDGE,width=15)
        txtcmp_address.place(x=120,y=250)

        btnAddComp = Button(DataFramerRight,command=self.addcmpdata,text="Add Comp Details",font=("arial",7,"bold"),width=20,bg="black",fg="white",pady=4)
        btnAddComp.place(x=250,y=250)




        lblSearchComp=Label(DataFramerRight, font=("arial",10,"bold"),text="Search By", bg="black", fg="white")
        lblSearchComp.place(x=0,y=280)


        self.takecategory_var=StringVar()
        self.takeinfo_var=StringVar()

        searchComp_combo=ttk.Combobox(DataFramerRight,textvariable=self.takecategory_var, width=20, font=("arial",10,"bold"),state="readonly")
        searchComp_combo["values"]=("company_name","company_owner")
        searchComp_combo.place(x=70,y=280)
        searchComp_combo.current(0)

        txtSearchComp=Entry(DataFramerRight,textvariable=self.takeinfo_var, bd=2,relief=RIDGE, width=15,font=("arial",10,"bold"))
        txtSearchComp.place(x=230,y=280)


        btnSearchCompany = Button(DataFramerRight,command=self.searchcompanyinfo,text="Search Company Info",font=("arial",7,"bold"),width=20,bg="black",fg="white",pady=4)
        btnSearchCompany.place(x=320,y=280)


        Framedeatils=Frame(self.root,bd=3,relief=RIDGE)
        Framedeatils.place(x=0,y=0,width=0,height=0)


        Table_frame=Frame(self.root,bd=15,relief=RIDGE)
        Table_frame.place(x=835,y=415,width=450,height=100)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.comp_table=ttk.Treeview(Table_frame,column=("RefNo","CompanyName","CompanyOwner","CompanyAddress","MedicineName"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.comp_table.xview)
        scroll_y.config(command=self.comp_table.yview)
        self.comp_table["show"]="headings"
        self.comp_table.heading("RefNo",text="Reference No")
        
        
        self.comp_table.heading("CompanyName",text="Company Name")
        self.comp_table.heading("CompanyOwner",text="CompanyOwner")
        self.comp_table.heading("CompanyAddress",text="Company Address")
        self.comp_table.heading("MedicineName",text="Medicine Name")
        
        
        self.comp_table.pack(fill=BOTH,expand=1)

        self.comp_table.column("RefNo",width=100)
        
        self.comp_table.column("CompanyName",width=100)
        self.comp_table.column("CompanyOwner",width=100)
        self.comp_table.column("CompanyAddress",width=100)
        self.comp_table.column("MedicineName",width=100)
        
        #========================= Frame Details =================================
        Framedeatils=Frame(self.root,bd=15,relief=RIDGE)
        Framedeatils.place(x=0,y=580,width=1350,height=180)


        Table_frame=Frame(self.root,bd=15,relief=RIDGE)
        Table_frame.place(x=0,y=580,width=1350,height=130)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)

        

        self.pharmacy_table=ttk.Treeview(Table_frame,column=("reg","type","tabletname","lotno","issuedate","expdate","uses","dosage","price"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)
        self.pharmacy_table["show"]="headings"
        self.pharmacy_table.heading("reg",text="Reference No")
        
        self.pharmacy_table.heading("type",text="Type of Medicine")
        self.pharmacy_table.heading("tabletname",text="Medicine Name")
        self.pharmacy_table.heading("lotno",text="Lot No")
        self.pharmacy_table.heading("issuedate",text="Issue Date")
        self.pharmacy_table.heading("expdate",text="Exp Date")
        self.pharmacy_table.heading("uses",text="Uses")
        
        
        self.pharmacy_table.heading("dosage",text="Dosage")
        self.pharmacy_table.heading("price",text="Price")
        
        self.pharmacy_table.pack(fill=BOTH,expand=1)

        self.pharmacy_table.column("reg",width=100)
        
        self.pharmacy_table.column("type",width=100)
        self.pharmacy_table.column("tabletname",width=100)
        self.pharmacy_table.column("lotno",width=100)
        self.pharmacy_table.column("issuedate",width=100)
        self.pharmacy_table.column("expdate",width=100)
        self.pharmacy_table.column("uses",width=100)
        
        
        self.pharmacy_table.column("dosage",width=100)
        self.pharmacy_table.column("price",width=100)
        
        self.fetch_dataMed()
        self.fatch_data()
        self.pharmacy_table.bind("<ButtonRelease-1>",self.get_cursor)


    def updatehospinfo(self):
        #messagebox.showinfo("Success","Start")
        conn=mysql.connector.connect(host="localhost",username="root",password="Pr@141001",database="dbms_project")
        my_cursor=conn.cursor()
        print(conn)
        my_cursor.execute("select * from dr_info where "+str(self.hospselect_var.get())+"="+str(f'"{self.hospdata_var.get()}"'))
        datas=my_cursor.fetchall()
        if(len(datas)!=0):
            self.comp_table1.delete(*self.comp_table1.get_children())
            for i in datas:
                self.comp_table1.insert("",END,values=i)


            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Data fetched successfully")
            self.hospdata_var.set("")
        else:
            messagebox.showinfo("Error","No data found with inserted query")
            self.hospdata_var.set("")
        


    def AddMed(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Pr@141001",database="dbms_project")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into pharma(ref,medname) values(%s,%s)",(self.refmed_var.get(),self.addmed_var.get()))

        conn.commit()
        
        self.fetch_dataMed()
        #self.Medget_cursor()
        conn.close()
        messagebox.showinfo("Success","Medicine added")
        

    def fetch_dataMed(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Pr@141001",database="dbms_project")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from pharma")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.medicine_table.delete(*self.medicine_table.get_children())
            for row in rows:
                self.medicine_table.insert("",END,values=row)

            conn.commit()            
        conn.close()



    def searchcompanyinfo(self):
        print("You are now in the page of company info")
        #print("select reference_no,company_name,company_owner,company_address,medname from pharma,company_details where "+str(self.takecategory_var.get())+"="+str(f'"{self.takeinfo_var.get()}"')+"and pharma.ref=medicine_details.reference_no")
        conn=mysql.connector.connect(host="localhost",username="root",password="Pr@141001",database="dbms_project")
        my_cursor=conn.cursor()
        my_cursor.execute("select reference_no,company_name,company_owner,company_address,medname from pharma,company_details where "+str(self.takecategory_var.get())+"="+str(f'"{self.takeinfo_var.get()}"')+"and pharma.ref=company_details.reference_no")

        #self.takecategory_var=StringVar()
        #self.takeinfo_var=StringVar()

        ph=my_cursor.fetchall()
        if len(ph)!=0:
            self.comp_table.delete(*self.comp_table.get_children())
            for i in ph:
                self.comp_table.insert("",END,values=i)
            
            conn.commit()
            conn.close()
        else:
            messagebox.showinfo("Error","No such data found")

        self.takecategory_var.set("")
        self.takeinfo_var.set("")


    def searchdata(self):
        #print(self.search_var.get())
        #print(self.searchtext_var.get())
        #print("select * from medicine_detail where "+str(self.search_var.get())+"="+str(f'"{self.searchtext_var.get()}"'))
        conn=mysql.connector.connect(host="localhost",username="root",password="Pr@141001",database="dbms_project")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from medicine_detail where "+str(self.search_var.get())+"="+str(f'"{self.searchtext_var.get()}"'))

        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in rows:
                self.pharmacy_table.insert("",END,values=i)
            
            conn.commit()
            conn.close()
        else:
            messagebox.showinfo("Error","No such data found")

        self.searchtext_var.set("")
        self.search_var.set("")
        
    def showall(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Pr@141001",database="dbms_project")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from medicine_detail")
        row = my_cursor.fetchall()
        if len(row)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in row:
                self.pharmacy_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def updateCredentials(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Pr@141001",database="dbms_project")
        my_cursor = conn.cursor()
        my_cursor.execute("insert into dr_info values(%s,%s,%s,%s)",(self.hospvarno_var.get(),self.hospitalname_var.get(),self.doctorname_var.get(),self.hospitaladdress_var.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success","Data entered successfully")
        self.hospvarno_var.set("")
        self.hospitalname_var.set("")
        self.doctorname_var.set("")
        self.hospitaladdress_var.set("")


    def fitch_dataMed(self):

        conn=mysql.connector.connect(host="localhost",username="root",password="Pr@141001",database="dbms_project")
        my_cursor=conn.cursor()
        my_cursor.execute("select ref,count(med_name) from pharma,medicine_detail where pharma.ref=medicine_detail.ref_no group by (ref);")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.update_table.delete(*self.update_table.get_children())
            for row in rows:
                self.update_table.insert("",END,values=row)

            conn.commit()            
        conn.close()
        
    def up(self):
        print("Hello world!")




    def Medget_cursor(self,event=""):

        cursor_row=self.medicine_table.focus()
        content=self.medicine_table.item(cursor_row)
        row=content["values"]
        self.refmed_var.set(row[0])
        self.addmed_var.set(row[1])    

    def UpdateMed(self):

        if self.refmed_var.get()=="" or self.addmed_var.get()=="":
            messagebox.showerror("Error","All fields are Required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Pr@141001",database="dbms_project")
            my_cursor=conn.cursor()
            my_cursor.execute("update pharma set medname=%s where ref=%s",(
                                                                            self.addmed_var.get(),
                                                                            self.refmed_var.get(),
                                                                        ))
            conn.commit()
            self.fetch_dataMed()
            conn.close()
            messagebox.showinfo("Success","Data has been updated successfully")



    def DeleteMed(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Pr@141001",database="dbms_project")
        my_cursor=conn.cursor()  

        sql="delete from pharma where ref=%s"
        val=(self.refmed_var.get(),)
        my_cursor.execute(sql,val)

        conn.commit() 
        self.fetch_dataMed()
        conn.close()
        messagebox.showinfo("Success","Medicine Deleted!")


    def ClearMed(self):
        self.refmed_var.set("")
        self.addmed_var.set("")


    def Add_Data(self):

        if self.refno_var=="" or self.lotno_var=="":
            messagebox.showerror("Error","Fields are compulsory")

        else:

            conn=mysql.connector.connect(host="localhost",username="root",password="Pr@141001",database="dbms_project")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into medicine_detail(ref_no,med_type,med_name,lot_no,date_of_issue,date_of_exp,uses,dosage,price) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                        self.refno_var.get(),
                                                                        
                                                                        self.medicinetype_var.get(),
                                                                        self.medicinename_var.get(),
                                                                        self.lotno_var.get(),
                                                                        self.issuedate_var.get(),
                                                                        self.expdate_var.get(),
                                                                        self.uses_var.get(),
                                                                        
                                                                        
                                                                        self.dosage_var.get(),
                                                                        self.tabletprice_var.get(),
                                                                        
                                                                                         ))
            conn.commit()
            self.fatch_data()
            conn.close()
            messagebox.showinfo("Success","Data inserted successfully")

    def fatch_data(self):

        conn=mysql.connector.connect(host="localhost",username="root",password="Pr@141001",database="dbms_project")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from medicine_detail")
        row = my_cursor.fetchall()
        if len(row)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in row:
                self.pharmacy_table.insert("",END,values=i)
            conn.commit()
        conn.close()



    def get_cursor(self,ev=""):
        cursor_row = self.pharmacy_table.focus()
        content = self.pharmacy_table.item(cursor_row)
        row=content["values"]


        self.refno_var.set(row[0]),
        
        self.medicinetype_var.set(row[1]),
        self.medicinename_var.set(row[2]),
        self.lotno_var.set(row[3]),
        self.issuedate_var.set(row[4]),
        self.expdate_var.set(row[5]),
        self.uses_var.set(row[6]),
        
        
        self.dosage_var.set(row[7]),
        self.tabletprice_var.set(row[8]),
       
 

    def Update(self):

        if self.refno_var.get()=="":
            messagebox.showerror("Error","All Fields are Required")
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='Pr@141001',database='dbms_project')
            my_cursor=conn.cursor()
            my_cursor.execute("update medicine_detail set med_type=%s,lot_no=%s,date_of_issue=%s,date_of_exp=%s,uses=%s,side_effect=%s,dosage=%s,price=%s where ref_no=%s",(

                                                                        
                                                                        
                                                                        self.medicinetype_var.get(),
                                                                        
                                                                        self.lotno_var.get(),
                                                                        self.issuedate_var.get(),
                                                                        self.expdate_var.get(),
                                                                        self.uses_var.get(),
                                                                        
                                                                        
                                                                        self.dosage_var.get(),
                                                                        self.tabletprice_var.get(),
                                                                        
                                                                        self.refno_var.get()
            ))
            conn.commit()
            self.fatch_data()
            conn.close()
            messagebox.showinfo("UPDATE","Record has been Updated Succussefully")



    def delete(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Pr@141001",database="dbms_project")
        my_cursor=conn.cursor()  

        sql="delete from medicine_detail where ref_no=%s"
        val=(self.refno_var.get(),)
        my_cursor.execute(sql,val)

        conn.commit() 
        self.fatch_data()
        conn.close()
        messagebox.showinfo("Delete","Medicine Information Deleted!")


    def reset(self):
        #self.refno_var=StringVar() 
        #self.compname_var.set("")
        #self.medicinetype_var.set("")
        #self.medicinename_var=StringVar()
        self.lotno_var.set("")
        self.issuedate_var.set("")
        self.expdate_var.set("")
        self.uses_var.set("")
        
       
        self.dosage_var.set("")
        self.tabletprice_var.set("")

    def addcmpdata(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Pr@141001",database="dbms_project")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into company_details(reference_no,company_name,company_owner,company_address) values(%s,%s,%s,%s)",(
                                                                                                self.referno_var.get(),
                                                                                                self.cmpname_var.get(),
                                                                                                self.cmpowner_var.get(),
                                                                                                self.cmpaddress_var.get(),
                                                                        
                                                                        
                                                                                         ))
        conn.commit()
        
        conn.close()
        messagebox.showinfo("Success","Data inserted successfully")
        self.referno_var.set("")
        self.cmpname_var.set("")
        self.cmpowner_var.set("")
        self.cmpaddress_var.set("")

        
    def exit_program(self):
        sys.exit()

if __name__ == "__main__":
    root=Tk()
    obj=PMS(root)
    root.mainloop()