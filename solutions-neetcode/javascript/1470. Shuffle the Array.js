/**
 * @param {number[]} nums
 * @param {number} n
 * @return {number[]}
 */
var shuffle = function(nums, n) {
    let left = 0;
    let right = n;

    //res arr
    let res = [];

    while(nums[right]){
        res.push(nums[left])
        res.push(nums[right])
        left+=1
        right+=1
    }

    //return arr
    return res;
};