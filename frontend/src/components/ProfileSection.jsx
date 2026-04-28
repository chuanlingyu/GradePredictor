const BRANCH_OPTIONS = ['CSE', 'Civil', 'ECE', 'Electrical', 'IT', 'Mechanical']

export default function ProfileSection({ value, onChange }) {
  function updateField(field, nextValue) {
    onChange({ ...value, [field]: nextValue })
  }

  return (
    <div>
      <div className="sectionHeader">
        <div>
          <h2 className="sectionTitle">Student Profile</h2>
          <p className="sectionHint">These answers help blend class difficulty with your study habits.</p>
        </div>
      </div>

      <div className="profileGrid">
        <div className="field">
          <label className="label" htmlFor="profile-age">Age</label>
          <input
            id="profile-age"
            className="input"
            type="number"
            min="0"
            value={value.age}
            onChange={(e) => updateField('age', e.target.value)}
            placeholder="20"
          />
        </div>

        <div className="field">
          <label className="label" htmlFor="profile-branch">Engineering Branch</label>
          <select
            id="profile-branch"
            className="select"
            value={value.branch}
            onChange={(e) => updateField('branch', e.target.value)}
          >
            <option value="">Optional</option>
            {BRANCH_OPTIONS.map((branch) => (
              <option key={branch} value={branch}>
                {branch}
              </option>
            ))}
          </select>
        </div>

        <div className="field">
          <label className="label" htmlFor="profile-study">Study hours / day</label>
          <input
            id="profile-study"
            className="input"
            type="number"
            min="0"
            step="0.25"
            value={value.study_hours_per_day}
            onChange={(e) => updateField('study_hours_per_day', e.target.value)}
            placeholder="3"
          />
        </div>

        <div className="field">
          <label className="label" htmlFor="profile-sleep">Sleep hours / night</label>
          <input
            id="profile-sleep"
            className="input"
            type="number"
            min="0"
            step="0.25"
            value={value.sleep_hours}
            onChange={(e) => updateField('sleep_hours', e.target.value)}
            placeholder="7"
          />
        </div>

        <div className="field">
          <label className="label" htmlFor="profile-screen">Screen time / day</label>
          <input
            id="profile-screen"
            className="input"
            type="number"
            min="0"
            step="0.25"
            value={value.screen_time_hours}
            onChange={(e) => updateField('screen_time_hours', e.target.value)}
            placeholder="5"
          />
        </div>

        <div className="field">
          <label className="label" htmlFor="profile-attendance">Attendance %</label>
          <input
            id="profile-attendance"
            className="input"
            type="number"
            min="0"
            max="100"
            value={value.attendance_percentage}
            onChange={(e) => updateField('attendance_percentage', e.target.value)}
            placeholder="90"
          />
        </div>

        <div className="field">
          <label className="label" htmlFor="profile-stress">Stress level</label>
          <input
            id="profile-stress"
            className="input"
            type="number"
            min="1"
            max="10"
            value={value.stress_level}
            onChange={(e) => updateField('stress_level', e.target.value)}
            placeholder="6"
          />
        </div>
      </div>
    </div>
  )
}
