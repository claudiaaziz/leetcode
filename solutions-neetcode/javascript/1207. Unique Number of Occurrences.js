/**
 * @param {number[]} arr
 * @return {boolean}
 */
var uniqueOccurrences = function(arr) {
    //make a hash to keep track of the occurrences of each number
    let occur = {};
    arr.forEach((num) => {
        if(occur[num]){
            occur[num]+=1
        } else {
            occur[num]=1
        }
    })

    //check if all the values are unique
    let uniqueValues = new Set();
    //iterate through the values, add them to a set
    for(let num in occur){
        if (uniqueValues.has(occur[num])){
            return false;
        } else {
            uniqueValues.add(occur[num])
        }
    }

    return true;
};