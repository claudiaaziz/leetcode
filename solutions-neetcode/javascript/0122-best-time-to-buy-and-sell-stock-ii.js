// problem link https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
// time coplexity O(n)

var maxProfit = function(prices) {
    let maxProfit = 0;
    for(let i = 0; i < prices.length; i++) {
        if(prices[i] < prices[i+1]) {
            maxProfit += prices[i+1] - prices[i];
        }
    }

    return maxProfit;
};

// claudia
// t o(n) - s o(1)
var maxProfit = function(prices) {
    let minPrice = Infinity
    let currMax = 0
    let res = 0

    for (let i = 0; i < prices.length; i++) {
        minPrice = Math.min(minPrice, prices[i])
        currMax = Math.max(currMax, prices[i])
        if (prices[i+1] < prices[i] || i === prices.length-1) { // ab to be a dip so sell
            res += currMax - minPrice
            currMax = 0
            minPrice = Infinity
        }
    }

    return res
};

// t o(n) - s o(1)
var maxProfit = function(prices) {
    let minPrice = Infinity
    let profit = 0

    for (const currPrice of prices) {
        minPrice = Math.min(minPrice, currPrice)
        if (currPrice - minPrice > 0) { 
            profit += currPrice - minPrice
            minPrice = currPrice
        }
    }

    return profit
};
