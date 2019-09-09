#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

int main(){

	string steveQuote = "A day without sunshine is like, you know, night";
	ofstream writer("steveQuote.txt");
	if (!writer){
	cout << "Error opening file" << endl;
	return -1;
	}else{
	writer << steveQuote << endl;
	writer.close();
	}

	ofstream writer2("steveQuote.txt", ios::app);
	// ios::app  - append
	// ios::binary - treat the file as binary
	// ios::in - open a file to read input
	// ios::trunc - Default
	// ios::out - open a file to write output
	if (!writer2){
	cout << "Error opening file" << endl;
	return -1;
	}else{
	writer2 << "\n -Steve Martin" << endl;
	writer2.close();
	}

	char letter;
	ifstream reader("steveQuote.txt");
	if(!reader){
	cout << "Error opening file" << endl;
        return -1;	
	}else{
	for(int i=0; !reader.eof(); i++){
	reader.get(letter);
	cout << letter;
	}

	cout << endl;
	reader.close();

	}




	return 0;
}

