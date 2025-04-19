/**
 * @param {number[]} position
 * @return {number}
 */
var minCostToMoveChips = function(position) {
    let e=0,o=0;
    for(let i=0;i<position.length;i++)
    {
        if((position[i]&1))
            o++;
        else
            e++;
    }
    return o<e?o:e;
};
