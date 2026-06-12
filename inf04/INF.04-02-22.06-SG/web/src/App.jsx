import { useState } from "react";

import "bootstrap/dist/css/bootstrap.css";
//import "./App.css";

function App() {
  const [fullName, setFullName] = useState("");
  const [courseId, setCourseId] = useState(0);

  const COURSE_NAMES = [
    "Programowanie w C#",
    "Angular dla początkujących",
    "Kurs Django"
  ];

  function submit(e) {
    e.preventDefault();

    console.log(fullName);

    const courseIdx = courseId - 1;

    if(isNaN(courseIdx) || courseIdx < 0 || courseIdx >= COURSE_NAMES.length) {
      console.log("Nieprawidłowy numer kursu");
      return;
    }

    console.log(COURSE_NAMES[courseIdx]);
  }

  return (
    <div id="main">
      <h2>Liczba kursów: {COURSE_NAMES.length}</h2>

      <ol>
        {COURSE_NAMES.map((v) => <li key={v}>{v}</li>)}
      </ol>

      <form onSubmit={submit}>
        <div className="form-group">
          <label htmlFor="inp-full-name">Imię i nazwisko:</label>
          <input type="text" className="form-control bg-primary-subtle border-secondary-subtle" id="inp-full-name" onChange={(e) => setFullName(e.target.value)} />
        </div>
        <br/>

        <div className="form-group">
          <label htmlFor="inp-course-id">Numer kursu:</label>
          <input type="number" className="form-control" id="inp-course-id" onChange={(e) => setCourseId(parseInt(e.target.value))} />
        </div>
        <br/>

        <input type="submit" className="btn btn-primary" value="Zapisz do kursu"/>
      </form>
    </div>
  )
}

export default App
