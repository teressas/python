// create a function that takes in two arrays into a dictionary 
// 1st array will be the key 
// 2nd arry wil be the value
// create new variable to store dictionary
// loop through 1st array to pull each value into the dictionary and store as key
// loop through 2nd array to pull each value into the dict and store as val
// print array
// edge case: check length of each array to determine if there's in inbalance of key to value

/* 
Zip Arrays into Map
  
  
Given two arrays, create an associative array (aka hash map, an obj / dictionary) containing keys from the first array, and values from the second.
Associative arrays are sometimes called maps because a key (string) maps to a value 
 */

/**
   * Converts the given arrays of keys and values into an object.
   * - Time: O(?).
   * - Space: O(?).
   * @param {Array<string>} keys
   * @param {Array<any>} values
   * @returns {Object} The object with the given keys and values.
   */
function zipArraysIntoMap(keys, values) {
    // use let so var i is only used in the for loop, keeps it to the scope of the funct
    // const is similiar to let
    // nested for loops use var i, j, k
    // dictionary is a python term; js uses object
    let dictionary={};
    for(let i=0; i < keys.length; i++){
        dictionary[keys[i]] = values[i];
    }
    // output dictionary will not be in the same order as array. Dictionary is not index based.
    console.log(dictionary);
}

const keys1 = ["abc", 3, "yo"];
const vals1 = [42, "wassup", true];
const expected1 = {
    abc: 42,
    3: "wassup",
    yo: true,
};

const keys2 = ["abc", 3, "yo", "bro"];
const vals2 = [42, "wassup", true];
const expected2 = {
    abc: 42,
    3: "wassup",
    yo: true,
    bro: null
};


const keys3 = ["abc", 3, "yo"];
const vals3 = [42, "wassup", true, 'bro'];
const expected3 = {
    abc: 42,
    3: "wassup",
    yo: true,
    "?":"?"
};
  

zipArraysIntoMap(keys2, vals2)







//   *****************************************

/* 
  Invert Hash
  A hash table / hash map is an obj / dictionary
  Given an object / dict,
  return a new object / dict that has the keys and the values swapped so that the keys become the values and the values become the keys
*/

const two_obj1 = { name: "Zaphod", charm: "high", morals: "dicey" };
const two_expected1 = { Zaphod: "name", high: "charm", dicey: "morals" };

const two_obj2 = { name: "Zaphod", charm: "high", morals: "dicey", something: "dicey" };
// const expected1 = { Zaphod: "name", high: "charm", dicey: ["morals","something"] };
// const expected1 = { Zaphod: "name", high: "charm", dicey: "something" };
// const expected1 = { Zaphod: "name", high: "charm", dicey: "morals", dicey1: "something" };

/**
 * Inverts the given object's key value pairs so that the original values
 * become the keys and the original keys become the values.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Object<string, string>} obj An object with string keys and string values.
 * @return The given object with key value pairs inverted.
 */
// function invertObj(obj) {}