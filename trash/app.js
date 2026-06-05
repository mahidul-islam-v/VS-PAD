console.log("connected!!");
// console.log(document);

const url = "https://dummyjson.com/todos";

const renderTodos = (todos) => {
    const container = document.getElementById("todos");
    container.innerHTML = "";

    todos.forEach((todo) => {
        const div = document.createElement("div");
        div.className =
            "bg-white p-4 pl-5 pr-5 rounded shadow flex justify-between";

        div.innerHTML = `<span>${todo.todo} <span class="text-sm text-gray-500">${todo.userId}</span></span> <span class="${todo.completed ? "text-green-600" : "text-red-600"}">${todo.completed ? "Completed" : "Not Completed"}</span>`;

        container.appendChild(div);
    });
};

const getTodoList = () => {
    fetch(url)
        .then((res) => res.json())
        .then((data) => {
            renderTodos(data.todos);
        })
        .catch((error) => console.log(error));
};

const getTodosAsync = async () => {
    try {
        const result = await fetch(url);
        const data = await result.json();
        renderTodos(data.todos);
    } catch (error) {
        console.log(error);
    }
};

const createTodo = async () => {
    const response = await fetch("https://dummyjson.com/todos/add", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            todo: "Use DummyJSON in the project",
            completed: false,
            userId: 5,
        }),
    });
    const newTodo = await response.json();
    renderTodos([newTodo]);
};

const updateTodoPut = async () => {
    const response = await fetch("https://dummyjson.com/todos/1", {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            completed: false,
        }),
    });
    const newTodo = await response.json();
    renderTodos([newTodo]);
};

const deleteTodo = async () => {
    const response = await fetch("https://dummyjson.com/todos/1", {
        method: "DELETE",
    });
    const data = await response.json();
    renderTodos([data]);
};

const el = document.getElementById("el");

el.onclick = () => alert(1);
