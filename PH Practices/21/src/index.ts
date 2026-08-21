function useState<T>(inputValue: T): T[] {
    function callMe(newInput: T): T {
        return newInput;
    }

    return [inputValue, callMe(inputValue)];
}

console.log(useState<string>("Yamete"));
