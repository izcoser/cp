#include <iostream>
using namespace std;

/*

Recursive way of generating subsets.
Suppose the set is {1, 2, 3}, let s be a subset:

                                Is 1 in s?
                            /               \
                           / no              \ yes # Rest of the tree omitted.
                          v                   v
                       
                       Is 2 in s?
                     /           \
                    / no          \ yes
                   v               v

           Is 3 in s?           Is 3 in s?
          /       \               |       \
         / no      \ yes          | no     \ yes
        v           v             v         v

      { }          { 3 }        { 2 }      { 2 3 }

This algorithm will generate the subsets and immediately their supersets.
That is useful because we don't care about the supersets once the subset sum
has already exceeded N, so we can easily ignore them.

We use an auxiliary boolean array of size N to generate subsets with this method.

*/

int S[5] = {1, 2, 3, 4, 5};
int N = 5;

void printCombinations(bool combs[], int begin, int n){
    if(begin >= n){
        cout << '{' << ' ';
        for(int i = 0; i < n; i++){
            if(combs[i]){
                cout << S[i] << ' ';
            }
        }
        cout << '}' << endl;
    }
    else{
        combs[begin] = 0;
        printCombinations(combs, begin + 1, n);
        combs[begin] = 1;
        printCombinations(combs, begin + 1, n);
    }
}

int main(){
    bool combs[N];
    printCombinations(combs, 0, N);
    return 0;
}
