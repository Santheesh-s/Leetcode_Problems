/**
 * @param {number[]} nums
 * @return {boolean}
 */
var hasTrailingZeros = function(nums) {
    let count=0;
    for(let i=0;i<nums.length;i++)
    {
        if((nums[i]&1)==0)
            count++;
        if(count>=2)
            return true;
    }
    return false;
};
