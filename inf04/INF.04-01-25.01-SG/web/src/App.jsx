import { useState } from "react"

import "bootstrap/dist/css/bootstrap.css"
import "./App.css";

function App() {

  const CATEGORY_FLOWERS = 1;
  const CATEGORY_PETS = 2;
  const CATEGORY_CARS = 3;

  const [images, setImages] = useState(
    [
      {id: 0, alt: "Mak", filename: "obraz1.jpg", category:1, downloads: 35},
      {id: 1, alt:"Bukiet", filename: "obraz2.jpg", category: 1, downloads: 43},
      {id: 2, alt:"Dalmatyńczyk", filename: "obraz3.jpg", category:2, downloads: 2},
      {id: 3, alt:"Świnka morska", filename: "obraz4.jpg", category:2, downloads: 53},
      {id: 4, alt:"Rotwailer", filename: "obraz5.jpg", category:2, downloads: 43},
      {id: 5, alt:"Audi", filename: "obraz6.jpg", category:3, downloads: 11},
      {id: 6, alt:"kotki", filename: "obraz7.jpg", category:2, downloads: 22},
      {id: 7, alt:"Róża", filename: "obraz8.jpg", category:1, downloads: 33},
      {id: 8, alt:"Świnka morska", filename: "obraz9.jpg", category:2, downloads: 123},
      {id: 9, alt:"Foksterier", filename: "obraz10.jpg", category:2, downloads: 22},
      {id: 10, alt:"Szczeniak", filename: "obraz11.jpg", category:2, downloads: 12},
      {id: 11, alt:"Garbus", filename: "obraz12.jpg", category:3, downloads: 321}
    ]
  );

  const [enabledCategories, setEnabledCategories] = useState([CATEGORY_FLOWERS, CATEGORY_PETS, CATEGORY_CARS]);
  const [renderCount, setRenderCount] = useState(0);

  function setCategoryEnabled(category, state) {
    const idx = enabledCategories.indexOf(category);

    if(state && idx == -1) {
      enabledCategories.push(category);
    }

    if(!state && idx != -1) {
      enabledCategories.splice(idx, 1);
    }

    setEnabledCategories(enabledCategories);
    forceRenderImages();
  }

  function download(imageIdx) {
    images[imageIdx].downloads += 1;
    setImages(images);
    forceRenderImages();
  }

  // React doesn't detect changes on objects properly
  function forceRenderImages() {
    setRenderCount(renderCount + 1);
  }

  return (
    <div>
      <h1>Kategorie zdjęć</h1>

      <div id="filters">
    
        <div className="form-check-inline form-switch">
          <input 
            className="form-check-input" 
            type="checkbox" 
            id="chk-flowers" 
            defaultChecked
            onChange={(e) => setCategoryEnabled(CATEGORY_FLOWERS, e.target.checked)}
          />
          <label className="form-check-label" htmlFor="chk-flowers">Kwiaty</label>
        </div>

        <div className="form-check-inline form-switch">
          <input 
            className="form-check-input" 
            type="checkbox" 
            id="chk-pets" 
            defaultChecked
            onChange={(e) => setCategoryEnabled(CATEGORY_PETS, e.target.checked)}
          />
          <label className="form-check-label" htmlFor="chk-pets">Zwierzęta</label>
        </div>

        <div className="form-check-inline form-switch">
          <input 
            className="form-check-input" 
            type="checkbox" 
            id="chk-cars" 
            defaultChecked
            onChange={(e) => setCategoryEnabled(CATEGORY_CARS, e.target.checked)}
          />
          <label className="form-check-label" htmlFor="chk-cars">Samochody</label>
        </div>
      </div>

      <div id="images">
        {
          images.map((v, i) => 
            enabledCategories.includes(v.category) ?
              <div key={i} data-force-render={renderCount} className="img-block">
                <img src={"assets/" + v.filename}/>
                <h4>Pobrań: {v.downloads}</h4>
                <button onClick={() => download(i)} className="btn btn-success">Pobierz</button>
              </div>
            : undefined
          )
        }
      </div>
    </div>
  )
}

export default App
