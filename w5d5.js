/* 
  Given an int to represent how much change is needed
  calculate the fewest number of coins needed to create that change,
  using the standard US denominations
*/

const cents1 = 25;
const expected1 = { quarter: 1 };

const cents2 = 50;
const expected2 = { quarter: 2 };

const cents3 = 9;
const expected3 = { nickel: 1, penny: 4 };

const cents4 = 99;
const expected4 = { quarter: 3, dime: 2, penny: 4 };

/**
 * Calculates the fewest coins of the standard American denominations needed
 *    to reach the given cents amount.
 * - Time: O(?).
 * - Space: O(?).
 * @param {number} cents
 * @param {string} sick
 * @returns {Object<string, number>} - A denomination table where the keys are
 *    denomination names and the value is the amount of that denomination
 *    needed.
 */

// create a coin dictionary with keys: quarter, nickel, dime, penny
// use modulus to get remainder
 


function fewestCoinChange(cents) {
    coin = { "quarter": 25, "dime": 10, "nickel": 5, "penny": 1 };
    var remainder = 0
    while cents >= coin["quarter"]{
        cents = cents - coin['quart']
    }

    remainder = cents % coin["quarter"];

    if cents > coin["quarter"]{

    }
    

}

fewestCoinChange(cents1);

/* 
  Missing Value
  You are given an array of length N that contains, in no particular order,
  integers from 0 to N . One integer value is missing.
  Quickly determine and return the missing value.
*/

// const nums1 = [3, 0, 1];
// const expected1 = 2;

// const nums2 = [3, 0, 1, 2];
// const expected2 = null;
// Explanation: nothing is missing

/* 
  Bonus: now the lowest value can now be any integer (including negatives),
  instead of always being 0. 
*/

// const nums3 = [2, -4, 0, -3, -2, 1];
// const expected3 = -1;

// const nums4 = [5, 2, 7, 8, 4, 9, 3];
// const expected4 = 6;

/**
 * Determines what the missing int is in the given unordered array of ints
 *    which spans from 0 to N where only one int is missing. With this missing
 *    int, a consecutive sequence of ints could be formed from the array.
 * Bonus: Given ints can span from N to M (start and end anywhere).
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} unorderedNums
 * @returns {number|null} The missing integer needed to be able to form an unbroken
 *    consecutive set of integers from the given array or null if none is missing.
 */
// function missingValue(unorderedNums) {}

function missingVal(unorderedNums){
  let min = unorderedNums[0];
  let max = unorderedNums[0];
  let sum = 0;
  for(let num of unorderedNums){
    if(num < min){
      min = num;
    } else if (num > max){
      max = num;
    }
    sum += num;
  }
  // const expectedSum = Math.floor((min+max) * (unorderedNums.length+1) / 2);// mathematical formula for sum of range of numbers
  let expectedSum = 0
  for(let i = min; i <= max; i++){
    expectedSum += i
  }
  const diff = expectedSum - sum;
  return diff == 0 ? null : diff;
}
console.log(missingVal(nums1))

const cents1 = 25;
const expected1 = { quarter: 1 };

const cents2 = 50;
const expected2 = { quarter: 2 };

const cents3 = 9;
const expected3 = { nickel: 1, penny: 4 };

const cents4 = 99;
const expected4 = { quarter: 3, dime: 2, penny: 4 };

const cents5 = 3;

function fewestCoinChange(cents) {
    var change ={}
    if (cents <= 0){
        return null
    }
    if(cents >= 25){
        change['quarter']=(Math.floor(cents/25))
        // console.log(change)
        cents=cents % 25
    }
    if(cents >= 10){
        change['dime']=(Math.floor(cents/10))
        // console.log(change)
        cents=cents % 10
    }
    if(cents >= 5){
        change['nikel']=(Math.floor(cents/5))
        // console.log(change)
        cents=cents % 5
    }
    if(cents >= 1){
        change['penny']=(Math.floor(cents/1))
        // console.log(change)
        cents=cents % 1
    }
    return change
}
console.log(fewestCoinChange(cents1))
console.log(fewestCoinChange(cents2))
console.log(fewestCoinChange(cents3))
console.log(fewestCoinChange(cents4))
console.log(fewestCoinChange(cents5)) 

function fewestChange(cents){
  const denoms = {
    quarters : 25,
    dimes : 10,
    nickels : 5,
    pennies : 1
  }
  const output = {}
  for(const [key,value] of Object.entries(denoms)){//does the same as below
//for(const key in denoms){
//  const value = denoms[key]
    if(value <= cents){
      output[key] = Math.floor(cents/value)
      cents = cents % value
    }
  }
  return output
}
console.log(fewestChange(94))