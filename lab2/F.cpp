#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
// F - Contest Scoreboard

struct Cont{
    int number;
    int solved;
    int penalty;
    bool submitted;
    vector<int> problemsSolved;
    int attempts[10];

    bool operator==(const Cont& c) const{
        return number == c.number;
    }
};

bool cont_sorter(Cont const& a, Cont const& b){
    if(a.solved != b.solved){
        return a.solved > b.solved;
    }
    else if(a.penalty != b.penalty){
        return a.penalty < b.penalty;
    }
    else{
        return a.number < b.number;
    }
}

int main(){
    int cases;
    cin >> cases;
    cin.ignore(256, '\n');
    string line;
    getline(cin, line);

    for(int i = 0; i < cases; i++){
        vector<Cont> contestants;

        while(getline(cin, line)){
            if(line.compare("") == 0){
                break;
            }

            int pos = line.find(" ");
            int number = stoi(line.substr(0, pos));
            line.erase(0, pos + 1);

            pos = line.find(" ");
            int problem = stoi(line.substr(0, pos));
            line.erase(0, pos + 1);

            pos = line.find(" ");
            int time = stoi(line.substr(0, pos));
            line.erase(0, pos + 1);

            char letter = line[0];

            auto it = find(contestants.begin(), contestants.end(), Cont{number});
            auto idx = it - contestants.begin();
            if(it != contestants.end()){
                auto it2 = find(contestants[idx].problemsSolved.begin(), contestants[idx].problemsSolved.end(), problem);
                if(it2 != contestants[idx].problemsSolved.end()){
                    continue; // user already solved this problem.
                }
                else if(letter == 'C'){
                    contestants[idx].solved++;
                    contestants[idx].penalty += (time + (contestants[idx].attempts[problem] * 20));
                    contestants[idx].problemsSolved.push_back(problem);
                }
                else if(letter == 'I'){
                    contestants[idx].attempts[problem]++;
                }
                contestants[idx].submitted = true;
                
            }
            else{
                Cont c = Cont{number};
                if(letter == 'C'){
                    c.solved++;
                    c.penalty += time;
                    c.problemsSolved.push_back(problem);
                }
                else if(letter == 'I'){
                    c.attempts[problem]++;
                }
                c.submitted = true;
                contestants.push_back(c);
            }

        }
        sort(contestants.begin(), contestants.end(), &cont_sorter);
        for(auto c : contestants){
            if(c.submitted){
                cout << c.number << " " << c.solved << " " << c.penalty << endl;
            }
        }
        if(i < cases - 1){
            cout << endl;
        }
        contestants.clear();
    }
    return 0;
}