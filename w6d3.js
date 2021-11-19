/* 
  Recursively reverse a string
  helpful methods:
  str.slice(beginIndex[, endIndex])
  returns a new string from beginIndex to endIndex exclusive
*/

const str1 = "abc";
const expected1 = "cba";

// const str2 = "";
// const expected2 = "";

// const str3 = "Tyler is awesome";
// const expected3 = "emosewa si relyT";

/**
 * Recursively reverses a string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The given str reversed.
 */
function reverseStr(str) {
    if (i === str.length){
        return ""
    }
    return sumArr(nums, i+1) + nums[i]
}
reverseStr(str1); 
// ********************************************************

/*
  Recursive Binary Search
  Input: SORTED array of ints, int value
  Output: bool representing if value is found
  Recursively search to find if the value exists, do not loop over every element.
  Approach:
  Take the middle item and compare it to the given value.
  Based on that comparison, narrow your search to a particular section of the array
*/

// const two_nums1 = [1, 3, 5, 6];
// const two_searchNum1 = 4;
// const two_expected1 = false;

// const two_nums2 = [4, 5, 6, 8, 12];
// const two_searchNum2 = 5;
// const two_expected2 = true;

// const two_nums3 = [3, 4, 6, 8, 12];
// const two_searchNum3 = 3;
// const two_expected3 = true;

// /**
//  * Add params if needed for recursion
//  * Recursively performs a binary search (divide and conquer) to determine if
//  * the given sorted nums array contains the given number to search for.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {Array<number>} sortedNums
//  * @param {number} searchNum
//  * @returns {boolean} Whether the searchNum was found in the sortedNums array.
//  */
// function binarySearch(sortedNums, searchNum) {}

// solutions

function binarySearch(
  sortedNums,
  searchNum,
  leftIdx = 0,
  rightIdx = sortedNums.length - 1
) {
  if (leftIdx > rightIdx) {
    return false;
  }

  const midIdx = Math.floor((rightIdx + leftIdx) / 2);

  if (sortedNums[midIdx] === searchNum) {
    return true;
  }

  if (searchNum < sortedNums[midIdx]) {
    return binarySearch(sortedNums, searchNum, 0, midIdx - 1);
  } else {
    return binarySearch(sortedNums, searchNum, midIdx + 1, rightIdx);
  }
}

function reverseStr(str) {
  if (str === "") {
    return "";
  }
  const strLessFirst = str.slice(1);
  return reverseStr(strLessFirst) + str[0];
}