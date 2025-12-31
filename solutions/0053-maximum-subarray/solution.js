/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let sum=nums[0],cur_sum=nums[0];
        for(let i=1;i<nums.length;i++)
        {
            if(cur_sum<0)
                cur_sum=0;
            cur_sum+=nums[i];
            if(cur_sum>sum)
                sum=cur_sum;
        }
        return sum;
};
