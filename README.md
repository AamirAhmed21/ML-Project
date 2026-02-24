# Student Exam Performance Predictor (End-to-End ML Project)

This project predicts a student's **Math score** using demographic and academic context such as gender, parental education, lunch type, test preparation status, reading score, and writing score.

It demonstrates a complete machine learning lifecycle: **data ingestion, preprocessing, model training, model selection, artifact saving, and Flask deployment**.

---

## Problem Statement

In many education settings, identifying students who may struggle in Math is done late, after exams are already completed.

The goal of this project is to build a predictive system that estimates Math performance early using available student attributes. This helps educators and stakeholders make proactive decisions and provide targeted support.

---

## How I Solved It

I implemented an end-to-end ML pipeline with modular components:

1. **Data Ingestion**
   - Reads the dataset from `notebook/data/stud.csv`.
   - Splits data into train/test sets (`80/20`).
   - Saves artifacts to `artifacts/` (`data.csv`, `train.csv`, `test.csv`).

2. **Data Transformation**
   - Handles missing values:
     - Numeric features: median imputation
     - Categorical features: most frequent imputation
   - Encodes categorical columns with One-Hot Encoding.
   - Scales numeric and encoded features.
   - Saves preprocessing object as `artifacts/preprocessor.pkl`.

3. **Model Training & Selection**
   - Trains and tunes multiple regression models using `GridSearchCV`:
     - Random Forest
     - Decision Tree
     - Gradient Boosting
     - Linear Regression
     - KNN Regressor
     - XGBoost Regressor
     - AdaBoost Regressor
   - Selects the best model based on **test R² score**.
   - Saves best model as `artifacts/model.pkl`.

4. **Prediction Pipeline + Web App**
   - Flask form accepts student details.
   - Loads saved preprocessor and model.
   - Returns predicted Math score on the UI.

---

## Model Performance

- ✅ Achieved **88% accuracy** on the test data.
- This corresponds to approximately **0.88 R² score** for the selected best regression model.

---

## Key Features

- End-to-end production-style ML structure (`src/components`, `src/pipeline`).
- Reusable training and prediction pipelines.
- Centralized exception handling and logging.
- Web interface for non-technical users.
- Dockerfile included for containerized run.

---

## Tech Stack

- **Language:** Python
- **ML/Data:** pandas, numpy, scikit-learn, xgboost
- **Visualization/EDA:** matplotlib, seaborn (in notebooks)
- **Web Framework:** Flask
- **Packaging:** setuptools
- **Containerization:** Docker

---

## Project Structure

```
src/
	components/
		data_ingestion.py
		data_transformation.py
		model_trainer.py
	pipeline/
		predict_pipeline.py
		train_pipeline.py
	exception.py
	logger.py
	utils.py

artifacts/
	data.csv
	train.csv
	test.csv
	preprocessor.pkl
	model.pkl

templates/
	home.html

app.py / application.py
```

---

## Input Features

- `gender`
- `race_ethnicity`
- `parental_level_of_education`
- `lunch`
- `test_preparation_course`
- `reading_score`
- `writing_score`

## Target

- `math_score`

---

## How to Run Locally

### 1) Create and activate virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 2) Install dependencies

```bash
pip install -r requirement.txt
```

### 3) Train pipeline and generate artifacts

```bash
python src/components/data_ingestion.py
```

### 4) Run Flask app

```bash
python app.py
```

Open: `http://127.0.0.1:5000`

---

## Recruiter Snapshot (What this project demonstrates)

- Strong understanding of supervised regression problems.
- Practical experience with feature engineering and preprocessing pipelines.
- Model benchmarking and hyperparameter tuning with `GridSearchCV`.
- Writing modular, maintainable, production-oriented Python code.
- Building and serving ML models through a web application.
- Logging and custom exception handling for debugging and reliability.

---

## Future Improvements

- Add experiment tracking (MLflow/W&B).
- Add unit/integration tests for pipeline components.
- Add CI/CD for automated checks and deployment.
- Expose prediction API endpoints with validation.

---

## Author

**Aamir Ahmed**

- Email: `aamirahmed2132@gmail.com`
