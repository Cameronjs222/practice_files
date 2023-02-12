let nums = [-1,0,1,2,-1,-4]
var threeSum = function(nums) {
    output = []
    for (i=0;i<nums.length;i++){
        a = 0 - nums[i]
        for (j=0 && j !== i;j<nums.length;j++){
            b = a - nums[j]
            for (k=0 && k !== j;k<nums.length;k++){
                if (nums[k] + b == 0 && !output.includes(nums[i], nums[j], nums[k])){
                    output.push(nums[i], nums[j], nums[k])
                    console.log(output)
                }
            }
        }
    }
    return output
};
console.log(threeSum(nums))