
import { Suspense } from 'react';
import './App.css'
import Countries from './Components/Countries';
import type { CountryType } from "./type";

let countrisPromise = async():Promise<CountryType[]> => {
  let res = await fetch("https://openapi.programming-hero.com/api/all");
  let data = await res.json();

  return data.countries;
}

function App() {

  return (
    <>
      <h1>Hello Nadir World...</h1>
      <Suspense fallback={<div>Nadir Loading...</div>}>
        <Countries countriesPromise={countrisPromise()}>

        </Countries>
      </Suspense>
    </>
  )
}

export default App
