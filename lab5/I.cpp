#include <iostream>
using namespace std;

int maxBookCount = 0;

int main(){
        int n, t;
        cin >> n >> t;
        int ns[n];
        for(int i = 0; i < n; i++){
            cin >> ns[i];
        }
        
        int timeCount = 0;
        int bookCount = 0;
        int startAt = 0;
        bool end = false;
        
        for(int i = 0; i < n && !end; i++){
            for(int j = startAt; j < n; j++){
                if(ns[j] + timeCount <= t){
                    timeCount += ns[j];
                    bookCount++;
                    if(bookCount > maxBookCount){
                        maxBookCount = bookCount;
                    }
                    if(j == n - 1){
                        end = true;
                    }
                }
                else{
                    bookCount--;
                    timeCount -= ns[i];
                    startAt = j;
                    break;
                }
            }
        }

        cout << maxBookCount << endl;
}
