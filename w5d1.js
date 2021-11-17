/* 
  Given a string that may have extra spaces at the start and the end,
  return a new string that has the extra spaces at the start and the end trimmed (removed)
  do not remove any other spaces.
*/

const str1 = "   hello world     ";
const expected1 = "hello world";

const str2 = "   hello  world my friend is tyler     ";
const expected2 = "hello  world my friend is tyler";

/**
 * Trims any leading or trailing white space from the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The given string with any leading or trailing white space
 *    stripped.
 */
// create two for loops
// 1. for loop starts from the start of string
// 2. for loops starts from the end of string
// store each index into new variable
// splice using new variables


function trim(str) {
    var start = 0;
    var end = 0;
    var newString = "";
    for(var i=0; i < str.length; i++){
        if (str[i] != " "){
            start = i
            break
        }
    }
    for (var i=str.length-1; i>=0; i--){
        if (str[i] != " "){
            end = i
            break
        }
    }
    newString = str.substring(start,end+1)
    return newString
}

console.log(trim(str2));

// ******************************************************************

/* 
  An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
  typically using all the original letters exactly once.
  Is there a quick way to determine if they aren't an anagram before spending more time?
  Given two strings
  return whether or not they are anagrams
*/

const strA1 = "yes";
const strB1 = "eys";
const expected1 = true;

const strA2 = "yes";
const strB2 = "eYs";
const expected2 = true;

const strA3 = "no";
const strB3 = "noo";
const expected3 = false;

const strA4 = "silent";
const strB4 = "listen";
const expected4 = true;

/**
 * Determines whether s1 and s2 are anagrams of each other.
 * Anagrams have all the same letters but in different orders.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} s1
 * @param {string} s2
 * @returns {boolean} Whether s1 and s2 are anagrams.
 */

// put strings into a object
// we need 1st for loop to put s1 into 1st object
// we need 2nd for loop to put s2 into 2nd object
// if 1st dict = 2nd dict then return True if nof False

function isAnagram(s1, s2) {
    var s1 = {};
    var s2 = {};
    s2 = key
}

isAnagram(strA1, strB1)