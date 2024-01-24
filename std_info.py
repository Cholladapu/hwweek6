from flask import Flask
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://chollada:i2kYflYG6WfAHetF@cluster0.kua1tuq.mongodb.net/retryWrites=true&w=majority"

client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    db = client["student"]
    collection = db["std_info"]
    while True:
        print("===MENU===")
        print("1: show all records")
        print("2: insert record")
        print("3: update record")
        print("4: delete record")
        print("5: exit")
        choice = input("Please choose:")
        choice = int(choice)
        if choice==1:
            print(f'found {collection.count_documents({})} records')
            all_students = collection.find()
            for std in all_students:
                print(std)
        elif choice==2:
            id=input("Input Student id : ")
            name=input("Input Fullname : ")
            major=input("Input Major : ")
            gpa=input("Input GPA : ")
            gpa=float(gpa)
            try:
                collection.insert_one({"_id":id,
                                    "Fullname":name,
                                    "Major":major,
                                    "GPA":gpa
                                    })
            except Exception as e:
                print(e)
        elif choice == 3:
            id = input("Enter the Student ID to update: ")
            new_id = input("Input new Student ID: ")
            new_name = input("Input new Fullname: ")
            new_major = input("Input new Major: ")
            new_gpa = float(input("Input new GPA: "))
            try:
                result = collection.update_one(
                {"_id": id},
                {"$set": {
                "_id": new_id,
                "Fullname": new_name,
                "Major": new_major,
                "GPA": new_gpa
                }}
                 )
                if result.modified_count > 0:
                    print(f"Record with ID {id} updated successfully.")
                else:
                    print(f"No record found with ID {id}.")

            except Exception as e:
                print(f"Error updating record: {e}")
        elif choice == 4:
            id = input("Student ID : ")

            try:
                result = collection.delete_one({"_id": id})

                if result.deleted_count > 0:
                    print(f"Record with ID {id} deleted successfully.")
                    
                else:
                    print(f"No record found with ID {id}.")

            except Exception as e:
                print(f"Error deleting record: {e}")
        elif choice==5:
            break
    
except Exception as e:
    print(e)
finally:
    client.close()