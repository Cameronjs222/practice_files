let nums = [-1,0,1,2,-1,-4];

var threeSum = function(nums) {
    let output = [];
    for (i=0;i<nums.length-2;i++){
        for (j=i+1;j<nums.length-1;j++){
            for (k=j+1;k<nums.length;k++){
                if (nums[i] + nums[j] + nums[k] == 0){
                    let solution = [nums[i], nums[j], nums[k]].sort();
                    let found = false;
                    for (let l=0;l<output.length;l++){
                        if (output[l].toString() == solution.toString()){
                            found = true;
                            break;
                        }
                    }
                    if (!found){
                        output.push(solution);
                    }
                }
            }
        }
    }
    return output;
};

console.log(threeSum(nums))
