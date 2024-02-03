/**
 * @param {number[]} nums
 * @param {number} target
 * Time O(log(N)) | Space O(1)
 * @return {number}
 */
var search = function (nums, target) {
    let [left, right] = [0, nums.length - 1];

    while (left <= right) {
        const mid = (left + right) >> 1;
        const guess = nums[mid];

        const isTarget = guess === target;
        if (isTarget) return mid;

        const isTargetGreater = guess < target;
        if (isTargetGreater) left = mid + 1;

        const isTargetLess = target < guess;
        if (isTargetLess) right = mid - 1;
    }

    return -1;
};

// claudia
// time o(log n) - space o(log n)  
const search = (nums, target) => {
    if (nums.length === 0) return -1
    const midIdx = Math.floor(nums.length / 2) 
    const left = nums.slice(0, midIdx)
    const right = nums.slice(midIdx + 1)

    if (nums[midIdx] === target) { 
        return midIdx
    } else if (nums[midIdx] > target) {
        return search(left, target)
    } else {
        const rightRes = search(right, target)
        return rightRes === -1 ? - 1 : rightRes + midIdx + 1
    }
};