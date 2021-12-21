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
    std::map<char, int> commonItemsBase;
    commonItemsBase['a'] = 0;
    commonItemsBase['b'] = 0;
    commonItemsBase['c'] = 0;
    commonItemsBase['d'] = 0;
    commonItemsBase['e'] = 0;
    commonItemsBase['f'] = 0;
    commonItemsBase['g'] = 0;
    commonItemsBase['h'] = 0;
    commonItemsBase['i'] = 0;
    commonItemsBase['j'] = 0;
    commonItemsBase['k'] = 0;
    commonItemsBase['l'] = 0;
    commonItemsBase['m'] = 0;
    commonItemsBase['n'] = 0;
    commonItemsBase['o'] = 0;
    commonItemsBase['p'] = 0;
    commonItemsBase['q'] = 0;
    commonItemsBase['r'] = 0;
    commonItemsBase['s'] = 0;
    commonItemsBase['t'] = 0;
    commonItemsBase['u'] = 0;
    commonItemsBase['v'] = 0;
    commonItemsBase['w'] = 0;
    commonItemsBase['x'] = 0;
    commonItemsBase['y'] = 0;
    commonItemsBase['z'] = 0;
    commonItems = commonItemsBase;
    std::string entry;
    std::string key;
    int value = 1;
    int lineNum = 0;
    while (getline(inFile, lineIn))
    {
        if (lineIn != "")
        {
            lineNum++;
            for (int i = 0; i < lineIn.size(); i++)
            {
                commonItems[lineIn[i]] = commonItems.find(lineIn[i])->second + 1;
            }
        }
        else
        {
            commonItems['L'] = lineNum;
            declarations.push_back(commonItems);
            commonItems = commonItemsBase;
            lineNum = 0;
        }
    }
    commonItems['L'] = lineNum;
    declarations.push_back(commonItems);
    std::map<char, int>::iterator current;
    int most = 0;
    int total = 0;
    for (int i = 0; i < declarations.size(); i++)
    {
        most = declarations[i].find('L')->second;
        declarations[i].erase('L');
        current = declarations[i].begin();
        while (current != declarations[i].end())
        {
            if (current->second == most)
            {
                total++;
            }
            ++current;
        }
    }
    std::cout << "Total: " << total << "\n";
    return 0;
}
