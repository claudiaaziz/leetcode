/**
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/
 * Time O(N) | Space O(N)
 * @param {string} s
 * @return {number}
 */

var lengthOfLongestSubstring = function (s) {
    const set = new Set();
    let l = 0;
    let max = 0;

    for (let r = 0; r < s.length; r++) {
        while (set.has(s[r])) {
            set.delete(s[l]);
            l++;
        }
        set.add(s[r]);
        max = Math.max(max, set.size);
    }
    return max;
};

var lengthOfLongestSubstring = function(s) {
    let maxLength = 0 
    const set = new Set() 
    let l = 0 
    let r = 0 

    while (r < s.length) {
        if (set.has(s[r])) {
            maxLength = Math.max(maxLength, r-l)
            set.delete(s[l])
            l++
        } else {
            set.add(s[r])
            r++
        }
    }

    return Math.max(maxLength, set.size)
};