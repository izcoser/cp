#include <iostream>

// F - Horror Dash
//

int main(){
	int T;
	std::cin >> T;
	for(int i = 0; i < T; i++){
		int N;
		std::cin >> N;
		int s;
		int max_s = -1;
		for(int i = 0; i < N; i++){
			std::cin >> s;
			if(s > max_s){
				max_s = s;
			}
		}
		std::cout << "Case " << std::to_string(i + 1) << ": " << max_s << std::endl;
	}
	return 0;
}

