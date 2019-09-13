#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

void makeMeYoung(int* age){
cout << "I used to be " << *age << endl;
*age = 21;
}

void actYourAge(int& age){
age = 89;
}

int main(){

	int myAge = 30;
	char myGrade = 'A';

	int* agePtr = &myAge;

	cout << "Size of int " << sizeof(myAge) << endl;
	cout << "Size of char " << sizeof(myGrade) << endl;
	cout << "myAge is locate at " << &myAge << endl;
        cout << "Address of pointer " << agePtr << endl;
	cout << "Data at momory address " << *agePtr << endl;

	int badNums[5] = {2,3,4,5,1};
	int* numArrayPtr = badNums;
	cout << "Address " << numArrayPtr << " Value " << *numArrayPtr << endl;
	numArrayPtr++;
	cout << "Address " << numArrayPtr << " Value " << *numArrayPtr << endl;
	cout << "Address " << badNums << " Value " << *badNums << endl;

        makeMeYoung(&myAge);
	cout << "Now I am " << myAge << " years old" << endl;

	int& ageRef = myAge;
	cout << "myAge : " << myAge << endl;
	cout << "ageRef : " << ageRef << endl;
	cout << "ageRef : " << &ageRef << endl;
	ageRef++;
	cout << "myAge : " << myAge << endl;
	(*agePtr)++;
	cout << "myAge : " << myAge << endl;
        

	actYourAge(ageRef);
	cout << "myAge : " << myAge << endl;
        


	// pointer no need to be initialized when created, and pointer can point to other variables all the time
	// while reference need to be initiallized when created, and once created, reference is stick to only one variable.



	return 0;
}

