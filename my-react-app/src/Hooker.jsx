import { useState } from "react"

function Hooker(props) {
    const [name, changeName] = useState("Guest");
    const updateName = () => changeName(props.username);

    const [age, changeAge] = useState(0);
    const decrementAge = () => age > 0 && changeAge(age-1);
    const incrementAge = () => changeAge(age + 1);
    
    const [es, toggleEs] = useState(false);
    const toggleEmploymentStatus = () => toggleEs(!es)

    return (
        <>
            <div> Name: {name} </div>
            <button onClick={updateName}>setName</button>

            <div> Age: {age} </div>
            <button onClick={decrementAge}>decrease</button>
            <button onClick={incrementAge}>increase</button>

            <div> Employed: {es ? "Yes" : "No"} </div>
            <button onClick={toggleEmploymentStatus}>Toggle Status</button>
        </>
    );
}

export default Hooker