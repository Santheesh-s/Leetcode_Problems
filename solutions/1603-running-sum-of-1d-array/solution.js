/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    let adder=0;
    for(let i=0;i<nums.length;i++)
    {
        adder+=nums[i];
        nums[i]=adder;
    }
    return nums;
};
