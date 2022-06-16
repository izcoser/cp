#include <iostream>
using namespace std;

/*

Another subset sum approach, now generating the sets as in
subset_sum_reloaded.cpp but now pruning dead branches of 
the search space.

*/

int X = 12;
int N = 5;
int S[5] = {1, 2, 3, 4, 5};

bool combs[5];

bool solve(int begin, int n, int curSum){
    if(begin >= n){
        if(curSum == X){
            return true;
        }
        return false;
    }
    else if(curSum > X){
        return false;
    }
    else{
        combs[begin] = false;
        bool without = solve(begin + 1, n, curSum);
        combs[begin] = true;
        bool with = solve(begin + 1, n, curSum + S[begin]);
        return with or without;
    }
}

int main(){
    cout << solve(0, N, 0) << endl;
    return 0;
}
