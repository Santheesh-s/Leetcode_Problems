/**
 * @param {number[]} nums
 * @return {number}
 */
var numIdenticalPairs = function(nums) {
    let n=nums.length,count=0;
    for(let i=0;i<n;i++)
        for(let j=i+1;j<n;j++)
            if(nums[i]==nums[j])
                count+=1;
    return count;
};
