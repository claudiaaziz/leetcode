// /**
//  * @param {number[]} nums
//  * @param {number} target
//  * Time O(log(N)) | Space O(1)
//  * @return {number}
//  */
// var search = (nums, target) => {
//     let [left, right] = [0, nums.length - 1];

//     while (left <= right) {
//         const mid = (left + right) >> 1;
//         const guess = nums[mid];
//         const [leftNum, rightNum] = [nums[left], nums[right]];

//         const isTarget = guess === target;
//         if (isTarget) return mid;

//         const isAscending = leftNum <= guess;
//         if (isAscending) {
//             const isInRange = leftNum <= target;
//             const isLess = target < guess;

//             const isTargetGreater = !(isInRange && isLess);
//             if (isTargetGreater) left = mid + 1;

//             const isTargetLess = isInRange && isLess;
//             if (isTargetLess) right = mid - 1;
//         }

//         const isDescending = guess < leftNum;
//         if (isDescending) {
//             const isGreater = guess < target;
//             const isInRange = target <= rightNum;

//             const isTargetGreater = isGreater && isInRange;
//             if (isTargetGreater) left = mid + 1;

//             const isTargetLess = !(isGreater && isInRange);
//             if (isTargetLess) right = mid - 1;
//         }
//     }

//     return -1;
// };

// claudia
// time o(log n) - space o(1)
const search = (nums, target) => {
  let l = 0;
  let r = nums.length - 1;

  while (l <= r) {
    const mid = Math.floor((l + r) / 2);

    if (nums[mid] === target) return mid;

    if (nums[l] <= nums[mid]) {
      if (target > nums[mid] || target < nums[l]) {
        l = mid + 1;
      } else {
        r = mid - 1;
      }
    } else {
      if (target < nums[mid] || target > nums[r]) {
        r = mid - 1;
      } else {
        l = mid + 1;
      }
    }
  }

  return -1;
};
