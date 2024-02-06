/**
 * @param {number[]} nums
 * Time O(log(N)) | Space O(1)
 * @return {number}
 */
var findMin = function (nums) {
    let [left, right] = [0, nums.length - 1];

    while (left < right) {
        const mid = (left + right) >> 1;
        const guess = nums[mid];
        const [leftNum, rightNum] = [nums[left], nums[right]];

        const isTarget = leftNum < rightNum;
        if (isTarget) return leftNum;

        const isTargetGreater = leftNum <= guess;
        if (isTargetGreater) left = mid + 1;

        const isTargetLess = guess < leftNum;
        if (isTargetLess) right = mid;
    }

    return nums[left];
};

// claudia
// time o(log n) - space o(1)
const findMin = (nums) => {
    let l = 0
    let r = nums.length - 1

    while (l < r) {
        const mid = l + Math.floor((r - l) / 2)
        if (nums[mid] > nums[r]) {
            l = mid + 1
        } else {
            r = mid
        }
    }

    return nums[l]
};