import streamlit as st

st.title("Student Information System")
st.header("Student Details")
st.subheader("Personal Information")
st.text("Department of Computer Science")
st.caption("Academic Year: 2026-2027")
st.code("print('Hello, Students!')", language='python')
st.latex(r"E = mc^2")

st.success("Registration completed successfully!")
st.info("Your examination is schedeuled for Monday.")
st.warning("Please submit your assginment before the deadline.")
st.error("Invalid username or password")
st.exception("An error occurred while processing your request.")
st.help(st.exception)

st.markdown("# Python Programming")
st.markdown("## Data Science")
st.markdown("**Machine Learning**")
st.markdown("*Deep Learning*")
st.markdown("~~Artificial Intelligence~~")
st.markdown("""
### Topics Covered
- Python Basics
- Data Analysis
- Machine Learning
- Deep Learning
- Artificial Intelligence
""")
st.markdown("[Visit Python Website](https://www.python.org/)")

name = st.text_input("Enter your name:")
if name:
    st.write("### Welcome ", name)

feedback = st.text_area("Provide your feedback:")
if feedback:
    st.write("Feedback Received:", feedback)

age = st.number_input("Enter your age:", 
                      min_value=18, 
                      max_value=100, 
                      value=25)

st.write("### Your age is:", age)

marks = st.slider("Enter your marks:", 
                  min_value=0, 
                  max_value=100, 
                  value=50)

st.write("### Your marks are:", marks)

course = st.selectbox("Select your programme:", 
                      ["Computer Science", "Mathematics", "Physics", "Chemistry"])
st.write("### You have selected:", course)

subjects = st.multiselect("Select your subjects:", 
                         ["Data Structures", "Algorithms", "Database Systems", "Operating Systems"])
st.write("### You have selected:", subjects)

gender = st.radio("Select your gender:", ["Male", "Female", "Prefer not to say"])
st.write("### You have selected:", gender)

agree = st.checkbox("I agree to the terms and conditions")
if agree:
    st.success("### Thank you for agreeing to the terms and conditions.")

if st.button("Click Me"):
    st.success("### Button Clicked!")

date = st.date_input("Select your date of birth:", max_value="today")
st.write("### Your date of birth is:", date)

file = st.file_uploader("Upload your profile picture:", type=["jpg", "png"])
if file:
    st.image(file, caption="Uploaded Profile Picture", use_column_width=True)

#Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Students", 120)
col2.metric("Average Marks", "88", "-5")
col3.metric("Pass Percentage", "92%", "+3%")

import pandas as pd
data = {"Student Name": ["Alice", "Bob", "Charlie", "David"],
        "Python": [85, 90, 78, 92],
        "Data Science": [88, 92, 80, 95],
        "Machine Learning": [90, 85, 88, 91]}

df = pd.DataFrame(data)
st.dataframe(df)
st.table(df)

st.line_chart(df.set_index("Student Name")[["Python", "Data Science", "Machine Learning"]])

st.bar_chart(df.set_index("Student Name")[["Python", "Data Science", "Machine Learning"]])

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.bar(df["Student Name"], df["Python"], label="Python", color='purple')
ax.set_xlabel("Student Name")
ax.set_ylabel("Marks")
ax.set_title("Python Marks")
st.pyplot(fig)

st.image(
    "https://picsum.photos/500/250",
    caption = "Random Image from Picsum",
    use_container_width=True
)

'''
st.audio("Audio.mp3",
         format="audio/mp3",
         start_time=0)

st.video("Video.mp4",
         format="video/mp4")
'''
         
st.map({"latitude": [37.76, 37.77, 37.78], "longitude": [-122.4, -122.41, -122.42]})
st.balloons()
st.snow()
st.progress(0.7)
#Forms
with st.form("Student form:"):
    name = st.text_input("Student Name:")
    roll_no = st.text_input("Register Number:")
    marks = st.number_input("Enter Marks:", 
                            min_value=0, 
                            max_value=100)

    submit = st.form_submit_button("Submit")

    if submit:
        st.success(f"Student Name: {name}")
        st.write(f"Register Number: {roll_no}")
        st.write(f"Marks: {marks}")

    st.spinner("Loading...")

    #Columns, tabs and layouts
col1, col2 = st.columns(2)

with col1:
    st.header("Column 1")
    st.write("This is the first column.")
    st.button("Button in Column 1")

with col2:
    st.header("Column 2")
    st.write("This is the second column.")
    st.button("Button in Column 2") 

tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1:
    st.text_area("Content for Tab 1")

with tab2:
    st.info("Content for Tab 2")

with tab3:
    st.radio("Content for Tab 3", ["Option 1", "Option 2", "Option 3"])

st.title("Student Dashboard")

st.sidebar.title("Filter options")

course = st.sidebar.selectbox("Select Course",
                                ["Computer Science", "Mathematics", "Physics", "Chemistry"])

year = st.sidebar.selectbox("Select Academic Year",
                            ["2023-2024", "2024-2025", "2025-2026", "2026-2027"])

st.write("Selected Course:", course)
st.write("Selected Academic Year:", year)