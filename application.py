import streamlit as st
from pymongo import MongoClient
import base64

Mongo_URL="mongodb+srv://San_enthu:root@Sandhya543.mongodb.net/mydb?retryWrites=true&w=majority&ssl=true"
client=MongoClient(Mongo_URL)
db=client["MyDB"]
collection = db["std_data"] 
def insertion(ID_pic,name,student_regno,email,phone_number):
    final_img=base64.b64encode(ID_pic.read()).decode('utf-8')
    data = {
        "ID_pic":final_img,
        "name":name,
        "Student_regno":student_regno,
        "email": email,
        "phone_number":phone_number
    }
    collection.insert_one(data)
def view(student_regno):
    result=collection.find_one({"student_regno":student_regno})
    return result
def main():
    st.title('STUDENT INFO PAGE')
    page = st.sidebar.selectbox("Select a page", ["Add Student", "View Student"])
    if page=="Add Student":
        st.header("Add Student")
        ID_pic = st.file_uploader("Upload ID Photo", type=["jpg", "jpeg"])
        name = st.text_input("Name")
        student_regno = st.text_input("Student reg.no")
        email = st.text_input("Email")
        phone_number = st.text_input("Phone Number")
        if st.button("submit"):
            if ID_pic is not None and name!="" and student_regno!="" and email!="" and phone_number!="":
                insertion(ID_pic,name,student_regno,email,phone_number)
                st.success("Student Registration done successfully")
            else:
                st.error("Insert All the required fields")

    elif page=="View Student":
        st.header("View Student")
        reg=st.text_input("Enter the student register number:")
        if st.button("View"):
            if reg!="":
                data=view(reg)
                if data:
                    st.write("Name:", data["name"])
                    st.write("Student Reg_no:", data["student_regno"])
                    st.write("Email:", data["email"])
                    st.write("Phone Number:", data["phone_number"])
                    if data["ID_pic"]:
                        st.image(base64.b64decode(data["ID_pic"]), caption="ID", use_column_width=True)
                    
                else:
                    st.error("Student not found")
            else:
                st.error("please enter the register number")

if __name__ == "__main__":
    main()



