import CourseRow from './CourseRow.jsx'

function newFutureCourseRow() {
  return {
    id: crypto.randomUUID(),
    subject: '',
    number: '',
    professor: '',
  }
}

export default function FutureCoursesSection({ value, onChange, validations, onValidate }) {
  function addRow() {
    onChange([...value, newFutureCourseRow()])
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
          <h2 className="sectionTitle">Future Courses</h2>
          <p className="sectionHint">Add the courses you plan to take (these will be predicted).</p>
        </div>

        <button type="button" className="secondary" onClick={addRow}>
          + Add future course
        </button>
      </div>

      <div className="rows">
        {value.map((row, idx) => (
          <CourseRow
            key={row.id}
            row={row}
            index={idx}
            variant="future"
            onUpdate={updateRow}
            onRemove={removeRow}
            disableRemove={value.length <= 1}
            validation={validations?.[row.id]}
            onValidate={onValidate}
          />
        ))}
      </div>
    </div>
  )
}

