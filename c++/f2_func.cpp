#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

int addNumbers(int firstNum, int secondNum = 0){
	int combinedValue = firstNum + secondNum;
	return combinedValue;
}

// you are able ot overload functions:
int addNumbers(int firstNum, int secondNum, int thirdNum){
	int combinedValue = firstNum + secondNum + thirdNum;
	return combinedValue;
}

int getFactorial(int number){

	int sum;
	if (number == 1) sum = 1;
	else sum = getFactorial(number - 1)*number;
	return sum;
}


int main(){

	cout << addNumbers(4) << endl;
	cout << addNumbers(4,5) << endl;
	cout << addNumbers(4,5,6) << endl;

	cout << "Factorial of 5: " << getFactorial(5) << endl
