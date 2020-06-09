#include"diaglib.hpp"
#include <iostream>
#include <fstream>

using namespace std;

/* Local prototypes */
bool validate_string(string id);


/* Public APIs */
void Diagnostic_Raise_DTC(string id)
{
    if( !validate_string(id) )
    {
	cout << "diaglib: Invalid DTC\n";
	return;
    }
    
    ofstream myfile;
    myfile.open("/tmp/diag_storage.txt", std::ios_base::app);
    myfile << id << "\n";
    myfile.close();
}

void Diagnostic_Clear_All_DTC()
{
    ofstream myfile;
    myfile.open("/tmp/diag_storage.txt");
    myfile << "";
    myfile.close();
}

string Diagnostic_Read_All_DTC()
{
    string resL = "";
    string line = "";
    ifstream myfile ("/tmp/diag_storage.txt");

    if (myfile.is_open())
    {
	while ( getline (myfile,line) )
	{
	    resL = resL + line + '\n';
	    //cout << "current line = " << line << endl;
	    //cout << "current resl = " << resL << endl;
	}
	
	myfile.close();
    }

    else
	cout << "diaglib: File error\n"; 

    return resL;
}

/*Local functs*/
bool validate_string(string id)
{    
    if( id.length() != 5 ) {
	//cout << "len err\n";
	return false;
    }
    
    if( id.at(0) < 'A' || id.at(0) > 'Z' ) {
	//cout << "A-Z err\n";
	return false;
    }

    for(int i  = 1; i < 5; i++)
    {
	if( id.at(i) < '0' || id.at(i) > '9' ) {
	    //cout << "0-9 err\n";
	    return false;
	}
    }
    
    return true;
}
