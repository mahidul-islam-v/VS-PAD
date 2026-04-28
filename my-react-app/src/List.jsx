
function List({ items = [], category = "category name"}) {
    // const items = items
    const cat = category

    items.sort((a, b) => a.calory - b.calory)

    const listItems = items.map((item) => (
        <li key={item.id}> 
            <div style={{ display: "flex", justifyContent: "space-between" }}>
                {item.name}: <b>{item.calory}</b>
            </div>
        </li>
    ));

    return (
        <>
            <h2>{cat}</h2>
            <ol>{listItems}</ol>
        </>
    );
}

export default List