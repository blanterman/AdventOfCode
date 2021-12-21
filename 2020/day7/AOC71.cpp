#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <map>
#include <sstream>

int main()
{
    std::string fileName = "AOC71.dat";
    std::ifstream inFile;
    inFile.open(fileName);
    if (inFile.fail())
    {
        std::cout << "File open failure\n";
        return -1;
    }
    std::string lineIn;
    while (getline(inFile, lineIn))
    {
    }
    return 0;
}
