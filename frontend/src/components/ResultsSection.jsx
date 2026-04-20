function formatPercent(value) {
  if (typeof value !== 'number' || Number.isNaN(value)) return null
  return `${Math.round(value * 100)}%`
}

export default function ResultsSection({ results, loading }) {
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
            No results yet. Fill in your courses and click <strong>Predict My Difficulty</strong>.
          </p>
        </div>
      )}

      {!loading && Array.isArray(results) && results.length === 0 && (
        <div className="emptyState">
          <p className="muted">Your backend returned an empty list.</p>
        </div>
      )}

      {!loading && Array.isArray(results) && results.length > 0 && (
        <div className="cards">
          {results.map((r, idx) => {
            const course = r?.course || `Course ${idx + 1}`
            const professor = r?.professor || '—'
            const predictedGrade = r?.predicted_grade || '—'
            const difficulty = r?.difficulty || '—'
            const confidence = formatPercent(r?.confidence)

            return (
              <article key={`${course}-${idx}`} className="card">
                <div className="cardTop">
                  <div>
                    <h3 className="cardTitle">{course}</h3>
                    <p className="muted">Professor: {professor}</p>
                  </div>
                  {confidence && <span className="pill">Confidence: {confidence}</span>}
                </div>

                <div className="cardGrid">
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

