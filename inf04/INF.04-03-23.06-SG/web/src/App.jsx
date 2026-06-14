
import "bootstrap/dist/css/bootstrap.css"
import "./App.css";
import { useState } from "react";

function App() {
  const [title, setTitle] = useState("");
  const [typeId, setTypeId] = useState("0");
  
  function submit(e) {
    e.preventDefault();

    console.log(`tytul: ${title}; rodzaj: ${typeId}`);
  }

  return (
    <form onSubmit={submit}>
      <div className="form-group">
        <label htmlFor="inp-title">Tytuł filmu</label>
        <input type="text" id="inp-title" className="form-control" onChange={(e) => setTitle(e.target.value)} />
      </div>
      <br/>

      <div className="form-group">
        <label htmlFor="sel-type">Rodzaj</label>
        <select className="form-control" onChange={(e) => setTypeId(e.target.value)}>
          <option value="0"></option>
          <option value="1">Komedia</option>
          <option value="2">Obyczajowy</option>
          <option value="3">Sensacyjny</option>
          <option value="4">Horror</option>
        </select>
      </div>
      <br/>

      <input type="submit" value="Dodaj" className="btn btn-primary"/>
    </form>
  )
}

export default App;
