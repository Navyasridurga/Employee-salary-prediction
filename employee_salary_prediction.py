# -*- coding: utf-8 -*-
"""Employee_salary_prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/github/Navyasridurga/Employee-salary-prediction/blob/main/Employee_salary_prediction.ipynb
"""

data.shape

import pandas as pd

# Load the CSV file
data = pd.read_csv("/content/adult 3.csv")

# Display the first few rows
data.head()

data.head()

data.tail()

data.isna()

data.isna().sum()

data.occupation.value_counts()

data.education.value_counts()

data.workclass.value_counts()

data.gender.value_counts()

print(data['marital-status'].value_counts())

print(data['education'].value_counts())

print(data['workclass'].value_counts())

data.occupation.replace({'?': 'others'}, inplace=True)
print(data['occupation'])  # or just data.head()

print(data.occupation.value_counts())

data

data.workclass.replace({'?':'Not Listed'},inplace=True)

print(data['workclass'].value_counts())

data=data[data['workclass']!='Without-pay']
data=data[data['workclass']!='Never-worked']

print(data['workclass'].value_counts())

data.shape

data=data[data['education']!='5th-6th']
data=data[data['education']!='1st-4th']
data=data[data['education']!= 'Preschool']

"""# New Section"""

print(data['education'].value_counts())

data

data.shape

data.drop(columns=['education'],inplace=True)

data

import matplotlib.pyplot as plt
plt.boxplot(data['age'])
plt.show()

from sklearn.preprocessing import LabelEncoder
encoder=LabelEncoder()
data['workclass'] = encoder.fit_transform(data['workclass'])
data['martial-status']=encoder.fit_transform(data['marital-status'])
data['occupation']=encoder.fit_transform(data['occupation'])
data['relationship']=encoder.fit_transform(data['relationship'])
data['race']=encoder.fit_transform(data['race'])
data['gender']=encoder.fit_transform(data['gender'])
data['native-country']=encoder.fit_transform(data['native-country'])
data

x=data.drop(columns=['income'])
y=data['income']

x

y

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
# Step 1: Convert categorical columns to numbers
x = pd.get_dummies(x)

# Step 2: Apply MinMaxScaler
scaler = MinMaxScaler()
x = pd.DataFrame(scaler.fit_transform(x), columns=x.columns)

x = scaler.fit_transform(x)
x

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=23,stratify=y)

xtrain

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier()
knn.fit(xtrain,ytrain)
predict = knn.predict(xtest)
predict

from sklearn.metrics import accuracy_score
accuracy_score(ytest,predict)

from sklearn.neural_network import MLPClassifier  # Correct class name
clf = MLPClassifier(solver='adam', hidden_layer_sizes=(5, 2), random_state=2, max_iter=2000)  # Corrected parameter name
clf.fit(xtrain, ytrain)
predict2 = clf.predict(xtest)
predict2

from sklearn.metrics import accuracy_score
accuracy_score(ytest,predict2)

from sklearn.datasets import load_iris
import pandas as pd

# Load sample dataset
data = load_iris()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define models
models = {
    "LogisticRegression": LogisticRegression(),
    "RandomForest": RandomForestClassifier(),
    "KNN": KNeighborsClassifier(),
    "SVM": SVC(),
    "GradientBoosting": GradientBoostingClassifier()
}

# Store results
results = {}

# Loop through models
for name, model in models.items():
    pipe = Pipeline([
        ('scaler', StandardScaler()),
        ('model', model)
    ])
    pipe.fit(X_train, y_train)
    y_pred = pipe.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    results[name] = acc
    print(f"{name} Accuracy: {acc:.4f}")
    print(classification_report(y_test, y_pred))

import matplotlib.pyplot as plt
plt.bar(results.keys(),results.values(),color='skyblue')
plt.xlabel('Models')
plt.ylabel('Accuracy')
plt.title('Model Accuracy Comparison')
plt.show()

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import joblib

# Step 1: Load dataset
df = pd.read_csv("/content/adult 3.csv")

# Step 2: Clean dataset
# Replace '?' with 'others' in all string columns
df.replace("?", "others", inplace=True)

# Step 3: Encode categorical columns
label_encoders = {}
for column in df.select_dtypes(include='object').columns:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoders[column] = le  # store for possible use later (e.g., inverse transform)

# Step 4: Define features and target
# ✅ Make sure the target column is correct. Use df.columns to check
x = df.drop('income', axis=1)  # Replace 'income' if your target column has another name
y = df['income']

# Step 5: Train-test split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Step 6: Define classification models
models = {
    "LogisticRegression": LogisticRegression(max_iter=1000),
    "RandomForest": RandomForestClassifier(),
    "KNN": KNeighborsClassifier(),
    "SVM": SVC(),
    "GradientBoosting": GradientBoostingClassifier()
}

# Step 7: Train and evaluate models
results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    results[name] = acc
    print(f"{name}: {acc:.4f}")

# Step 8: Save the best model
best_model_name = max(results, key=results.get)
best_model = models[best_model_name]
print(f"\n✅ Best model: {best_model_name} with accuracy {results[best_model_name]:.4f}")

# Save the model to disk
joblib.dump(best_model, "best_model.pkl")
print("✅ Saved best model as best_model.pkl")

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import streamlit as st
# import pandas as pd
# import joblib
# 
# # Load the trained model
# model = joblib.load("best_model.pkl")
# 
# st.set_page_config(page_title="Employee Salary Classification", page_icon="💼", layout="centered")
# 
# st.title("💼 Employee Salary Classification App")
# st.markdown("Predict whether an employee earns >50K or ≤50K based on input features.")
# 
# # Sidebar inputs (these must match your training feature columns)
# st.sidebar.header("Input Employee Details")
# 
# # ✨ Replace these fields with your dataset's actual input columns
# age = st.sidebar.slider("Age", 18, 65, 30)
# education = st.sidebar.selectbox("Education Level", [
#     "Bachelors", "Masters", "PhD", "HS-grad", "Assoc", "Some-college"
# ])
# occupation = st.sidebar.selectbox("Job Role", [
#     "Tech-support", "Craft-repair", "Other-service", "Sales",
#     "Exec-managerial", "Prof-specialty", "Handlers-cleaners", "Machine-op-inspct",
#     "Adm-clerical", "Farming-fishing", "Transport-moving", "Priv-house-serv",
#     "Protective-serv", "Armed-Forces"
# ])
# hours_per_week = st.sidebar.slider("Hours per week", 1, 80, 40)
# experience = st.sidebar.slider("Years of Experience", 0, 40, 5)
# 
# # Build input DataFrame (⚠️ must match preprocessing of your training data)
# input_df = pd.DataFrame({
#     'age': [age],
#     'education': [education],
#     'occupation': [occupation],
#     'hours-per-week': [hours_per_week],
#     'experience': [experience]
# })
# 
# st.write("### 🔎 Input Data")
# st.write(input_df)
# 
# # Predict button
# if st.button("Predict Salary Class"):
#     prediction = model.predict(input_df)
#     st.success(f"✅ Prediction: {prediction[0]}")
# 
# # Batch prediction
# st.markdown("---")
# st.markdown("#### 📂 Batch Prediction")
# uploaded_file = st.file_uploader("Upload a CSV file for batch prediction", type="csv")
# 
# if uploaded_file is not None:
#     batch_data = pd.read_csv(uploaded_file)
#     st.write("Uploaded data preview:", batch_data.head())
#     batch_preds = model.predict(batch_data)
#     batch_data['PredictedClass'] = batch_preds
#     st.write("✅ Predictions:")
#     st.write(batch_data.head())
#     csv = batch_data.to_csv(index=False).encode('utf-8')
#     st.download_button("Download Predictions CSV", csv, file_name='predicted_classes.csv', mime='text/csv')
# 
#