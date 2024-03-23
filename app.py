import streamlit as st
import pandas as pd
st.header('RAMACHANDRA COLLEGE OF ENGINEERING')
st.title('STUDENT FEEDBACK ANALYZER')
csv=st.file_uploader('Enter CSV')
# Load the dataset
df = pd.read_csv(csv)
# Specify the range of teachers to consider
start_teacher = 1
end_teacher = 5  # Adjust as needed
# Generate summary for each teacher in the specified range
for i in range(start_teacher, end_teacher + 1):
    teacher = f'Teacher {i}'
    if teacher in df.columns and not df[teacher].isnull().all():
        teacher_feedback = df[teacher].dropna().str.cat(sep=' ')
        st.text("Summary of feedback for :"+teacher)
        st.text(generate_summary(teacher_feedback))

    else:
        st.text("No feedback available for"+teacher)

