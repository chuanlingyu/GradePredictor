# grade-predictor
The repository for the GradePredictor guided project for the UIUC SIGAIDA club. The ultimate goal is to create a class schedule generator for students in UIUC.
1. We will take a student's past course grades and use them to estimate their academic strengths overall and by subject. 
2. Then, when the student enters the classes they want to take, we compare their subject-level performance to the historical difficulty of those classes in our database. 
3. This lets us predict how difficult each class may be for that specific student, rather than just saying whether the class is hard in general.

## To Run the Frontend
1. In the terminal, at the repo root GradePredictor/, type in:
    npm run frontend:install
  To download the dependencies
2. To run the website, do
    npm run dev
  In the terminal. However, for the real functions to work, need to run the backend first using npm run backend. For detail check below.

## To Run the Backend
1. Install the Python dependencies:
    pip install -r requirements.txt
2. Train or refresh the model artifacts:
    python src/models/class_gpa.py
    python src/models/student_gpa.py
3. Start the Flask prediction API:
    npm run backend

The frontend posts to `http://localhost:5000/predict` by default.

## Project Structure

```
uiuc-schedule-ai/
│
├── data/
│   ├── raw/
│   │   └── grades.csv
│   ├── processed/
│   │   └── cleaned_grades.csv
│
├── notebooks/
│   └── exploration.ipynb
│
├── src/
│   ├── data_processing/
│   │   └── clean_data.py
│   │
│   ├── features/
│   │   └── build_features.py
│   │
│   ├── models/
│   │   ├── class_gpa.py
│   │   ├── student_gpa.py
│   │   ├── schedule_pipeline.py
│   │   └── predict.py
│   │
│   ├── api/
│   │   └── app.py
│   │
│   └── utils/
│       └── helpers.py
│
├── outputs/
│   ├── models/
│   │   ├── class_gpa_model.joblib
│   │   └── student_gpa_model.joblib
│   └── plots/
│
├── requirements.txt
├── README.md
└── main.py
```

## File Description

### Root
- 'main.py':
  Entry point of the project
- 'requirements.txt':
  List Python dependencies required to run the project

### data/
- 'raw/uiuc-gpa-dataset.csv/':
  Stores the original dataset. NEVER MODIFIED
- 'processed/cleaned_grades.csv':
  Stores the cleaned and transformed dataset

### notebooks/
- `exploration.ipynb`  
  A Jupyter Notebook that is used for exploratory data analysis and understanding the dataset.


### src/data_processing/
- `clean_data.py`  
  Cleans raw grade data and outputs processed datasets.

---

### src/features/
- `build_features.py`  
  Converts cleaned data into numerical features for model training.

---

### src/models/
- `class_gpa.py`  
  Trains the class GPA prediction model.

- `student_gpa.py`  
  Trains the student GPA prediction model.

- `predict.py`  
  Uses the trained model to predict grades for a course/professor.

- `schedule_pipeline.py`
  Combines past-course adjustment, future class GPA, and student profile GPA into one final projected GPA.

---

### src/api/
- `app.py`
  Flask API with the `/predict` endpoint used by the frontend.

---

### outputs/
- `outputs/models/`  
  Stores trained machine learning models.

- `outputs/plots/`  
  Stores generated visualizations and graphs.
