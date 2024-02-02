/**
 * https://leetcode.com/problems/car-fleet
 * Time O(N * log(N)) | Space O(N)
 * @param {number} target
 * @param {number[]} position
 * @param {number[]} speed
 * @return {number}
 */
var carFleet = function(target, position, speed) {
    const coordinates = getCoordinates(target, position, speed);    /* Time O(N * log(N)) | Space O(N) */

    return searchAscending(coordinates);                            /* Time O(N)          | Space O(N) */
};

var getCoordinates = (target, position, speed) => position
    .map((_position, index) => [ _position, speed[index] ])         /* Time O(N)          | Space O(N) */
    .sort(([ aPosition ], [ bPosition ]) => aPosition - bPosition)  /* Time O(N * log(N)) | HeapSort Space 0(1) | QuickSort Space O(log(N)) */
    .map(([ _position, _speed ]) => (target - _position) / _speed); /* Time O(N)          | Space O(N) */

var searchAscending = (coordinates, stack = []) => {
    for (const coordinate of coordinates) {                         /* Time O(N + N) */
        shrink(coordinate, stack);                                  /* Time O(N + N) */
        stack.push(coordinate);                                     /* Space O(N) */
    }

    return stack.length;
}

const shrink = (coordinate, stack) => {
    const isPreviousLess = () => stack[stack.length - 1] <= coordinate;
    while (stack.length && isPreviousLess()) stack.pop();                /* Time O(N + N) */
}

/**
 * https://leetcode.com/problems/car-fleet
 * Time O(N * log(N)) | Space O(N)
 * @param {number} target
 * @param {number[]} position
 * @param {number[]} speed
 * @return {number}
 */
 var carFleet = function(target, position, speed) {
    const coordinates = getCoordinates(target, position, speed);   /* Time O(N * log(N)) | Space O(N) */

    return searchDescending(coordinates);                          /* Time O(N) */
};

var getCoordinates = (target, position, speed) => position
    .map((_position, index) => [ _position, speed[index] ])        /* Time O(N)          | Space O(N) */
    .sort(([ aPosition ], [ bPosition ]) => bPosition - aPosition) /* Time O(N * log(N)) | HeapSort Space 0(1) | QuickSort Space O(log(N)) */
    .map(([ _position, _speed ]) => (target - _position) / _speed);/* Time O(N)          | Space O(N) */

var searchDescending = (coordinates, previous = 0, fleets = 0) => {
    for (const coordinate of coordinates) {                        /* Time O(N) */
        const isPreviousLess = previous < coordinate
        if (!isPreviousLess) continue

        previous = coordinate
        fleets++
    }

    return fleets;
}

// claudia
// time o(n log n) - space o(n) 
const carFleet = (target, position, speed) => {
    const n = position.length
    const indices = []
    for (let i = 0; i < n; i++) indices.push(i)
    indices.sort((a, b) => position[b] - position[a])

    let curr = indices[0]
    let res = 1

    for (let i = 1; i < indices.length; i++) {
        const idx = indices[i]
        if ((target - position[idx]) * speed[curr] > (target - position[curr]) * speed[idx]) {
            res++
            curr = idx
        }
    }

    return res
};