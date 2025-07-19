Diabetes Prediction App
This repository contains a Streamlit web application that predicts the likelihood of a person having diabetes based on various health parameters using a Logistic Regression model.

📝 Description
This application provides an intuitive and user-friendly interface for individuals to input their health data and receive an instant prediction regarding their diabetes status. It leverages a pre-trained Logistic Regression model to make these predictions, making it a simple yet effective tool for preliminary health assessment.

✨ Features
Interactive Input Form: Easily enter health metrics such as BMI, Insulin level, Glucose, Blood Pressure, Skin Thickness, Pregnancy, Diabetes Pedigree Function, and Age.

Real-time Prediction: Get an immediate prediction (Diabetic/Non-Diabetic) upon submitting the data.

Clear Results: The prediction is displayed clearly on the screen.

User-Friendly Interface: Built with Streamlit for a clean and responsive web interface.

🛠️ Technologies Used
Python: The core programming language.

Streamlit: For creating the interactive web application.

Scikit-learn: For the Logistic Regression model and data preprocessing.

Pandas: For data manipulation and handling.

NumPy: For numerical operations.

🚀 How to Run Locally
Follow these steps to set up and run the application on your local machine:

Prerequisites
Python 3.x installed on your system.

Installation
Clone the repository:

git clone https://github.com/akshay-mani-tripathi/Diabetes-Prediction-Using-ML.git

Create a virtual environment (recommended):

python -m venv venv
source venv/bin/activate  # On Windows: `venv\Scripts\activate`

Install the required libraries:

pip install -r requirements.txt

Example requirements.txt:

streamlit
scikit-learn
pandas
numpy

Running the Application
Run the Streamlit app:

streamlit run app.py

Access the app:
The application will open in your default web browser at (https://diabetes-prediction-using-ml-mdenqi52ipxakmcpcelqt2.streamlit.app/).

💡 Usage
Once the application is running:

Enter the required health parameters into the input fields.

Click the "Predict" button.

The prediction (Diabetic or Non-Diabetic) will be displayed below the button.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
