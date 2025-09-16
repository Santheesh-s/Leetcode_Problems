/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let count=0,cand=nums[0];
    for(let i=0;i<nums.length;i++)
    {
        if(count==0)
            cand=nums[i];
        if(cand==nums[i])
            count++;
        else
            count--;
    }
    return cand;
};
