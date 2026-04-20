export default function Header() {
  return (
    <header className="header">
      <div className="container">
        <div className="brand">
          <div className="logo" aria-hidden="true">
            UIUC
          </div>
          <div>
            <h1 className="title">UIUC Course Difficulty Predictor</h1>
            <p className="subtitle">
              Enter your past courses and grades, then the courses you plan to take next. We’ll send your info to your
              existing model and display predicted difficulty and grade.
            </p>
          </div>
        </div>
      </div>
    </header>
  )
}

