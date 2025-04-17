# complete project with a user interface ,libraries used are :
# 1. streamlit : For web dev
# 2. pandas : For dataframe
# 3. numpy : For array computations
# 4. sklearn.linear_model import LogisticRegression : for implementing logistic regression
# 5. sklearn.model_selection import train_test_split : for training and  testing of data 
# 6. sklearn.metrics import confusion_matrix, accuracy_score : for showing computed data on web


#------------------------------------------------------------------------------------------------------------------------


# Instruction to run :
# 1. Create a folder and put provided dataset in it.
# 2. create file named app.py in folder
# 3. then after , open folder cmd 
# 4. Run the command: streamlit run app.py
# your web application will be deployed .

#-------------------------------------------------------------------------------------------------------------------------

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score

# Load dataset
dataset = pd.read_csv('diabetes.csv')

# Preprocess the data
dataset_new = dataset.copy()
dataset_new[["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]] = dataset_new[["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]].replace(0, np.nan) 
dataset_new["Glucose"].fillna(dataset_new["Glucose"].mean(), inplace=True)
dataset_new["BloodPressure"].fillna(dataset_new["BloodPressure"].mean(), inplace=True)
dataset_new["SkinThickness"].fillna(dataset_new["SkinThickness"].mean(), inplace=True)
dataset_new["Insulin"].fillna(dataset_new["Insulin"].mean(), inplace=True)
dataset_new["BMI"].fillna(dataset_new["BMI"].mean(), inplace=True)

# Split the data
y = dataset_new['Outcome']
X = dataset_new.drop('Outcome', axis=1)
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.20, random_state=42, stratify=dataset_new['Outcome'])

# Train the model
model = LogisticRegression()
model.fit(X_train, Y_train)

# Define the Streamlit app layout
st.title('Diabetes Prediction App')

st.sidebar.header('Patient Data Input')

# Create input fields for user to provide data
pregnancies = st.sidebar.number_input('Pregnancies', min_value=0, max_value=20, value=1, step=1, format='%d')
glucose = st.sidebar.number_input('Glucose', min_value=0, max_value=300, value=148, step=1, format='%d')
blood_pressure = st.sidebar.number_input('Blood Pressure', min_value=0, max_value=200, value=72, step=1, format='%d')
skin_thickness = st.sidebar.number_input('Skin Thickness', min_value=0, max_value=100, value=35, step=1, format='%d')
insulin = st.sidebar.number_input('Insulin', min_value=0.0, max_value=1000.0, value=79.799, step=0.001)
bmi = st.sidebar.number_input('BMI', min_value=0.0, max_value=70.0, value=33.6, step=0.1)
dpf = st.sidebar.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=5.0, value=0.627, step=0.001)
age = st.sidebar.number_input('Age', min_value=0, max_value=120, value=50, step=1, format='%d')

# Predict diabetes using the model
if st.sidebar.button('Predict'):
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])
    prediction = model.predict(input_data)
    
    if prediction == 1:
        st.write('The model predicts: *Diabetic*')
    else:
        st.write('The model predicts: *Non-Diabetic*')

# Display model accuracy
y_predict = model.predict(X_test)
accuracy = accuracy_score(Y_test, y_predict)
st.write(f'Model Accuracy: {accuracy * 100:.2f}%')

# Display confusion matrix
if st.checkbox('Show Confusion Matrix'):
    cm = confusion_matrix(Y_test, y_predict)
    st.write('Confusion Matrix:')
    st.write(cm)
