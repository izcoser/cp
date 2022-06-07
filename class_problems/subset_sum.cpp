#include<iostream>
#define ULL unsigned long long int

/*

Problem: Given a set of positive integers S and
an integer X, find all subsets which have a sum equal to X.

Possible solution: Because a set with N elements will have 2^N subsets,
we can use integers from 0 to N - 1 to represent all subsets,
where each tells whether or not an element is in the subset.

Example for S = { 1, 2, 3 }:

Decimal     Binary      Subset
0           000         { }
1           001         { 1 }
2           010         { 2 }
3           011         { 1, 2 }
4           100         { 3 }
5           101         { 1, 3 }
6           110         { 2, 3 }
7           111         { 1, 2, 3}

Then just sum the elements of the subset and compare to X.

*/

using namespace std;

int N = 3;
int S[3] = {1,2,3};
int X = 5;

bool solve() {
	for (ULL i = 0; i < (1LLU << N); i++) { // all subsets
    int sum = 0;
		for (int j = 0; j < N; j++) {
  		if (i & (1 << j)) {
			  sum += S[j];
		  }
	  }
    if (sum == X) {
			return true;
		}
  }
  return false;
}

int main() {
	bool found = solve();

	if (found) 
		cout << "YES" << endl;
	else
		cout << "NO" << endl;
	return 0;
}
