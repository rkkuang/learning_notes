#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

class Animal{
	public:
		virtual void makeSound(){cout << "The Animal says grr" << endl;}
};

class Dog : public Animal{
	public:
		void makeSound(){cout << "The Dog says wolf" << endl;}

};

class Cat : public Animal{
	public:
		void makeSound(){cout << "The Cat says meow" << endl;}

};

class Car{
	public:
		virtual int getNumOfWheels() = 0;
		virtual int getNumOfDoors() = 0;
};

class StationWagon : public Car{
	public:
		int getNumOfWheels(){cout << "StationWagon has 4 wheels" << endl;}
		int getNumOfDoors(){cout << "StationWagon has 4 doors" << endl;}
		StationWagon(){}
		~StationWagon();
};



int main(){

	Animal* pCat = new Cat;
	Animal* pDog = new Dog;
	pCat -> makeSound();
	pDog -> makeSound();

	Car* stWagon = new StationWagon;
	stWagon -> getNumOfWheels();










	return 0;
}

