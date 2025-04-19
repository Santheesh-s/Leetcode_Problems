/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    let n=(nums.length*(nums.length+1))/2,sum=0;
    for(let i=0;i<nums.length;i++)
        sum+=nums[i];
    return n-sum;
};
