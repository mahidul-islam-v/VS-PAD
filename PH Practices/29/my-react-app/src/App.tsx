
import './App.css'
import type { CountryType } from "./type";

let countrisPromise = async():Promise<CountryType[]> => {
  let res = await fetch("openapi.programming-hero.com/api/all");
  let data = await res.json();

  return data.countries;
}

function App() {

  return (
    <>
    </>
  )
}

export default App
