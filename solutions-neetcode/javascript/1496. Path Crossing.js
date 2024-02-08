/**
 * @param {string} path
 * @return {boolean}
 */
var isPathCrossing = function(path) {
    //have a set to keep track of the coordinates
    let pathSoFar = new Set();

    //current coord
    let currCoord = [0, 0];
    pathSoFar.add(currCoord.join(','));

    //iterate thru the path and update the current coord
    for (let char of path) {
        //update curr
        if(char == "N"){
            currCoord[1] += 1;
        } else if (char == "S"){
            currCoord[1] -= 1;
        } else if (char == "E"){
            currCoord[0] += 1;
        } else {
            currCoord[0] -= 1;
        }
        //check if the current coord is in set
        let coordStr = currCoord.join(',');
        if(pathSoFar.has(coordStr)){
            //if it is, return true
            return true;
        } else{
            //if it's not, add to it
            pathSoFar.add(coordStr);
        }
    }
    
    //return false
    return false;
};

//[0, 0], [0,1], [1,1], [1,0], [0,0], [-1, 0]