#include <iostream>
#include <string>
#include <stack>
#include <set>

using namespace std;

set<string> outputset;
stack<string> output;

void stackSumsEqualToN(int ns[], bool combs[], int begin, int len, int sum, int N){
    if(begin >= len){
        if(sum == N){
            bool first = true;
            string s = "";
            for(int i = 0; i < len; i++){
                if(combs[i]){
                    s += (first ? to_string(ns[i]) : "+" + to_string(ns[i]));
                    first = false;
                }
            }
            s += "\n";
            if(outputset.find(s) == outputset.end()){
                output.push(s);
                outputset.insert(s);
            }
        }
    }
    else if(sum > N){
        return;
    }
    else{
        combs[begin] = false;
        stackSumsEqualToN(ns, combs, begin + 1, len, sum, N);
        combs[begin] = true;
        stackSumsEqualToN(ns, combs, begin + 1, len, sum + ns[begin], N);
    }
}


int main(){
    while(1){
        int t, n;
        cin >> t >> n;
        if(n == 0){
            break;
        }
        
        int ns[n];
        bool combs[n];
        for(int i = 0; i < n; i++){
            cin >> ns[i];
        }
        
        stackSumsEqualToN(ns, combs, 0, n, 0, t);
        outputset.clear();
        cout << "Sums of " << t << ":" << endl;
        if(output.empty()){
            cout << "NONE" << endl;
        }
        else{
            while(!output.empty()){
                cout << output.top();
                output.pop();
            }
        }

    }
}
