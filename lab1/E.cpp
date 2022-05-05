#include <iostream>

// E - Cost Cutting
//

int middle(int a, int b, int c){
	if((a > b && a < c) || (a < b && a > c)){
		return a;
	}
	if((b > a && b < c) || (b < a && b > c)){
		return b;
	}
	return c;
}

int main(){
	int T;
	std::cin >> T;
	for(int i = 0; i < T; i++){
		int a;
		int b;
		int c;
		std::cin >> a;
		std::cin >> b;
		std::cin >> c;
		std::cout << "Case " + std::to_string(i + 1) + ": " << middle(a, b, c) << std::endl;
	}
	return 0;
}

