import { useState } from "react"

function Hooker(props) {
    const [name, changeName] = useState("Guest")

    const updateName = () => changeName(props.username)

    return (
        <>
            <div> Name: {name} </div>
            <button onClick={updateName}>
                setName
            </button>
        </>
    );
}

export default Hooker