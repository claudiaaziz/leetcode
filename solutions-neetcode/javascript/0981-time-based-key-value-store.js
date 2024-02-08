/**
 * Your TimeMap object will be instantiated and called as such:
 * var obj = new TimeMap()
 * obj.set(key,value,timestamp)
 * var param_2 = obj.get(key,timestamp)
 */
class TimeMap {
    constructor() {
        this.map = {};
    }

    /**
     * @param {string} key
     * @param {string} value
     * @param {number} timestamp
     * Time O(1) | Space O(1)
     * @return {void}
     */
    set(key, value, timestamp) {
        const bucket = this.map[key] || [];

        this.map[key] = bucket;

        bucket.push([value, timestamp]);
    }

    /**
     * @param {string} key
     * @param {number} timestamp
     * Time O(log(N)) | Space O(1)
     * @return {string}
     */
    get(key, timestamp, value = '', bucket = this.map[key] || []) {
        let [left, right] = [0, bucket.length - 1];

        while (left <= right) {
            const mid = (left + right) >> 1;
            const [guessValue, guessTimestamp] = bucket[mid];

            const isTargetGreater = guessTimestamp <= timestamp;
            if (isTargetGreater) {
                value = guessValue;
                left = mid + 1;
            }

            const isTargetLess = timestamp < guessTimestamp;
            if (isTargetLess) right = mid - 1;
        }

        return value;
    }
}

// claudia
// space o(n)
class TimeMap {
    constructor() {
        this.map = {}
    };

    // time o(1) - space o(1)
    set(key, value, timestamp) {
        this.map[key] = this.map[key] || []
        this.map[key].push({ value, timestamp })
    };

    // time o(log n) - space o(1)
    get(key, timestamp) {
        const vals = this.map[key] || []
        let res = ""
        let l = 0
        let r = vals.length - 1

        if (vals.length === 0) return "";
        if (timestamp < vals[0].timestamp) return "";

        while (l <= r) {
            const mid = Math.floor((l+r) / 2)

            if (vals[mid].timestamp === timestamp) {
                return vals[mid].value;
            } else if (vals[mid].timestamp < timestamp) {
                res = vals[mid].value
                l = mid + 1
            } else {
                r = mid - 1
            }
        }

        return res
    };
};