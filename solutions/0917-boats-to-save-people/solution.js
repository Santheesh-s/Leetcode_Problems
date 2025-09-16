/**
 * @param {number[]} people
 * @param {number} limit
 * @return {number}
 */
var numRescueBoats = function(people, limit) {
    let boat=0;
        let left=0,right=people.length-1;
        people.sort((a, b) => a - b);  // Correct numeric sort

        while(left < right)
        {
            if(people[left]+people[right] <= limit)
            {
                boat++;
                left++;
                right--;
            }
            else
            {
                if(people[right]<=limit)
                    boat++;
                right--;
            }
            if(left==right)
                boat++;
        }
        return boat;
};
