#include <iostream>

// D - Division of Nlogonia

int main(){
	while(1){

		int K;
		std::cin >> K;
		if(K == 0){
			break;
		}
		int N;
		int M;
		std::cin >> N;
		std::cin >> M;
		for(int i = 0; i < K; i++){
			int X;
			int Y;
			std::cin >> X;
			std::cin >> Y;

			if(X < N && Y > M){
				std::cout << "NO" << std::endl;
			}
			else if(X > N && Y > M){
				std::cout << "NE" << std::endl;
			}
			else if(X > N && Y < M){
				std::cout << "SE" << std::endl;
			}
			else if(X < N && Y < M){
				std::cout << "SO" << std::endl;
			}
			else{
				std::cout << "divisa" << std::endl;
			}

		}
	}
	return 0;
}
