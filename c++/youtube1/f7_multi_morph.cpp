#include <iostream>
#include <vector>
#include <string>
#include <fstream>
// multi morph

using namespace std;
class Animal{
	public:
		void getFamily(){cout << "We are animals" << endl;}
                virtual void getClass(){cout << "I am an animal" << endl;}
};

class Dog : public Animal{
	public:
		void getClass(){cout << "I am a dog" << endl;}
};

class GermanShepard : public Dog{
	public:
		void getClass(){cout << "I am a German Shepard" << endl;}
		void getDerived(){cout << "I am an Animal and dog" << endl;}
};

void whatClassAreYou(Animal *animal){
animal->getClass();
}


int main(){

	Animal *animal = new Animal;
	Dog *dog = new Dog;
	animal->getClass();
	dog->getClass();

	whatClassAreYou(animal);
	whatClassAreYou(dog);

        Dog spot;
	GermanShepard max;
	Animal* ptrDog = &spot;
	Animal* ptrGShepard = &max;

	ptrDog -> getFamily();
	ptrDog -> getClass();

	ptrGShepard -> getFamily();
	ptrGShepard -> getClass();
	//ptrGShepard -> getDerived();
        //max -> getDerived();









	return 0;
}

