import streamlit as st
import pandas as pd
import pickle
import sklearn

from joblib import load
model = load('final_model_banking.joblib')


# Title
st.title('Bank Term Deposit Prediction Model 🏦')

# Using columns to organize the inputs
col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input('Age', min_value=18, max_value=100)
    job = st.selectbox('Job', ['admin', 'blue-collar', 'entrepreneur', 'housemaid', 'management', 'retired', 'self-employed', 'services', 'student', 'technician', 'unemployed', 'unknown'], format_func=lambda x: '👤 ' + x)
    marital = st.selectbox('Marital Status', ['married', 'single', 'divorced', 'unknown'], format_func=lambda x: '💍 ' + x)
    education = st.selectbox('Education', ['basic.4y', 'basic.6y', 'basic.9y', 'high.school', 'illiterate', 'professional.course', 'university.degree', 'unknown'], format_func=lambda x: '🎓 ' + x)

with col2:
    default = st.selectbox('Credit Default', ['yes', 'no', 'unknown'], format_func=lambda x: '✅ ' + x if x != 'unknown' else '❓ unknown')
    housing = st.selectbox('Housing Loan', ['yes', 'no', 'unknown'], format_func=lambda x: '🏠 ' + x if x != 'unknown' else '❓ unknown')
    loan = st.selectbox('Personal Loan', ['yes', 'no', 'unknown'], format_func=lambda x: '💵 ' + x if x != 'unknown' else '❓ unknown')
    contact = st.selectbox('Contact Type', ['cellular', 'telephone'], format_func=lambda x: '📱 ' + x)

with col3:
    month = st.selectbox('Last Contact Month', ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'], format_func=lambda x: '📅 ' + x)
    day_of_week = st.selectbox('Last Contact Day of the Week', ['mon', 'tue', 'wed', 'thu', 'fri'], format_func=lambda x: '📆 ' + x)
    duration = st.number_input('Last Contact Duration (in seconds)', min_value=0, max_value=3600)
    campaign = st.number_input('Number of Contacts During this Campaign', min_value=1, max_value=50)

# Additional inputs outside the columns for layout reasons
pdays = st.number_input('Days Passed After Last Contact', min_value=0, max_value=999)
previous = st.number_input('Contacts Before Current Campaign', min_value=0, max_value=50)
poutcome = st.selectbox('Previous Campaign Outcome', ['failure', 'nonexistent', 'success'], format_func=lambda x: '📊 ' + x)

# Predict button
if st.button('Predict 🔮'):
    try:
        # Convert features into DataFrame for prediction
        input_data = {
            'age': [age], 'job': [job], 'marital': [marital], 'education': [education],
            'default': [default], 'housing': [housing], 'loan': [loan], 'contact': [contact],
            'month': [month], 'day_of_week': [day_of_week], 'duration': [duration],
            'campaign': [campaign], 'pdays': [pdays], 'previous': [previous], 'poutcome': [poutcome]
        }
        df = pd.DataFrame.from_dict(input_data)
        # Assuming model is loaded and ready to predict
        prediction = model.predict(df)
        result = "will subscribe" if prediction[0] == 1 else "will not subscribe"
        st.write(f'Prediction: {result}')
    except Exception as e:
        st.error(f"An error occurred: {e}")
