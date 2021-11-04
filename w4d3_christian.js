function bracesValid(str) {
    const stack = [];//create array to be used as a stack (only add to the end and remove from the end)
    const braces = {//create object mapping open brackets to their closing counterparts
        "(": ")",
        "{": "}",
        "[": "]"
    };
    for (let char of str) {//loop over each character in the string
        if (char in braces) {//if char is an open bracket
            stack.push(braces[char]);//push the corresponding close bracket into the stack
        } else if (char === stack[stack.length - 1]) {//if char matches the last thing in the stack (a close bracket)
            stack.pop();//remove it from the stack
        } else if (Object.values(braces).includes(char)) {//if char is a close bracket but not the expected close bracket
            return false//return early
        }
    }
    return stack.length === 0;//if stack is empty then all brackets are paired properly so return true otherwise returns false
}
console.log(bracesValid("W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!"))
console.log(bracesValid("A(1)s[O (n]0{t) 0}k"))