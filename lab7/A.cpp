#include <iostream>
using namespace std;

int w[105] = { 0 };
int v[105] = { 0 };
long long int F[105][100005] = { 0 };

long long int MFKnapsack(int i, int j){
    long long int val;
    if(F[i][j] < 0){
        if(j < w[i]){
            val = MFKnapsack(i - 1, j);
        }
        else{
            val = max(MFKnapsack(i - 1, j), v[i] + MFKnapsack(i - 1, j - w[i]));
        }
        F[i][j] = val;
    }
    return F[i][j];
}

int main(){
    int N, W;
    cin >> N >> W;

    for(int i = 1; i < N + 1; i++){
        for(int j = 1; j < W + 1; j++){
            F[i][j] = -1;
        }
    }

    w[0] = 1;
    v[0] = -1;
    for(int i = 1; i < N + 1; i++){
        cin >> w[i];
        cin >> v[i];
    }

    cout << MFKnapsack(N, W) << endl;
    return 0;
}
