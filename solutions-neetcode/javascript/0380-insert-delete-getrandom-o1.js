var RandomizedSet = function () {
    this.set = new Set();
};

/**
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.insert = function (val) {
    const res = !this.set.has(val);
    if (res) {
        this.set.add(val);
    }
    return res;
};

/**
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.remove = function (val) {
    return this.set.delete(val);
};

/**
 * @return {number}
 */
RandomizedSet.prototype.getRandom = function () {
    const keys = Array.from(this.set.keys());
    const seed = Math.floor(Math.random() * keys.length);
    return keys[seed];
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * var obj = new RandomizedSet()
 * var param_1 = obj.insert(val)
 * var param_2 = obj.remove(val)
 * var param_3 = obj.getRandom()
 */

// claudia
// t o(1) - s o(n)
class RandomizedSet {
    constructor() {
        this.map = new Map()
        this.array = []
    }

    insert(val) {
        if (this.map.has(val)) return false
        this.map.set(val, this.array.length)
        this.array.push(val)
        return true
    };

    remove(val) {
        if (!this.map.has(val)) return false
        const idx = this.map.get(val)
        this.array[idx] = this.array[this.array.length-1]
        this.map.set(this.array[idx], idx)

        this.array.pop()
        this.map.delete(val)
        return true
    };

    getRandom() {
        const randomIdx = Math.floor(Math.random() * this.array.length)
        return this.array[randomIdx]
    };
};