/**
 * @param {number[]} nums
 * @return {number}
 */
var arraySign = function(nums) {
    let n=1;
    for(let i=0;i<nums.length;i++)
    {    
        if(nums[i]>0)
            n*=1;
        else if(nums[i]<0)
            n*=-1;
        else
            return 0;
    }
    return n;
};
