
/* 
  Binary String Expansion
  You are given a STRING containing chars "0", "1", and "?"
  For every "?" character, either "0" or "1" can be substituted.
  Write a recursive function to return array of all valid strings with "?" chars expanded to "0" or "1". 
*/

const str1 = "1?0?";
const expected1 = ["1000", "1001", "1100", "1101"];
// output list order does not matter

const str2 = "???"
const expected2 = ['000', '001', '010', '011', '100', '101', '110', '111']

/**
 * Add params with defaults if needed for recursion <------- you will need to
 * Expands a string such that each "?" in the given string will be replaced
 * with a "0" and a "1".
 * Useful built in: .indexOf, returns index of first instance of a value, -1 if not found
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str The string containing to expand.
 * @returns {Array<string>} The expanded versions of the given string.
*/
function binaryStringExpansion(str) {
    //Your code here
    // base case? 

    // logic? 

    // recursive call?

    // return?

}

/*****************************************************************************/


console.log(binaryStringExpansion(str1)) // expected ["1000", "1001", "1100", "1101"]
console.log(binaryStringExpansion(str2)) // expected ['000', '001', '010', '011', '100', '101','110', '111']
















function binaryStringExpansion(str, solutions = [], processed = "") {
    const index = str.indexOf("?"); // will return index of first "?" or -1

    if (index < 0) { //if we don't find a "?" we're done
        solutions.push(processed + str);
    } else {
        const front = str.slice(0, index); //take everything before the ?
        const back = str.slice(index + 1); // take everything after the ?
        const prefix = processed + front; //moved the front into the already processed string
        binaryStringExpansion(back, solutions, prefix + "0"); //pass the back as what's left to process, add 0 to processed string
        binaryStringExpansion(back, solutions, prefix + "1"); // same but adding 1 to processed string
    }
    return solutions;
}
















// No built-ins version
function binaryStringExpansion(str, solutions = [], processed = "") {
    //Your code here
    // base case? 
    let found = false; //searching for "?"
    let index = 0;
    for (let i = 0; i < str.length; i++) {
        if (str[i] === "?") { // if found,   
            index = i; //capture index,
            found = true; //set found to true,
            break //and stop loop
        }
    }
    if (!found) { //-- if no ? left, done with recursion
        solutions.push(processed + str) //put the string back together and add to solutions
        return // end function call
    }
    // logic? 

    for (let i = 0; i < index; i++) { // grab all the chars before the ?
        processed += str[i] // they are now considered processed
    }

    let toBeProcessed = ""; // grab all the chars after the ?
    for (let i = index+1; i < str.length; i++) {
        toBeProcessed += str[i] // they are now what's left to process
    }
    // recursive call?
    binaryStringExpansion(toBeProcessed, solutions, processed + "0") // one call adding 0 for the ?
    binaryStringExpansion(toBeProcessed, solutions, processed + "1") // one call adding 1 for the ?
    // return?
    return solutions
}

function binaryStringExpansion(str, results = []) {
    var i = str.indexOf("?")
    if (i == -1){
        results.push(str);
    }
    else{
        var strArr = str.split("");
        strArr[i] = 0;
        binaryStringExpansion(strArr.join(""), results);
        strArr[i] = 1;
        binaryStringExpansion(strArr.join(""), results);
    }

    return results;
}






