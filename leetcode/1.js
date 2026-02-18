function twoSumBruteForce(nums, target) {
    for (let i = 0; i < nums.length; i++){
        for (let j = i+1; j < nums.length;j++){
            if (nums[i] + nums[j] === target){
                return [i, j];
            }
        }
    }
}


/*
[5,4,6] => target 10

map = {
    5: 0,
    4: 1,
    6: 2
}

map[4] returns the value, which in this case is the INDEX


*/


function twoSumOptimization(nums, target){
    const numberToIndex = {};

    // build the map
    for (let i = 0; i < nums.length; i++){
        numberToIndex[nums[i]] = i;
    }

    for (let i = 0; i < nums.length; i++){
        let targetNum = target - nums[i];
        // if not undefined and can't be the same as the looping index
        if (numberToIndex[targetNum] !== undefined && numberToIndex[targetNum] !== i) {
            return [i, numberToIndex[targetNum]]
        }
    }
}