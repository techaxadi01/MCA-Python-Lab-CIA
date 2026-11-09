import streamlit as st
with st.form("Student form:"):
    st.title("Student Registration System")
    st.header("Enter the Details")
    name = st.text_input("Student Name")
    reg = st.text_input("Registration Number")
    prg = st.selectbox("Program",["Computer Science", "Mathematics", "Physics", "Chemistry"])
    sem = st.radio("Semester",[1,2,3,4,5,6,7,8])
    sub = st.multiselect("Subjects",["Mathematics","DSA","Python"])
    dob = st.date_input("DoB",max_value="today")
    mt = st.time_input("Preferred Meeting Time")
    age = st.number_input("Age",min_value=0)
    photo = st.file_uploader("Student Photo",type=['jpeg','jpg','png'])
    chk = st.checkbox("Accept Terms and Condition")
    sub = st.form_submit_button("Submit")
    if sub:
        st.balloons()
        if chk:
            st.success("Registration Successful")
            st.write("Student Name:",name)
            st.write("Registration Number:",reg)
            st.write("Program:",prg)
            st.write("Semester:",sem)
            st.write("Subjects:",sub)
            st.write("Date of Birth:",dob)
            st.write("Preferred Meeting Time:",mt)
            st.write("Age:",age)
            if photo is not None:
                st.image(photo,caption="Uploaded Photo",use_column_width=True)
        else:
            st.error("Please accept the terms and conditions to proceed.")
