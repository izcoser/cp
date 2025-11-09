#include <vector>
#include <unordered_map>
using std::vector;
using std::unordered_map;
// https://leetcode.com/problems/two-sum/
// O(n) solution

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> numToIndex;
        
        for(int i = 0; i < nums.size(); i++){
            int complement = target - nums[i];
            if(numToIndex.find(complement) != numToIndex.end()){
                return {numToIndex[complement], i};
            }
            numToIndex.insert_or_assign(nums[i], i);
        }

        return {};
    }
};