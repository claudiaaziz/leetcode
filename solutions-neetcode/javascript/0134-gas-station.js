/**
 * https://leetcode.com/problems/gas-station/
 * Time: O(n)
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */
var canCompleteCircuit = function (gas, cost) {
  let netDistance = 0;
  let res = 0;

  //Checks if theres enough gas to complete a cycle
  if (gas.reduce((a, b) => a + b) - cost.reduce((a, b) => a + b) < 0) return -1;

  // Finds the first appearence of a positive netDistance, if the cycle can't
  // be completed (netDistance < 0), starts cycle again @ the next positive netDistance value.
  for (let i = 0; i < gas.length; i++) {
    netDistance += gas[i] - cost[i];

    if (netDistance < 0) {
      netDistance = 0;
      res = i + 1;
    }
  }

  return res;
};

/**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */
var canCompleteCircuit = function (gas, cost) {
  let [totalTank, currTank, startingStation] = [0, 0, 0];

  for (let i = 0; i < gas.length; i++) {
    totalTank += gas[i] - cost[i];
    currTank += gas[i] - cost[i];

    const isEmpty = currTank < 0;
    if (isEmpty) {
      startingStation = i + 1;
      currTank = 0;
    }
  }

  return 0 <= totalTank ? startingStation : -1;
};

// claudia
// t o(n) - s o(1)
var canCompleteCircuit = function(gas, cost) {
    let startingStation = 0 
    let currentTank = 0 
    let totalTank = 0

    for (let i = 0; i < gas.length; i++) {
        const netCost = gas[i] - cost[i]
        currentTank += netCost
        totalTank += netCost
        
        if (currentTank < 0) {
            startingStation = i+1
            currentTank = 0
        }
    }

    return totalTank < 0 ? -1 : startingStation
};