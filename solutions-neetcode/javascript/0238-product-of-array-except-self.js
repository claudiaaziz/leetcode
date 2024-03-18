/**
 * Array
 * Time O(N) | Space O(N)
 * https://leetcode.com/problems/product-of-array-except-self/
 * @param {number[]} nums
 * @return {number[]}
 */
 function productExceptSelf(nums) {
    const result = [];
    let prefix = 1;
    let postfix = 1;
    
    for (let i = 0; i < nums.length; i++) {
        result[i] = prefix;
        prefix *= nums[i];
    }
    for (let i = nums.length - 2; i >= 0; i--) {
        postfix *= nums[i + 1];
        result[i] *= postfix;
    }
    
    return result;
};

// claudia
// t o(n) - s o(1)
var productExceptSelf = function (nums) {
  const n = nums.length;
  const res = Array(n).fill(0);

  let prefix = 1;
  for (let i = 0; i < n; i++) {
    res[i] = prefix;
    prefix *= nums[i];
  }

  let suffix = 1;
  for (let i = n - 1; i >= 0; i--) {
    res[i] *= suffix;
    suffix *= nums[i];
  }

  return res;
};