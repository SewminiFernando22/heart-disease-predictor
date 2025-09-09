***Heart Disease Predictor***


*What is this Project?*

The Heart Disease Predictor is a machine learning-based application designed to predict the risk of heart disease in individuals based on clinical data. Using the UCI Heart Disease dataset, it employs a Logistic Regression model to classify patients as either "Healthy" (no heart disease) or "Not Healthy" (at risk of heart disease). The project includes a user-friendly web application built with Streamlit, allowing users to input their medical data and receive an instant prediction with a confidence score and personalized health tips.


**Who Needs This?**
*This project is ideal for:*

Healthcare Enthusiasts and Students: Individuals learning about machine learning in healthcare or exploring data science applications.

Developers: Those interested in building and deploying interactive ML web apps using Python and Streamlit.

Researchers: People studying heart disease risk factors or working with the UCI dataset.

General Public: Anyone curious about their heart health (though not a substitute for medical advice).*

*Note: This tool is for educational purposes only and should not be used for medical diagnosis. Always consult a healthcare professional for accurate assessments.
Purpose*




**The primary goals of this project are:**

Predict Heart Disease Risk: Provide a simple way to assess heart disease risk based on 13 clinical features (e.g., age, cholesterol, blood pressure).

Educate Users: Raise awareness about heart health through intuitive visualizations (e.g., risk probability bar charts) and health tips.

Demonstrate ML Workflow: Showcase a complete machine learning pipeline, from data preprocessing to model training and deployment in a web app.

Promote Accessibility: Offer an easy-to-use interface for non-technical users to interact with a machine learning model.




**Technologies Used**

Python: Core programming language for data processing and modeling.

Pandas: For data manipulation and preprocessing.

Scikit-learn: For training the Logistic Regression model and scaling features.

Streamlit: For building the interactive web application.

Matplotlib and Seaborn: For exploratory data analysis and visualizations.

Joblib: For saving and loading the trained model and scaler.

Git: For version control and hosting on GitHub.


**Other Details**

Dataset

Source: UCI Heart Disease Dataset (303 samples, 14 features).

Features: Includes age, sex, chest pain type, resting blood pressure, cholesterol, fasting blood sugar, resting ECG, max heart rate, exercise-induced angina, ST depression, ST slope, number of major vessels, and thalassemia.

Target: Binary classification (0 = Healthy, 1 = Not Healthy, derived from original 0-4 severity scale).


**Project Structure**

heart.csv: The UCI dataset used for training and testing.

train.py: Script for preprocessing data, training the Logistic Regression model, and saving heart_model.pkl and scaler.pkl.

app.py: Streamlit web app for user input and predictions.

heart_model.pkl: Trained Logistic Regression model.

scaler.pkl: StandardScaler for feature scaling.

README.md: This file, documenting the project.

**Installation**

Clone the Repository:

git clone https://github.com/SewminiFernando22/heart-disease-predictor.git

Replace your-username with your actual GitHub username.

Install Dependencies:
pip install pandas scikit-learn streamlit matplotlib seaborn joblib


Run the Training Script (optional, to retrain the model):
python train.py


Launch the Web App:
streamlit run app.py

Open the provided URL (e.g., http://localhost:8501) in your browser.


**Usage**

Training: Run train.py to preprocess the dataset, train the model, and generate heart_model.pkl and scaler.pkl.
Web App: Run app.py to launch the Streamlit app. Enter patient details (e.g., age, cholesterol) via sliders and dropdowns, then click "Predict My Heart Health!" to see the result, risk probability, and health tips.
Visualizations: The app displays a bar chart showing the probability of being healthy vs. at risk.

**Model Performance**

Algorithm: Logistic Regression (chosen for simplicity and ~88.5% accuracy).
Evaluation: Tested on 20% of the dataset, achieving good precision and recall for both classes.
Alternative Model: Random Forest was tested (~86.9% accuracy) but not used in the app (saved as rf_model.pkl).

**Deployment**

The Streamlit app can be deployed to Streamlit Community Cloud:
Add a requirements.txt with dependencies.
Push to GitHub.
Deploy via share.streamlit.io by selecting app.py as the main file.



**Limitations**

The model is trained on a small dataset (303 samples), which may limit generalizability.
Predictions are for educational use only and not medically certified.
Missing values in the dataset were imputed with median values, which is a simple approach.

**Future Improvements**

Add hyperparameter tuning (e.g., GridSearchCV) for better model performance.
Include more advanced models (e.g., XGBoost, neural networks).
Enhance the app with additional visualizations (e.g., feature importance).
Expand health tips with more personalized recommendations.

LicenseMIT License
ContactFor questions or contributions, open an issue on GitHub or contact [sewminifernando22456@gmail.com].
