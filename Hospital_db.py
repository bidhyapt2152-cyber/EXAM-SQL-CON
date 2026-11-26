import mysql.connector


class Hospital_management:
    def __init__(self):
        try:
            self.con=mysql.connector.connect(
                host="localhost",user="root",
                password="Bidhya",database="hospital_management"
            )

        except Exception:
            print("DATABASE CONNECTION FAILED")
            self.con=None


    #register
    def register(self,patient_name,age,phone,department,doctor_name,appointment_date):
        if self.con is None:
            return
        try:
            cursor=self.con.cursor()
            query="INSERT INTO patients(patient_name,age,phone,department,doctor_name,appointment_date) VALUES(%s,%s,%s,%s,%s,%s)"

            data=(patient_name,age,phone,department,doctor_name,appointment_date)

            cursor.execute(query,data)

            self.con.commit()
            print("PATIENT REGISTRATION SUCCESS")
        except Exception:
            print("FAILED TO REGISTER PATIENT")
        finally:
            cursor.close()

    #view
    def view(self):
        if self.con is None:
            return
        try:
            cursor = self.con.cursor()
            query="SELECT patient_id,patient_name,age,phone,department,doctor_name,appointment_date FROM patients"
            cursor.execute(query)

            records=cursor.fetchall()

            if records:
                for rows in records:
                    print(rows)
            else:
                print("NO RECORDS FOUND")

        except Exception:
            print("FAILED TO VIEW APPOINTMENTS")

        finally:
            cursor.close()



    #search
    def search(self,search_type, value):
        if self.con is None:
            return
        try:
            cursor= self.con.cursor()
            if search_type==1:

                query= "SELECT * FROM patients WHERE patient_id = %s"
                data=(value,)

            elif search_type==2:

                query="SELECT * FROM patients WHERE patient_name LIKE %s"
                data=("%"+value+"%",)

            else:

                query="SELECT * FROM patients WHERE doctor_name LIKE %s"
                data=("%"+value+"%",)

            cursor.execute(query,data)

            records=cursor.fetchall()

            if records:
                for row in records:
                    print(row)
            else:
                print("No matching patient found.")

        except Exception :
            print("Failed to search patient:", e)

        finally:
                cursor.close()






    #update
    def update(self,patient_id,patient_name,age,phone,department,doctor_name,appointment_date):
        if self.con is None:
            return
        try:
            cursor = self.con.cursor()
            query="UPDATE INTO patients SET patient_name=%s,age=%s,phone=%s,department=%s,doctor_name=%s,appointment_date=%s WHERE patient_id=%s"

            data=(patient_name,age,phone,department,doctor_name,appointment_date,patient_id)

            cursor.execute(query,data)
            self.con.commit()
            if cursor.rowcount>0:
                print("PATIENT WITH ID",patient_id," UPDATED SUCCESSFULLY")
            else:
                print("PATIENT WITH ID", patient_id, "FAILED TO UPDATE")
        except:
            print("FAILED TO UPDATE RECORD")
        finally:
            cursor.close()



    #delete
    def delete(self,patient_id,):
        if self.con is None:
            return
        try:
            cursor = self.con.cursor()
            query="DELETE FROM patients WHERE patient_id=%s"
            cursor.execute(query,(patient_id,))

            self.con.commit()

            if cursor.rowcount>0:
                print("PATIENT WITH ID",patient_id," DELETED SUCCESSFULLY")
            else:
                print("PATIENT WITH ID", patient_id, "FAILED TO DELETE")
        except:
            print("FAILED TO DELETE RECORD")
        finally:
            cursor.close()


#menu
b=Hospital_management()

while True:
    print("\n")
    print("HOSPITAL MANAGEMENT SYSTEM")
    print("____________________________")

    print("1.Register Patient")
    print("2.View Appointments")
    print("3.Search Patient")
    print("4.Update Appointment Date")
    print("5.Delete Patient Record")
    print("6.Department Summary")
    print("7.Exit")

    ch=int(input("Enter the Choice :"))

    if ch==1:
        patient_name=input("Enter Patient Name :")
        age=int(input("Enter Patient Age :"))
        phone=input("Enter Patient Phone no. :")
        department=input("Enter Department :")
        doctor_name=input("Enter Doctor Name :")
        appointment_date=int(input("Enter Appointment Date :"))

        b.register(patient_name,age,phone,department,doctor_name,appointment_date)

    elif ch==2:

        b.view()
    elif ch== 3:


        print("1. Search by Patient ID")
        print("2. Search by Patient Name")
        print("3. Search by Doctor Name")

        option = int(input("Enter choice: "))

        if option == 1:

            patient_id = int(input("Enter Patient ID: "))

            b.search(1, patient_id)

        elif option == 2:

            name = input("Enter Patient Name: ")

            b.search_patient(2, name)

        elif option == 3:

            doctor = input("Enter Doctor Name: ")

            b.search_patient(3, doctor)

        else:
            print("Invalid choice")

    elif ch==4:
        patient_id = int(input("Enter Patient ID: "))

        patient_name = input("Enter Patient Name :")
        age = int(input("Enter Patient Age :"))
        phone = input("Enter Patient Phone no. :")
        department = input("Enter Department :")
        doctor_name = input("Enter Doctor Name :")
        appointment_date = int(input("Enter Appointment Date :"))



        b.update(patient_id,patient_name,age,phone,department,doctor_name,appointment_date)

    elif ch==5:
        patient_id = int(input("Enter Patient ID: "))


        b.delete(patient_id)

    elif ch==6:
        pass

    elif ch==7:
        break
    else:
        print("INVALID CHOICE")






