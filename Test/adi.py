import streamlit as st
st.title("Student Information System")
st.header("Student Details")
st.subheader("personal Information")
st.text("Department of computer science")
st.write("Programe: MCA")
st.caption("Academic Year: 2026-2027")
st.code("print('Hello World)",language="python")
st.latex(r"E=mc^2")
st.success("it was a success")
st.info("your examination is schedule for monday")
st.warning("there  is a warning")
st.error("there is an error")
st.exception("Invalid username and password")
st.help(st.exception)
st.markdown("# H1")
st.markdown("## H2")
st.markdown("### H3")
st.markdown("**Bold**")
st.markdown("*Itaalics*")
st.markdown("""
### UL
- 1
- 2
- 3
""")
st.markdown("[URL](google.com)")
name = st.text_input("Enter the name")
if name: 
    st.write(f"Welcome {name}")

feedback = st.text_area("Enter the feedback")
if feedback:
    st.write("your feedback: \n",feedback)

age = st.number_input("Enter the Age",min_value=0,max_value=50,value=25)
st.write("Age : ",age)

marks = st.slider("Slect Marks",min_value=0,max_value=100,value=75)
st.write("marks",marks)

course = st.selectbox("Select course :",['BCA','MCA','AIML'])
st.write("cource:",course)
st.write("")
st.write(course)

lang = st.multiselect("Select course :",['BCA','MCA','AIML'])
st.write("cource:",lang)

rad = st.radio("Select course :",['BCA','MCA','AIML'])
st.write("cource:",rad)

chb = st.checkbox("Select course :")
if chb:
    st.success("Checked")

if st.button("click"):
    st.success("Clicked")

date = st.date_input("DOB",min_value="today",max_value="2026-12-15")
st.write("date",date)

file = st.file_uploader("File Upload", type=['csv','py'])
if file is not None:
    st.write("Added")

col1,col2,col3 = st.columns(3)
col1.metric("Total Student",120,4)
col2.metric("Avg",85,-5)
col3.metric("Pass %",95,"+3%")

import pandas as pd
data = {"Student Name": ["Alice", "Bob", "Charlie", "David"],
        "Python": [85, 90, 78, 92],
        "Data Science": [88, 92, 80, 95],
        "Machine Learning": [90, 85, 88, 91]}

df = pd.DataFrame(data)
st.dataframe(df)
st.table(df)

st.line_chart(df[["Python", "Data Science", "Machine Learning"]])
