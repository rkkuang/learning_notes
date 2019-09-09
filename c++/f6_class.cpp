#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

class Animal{
// Attributes: height weight --> variables
// Capabilities: Run Eat --> functions/methods

	private: // means these variables can only be modified by methods within class Animal
		int height;
		int weight;
		string name;

		// static means the value of this variable is going to be share by every object of type Animal that was ever created
		static int numOfAnimals;
	public:
		int getHeight(){return height;}
		int getWeight(){return weight;}
		string getName(){return name;}
		void setHeight(int cm){height = cm;}
		void setWeight(int kg){weight = kg;}
		void setName(string animalName){name = animalName;}

		void setAll(int,int,string);//a prototype

		Animal(int, int, string);

		// destructor
		~Animal();

		//overload
		Animal();

		static int getNumOfAnimals(){return numOfAnimals;}

		void toString();

};



// declare
int Animal::numOfAnimals = 0;

// make the prototype function in class specific
// Animal::setAll is just a example of how regular function can be constructed.
void Animal::setAll(int height, int weight, string animalName){

	this -> height = height;
	this -> weight = weight;
	this -> name = animalName;
        Animal::numOfAnimals++;

}

Animal::Animal(int height, int weight, string animalName){

	this -> height = height;
	this -> weight = weight;
	this -> name = animalName;
        Animal::numOfAnimals++;

}

Animal::Animal(){
        Animal::numOfAnimals++;
}


Animal::~Animal(){
cout << "Animal " << this -> name << " destroyed" << endl;
}

void Animal::toString(){
cout << this -> name << " is " << this -> height <<
	" cms tall and " << this -> weight << " kgs in weight" << endl; 
}



// inheritate
class Dog : public Animal{
	private:
		string sound = "Woof";
	public:
                // void getSound(){cout << sound << endl;}
		string getSound(){return sound;}
                // constructor
		Dog(int, int, string, string);
		Dog() : Animal(){};
		void toString();
};

Dog::Dog(int height, int weight, string name, string bark):
	Animal(height,weight,name){
	this -> sound = bark;
	}

void Dog::toString(){
cout << this -> getName() << " is " << this -> getHeight() << " cms tall and " << this -> getWeight() << " kgs in weight and says " << this -> getSound() << endl;
}


int main(){

	Animal zhuzhu;

	zhuzhu.setHeight(33);
	zhuzhu.setWeight(50);
	zhuzhu.setName("zhuzhu");

        cout << zhuzhu.getName() << " is " << zhuzhu.getHeight() <<
	" cms tall and " << zhuzhu.getWeight() << " kgs in weight" << endl;

	Animal tom(36,30,"tom");
        cout << tom.getName() << " is " << tom.getHeight() <<
	" cms tall and " << tom.getWeight() << " kgs in weight" << endl;

        Dog spot(38,16,"spot","Wolfff");
	cout << "Number of Animals : " << Animal::getNumOfAnimals() << endl;

	spot.getSound();
	tom.toString();
	spot.toString();

	////spot's animal version of toString
	spot.Animal::toString();
	return 0;
}












