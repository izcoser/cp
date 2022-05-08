#include <iostream>

// B - Loansome Car Buyer 

int main(){
    while(1){
        int duration;
        double downPayment;
        double loan;
        int records;

        std::cin >> duration;
        std::cin >> downPayment;
        std::cin >> loan;
        std::cin >> records;

        if(duration < 0){
            break;
        }

        std::cin.ignore(256, '\n');

        double depreciations[duration + 1] = { 0 }; // or duration?

        for(int i = 0; i < records; i++){
            int monthNumber;
            double depreciation;
            std::cin >> monthNumber;
            std::cin >> depreciation;
            depreciations[monthNumber] = depreciation;
        }

        double prevDepreciation = depreciations[0];
        for(int i = 1; i < duration + 1; i++){ // fill array for all months
            if(depreciations[i] < 1.0 / 100000000000000){
                depreciations[i] = prevDepreciation;
            }
            prevDepreciation = depreciations[i];
        }

        double carValue = loan + downPayment;
        double monthlyPayment = loan / duration;
 
        for(int i = 0; i < duration + 1; i++){
            carValue *= (1 - depreciations[i]);
            double owed = loan - i * monthlyPayment;
 
            if(carValue > owed){
                std::cout << std::to_string(i) << (i == 1 ? " month" : " months") << std::endl;
                break;
            }
        }

    }
    return 0;

}