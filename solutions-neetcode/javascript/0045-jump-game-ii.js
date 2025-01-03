/**
 * https://leetcode.com/problems/jump-game-ii/
 * Time O(N) | Space O(1)
 * @param {number[]} nums
 * @return {number}
 */
var jump = function (nums) {
    let [ left, right, jumps ] = [ 0, 0, 0 ];

    while (right < nums.length - 1) {
        const maxReach = getMaxReach(nums, left, right);

        left = right + 1;
        right = maxReach;
        jumps += 1;
    }

    return jumps;
};

const getMaxReach = (nums, left, right, maxReach = 0) => {
    for (let i = left; i < right + 1; i++) {
        const reach = nums[i] + i;
        maxReach = Math.max(maxReach, reach);
    }

    return maxReach;
}

/**
 * https://leetcode.com/problems/jump-game-ii/
 * Time O(N) | Space O(1)
 * @param {number[]} nums
 * @return {number}
 */
 var jump = function(nums) {
    let [ jumps, currentJumpEnd, farthest ] = [ 0, 0, 0];
    
    for (let i = 0; i < nums.length - 1; i++) {
        farthest = Math.max(farthest, (i + nums[i]));

        const canJump = i === currentJumpEnd
        if (canJump) { jumps++; currentJumpEnd = farthest; }
    }

    return jumps;
}

// claudia
// t o(n) - s o(1)
const jump = (nums) => {
  if (nums.length === 1) return 0;

  let totalJumps = 0;
  const destination = nums.length - 1;
  let coverage = 0;
  let lastJumpIdx = 0;

  for (let i = 0; i < nums.length; i++) {
    coverage = Math.max(coverage, i + nums[i]);

    if (i === lastJumpIdx) {
      lastJumpIdx = coverage;
      totalJumps++;

      if (coverage >= destination) return totalJumps;
    }
  }

  return totalJumps;
};