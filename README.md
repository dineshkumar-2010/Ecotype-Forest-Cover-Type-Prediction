🌲 EcoType: Forest Cover Type Prediction

EcoType is a machine learning application that predicts the type of forest cover in a geographical area using cartographic and environmental variables.
The project uses a Random Forest classification model and provides an interactive Streamlit web application for real-time predictions.

📌 Project Overview

Forest cover classification plays an important role in:

Environmental monitoring

Forestry management

Land-use planning

EcoType uses terrain and environmental data such as elevation, slope, and hydrological distances to automatically predict the dominant forest cover type in a region.

⚙️ Technologies Used

Python

Pandas

NumPy

Scikit-learn

Streamlit

Joblib

📊 Machine Learning Model

The project implements several classification algorithms:

Random Forest

Decision Tree

Logistic Regression

K-Nearest Neighbors (KNN)

XGBoost

After evaluation using accuracy, confusion matrix, and classification reports, Random Forest performed the best and was selected for deployment.

Best Model Accuracy:
~87%

📂 Dataset

The dataset contains cartographic variables such as:

Elevation

Aspect

Slope

Horizontal distance to hydrology

Vertical distance to hydrology

Distance to roadways

Hillshade values

Distance to fire points

Wilderness area indicators

Soil type indicators

These variables are used to classify the forest cover type.

🚀 Streamlit Web Application

The project includes an interactive Streamlit application where users can:

Enter environmental and cartographic variables

Click Predict

Get the predicted forest cover type

🖥️ Running the Application

1️⃣ Clone the repository

git clone https://github.com/yourusername/ecotype-forest-prediction.git

2️⃣ Navigate to the project folder

cd ecotype-forest-prediction

3️⃣ Install dependencies

pip install -r requirements.txt

4️⃣ Run the Streamlit app

streamlit run app.py

📁 Project Structure
EcoType-Forest-Prediction
│
├── app.py
├── best_random_forest_model.pkl
├── label_encoder.pkl
├── forest_cover_prediction.ipynb
├── requirements.txt
└── README.md

🎯 Features

Data preprocessing and feature engineering

Multiple model comparison

Hyperparameter tuning

Model deployment using Streamlit

Interactive user interface

📌 Future Improvements

Deploy the application online

Add visualization dashboards

Integrate geospatial data sources

Improve UI design and usability

👨‍💻 Author

Dinesh kumar N

Data Science / Machine Learning Project
