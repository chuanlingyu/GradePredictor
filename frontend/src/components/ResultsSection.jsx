function formatGpa(value) {
  if (typeof value !== 'number' || Number.isNaN(value)) return '—'
  return value.toFixed(2)
}

function SummaryMetric({ label, value, description }) {
  return (
    <div className="metric summaryMetric">
      <div className="metricLabel">{label}</div>
      <div className="metricValue">{value}</div>
      <p className="metricDescription">{description}</p>
    </div>
  )
}

export default function ResultsSection({ results, loading }) {
  const courseResults = Array.isArray(results) ? results : results?.course_predictions

  return (
    <section className="results">
      <div className="sectionHeader">
        <div>
          <h2 className="sectionTitle">Results</h2>
          <p className="sectionHint">Predictions returned by your backend will appear here.</p>
        </div>
      </div>

      {loading && (
        <div className="emptyState">
          <div className="spinner" aria-hidden="true" />
          <p>Waiting for your model…</p>
        </div>
      )}

      {!loading && !results && (
        <div className="emptyState">
          <p className="muted">
            No results yet. Fill in your courses and profile, then click <strong>Predict My GPA</strong>.
          </p>
        </div>
      )}

      {!loading && courseResults && courseResults.length === 0 && (
        <div className="emptyState">
          <p className="muted">Your backend returned an empty list.</p>
        </div>
      )}

      {!loading && results && !Array.isArray(results) && (
        <div className="summaryGrid singleSummary">
          <SummaryMetric
            label="Final projected GPA"
            value={formatGpa(results.final_projected_gpa)}
            description="Your personalized projected GPA based on future classes, past performance, and profile."
          />
        </div>
      )}

      {!loading && results?.profile_error && (
        <p className="error" role="alert">{results.profile_error}</p>
      )}

      {!loading && results?.skipped_past_courses?.length > 0 && (
        <div className="notice">
          <strong>Skipped past courses:</strong>{' '}
          {results.skipped_past_courses.map((course) => `${course.course} (${course.reason})`).join(', ')}
        </div>
      )}

      {!loading && courseResults && courseResults.length > 0 && (
        <div className="cards">
          {courseResults.map((r, idx) => {
            const course = r?.course || `Course ${idx + 1}`
            const professor = r?.professor || '—'
            const predictedGrade = r?.predicted_grade || '—'
            const difficulty = r?.difficulty || '—'
            const rowError = r?.error

            return (
              <article key={`${course}-${idx}`} className="card">
                <div className="cardTop">
                  <div>
                    <h3 className="cardTitle">{course}</h3>
                    <p className="muted">Professor: {professor}</p>
                  </div>
                </div>

                {rowError && <p className="error courseError">{rowError}</p>}

                <div className="cardGrid">
                  <div className="metric">
                    <div className="metricLabel">Adjusted GPA</div>
                    <div className="metricValue">{formatGpa(r?.adjusted_gpa)}</div>
                  </div>
                  <div className="metric">
                    <div className="metricLabel">Predicted grade</div>
                    <div className="metricValue">{predictedGrade}</div>
                  </div>
                  <div className="metric">
                    <div className="metricLabel">Difficulty</div>
                    <div className="metricValue">{difficulty}</div>
                  </div>
                </div>
              </article>
            )
          })}
        </div>
      )}
    </section>
  )
}

