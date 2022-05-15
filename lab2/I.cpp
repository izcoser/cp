#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int n = 0;
    cin >> n;
    int times[n];
    for(int i = 0; i < n; i++){
        cin >> times[i]; 
    }
    sort(times, times + n);
 
    long long int sum = 0;
    int notDisappointed = 0;
    for(int i = 0; i < n; i++){
        if(sum <= times[i]){
            notDisappointed++;
            sum += times[i];
        }
    }
    cout << notDisappointed << endl;
}