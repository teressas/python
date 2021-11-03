/* 
  Given an arr and a separator string, output a string of every item in the array separated by the separator.
  
  No trailing separator at the end
  Default the separator to a comma with a space after it if no separator is provided
*/

const arr1 = [1, 2, 3];
const separator1 = ", ";
const expected1 = "1, 2, 3";

const arr2 = [1, 2, 3];
const separator2 = "-";
const expected2 = "1-2-3";

const arr3 = [1, 2, 3];
const separator3 = " - ";
const expected3 = "1 - 2 - 3";

// edge case
const arr4 = [1];
const separator4 = ", ";
const expected4 = "1";

const arr5 = [];
const separator5 = ", ";
const expected5 = "";

/**
 * Converts the given array into a string of items separated by the given separator.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string|number|boolean>} arr The items to be joined as a string.
 * @param {string} separator To separate each item of the given arr.
 * @returns {string} The given array items as a string separated by the given separator.
 */

function join(arr, separator) {
    var newlist = [];
    for (var i = 0; i < arr.length; i++){
        newlist.push(arr[i]);
        newlist.push(separator);
    }
    newerlist = "";
    for (var x = 0; x < newlist.length-1; x++){
        newerlist += newlist[x];
    }
    console.log(newerlist);
    return

}
// 2 for loops outside of each other - time complexity
join(arr4,separator4)

// ****************************************************

/* 
Book Index
Given an array of ints representing page numbers
return a string with the page numbers formatted as page ranges when the nums span a consecutive range
*/

const two_nums1 = [1, 13, 14, 15, 37, 38, 70];
const two_expected1 = "1, 13-15, 37-38, 70";

const two_nums2 = [1, 13, 14, 15, 16,17,18, 37, 38, 70, 71, 72, 73, 74, 75];
const two_expected2 = "1, 13-18, 37-38, 70-75";

/**
 * Turns the given arr of page numbers into a string of comma hyphenated
 * page ranges.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums Page numbers.
 * @returns {string} The given page numbers as comma separated hyphenated
 *    page ranges.
 */

function bookIndex(nums) {
    let a = "";
    for (var i=0; i < nums.length; i++){
        if (nums[i]+1 === nums[i+1])
        // if 1
            while (nums[i] === nums[i+1])

    }
}

bookIndex(two_nums1,two_expected1)

/* 
Book Index
Given an array of ints representing page numbers
return a string with the page numbers formatted as page ranges when the nums span a consecutive range
*/

const nums1 = [1, 13, 14, 15, 37, 38, 70];
const expected1 = "1, 13-15, 37-38, 70";

/**
 * Turns the given arr of page numbers into a string of comma hyphenated
 * page ranges.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums Page numbers.
 * @returns {string} The given page numbers as comma separated hyphenated
 *    page ranges.
 */
function bookIndex(nums) {
  // SETUP
  // new string that we are going to build
    var newString = " "

  // WORK
  // Loop through the nums array
    for (var i = 0; i < nums.length-1; i++){
        var consecutiveNumIdx = i + 1;
        while (nums[consecutiveNumIdx] === nums[consecutiveNumIdx - 1] + 1){
            consecutiveNumIdx++;
        }
        if (consecutiveNumIdx === i + 1){
            newString += nums[i]
        }

        if (consecutiveNumIdx > i + 1){
            newString += nums[i] + "-" + nums[consecutiveNumIdx - 1];
            i = consecutiveNumIdx - 1;
        }

        if (i < nums.length - 1){
            newString += ", ";
        }
    // check if the next element after the current is a consecutive number e.g. if i = 0, look at i = 1
      // if that element is consecutive, continue looking ahead until we come across an element that is no longer consecutive
      // we can use a while loop to continue looking ahead until the numbers are no longer consecutive
    // add the page numbers to the string
      // if there was not a consecutive, just add the number and the ", "
      // if there was a consecutuve, add the first and last of the consecutive numbers, separated by a dash, followed by the ", "


  // RETURN
  // return that new string
  return newString
}

console.log(bookIndex(nums1))