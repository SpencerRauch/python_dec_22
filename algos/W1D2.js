/* 
  String: Reverse
  Given a string,
  return a new string that is the given string reversed
*/

const str1 = "creature";
const expected1 = "erutaerc";

const str2 = "dog";
const expected2 = "god";

const str3 = "hello";
const expected3 = "olleh";

const str4 = "";
const expected4 = "";

/**
 * Reverses the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str String to be reversed.
 * @returns {string} The given str reversed.
 */
function reverseString(str) {
  newStr = ""
  for (let letter of str){
    console.log(letter)
    newStr = letter + newStr
  }
  return newStr
}

//TEST CODE FOR REVERSE
console.log(reverseString(str1)) // Expected: erutaerc
console.log(reverseString(str2)) // Expected: god
console.log(reverseString(str3)) // Expected: olleh
console.log(reverseString(str4)) // Expected: ""

function reverseString(str){
  var newstr = "";
  for(var i = str.length - 1; i >= 0; i--){
          newstr += str[i];
      }
  return newstr;
}

function reverseString2(str) {
  var len = str.length;
  var tempStr = str.split("");
  var revStr = [];
  
  for (var i=0; i<len; i++){
      revStr.push(tempStr.pop());
  }
  return revStr.join();
}