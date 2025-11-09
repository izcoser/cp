#include <vector>
using std::vector;
// https://leetcode.com/problems/container-with-most-water/

class Solution {
public:
    int maxArea(vector<int>& height) {
        int max = 0;
        int l = 0;
        int r = height.size() - 1;

        while(l != r){
            int min_height = height[l] < height[r] ? height[l] : height[r];
            int area = min_height * (r - l);
            if(area > max){
                max = area;
            }
            if(height[l] > height[r]){
                r--;
            }
            else{
                l++;
            }
        }
        return max;
        
    }
};