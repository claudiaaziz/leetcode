/**
 * @param {number[]} piles
 * @param {number} h
 * Time O(N * log(M)) | Space O(1)
 * @return {number}
 */
var minEatingSpeed = function (piles, h) {
    let [left, right] = [1, Math.max(...piles)];

    while (left < right) {
        const mid = (left + right) >> 1;
        const hourSpent = getHourSpent(mid, piles);

        const isTargetGreater = h < hourSpent;
        if (isTargetGreater) left = mid + 1;

        const isTargetLess = hourSpent <= h;
        if (isTargetLess) right = mid;
    }

    return right;
};

const getHourSpent = (mid, piles, hourSpent = 0) => {
    for (const pile of piles) {
        hourSpent += Math.ceil(pile / mid);
    }

    return hourSpent;
};

// claudia
// time o(n log m) - space o(1)
const minEatingSpeed = (piles, h) => {
    let min = 1
    let max = Math.max(...piles)
    let best = max

    const totalTime = speed => piles.reduce((sum, pile) => sum + Math.ceil(pile / speed), 0)

    while (min <= max) {
        const mid = Math.floor((min + max) / 2)

        if (totalTime(mid) <= h) {
            best = mid
            max = mid - 1
        } else {
            min = mid + 1
        }
    }

    return best
};