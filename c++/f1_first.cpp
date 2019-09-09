#include <iostream>
#include <vector>
#include <string>
#include <fstream>

//This is a comment
//
/*
 Multi line comment

 int main(){
 std::cout
 }

or:

using namespace std;


*/

using namespace std;

int main(){

	cout << "Hello World" << endl;
        
	const double PI = 3.1415926535;
	char myGrade = 'A';//must be ' not "
	bool isHappy = true;
	int myAge = 22;
	float favNum = 3.14;
	double otherfavNum = 1.3434343434;

	cout << "Favorite Number:" << favNum << endl;

	cout << "Size of int:" << sizeof(myAge)
		<< endl;

	int largestInt = 2147483647;
	cout << "Largest int: " << largestInt << endl;

	largestInt += 1;
	cout << "Largest int: " << largestInt << endl;

	int five = 5;
	cout << "5++ = " << five++ << endl;
	cout << "++5 = " << ++five << endl;
	cout << "5-- = " << five-- << endl;
	cout << "--5 = " << --five << endl;

	cout << "4/5 = " << 4/5 << endl;
	cout << "4/5 = " << (float)4/5 << endl;


	// if, not equal: !=, && || !
	//

	int age = 70;
	int ageAtLastExam = 16;
	bool isNotIntoxicated = true;

	if((age>=1)&&(age<16)){
	cout << "you can not drive" << endl;
	}else if(!isNotIntoxicated){
	cout << "you can not drive" << endl;
	}else if(age>80 && ((age>100)||((age-ageAtLastExam)>5))){
	cout << "you can not drive" << endl;	
	}else{
	cout << "you can drive" << endl;
	}

	int greetingOption = 2;
	switch(greetingOption){
		case 1:
			cout << "bonjour" << endl;
			break;
		case 2:
			cout << "hola" << endl;
			break;
		case 3:
			cout << "hallo" << endl;
			break;
		default:
			cout << "hello" << endl;
	}

	// variable = (condition) ? value_if_true : value_if_false
	//


	int largerNum = (5>2)?5:2;

	// array
	
	int myFavNums[5]; // 5 numbers
	int badNums[5] = {3,2,2,1,4};

	cout << "Bad Number 1: " << badNums[0] << endl;

	char myName[5][5] = {{'r','e','n','k','u'},
		{'k','u','a','n','g'}
	};

	cout << "2nd letter in 2nd array: " << myName[1][1]  << endl;

	myName[0][2] = 'e';
	cout << "3rd letter in 1st array: " << myName[0][2]  << endl;

	
	for(int i=1;i<=10;i++){
	cout << i << endl;
	}
	for(int j=0;j<5;j++){
	for(int k=0;k<5;k++){
	cout << myName[j][k];
	}
	cout << endl;
	}
        

	// while loops
        
	int randNum = (rand() % 100 ) + 1;
	while(randNum!=100){
	cout << randNum << ",";
	randNum = (rand()%100)+1;
	}
	cout << endl;

	// do while, user input
	string numberGuessed;
	int intNumberGuessed = 0;
	do{
	cout << "Guess between 1 and 10: ";
	
	getline(cin, numberGuessed);

	// stod: converts from string to double
	// stoi: converts from string to int
	intNumberGuessed = stoi(numberGuessed);

	cout << intNumberGuessed << endl;

	}while(intNumberGuessed != 4);

	cout << "You win" << endl;

	char happyArray[6] = {'H','a','p','p','y','\0'};
	string birthdayString = " Birthday";

	cout << happyArray + birthdayString << endl;

	string yourName;
	cout << "What is your name: ";
	getline(cin, yourName);
	cout << "hello " << yourName << endl;

	double eulersConstant = .57721;
	string eulersGuess;
	double eulersGuessDouble;

	cout << "What is Euler's Constant? ";

	getline(cin, eulersGuess);
	eulersGuessDouble = stod(eulersGuess);
	if (eulersGuessDouble == eulersConstant){
	cout << "you are right" << endl;
	}else{
	cout << "you are wrong" << endl;
	}

	cout << "Size of String: " << eulersGuess.size() << endl;
	cout << "Is string empty? " << eulersGuess.empty() << endl;
	cout << eulersGuess.append(" was your guess") << endl;

	string dogString = "dog";
	string catString = "cat";
	cout << dogString.compare(catString) << endl;
	cout << dogString.compare(dogString) << endl;
	cout << catString.compare(dogString) << endl;

	string wholeName = yourName.assign(yourName);
	cout << wholeName << endl;
	string firstName = wholeName.assign(wholeName,0,5);
	cout << firstName << endl;

	int lastNameIndex = yourName.find("Kuang",0);
	cout << "Index for last name " << lastNameIndex << endl;

	yourName.insert(5, "Just");
	cout << yourName << endl;

        yourName.erase(6,7);
	cout << yourName << endl;

	yourName.replace(6,5,"Maxi");
	cout << yourName << endl;

	

	
	vector <int> lotNumVect(10);
	int lotNumArray[5] = {4,1,2,5,3};
	lotNumVect.insert(lotNumVect.begin(), lotNumArray,lotNumArray+3);
	cout << "init" << lotNumVect.back() << endl;
	cout << lotNumVect.at(2) << endl;

	lotNumVect.insert(lotNumVect.begin()+5,44);
	cout << lotNumVect.at(5) << endl;

	lotNumVect.push_back(64);
	cout << lotNumVect.back() << endl;
	cout << "Final Value: " << lotNumVect.back() << endl;
	lotNumVect.pop_back();
	cout <<"After pop_back: "<< lotNumVect.back() << endl;

	cout << "First Value: " << lotNumVect.front() << endl;
	cout << "Is empty: " << lotNumVect.empty() << endl;
	cout << "Vector Size: " << lotNumVect.size() << endl;
        























































	/*
	 *other type:
	 short int: >= 16 bits
	 long int: >= 32 bits
	 long long int: >= 64 bits
	 usigned int: same as signed version
	 long double: >= double
	 *
	 * */

	return 0;
}

// using following code to compile and run
// g++ -std=c++11 f1_first.cpp -o f1_first.out && ./f1_first.out
// -std=c++11 means using the version 11 of c++
