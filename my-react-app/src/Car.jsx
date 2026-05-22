import { useState } from "react";

export default function Car(props) {
    const noMargin = `margin:"none"`;
    const [cars, setCars] = useState([
        {
            year: 2024,
            make: "Tesla",
            model: "Roadster",
        },
    ]);

    function handleAddCar() {
        const year = document.getElementById("year").value;
        const make = document.getElementById("make").value;
        const model = document.getElementById("model").value;

        setCars((cs) => [
            ...cs,
            {
                year: year,
                make: make,
                model: model,
            },
        ]);
    }

    return (
        <>
            <h1>Cars</h1>
            <ul>
                {cars.map((car, index) => (
                    <li key={index}>
                        {car.year} {car.make} {car.model}
                    </li>
                ))}
            </ul>
            <div>
                <input
                    id="year"
                    type="number"
                    placeholder="Year"
                    className="ip"
                />
                <br />
                <input
                    id="make"
                    type="text"
                    placeholder="Make"
                    className="ip"
                />
                <br />
                <input
                    id="model"
                    type="text"
                    placeholder="Model"
                    className="ip"
                />
                <br />
                <button
                    className="ip"
                    onClick={handleAddCar}
                    style={{ cursor: "pointer" }}
                >
                    Add Car
                </button>
            </div>
        </>
    );
}
