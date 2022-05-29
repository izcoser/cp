#include <iostream>

// B - Heap Operations

using namespace std;

#include <queue>
#include <string>
#include <sstream>

int main(){
    priority_queue<int, vector<int>, greater<int>> pq;
    stringstream out;
    int opcount = 0;
    int N;
    cin >> N;
    for(int i = 0; i < N; i++){
        string op;
        cin >> op;

        if(op[0] == 'i'){
            int val;
            cin >> val;
            pq.push(val);
            out << (op + " " + to_string(val)) << endl;
            opcount++;
        }

        else if(op[0] == 'g'){
            int val;
            cin >> val;

            if(!pq.empty()){
                while(!pq.empty() && pq.top() < val){
                    pq.pop();
                    out << "removeMin" << endl;
                    opcount++;
                }
                if(pq.empty() || pq.top() > val){
                    pq.push(val);
                    out << "insert " + to_string(val) << endl;
                    opcount++;
                }
            }
            else{
                pq.push(val);
                out << "insert " + to_string(val) << endl;
                opcount++;
            }
            out << op + " " + to_string(val) << endl;
            opcount++;
        }
        else{
            if(pq.empty()){
                out << "insert 1" << endl;
                opcount++;
            }
            else{
                pq.pop();
            }
            out << "removeMin" << endl;
            opcount++;
        }
    }
    cout << opcount << endl;
    cout << out.str();
    return 0;
}
