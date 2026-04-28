import './App.css'

import { useMemo, useState } from 'react'
import Header from './components/Header.jsx'
import PastCoursesSection from './components/PastCoursesSection.jsx'
import FutureCoursesSection from './components/FutureCoursesSection.jsx'
import ProfileSection from './components/ProfileSection.jsx'
import ResultsSection from './components/ResultsSection.jsx'
import { predictCourses } from './utils/api.js'

const GRADE_OPTIONS = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F']

function newPastCourseRow() {
  return {
    id: crypto.randomUUID(),
    subject: '',
    number: '',
    professor: '',
    grade: '',
  }
}

function newFutureCourseRow() {
  return {
    id: crypto.randomUUID(),
    subject: '',
    number: '',
    professor: '',
  }
}

function newStudentProfile() {
  return {
    age: '',
    branch: '',
    study_hours_per_day: '',
    sleep_hours: '',
    screen_time_hours: '',
    attendance_percentage: '',
    stress_level: '',
  }
}

function isRowEffectivelyEmpty(row) {
  // Treat rows with all-blank inputs as "not provided" (so users can leave a starter row empty).
  return Object.values(row).every((v) => String(v ?? '').trim() === '' || v === row.id)
}

function normalizeCourseRow(row) {
  // Keep the payload predictable for your backend:
  // - subject uppercased (CS, MATH)
  // - number trimmed (225, 241)
  // - professor trimmed (allow any capitalization)
  return {
    subject: row.subject.trim().toUpperCase(),
    number: row.number.trim(),
    professor: row.professor.trim(),
  }
}

export default function App() {
  const [pastCourses, setPastCourses] = useState([newPastCourseRow()])
  const [futureCourses, setFutureCourses] = useState([newFutureCourseRow()])
  const [studentProfile, setStudentProfile] = useState(newStudentProfile())

  const [results, setResults] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const canPredict = useMemo(() => {
    const anyPast = pastCourses.some((r) => !isRowEffectivelyEmpty(r))
    const anyFuture = futureCourses.some((r) => !isRowEffectivelyEmpty(r))
    const anyProfile = Object.values(studentProfile).some((v) => String(v ?? '').trim() !== '')
    return anyPast || anyFuture || anyProfile
  }, [pastCourses, futureCourses, studentProfile])

  async function onPredict() {
    setError('')
    setResults(null)

    // Filter empty rows so your backend only receives meaningful entries.
    const cleanedPast = pastCourses
      .filter((r) => !isRowEffectivelyEmpty(r))
      .map((r) => ({
        ...normalizeCourseRow(r),
        grade: r.grade.trim(),
      }))

    const cleanedFuture = futureCourses
      .filter((r) => !isRowEffectivelyEmpty(r))
      .map((r) => normalizeCourseRow(r))

    const payload = {
      past_courses: cleanedPast,
      future_courses: cleanedFuture,
      student_profile: studentProfile,
    }

    if (!canPredict) {
      setError('Please enter at least one course or profile answer before predicting.')
      return
    }

    try {
      setLoading(true)
      const response = await predictCourses(payload)
      setResults(response)
    } catch (e) {
      setError(e?.message || 'Prediction request failed. Please try again.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="page">
      <Header />

      <main className="container">
        <div className="grid">
          <section className="panel">
            <PastCoursesSection
              value={pastCourses}
              onChange={setPastCourses}
              gradeOptions={GRADE_OPTIONS}
            />
          </section>

          <section className="panel">
            <FutureCoursesSection value={futureCourses} onChange={setFutureCourses} />
          </section>
        </div>

        <section className="panel profilePanel">
          <ProfileSection value={studentProfile} onChange={setStudentProfile} />
        </section>

        <section className="actions">
          <button className="primary" onClick={onPredict} disabled={loading || !canPredict}>
            {loading ? 'Predicting…' : 'Predict My GPA'}
          </button>

          {!canPredict && <p className="hint">Add at least one course or profile answer to enable prediction.</p>}
          {error && <p className="error" role="alert">{error}</p>}
        </section>

        <ResultsSection results={results} loading={loading} />
      </main>

      <footer className="footer">
        <p>
          Tip: You can change the backend URL via <code>VITE_PREDICT_URL</code>.
        </p>
      </footer>
    </div>
  )
}
