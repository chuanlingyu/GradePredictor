export default function CourseRow({
  row,
  index,
  variant, // "past" | "future"
  gradeOptions = [],
  onUpdate,
  onRemove,
  disableRemove,
  validation,
  onValidate,
}) {
  function updateField(field, value) {
    onUpdate(row.id, { ...row, [field]: value })
  }

  return (
    <div className="row">
      <div className="field">
        <label className="label" htmlFor={`${variant}-subject-${row.id}`}>
          Subject
        </label>
        <input
          id={`${variant}-subject-${row.id}`}
          className="input"
          value={row.subject}
          onChange={(e) => updateField('subject', e.target.value)}
          onBlur={() => onValidate?.(row)}
          placeholder="CS"
          autoComplete="off"
          inputMode="text"
        />
      </div>

      <div className="field">
        <label className="label" htmlFor={`${variant}-number-${row.id}`}>
          Course #
        </label>
        <input
          id={`${variant}-number-${row.id}`}
          className="input"
          value={row.number}
          onChange={(e) => updateField('number', e.target.value)}
          onBlur={() => onValidate?.(row)}
          placeholder="225"
          autoComplete="off"
          inputMode="numeric"
        />
      </div>

      <div className="field grow">
        <label className="label" htmlFor={`${variant}-prof-${row.id}`}>
          Professor
        </label>
        <input
          id={`${variant}-prof-${row.id}`}
          className="input"
          value={row.professor}
          onChange={(e) => updateField('professor', e.target.value)}
          onBlur={() => onValidate?.(row)}
          placeholder="Last name (optional)"
          autoComplete="off"
          inputMode="text"
        />
      </div>

      {variant === 'past' && (
        <div className="field">
          <label className="label" htmlFor={`${variant}-grade-${row.id}`}>
            Grade
          </label>
          <select
            id={`${variant}-grade-${row.id}`}
            className="select"
            value={row.grade}
            onChange={(e) => updateField('grade', e.target.value)}
          >
            <option value="">Select</option>
            {gradeOptions.map((g) => (
              <option key={g} value={g}>
                {g}
              </option>
            ))}
          </select>
        </div>
      )}

      <div className="field actionsCell">
        <span className="label muted">Row</span>
        <div className="rowActions">
          <button
            type="button"
            className="danger"
            onClick={() => onRemove(row.id)}
            disabled={disableRemove}
            aria-label={`Remove row ${index + 1}`}
            title={disableRemove ? 'Keep at least one row' : 'Remove this row'}
          >
            Remove
          </button>
        </div>
      </div>

      {validation?.message && (
        <div className={`validationMessage ${validation.valid ? 'valid' : 'invalid'}`}>
          {validation.message}
        </div>
      )}
    </div>
  )
}

