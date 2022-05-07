#include <iostream>
#include <string>
// A - A request for Proposal 

int main(){
    int rfp = 1;
    while(1){
        int n;
        int p;
        std::string req;
        std::string prop;
        float d;
        int r;
        int compliance;

        int highestCompliance = 0;
        float lowestPrice = -1;
        std::string selectedProposal;

        std::cin >> n;
        std::cin >> p;

        if(n + p == 0){
            break;
        }
        if(rfp > 1){
            std::cout << std::endl;
        }

        std::cin.ignore(256, '\n');
        for(int i = 0; i < n; i++){
            getline(std::cin, req);
        }

        for(int i = 0; i < p; i++){
            getline(std::cin, prop);
            std::cin >> d;
            std::cin >> r;
            compliance = r;

            if(lowestPrice == -1){
                lowestPrice = d;
            }

            if(compliance > highestCompliance){
                highestCompliance = compliance;
                lowestPrice = d;
                selectedProposal = prop;
            }
            else if(compliance == highestCompliance && d < lowestPrice){
                lowestPrice = d;
                selectedProposal = prop;
            }

            std::cin.ignore(256, '\n');
            for(int i = 0; i < r; i++){
                getline(std::cin, req);
            }

        }

        std::cout << "RFP #" << std::to_string(rfp) << std::endl;
        std::cout << selectedProposal << std::endl;

        rfp++;
    }
    return 0;

}