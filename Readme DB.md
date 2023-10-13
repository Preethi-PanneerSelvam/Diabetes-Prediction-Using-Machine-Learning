
# Diabetes Prediction App with Streamlit

This is a simple web application built with Streamlit for predicting diabetes risk based on user input. Users can input information such as age, gender, smoking history, BMI, HbA1c level, hypertension, and heart disease status to get a prediction of their diabetes risk.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)


## Features

- User-friendly interface for diabetes risk prediction.
- Machine learning model based on Random Forest Classifier for accurate predictions.
- Input validation to ensure data integrity.
- Instant feedback on the prediction outcome.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or later.
- Pip package manager.
- You can install the required Python packages using the following command:

```

## Setup

1. Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/diabetes-prediction-app.git
```

2. Change your working directory to the project folder:

```bash
cd diabetes-prediction-app
```

3. Run the Streamlit app:

```bash
streamlit run diabetes_app.py
```

This will open the application in your default web browser.

## Usage

1. Launch the Streamlit app using the instructions in the "Setup" section.
2. Fill in the requested information, such as gender, age, smoking history, BMI, HbA1c level, hypertension, and heart disease status.
3. Click the "Predict" button to receive the prediction result.
4. The app will display either "Diabetic: Negative" or "Diabetic: Positive" along with a recommendation.

