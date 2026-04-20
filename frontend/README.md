# UIUC Course Difficulty Predictor (Frontend)

This folder contains a **React + Vite** frontend that collects:

- Past courses + letter grades
- Future courses you want to take

Then it sends a POST request to your existing Python backend endpoint and renders the predictions as cards.

## Run the frontend

From the repo root:

```bash
cd frontend
npm install
npm run dev
```

Vite will print a local URL (usually `http://localhost:5173`).

## Connect to your existing backend (no model changes)

This frontend treats your backend as a black box. It only needs **one HTTP endpoint** that accepts JSON and returns JSON.

### 1) Make sure your backend is running

Example (your choice of framework):

- Flask or FastAPI server listening on `http://localhost:5000`
- A route at `POST /predict`

### 2) Configure the backend URL (optional)

By default, the frontend calls:

- `http://localhost:5000/predict`

To change it without touching code:

- Copy `frontend/.env.example` to `frontend/.env`
- Edit `VITE_PREDICT_URL`

Example:

```bash
VITE_PREDICT_URL=http://localhost:8000/predict
```

Then restart `npm run dev`.

### 3) Request/response shapes

The frontend sends:

```json
{
  "past_courses": [
    { "subject": "CS", "number": "225", "professor": "X", "grade": "A-" }
  ],
  "future_courses": [
    { "subject": "CS", "number": "374", "professor": "Y" }
  ]
}
```

And expects something like:

```json
[
  {
    "course": "CS 374",
    "professor": "Y",
    "predicted_grade": "B+",
    "difficulty": "Hard",
    "confidence": 0.78
  }
]
```

If your backend uses different field names, update only `src/utils/api.js` (keep your backend/model untouched).

## CORS note (common when frontend/backend are on different ports)

If your frontend runs on `5173` and your backend runs on `5000`, browsers will enforce CORS.

This frontend doesn’t change your backend. If you already have CORS enabled, you’re good. If not, you’ll need to enable CORS in *your server layer* (without changing your model code).
