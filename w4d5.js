/* 
  String: Rotate String
  Create a standalone function that accepts a string and an integer,
  and rotates the characters in the string to the right by that given
  integer amount.
*/

const str = "Hello World";

const rotateAmnt1 = 0;
const expected1 = "Hello World";


const rotateAmnt2 = 1;
const expected2 = "dHello Worl";

const rotateAmnt3 = 2;
const expected3 = "ldHello Wor";

const rotateAmnt4 = 4;
const expected4 = "orldHello W";

const rotateAmnt5 = 13;
const expected5 = "ldHello Wor";

const rotateAmnt6 = 6;
const expected1 = " WorldHello";
/* 
Explanation: this is 2 more than the length so it ends up being the same
as rotating it 2 characters because after rotating every letter it gets back
to the original position.
*/

/**
 * Rotates a given string's characters to the right by the given amount,
 * wrapping characters to the beginning.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @param {number} amnt The amount of characters in the given str to rotate to the
 *    right.
 * @returns {string} The string rotated by the given amount.
 */
function rotateStr(str, amnt) {}

function rotateStr(str,amt){
    let idx = str.length - ((str.length + amt) % str.length)
    return str.slice(idx) + str.slice(0,idx)
  }
  console.log(rotateStr('helloworld',19))
  console.log(rotateStr('helloworld',-1))

// *****************************************


/* 
  Create the function isRotation(str1,str2) that
  returns whether the second string is a rotation of the first.
*/

const strA1 = "ABCD";
const strB1 = "CDAB";
const expected1 = true;
// Explanation: if you start from A in the 2nd string, the letters are in the same order, just rotated

const strA2 = "ABCD";
const strB2 = "CDBA";
const expected2 = false;
// Explanation: all same letters in 2nd string, but out of order

/**
 * Determines whether the second string is a rotated version of the first.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} s1
 * @param {string} s2
 * @returns {boolean} Whether the second string is a rotated version of the 1st.
 */
function isRotation(s1, s2) {}


// solutions #2

function isRotation(s1, s2) {

    let newString = ""
    for(let amnt = 0;  amnt <s1.length; amnt++ ){
    newString = s1.slice(s1.length-amnt,s1.length) + s1.slice(0, s1.length-amnt)
    console.log(newString)
    if(newString === s2){
        return true
    }
    newString = ""
}
 return false   
}

console.log(isRotation(strA2,strB2))

// solutions #1

const str = "Hello World";

const rotateAmnt1 = 0;
const notExpected1 = "Hello World";


const rotateAmnt2 = 1;
const notexpected2 = "dHello Worl";

const rotateAmnt3 = 2;
const notexpected3 = "ldHello Wor";

const rotateAmnt4 = 4;
const notexpected4 = "orldHello W";

const rotateAmnt5 = 13;
const notexpected5 = "ldHello Wor";

const rotateAmnt6 = 6;
const notexpected1 = " WorldHello";

function rotateStr(str, amnt) {
    let newStr = ""
    let newNewStr = ""
    if (amnt > str.length){
        amnt -= str.length
    }
    for (let i = str.length - amnt; i < str.length; i++){
        newStr += str[i]
    }
    for(let i = 0; i < str.length - amnt; i++){
        newNewStr += str[i]
    }
    return newStr += newNewStr
}
console.log(rotateStr(str, rotateAmnt5))

