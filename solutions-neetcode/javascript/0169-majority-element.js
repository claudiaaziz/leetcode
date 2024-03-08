/**
 * Boyer Moore Algorithm
 * Time O(N) | Space O(1)
 * https://leetcode.com/problems/majority-element
 * @param {number[]} nums
 * @return {number}
 */

var majorityElement = function (nums) {
	let res = nums[0];
	let count = 1;

	for (let i = 1; i < nums.length - 1; i++) {
		if (nums[i] === res) count++;
		else if (!--count) {
			res = nums[i + 1];
			count = 0;
		}
	}

	return res;
};

/**
 * HashMap
 * Time O(N) | Space O(N)
 * https://leetcode.com/problems/majority-element
 * @param {number[]} nums
 * @return {number}
 */

var majorityElement = function (nums) {
	const occuranceOfElement = new Map();
	
	for (let i = 0; i < nums.length; i++) {
		if (occuranceOfElement.has(nums[i])) {
			let occurance = occuranceOfElement.get(nums[i]);
			occuranceOfElement.set(nums[i], occurance + 1);
		} else {
			occuranceOfElement.set(nums[i], 1);
		}
	}

	for (let [key, value] of occuranceOfElement) {
		if (value > nums.length / 2) return key;
	}
};

// claudia
// t o(n) - s o(1)
var majorityElement = function(nums) {
    let count = 0
    let majorityEle;

    for (const num of nums) {
        if (count === 0) majorityEle = num
        if (num === majorityEle) {
            count++
        } else {
            count--
        }
    }

    return majorityEle
};