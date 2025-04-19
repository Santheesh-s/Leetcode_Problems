/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function(nums) {
    let arr=new Array();
    for(let i=0;i<nums.length;i++)
    {
        if(arr[nums[i]])
            return nums[i];
        arr[nums[i]]=1;
    }
    return 0;
};
