#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <map>
#include <sstream>

int main()
{
    std::string fileName = "AOC61.dat";
    std::ifstream inFile;
    inFile.open(fileName);
    if (inFile.fail())
    {
        std::cout << "File open failure\n";
        return -1;
    }
    std::string lineIn;
    std::vector<std::map<char, int>> declarations;
    std::map<char, int> commonItems;
    std::string entry;
    std::string key;
    int value = 1;
    while (getline(inFile, lineIn))
    {
        if (lineIn != "")
        {
            for (int i = 0; i < lineIn.size(); i++)
            {
                commonItems[lineIn[i]] = value;
            }
        }
        else
        {
            declarations.push_back(commonItems);
            commonItems.clear();
        }
    }
    declarations.push_back(commonItems);
    int total = 0;
    for (int i = 0; i < declarations.size(); i++)
    {
        total += declarations[i].size();
    }
    std::cout << "Total: " << total << "\n";
    /*
    std::cout << declarations.size() << "\n";
    std::map<char, int> toPrint;
    toPrint = declarations[4];
    std::map<char, int>::iterator current = toPrint.begin();
    while (current != toPrint.end())
    {
        std::cout << current->first << ":" << current->second << "\n";
        ++current;
    }
    */
    return 0;
}
