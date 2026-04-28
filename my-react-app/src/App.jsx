import List from "./List.jsx";


function App() {

    const foods = [
        {
            id: 1,
            name: "Rice",
            calory: 700,
        },
        {
            id: 2,
            name: "Fish",
            calory: 1400,
        },
        {
            id: 3,
            name: "Chicken",
            calory: 1200,
        },
        {
            id: 4,
            name: "Beef",
            calory: 1800,
        },
        {
            id: 5,
            name: "Mutton",
            calory: 1600,
        },
        {
            id: 6,
            name: "Water",
            calory: 350,
        },
        {
            id: 7,
            name: "Salad",
            calory: 500,
        },
    ];
    const workouts = [
        {
            id: 1,
            name: "Push Up",
            calory: 1200,
        },
        {
            id: 2,
            name: "Pull Up",
            calory: 2400,
        },
        {
            id: 3,
            name: "Bicep Curl",
            calory: 1000,
        }
    ];

    return (
        <>
            {foods.length > 0 && <List items={foods} category="Foods" />}
            {workouts.length > 0 && <List category="Workouts" />}
        </>
    );
}

export default App
