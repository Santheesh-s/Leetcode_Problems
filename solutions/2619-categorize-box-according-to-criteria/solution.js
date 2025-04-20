/**
 * @param {number} length
 * @param {number} width
 * @param {number} height
 * @param {number} mass
 * @return {string}
 */
var categorizeBox = function(length, width, height, mass) {
    let b=0,h=0;
    let a=1;
    a*=length;
    a*=height;
    a*=width;
    if(length>=10000 ||width>=10000 ||height>=10000 || a>=1000000000)
        b=1;
    if(mass>=100)
        h=1;
    if(b && h)
        return "Both";
    else if(!b && !h)
        return "Neither";
    else if(b && !h)
        return "Bulky";
    return "Heavy";
};
