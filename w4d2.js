// Pseduo Code
// build frequency table from nums array
// loop over frequency table
// check if keys have a odd value and return

/* 
  Given an array of strings
  return a sum to represent how many times each array item is found (a frequency table)
  Useful methods:
    Object.hasOwnProperty("keyName")
      - returns true or false if the object has the key or not
    Python: key in dict
*/

const arr1 = ["a", "a", "a"];
const expected1 = {
  a: 3,
};

const arr2 = ["a", "b", "a", "c", "B", "c", "c", "d"];
const expected2 = {
  a: 2,
  b: 1,
  c: 3,
  B: 1,
  d: 1,
};

const arr3 = [];
const expected3 = {};

/**
 * Builds a frequency table based on the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string>} arr
 * @returns {Object<string, number>} A frequency table where the keys are items
 *    from the given arr and the values are the amnt of times that item occurs.
 */
function frequencyTableBuilder(arr) {
    newdict = {};
    for (let i=0; i < arr.length; i++){
        newdict[arr[i]] = 0;   
    }
    for (let i=0; i < arr.length; i++){
        newdict[arr[i]] += 1;  
    }
    return newdict;
}

function frequencyTableBuilder2(arr) {
    newdict = {};
    for (let i=0; i < arr.length; i++){
        if (arr[i] in newdict){
            newdict[arr[i]]++;
        }   
        else {
            newdict[arr[i]]=1;
        } 
    } 
    return newdict  
}

console.log(frequencyTableBuilder(arr2));
console.log(frequencyTableBuilder2(arr2));

// ************************************************************


// https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/

/* 
Given a non-empty array of odd length containing ints where every int but one
has a matching pair (another int that is the same)
return the only int that has no matching pair.
*/

const nums1 = [1];
const expected1 = 1;

const nums2 = [5, 4, 5];
const expected2 = 4;

const nums3 = [5, 4, 3, 4, 3, 4, 5];
const expected3 = 4; // there is a pair of 4s but one 4 has no pair.

const nums4 = [5, 2, 6, 2, 3, 1, 6, 3, 2, 5, 2];
const expected4 = 1;

function oddOccurrencesInArray(nums) {
    let newdict = frequencyTableBuilder(nums)
    for (let key in newdict){
        if(newdict[key] % 2 == 1){
            return key
        }
    }
}

console.log(oddOccurrencesInArray(nums4));
