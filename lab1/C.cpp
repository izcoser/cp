#include <iostream>

// C - Relational Operator
//

int main(){
	int t;
	std::cin >> t;
	for(int i = 0; i < t; i++){
		int a;
		int b;
		// a, b < 1000000001
		// max int = 2147483647
		std::cin >> a;
		std::cin >> b;
		if(a > b){
			std::cout << '>' << std::endl;
		}
		else if (a < b){
			std:: cout << '<' << std::endl;
		}
		else{
			std::cout << '=' << std::endl;
		}

	}
	return 0;
}
