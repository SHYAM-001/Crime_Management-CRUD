from tkinter import*
from tkinter import ttk
import mysql.connector 
from tkinter import messagebox
from PIL import Image,ImageTk

class Criminal:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x790+0+0')
        self.root.title('CRIMINAL MANAGEMENT SYSTEM ')

        # variables
        self.var_case_id=StringVar()
        self.var_criminal_no=StringVar()
        self.var_name=StringVar()
        self.var_nickname=StringVar()
        self.var_arrest_date=StringVar()
        self.var_date_of_crime=StringVar()
        self.var_address=StringVar()
        self.var_age=StringVar()
        self.var_occupation=StringVar()
        self.var_birthmark=StringVar()
        self.var_crime_type=StringVar()
        self.var_father_name=StringVar()
        self.var_gender=StringVar()
        self.var_wanted=StringVar()
        self.var_phone=StringVar()
        self.var_location=StringVar()

        lbl_title = Label(self.root,text='CRIMINAL MANAGEMENT',font=('times now roman',40,'bold'),bg='black',fg='gold')
        lbl_title.place(x=0,y=0,width=1530,height=70)

        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=70,width=1530,height=130)

        img_1=Image.open('police0.jpg')
        img_1=img_1.resize((540,160),Image.LANCZOS)
        self.photo1=ImageTk.PhotoImage(img_1)

        self.img_1=Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=540,height=160)

        img_2=Image.open('police1.jpg')
        img_2=img_2.resize((540,160),Image.LANCZOS)
        self.photo2=ImageTk.PhotoImage(img_2)

        self.img_2=Label(img_frame,image=self.photo2)
        self.img_2.place(x=540,y=0,width=540,height=160)

        img_3=Image.open('police2.jpg')
        img_3=img_3.resize((540,160),Image.LANCZOS)
        self.photo3=ImageTk.PhotoImage(img_3)

        self.img_3=Label(img_frame,image=self.photo3)
        self.img_3.place(x=1080,y=0,width=540,height=160)

        # MAIN FRAME

        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=10,y=200,width=1500,height=560)

        # UPPER FRAME

        upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Criminal Information',font=('times now roman',11,'bold'),fg='red')
        upper_frame.place(x=10,y=10,width=1480,height=270)

        # Labels Entry

        # case id

        case_id=Label(upper_frame,text='Case ID:',font=('arial',11,'bold'),bg='white')
        case_id.grid(row=0,column=0,padx=2,sticky=W)

        case_entry=ttk.Entry(upper_frame,textvariable=self.var_case_id,width=22,font=('arial',11,'bold'))
        case_entry.grid(row=0,column=1,padx=2,sticky=W)

        # criminal no

        lbl_criminal_no=Label(upper_frame,text='Criminal No:',font=('arial',11,'bold'),bg='white')
        lbl_criminal_no.grid(row=0,column=2,padx=2,pady=7)

        txt_criminal_no=ttk.Entry(upper_frame,textvariable=self.var_criminal_no,width=22,font=('arial',11,'bold'))
        txt_criminal_no.grid(row=0,column=3,padx=2,pady=7)

        # Criminal Name

        lbl_Name=Label(upper_frame,text='Criminal Name:',font=('arial',11,'bold'),bg='white')
        lbl_Name.grid(row=1,column=0,padx=2,sticky=W,pady=7)

        case_entry=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=('arial',11,'bold'))
        case_entry.grid(row=1,column=1,sticky=W,padx=2,pady=7)

        # NickName

        lbl_nickname=Label(upper_frame,text='NickName:',font=('arial',11,'bold'),bg='white')
        lbl_nickname.grid(row=1,column=2,padx=2,sticky=W,pady=7)

        txt_nickname=ttk.Entry(upper_frame,textvariable=self.var_nickname,width=22,font=('arial',11,'bold'))
        txt_nickname.grid(row=1,column=3,sticky=W,padx=2,pady=7)

        # Arrest Date

        lbl_arrestDate=Label(upper_frame,text='Arrest Date:',font=('arial',11,'bold'),bg='white')
        lbl_arrestDate.grid(row=2,column=0,padx=2,sticky=W,pady=7)

        txt_arrestDate=ttk.Entry(upper_frame,textvariable=self.var_arrest_date,width=22,font=('arial',11,'bold'))
        txt_arrestDate.grid(row=2,column=1,sticky=W,padx=2,pady=7)

        # Date of crime
        lbl_dateofcrime=Label(upper_frame,text='Date Of Crime:',font=('arial',11,'bold'),bg='white')
        lbl_dateofcrime.grid(row=2,column=2,padx=2,sticky=W,pady=7)

        txt_dateofcrime=ttk.Entry(upper_frame,textvariable=self.var_date_of_crime,width=22,font=('arial',11,'bold'))
        txt_dateofcrime.grid(row=2,column=3,sticky=W,padx=2,pady=7)

        # address

        lbl_address=Label(upper_frame,text='Address:',font=('arial',11,'bold'),bg='white')
        lbl_address.grid(row=3,column=0,padx=2,sticky=W,pady=7)

        txt_address=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=('arial',11,'bold'))
        txt_address.grid(row=3,column=1,sticky=W,padx=2,pady=7)

        # Age

        lbl_age=Label(upper_frame,text='Age:',font=('arial',11,'bold'),bg='white')
        lbl_age.grid(row=3,column=2,padx=2,sticky=W,pady=7)

        txt_age=ttk.Entry(upper_frame,textvariable=self.var_age,width=22,font=('arial',11,'bold'))
        txt_age.grid(row=3,column=3,sticky=W,padx=2,pady=7)

        # Occupation

        lbl_occupation=Label(upper_frame,text='Occupation:',font=('arial',11,'bold'),bg='white')
        lbl_occupation.grid(row=4,column=0,padx=2,sticky=W,pady=7)

        txt_occupation=ttk.Entry(upper_frame,textvariable=self.var_occupation,width=22,font=('arial',11,'bold'))
        txt_occupation.grid(row=4,column=1,sticky=W,padx=2,pady=7)

        # birthMark

        lbl_birthmark=Label(upper_frame,text='Birth Mark:',font=('arial',11,'bold'),bg='white')
        lbl_birthmark.grid(row=4,column=2,padx=2,sticky=W,pady=7)

        txt_birthmark=ttk.Entry(upper_frame,textvariable=self.var_birthmark,width=22,font=('arial',11,'bold'))
        txt_birthmark.grid(row=4,column=3,sticky=W,padx=2,pady=7)

        # Crime type

        
        lbl_crimetype=Label(upper_frame,text='Crime Type:',font=('arial',11,'bold'),bg='white')
        lbl_crimetype.grid(row=5,column=0,padx=2,sticky=W,pady=7)

        txt_crimetype=ttk.Entry(upper_frame,textvariable= self.var_crime_type,width=22,font=('arial',11,'bold'))
        txt_crimetype.grid(row=5,column=1,sticky=W,padx=2,pady=7)

        # Father Name

        
        lbl_fathername=Label(upper_frame,text='Father Name:',font=('arial',11,'bold'),bg='white')
        lbl_fathername.grid(row=0,column=4,padx=2,sticky=W,pady=7)

        txt_fathername=ttk.Entry(upper_frame,textvariable= self.var_father_name,width=22,font=('arial',11,'bold'))
        txt_fathername.grid(row=0,column=5,sticky=W,padx=2,pady=7)

        # gender 
        
        lbl_gender=Label(upper_frame,text='Gender:',font=('arial',11,'bold'),bg='white')
        lbl_gender.grid(row=1,column=4,padx=2,sticky=W,pady=7)

        # Wanterd

        lbl_wanted=Label(upper_frame,text='Most Wanted:',font=('arial',11,'bold'),bg='white')
        lbl_wanted.grid(row=2,column=4,padx=2,sticky=W,pady=7)
        
        # Phone Number
        
        lbl_phone = Label(upper_frame,text='PHONE NO. :',font=('arial',11,'bold'),bg='white')
        lbl_phone.grid(row=3,column=4,sticky=W,)
        
        txt_phone=ttk.Entry(upper_frame,textvariable= self.var_phone,width=22,font=('arial',11,'bold'))
        txt_phone.grid(row=3,column=5,sticky=W,padx=2,pady=7)

        # Radio Button gender

        radio_frame_gender=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_gender.place(x=710,y=40,width=190,height=30)

        male=Radiobutton(radio_frame_gender,variable=self.var_gender,text='Male',value='male',font=('arial',9,'bold'),bg='white')
        male.grid(row=0,column=0,pady=2,padx=5,sticky=W)
        self.var_gender.set('male')

        female=Radiobutton(radio_frame_gender,variable=self.var_gender,text='Female',value='female',font=('arial',9,'bold'),bg='white')
        female.grid(row=0,column=1,pady=2,padx=5,sticky=W)

        # Radio Button wanted

        radio_frame_wanted=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_wanted.place(x=710,y=80,width=190,height=30)

        yes=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text='Yes',value='yes',font=('arial',9,'bold'),bg='white')
        yes.grid(row=0,column=0,pady=2,padx=5,sticky=W)
        self.var_wanted.set('yes')

        no=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text='No',value='no',font=('arial',9,'bold'),bg='white')
        no.grid(row=0,column=1,pady=2,padx=5,sticky=W)

        # Button

        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=5,y=200,width=1000,height=45)

        # add button

        btn_add=Button(button_frame,text='Record Save',font=('arial',13,'bold'),width=14,bg='blue',fg='white',command=self.add_data)
        btn_add.grid(row=0,column=0,padx=3,pady=5,sticky=W)

        btn_update=Button(button_frame,text='Update',font=('arial',13,'bold'),width=14,bg='blue',fg='white',command=self.update_data)
        btn_update.grid(row=0,column=1,padx=3,pady=5,sticky=W)

        btn_delete=Button(button_frame,text='Delete',font=('arial',13,'bold'),width=14,bg='blue',fg='white',command=self.delete_data)
        btn_delete.grid(row=0,column=2,padx=3,pady=5,sticky=W)

        btn_clear=Button(button_frame,text='Clear',font=('arial',13,'bold'),width=14,bg='blue',fg='white',command=self.clear_data)
        btn_clear.grid(row=0,column=3,padx=3,pady=5,sticky=W)
        
        btn_location=Button(button_frame,text='Location',font=('arial',13,'bold'),width=14,bg='blue',fg='white',command=self.location_data)
        btn_location.grid(row=0,column=4,padx=3,pady=5,sticky=W)

        btn_social=Button(button_frame,text='Social Link',font=('arial',13,'bold'),width=14,bg='blue',fg='white',command=self.social_data)
        btn_social.grid(row=0,column=5,padx=3,pady=5,sticky=W)


        # background right side image

        img_crime=Image.open('jail.jpg')
        img_crime=img_crime.resize((470,245),Image.LANCZOS)
        self.photo5=ImageTk.PhotoImage(img_crime)

        self.imag_crime=Label(upper_frame,image=self.photo5)
        self.imag_crime.place(x=950,y=0,width=540,height=240)
 
         # DOWN FRAME
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Criminal Information Table',font=('times now roman',11,'bold'),fg='red')
        down_frame.place(x=10,y=280,width=1480,height=270)
         
        # SEARCH FRAME

        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,text=' Search Criminal Record',font=('times now roman',11,'bold'),fg='red')
        search_frame.place(x=0,y=0,width=1470,height=60)

        search_by=Label(search_frame,text='Search By:',font=('arial',11,'bold'),bg='red',fg='white')
        search_by.grid(row=0,column=0,padx=5,sticky=W)

        self.var_com_search=StringVar()
        combo_search_box=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=('arial',11,'bold'),width=18,state='readonly')
        combo_search_box['value']=('Select Option','Case_ID','Criminal_No')
        combo_search_box.current(0)
        combo_search_box.grid(row=0,column=1,padx=5,sticky=W)

        self.var_search=StringVar()
        search_txt=ttk.Entry(search_frame,textvariable=self.var_search,width=18,font=('arial',11,'bold'))
        search_txt.grid(row=0,column=2,sticky=W,padx=5)

        btn_search=Button(search_frame,text='Search',font=('arial',13,'bold'),width=14,bg='blue',fg='white',command=self.search_data)
        btn_search.grid(row=0,column=3,padx=5,sticky=W)

        btn_all=Button(search_frame,text='Show All',font=('arial',13,'bold'),width=14,bg='blue',fg='white',command=self.fetch_data)
        btn_all.grid(row=0,column=4,padx=5,sticky=W)

        crimeagency=Label(search_frame,text='Crime Agency',font=('arial',30,'bold'),bg='white',fg='crimson')
        crimeagency.grid(row=0,column=5,padx=50,sticky=W)

        # table_frame

        table_frame=Frame(down_frame,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1470,height=170)

        # scroll bar 

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.criminal_table=ttk.Treeview(table_frame,columns=('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        self.criminal_table.heading('1',text='CaseID')
        self.criminal_table.heading('2',text='CrimeNo')
        self.criminal_table.heading('3',text='Criminal Name')
        self.criminal_table.heading('4',text='NickName')
        self.criminal_table.heading('5',text='ArrestDate')
        self.criminal_table.heading('6',text='CrimeOfDate')
        self.criminal_table.heading('7',text='Adress')
        self.criminal_table.heading('8',text='Age')
        self.criminal_table.heading('9',text='Occupation')
        self.criminal_table.heading('10',text='Birth Mark')
        self.criminal_table.heading('11',text='Crime Type')
        self.criminal_table.heading('12',text='Father Name')
        self.criminal_table.heading('13',text='Gender')
        self.criminal_table.heading('14',text='Wanted')
        self.criminal_table.heading('15',text='Phone')
        self.criminal_table.heading('16',text='Location')
        

        self.criminal_table['show']='headings'

        self.criminal_table.column('1',width=100)
        self.criminal_table.column('2',width=100)
        self.criminal_table.column('3',width=100)
        self.criminal_table.column('4',width=100)
        self.criminal_table.column('5',width=100)
        self.criminal_table.column('6',width=100)
        self.criminal_table.column('7',width=100)
        self.criminal_table.column('8',width=100)
        self.criminal_table.column('9',width=100)
        self.criminal_table.column('10',width=100)
        self.criminal_table.column('11',width=100)
        self.criminal_table.column('12',width=100)
        self.criminal_table.column('13',width=100)
        self.criminal_table.column('14',width=100)
        self.criminal_table.column('15',width=100)
        self.criminal_table.column('16',width=100)


        self.criminal_table.pack(expand=1,fill=BOTH)

        self.criminal_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()

    # Add function

    def add_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All Fields Are Required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='shyamsharmi-007',database='management')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into criminal values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(self.var_case_id.get(),self.var_criminal_no.get(),self.var_name.get(),self.var_nickname.get(),self.var_arrest_date.get(),self.var_date_of_crime.get(),self.var_address.get(),self.var_age.get(),self.var_occupation.get(),self.var_birthmark.get(),self.var_crime_type.get(),self.var_father_name.get(),self.var_gender.get(),self.var_wanted.get(),self.var_phone.get(),self.var_location))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','Criminal record has been added')
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}')

    # fetch

    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='shyamsharmi-007',database='management')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from criminal')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert('',END,values=i)
            conn.commit()
        conn.close()
    
    # get cursor

    def get_cursor(self,event=""):
        cursor_row=self.criminal_table.focus()
        content=self.criminal_table.item(cursor_row)
        data=content['values']

        self.var_case_id.set(data[0])
        self.var_criminal_no.set(data[1])
        self.var_name.set(data[2])
        self.var_nickname.set(data[3])
        self.var_arrest_date.set(data[4])
        self.var_date_of_crime.set(data[5])
        self.var_address.set(data[6])
        self.var_age.set(data[7])
        self.var_occupation.set(data[8])
        self.var_birthmark.set(data[9])
        self.var_crime_type.set(data[10])
        self.var_father_name.set(data[11])
        self.var_gender.set(data[12])
        self.var_wanted.set(data[13])
        self.var_phone.set(data[14])
        self.var_location.set(data[15])

    # update

    def update_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All Fields Are Required')
        else:
            try:
                update=messagebox.askyesno('update','Are You Sure Update This Criminal Record')
                if update>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='shyamsharmi-007',database='management')
                    my_cursor=conn.cursor()
                    my_cursor.execute('update criminal set Criminal_No=%s, Criminal_Name=%s, Nick_name=%s, arrest_date=%s, dateofcrime=%s, address=%s, age=%s, occupation=%s, BirthMark=%s, crimeType=%s, fatherName=%s, gender=%s, wanted=%s, phone=%s, Location=%s  where Case_ID=%s',(self.var_criminal_no.get(),self.var_name.get(),self.var_nickname.get(),self.var_arrest_date.get(),self.var_date_of_crime.get(),self.var_address.get(),self.var_age.get(),self.var_occupation.get(),self.var_birthmark.get(),self.var_crime_type.get(),self.var_father_name.get(),self.var_gender.get(),self.var_wanted.get(),self.var_phone.get(),self.var_location,self.var_case_id.get()))
                else:
                    if not update :
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success','Criminal Record Successfully Updated')
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}')

    # delete

    def delete_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All Fields Are Required')
        else:
            try:
                Delete=messagebox.askyesno('Delete','Are You Sure Delete This Criminal Record')
                if Delete>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='shyamsharmi-007',database='management')
                    my_cursor=conn.cursor()
                    sql='delete from criminal where Case_ID=%s'
                    value=(self.var_case_id.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return 
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success','Criminal Record Successfully Deleted')
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}')

    # clear

    def clear_data(self):
        self.var_case_id.set("")
        self.var_criminal_no.set("")
        self.var_name.set("")
        self.var_nickname.set("")
        self.var_arrest_date.set("")
        self.var_date_of_crime.set("")
        self.var_address.set("")
        self.var_age.set("")
        self.var_occupation.set("")
        self.var_birthmark.set("")
        self.var_crime_type.set("")
        self.var_father_name.set("")
        self.var_gender.set("")
        self.var_wanted.set("")
        self.var_phone.set("")

    # search 

    def search_data(self):
        if self.var_com_search.get()=="":
            messagebox.showerror('Error','All Filds Are Required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='shyamsharmi-007',database='management')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from criminal where ' +str(self.var_com_search.get())+" LIKE'%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.criminal_table
                    if len(rows)!=0:
                        self.criminal_table.delete(*self.criminal_table.get_children())
                        for i in rows:
                            self.criminal_table.insert('',END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}')
        
    def location_data(self):
        import phonenumbers
        import opencage
        import folium
        from opencage.geocoder import OpenCageGeocode
        from phonenumbers import carrier
        from phonenumbers import geocoder

        number=self.var_phone.get()
        number="+"+number
        print(number)
        pepnumber = phonenumbers.parse(number)
        self.var_location = geocoder.description_for_number(pepnumber,"en")
        print(self.var_location)
        service_pro=phonenumbers.parse(number)
        print(carrier.name_for_number(service_pro, "en"))
        key = '15836a8f01724c60b05865e4ca77a506'
        geocoder = OpenCageGeocode(key)
        query=str(self.var_location)
        results=geocoder.geocode(query)
        lat=results[0]['geometry']['lat']
        lng=results[0]['geometry']['lng']
        print(lat,lng)
        myMap=folium.Map(location=[lat,lng],zoom_start= 9)
        folium.Marker([lat, lng], popup=self.var_location).add_to(myMap)
        myMap.save("mylocation.html")
        import os
        filename ='mylocation.html'
        if os.name == 'nt':
            browser = 'start'
        else:
            browser = 'open'
        os.system('{} {}'.format(browser, filename))

    def social_data(self):
        import subprocess
        import os
        os.chdir('sherlock/sherlock')
        name=self.var_name.get()
        command=f'python sherlock --timeout 1 {name}'
        result = subprocess.run(command, stdout=subprocess.PIPE, shell=True, text=True)
        print(result.stdout)
        path=f'{name}.txt'
        os.startfile(path)      

if __name__=="__main__":
    root=Tk()
    obj=Criminal(root)
    root.mainloop()
      











