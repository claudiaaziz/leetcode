/**
 * https://leetcode.com/problems/container-with-most-water/
 * Two pointers, Time O(N) | Space(1)
 * @param {number[]} height
 * @return {number}
 */

var maxArea = function (height) {
    let [left, right, max] = [0, height.length - 1, 0];

    while (left < right) {
        let containerHeight, area;
        let containerWidth = right - left;

        if (height[left] < height[right]) {
            containerHeight = height[left];
            left++;
        } else {
            containerHeight = height[right];
            right--;
        }

        area = containerWidth * containerHeight;

        if (area > max) {
            max = area;
        }
    }

    return max;
};

// t o(n) - s o(1)
var maxArea = function(height) {
    let max = 0
    let l = 0
    let r = height.length-1

    while (l < r) {
        const minHeight = Math.min(height[l], height[r])
        max = Math.max((r-l) * minHeight, max)
        
        if (height[l] < height[r]) {
            l++
        } else {
            r--
        }
    }

    return max
};