/**
 * https://leetcode.com/problems/longest-repeating-character-replacement/
 * Time O(((N + 26) * N) * (M - N)) | Space O(1)
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function(s, k) {
    let res = 0;
    let count = new Map();
    let l = 0;

    for (let r = 0; r < s.length; r++) {
        let len  = r - l + 1
        count.set(s[r], 1 + (count.get(s[r]) || 0))

        if ((len - Math.max(...count.values())) > k) {
            count.set(s[l], count.get(s[l]) - 1)
            l++;
        }
        len = r - l + 1;
        res = Math.max(res, len)
    }

    return res;
};

/**
 * https://leetcode.com/problems/longest-repeating-character-replacement/
 * Time O(((N + 26) * N) * (M - N)) | Space O(1)
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function (s, k) {
    let [left, right, longest, max] = new Array(4).fill(0);
    const frequencyMap = new Array(26).fill(0);

    while (right < s.length) {
        const count = addRightFrequency(s, right, frequencyMap);

        longest = Math.max(longest, count);

        let window = right - left + 1;
        const canSlide = k < window - longest;
        if (canSlide) {
            subtractLeftFrequency(s, left, frequencyMap);
            left++;
        }

        window = right - left + 1;
        max = Math.max(max, window);

        right++;
    }

    return max;
};

const addRightFrequency = (s, right, map) => {
    const char = s[right];
    const index = getCode(char);

    map[index]++;

    return map[index];
};

const subtractLeftFrequency = (s, left, map) => {
    const char = s[left];
    const index = getCode(char);

    map[index]--;

    return map[index];
};

const getCode = (char) => char.charCodeAt(0) - 'A'.charCodeAt(0);

// t o(n) - s o(1)
var characterReplacement = function(s, k) {
    let l = 0 
    let r = 0 
    const windowCount = {} 
    let topFreq = 0 
    let longest = 0 

    while (r < s.length) {
        const rChar = s[r]
        windowCount[rChar] = windowCount[rChar] + 1 || 1
        topFreq = Math.max(topFreq, windowCount[rChar])

        while ((r-l+1) - topFreq > k) {
            const lChar = s[l]
            windowCount[lChar]--
            l++
        }

        longest = Math.max((r-l+1), longest)
        r++
    }

    return longest
};