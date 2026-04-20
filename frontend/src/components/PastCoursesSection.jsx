import CourseRow from './CourseRow.jsx'

function newPastCourseRow() {
  return {
    id: crypto.randomUUID(),
    subject: '',
    number: '',
    professor: '',
    grade: '',
  }
}

export default function PastCoursesSection({ value, onChange, gradeOptions }) {
  function addRow() {
    onChange([...value, newPastCourseRow()])
  }

  function updateRow(id, nextRow) {
    onChange(value.map((r) => (r.id === id ? nextRow : r)))
  }

  function removeRow(id) {
    if (value.length <= 1) return
    onChange(value.filter((r) => r.id !== id))
  }

  return (
    <div>
      <div className="sectionHeader">
        <div>
          <h2 className="sectionTitle">Past Courses</h2>
          <p className="sectionHint">Add as many past courses as you can (more history usually improves predictions).</p>
        </div>

        <button type="button" className="secondary" onClick={addRow}>
          + Add past course
        </button>
      </div>

      <div className="rows">
        {value.map((row, idx) => (
          <CourseRow
            key={row.id}
            row={row}
            index={idx}
            variant="past"
            gradeOptions={gradeOptions}
            onUpdate={updateRow}
            onRemove={removeRow}
            disableRemove={value.length <= 1}
          />
        ))}
      </div>
    </div>
  )
}

