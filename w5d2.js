/* 
  Balance Index
  Here, a balance point is ON an index, not between indices.
  Return the balance index where sums are equal on either side
  (exclude its own value).
  
  Return -1 if none exist.
  
*/

const nums1 = [-2, 5, 7, 0, 3];
const expected1 = 2;

const nums2 = [9, 9];
const expected2 = -1;

const nums3 = [7, 2, 4, 10, 3, 10];
const expected3 = 3;

const nums4 = [7, 2, 4, 10, 3, 13];
const expected4 = -1;

/**
 * Finds the balance index in the given array where the sum to the left of the
 *    index is equal to the sum to the right of the index.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number} The balance index or -1 if there is none.
 */
// edge case: check array length - if array.length is < 2 then return -1
// create 2 temp vars to sum the start of arrary and end of array
// create for loop to loop through array
// two loops that find the sums - left and right sum
// temp var1 = temp var2
// return index

function addIndex(arr,start,end){
    var sum = 0;
    for(let x = start; x < end; x++){
        sum += arr[x]
    }
    return sum
}

function balanceIndex(nums) {
    var start_sum = 0;
    var end_sum = 0;
    if (nums.length <= 2){
        return -1;
    }
    for(let i=1; i < nums.length-1; i++){
        start_sum = 0;
        end_sum = 0;
        // for(let x = 0; x < i; x++){
        //     start_sum += nums[x]
        //     // console.log(x)
        // }
        // for(let x = i+1; x < nums.length; x++){
        //     end_sum += nums[x]
        //     // console.log(x)
        // }

        start_sum = addIndex(nums,0,i)
        end_sum = addIndex(nums,(i+1),nums.length)

        console.log("start_sum:" + start_sum);
        console.log("end_sum:" + end_sum);
        if(start_sum == end_sum){
            return i
        }
    }
    return -1
}
console.log(balanceIndex(nums2));




