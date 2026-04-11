# GradePredictor
The repository for the GradePredictor guided project for the UIUC SIGAIDA club. The ultimate goal is to create a class schedule generator for students in UIUC.
1. We will take a student's past course grades and use them to estimate their academic strengths overall and by subject. 
2. Then, when the student enters the classes they want to take, we compare their subject-level performance to the historical difficulty of those classes in our database. 
3. This lets us predict how difficult each class may be for that specific student, rather than just saying whether the class is hard in general.


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
│   │   ├── train_model.py
│   │   └── predict.py
│   │
│   └── utils/
│       └── helpers.py
│
├── outputs/
│   ├── models/
│   │   └── grade_model.pkl
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
- `train_model.py`  
  Trains the grade prediction model.

- `predict.py`  
  Uses the trained model to predict grades for a course/professor.

---

### outputs/
- `outputs/models/`  
  Stores trained machine learning models.

- `outputs/plots/`  
  Stores generated visualizations and graphs.
