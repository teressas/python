/* 
  Recursively sum an arr of ints
*/

const nums1 = [1, 2, 3];
const expected1 = 6;

/**
 * Add params if needed for recursion
 * Recursively sums the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number} The sum of the given nums.
 */
function sumArr(nums, i=0) {
    // // edge case

    // // base case
    if (i === nums.length){
        return 0
    }

    // // recursive statement
    return sumArr(nums, i+1) + nums[i]
}

console.log(sumArr(nums1));

// ************************************

/* 
Recursive Sigma
Input: integer
Output: sum of integers from 1 to Input integer
*/

// const num1 = 5;
// const expected1 = 15;
// // Explanation: (1+2+3+4+5)

// const num2 = 2.5;
// const expected2 = 3;
// // Explanation: (1+2)

// const num3 = -1;
// const expected3 = 0;

/**
 * Recursively sum the given int and every previous positive int.
 * - Time: O(?).
 * - Space: O(?).
 * @param {number} num
 * @returns {number}
 */
// function recursiveSigma(num) {
//     // edge case
//     // base case -> when you get to the end
//     // recusion call -> calls itself
// }