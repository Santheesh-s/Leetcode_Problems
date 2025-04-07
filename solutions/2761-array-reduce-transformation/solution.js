/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    var n=init;
    for(let i=0;i<nums.length;i++)
    {
        n=fn(init,nums[i])
        init=n
    }
    return n;
};
