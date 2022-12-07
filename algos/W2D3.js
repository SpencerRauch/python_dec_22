/* 
Parens Valid
Given an str that has parenthesis in it
return whether the parenthesis are valid
*/

const str1 = "Y(3(p)p(3)r)s"; // ( () () )
const expected1 = true;

const str2 = "N(0(p)3"; // ( ( ) 
const expected2 = false;
// Explanation: not every parenthesis is closed.

const str3 = "N(0)t ) 0(k"; // ( ) ) (
const expected3 = false;
// Explanation: because the second ")" is premature: there is nothing open for it to close.


/**
 * Determines whether the parenthesis in the given string are valid.
 * Each opening parenthesis must have exactly one closing parenthesis.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the parenthesis are valid.
 */
function parensValid(str) {
    //Your code here

}

console.log(parensValid(str1)) // expected: true
console.log(parensValid(str2)) // expected: false
console.log(parensValid(str3)) // expected: false


/* 
Braces Valid
Given a string sequence of parentheses, braces and brackets, determine whether it is valid. 
*/

const strA = "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!";// ( {} [ ({}) ] ) [{}]!
const expectedA = true;

const strB = "D(i{a}l[ t]o)n{e"; // "({} []) {"
const expectedB = false;

const strC = "A(1)s[O (n]0{t) 0}k"; // () [(] {) }"
const expectedC = false;

/**
 * Determines whether the string's braces, brackets, and parenthesis are valid
 * based on the order and amount of opening and closing pairs.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the given strings braces are valid.
 */
function bracesValid(str) {
    //Your code here
}
console.log(bracesValid(strA)) // expected: true
console.log(bracesValid(strB)) // expected: false
console.log(bracesValid(strC)) // expected: false




function parensValid(str) {
    let unmatchedOpens = 0;
    for (let char of str) {
        if (char === "(") unmatchedOpens++
        if (char === ")") unmatchedOpens--
        if (unmatchedOpens < 0) return false
    }
    return unmatchedOpens == 0;
}






function bracesValid(str) {
    const stack = [];
    const isOpen = { "(": true, "{": true, "[": true }
    const closesToOpens = { ")": "(", "}": "{", "]": "[" };

    for (let char of str) {
        if (isOpen[char]) {
            stack.push(char);
        } else if (closesToOpens[char]) {
            if (closesToOpens[char] === stack[stack.length - 1]) {
                stack.pop();
            } else {
                return false;
            }
        }
    }
    return stack.length === 0;
}





//from Aarti Chandrasekar

const parenMap = new Map([["{", "}"],
["(", ")"],
["[", "]"]]);

function bracesValid(str) {
    // const strB = "D(i{a}l[ t]o)n{e";
    var len = str.length;
    var parenList = [];
    // For each character in the string, check if it is one of the valid OPEN parenthesis
    // and add the OPEN parenthesis to a list. When we encounter a CLOSE parenthesis, 
    // pop the last OPEN parenthesis from the parenthesis List.
    // Check if it is the CLOSE parenthesis we are expecting for the OPEN parenthesis 
    // if ( then we are expecting ), { then we are expecting }, and so on
    // if it is not what is expected return false
    for (var i = 0; i < len; i++) {
        // console.log(parenList);
        if (parenMap.has(str[i])) { // if a valid OPEN parenthesis
            parenList.push(str[i]);
        } else if (contains(parenMap.values(), str[i])) { // if a valid CLOSE parenthesis
            // if not a matching closing bracket
            // For example, if the last 
            if (parenMap.get(parenList.pop()) != str[i]) {
                return false;
            }
        }
    }
    if (parenList.length > 0) {
        return false;
    }
    return true;
}

function contains(itr, letter) {
    for (var val of itr) {
        if (val == letter) {
            return true;
        }
    }
    return false;
}