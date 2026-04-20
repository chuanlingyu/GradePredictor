const DEFAULT_PREDICT_URL = 'http://localhost:5000/predict'

function getPredictUrl() {
  // Vite exposes env vars that start with VITE_ at build time.
  // You can set this in `frontend/.env` as:
  // VITE_PREDICT_URL=http://localhost:5000/predict
  return import.meta.env.VITE_PREDICT_URL || DEFAULT_PREDICT_URL
}

async function readErrorMessage(response) {
  // Backend might return JSON or plain text on errors; handle both.
  const contentType = response.headers.get('content-type') || ''
  try {
    if (contentType.includes('application/json')) {
      const data = await response.json()
      return data?.error || data?.message || JSON.stringify(data)
    }
    return await response.text()
  } catch {
    return ''
  }
}

export async function predictCourses(payload) {
  const url = getPredictUrl()

  const response = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  })

  if (!response.ok) {
    const message = await readErrorMessage(response)
    throw new Error(message || `Request failed (${response.status})`)
  }

  // Expected backend response shape (example):
  // [
  //   { course, professor, predicted_grade, difficulty, confidence }
  // ]
  return await response.json()
}

