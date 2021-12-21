#include <iostream>
#include <vector>
#include <fstream>
#include <string>

int main()
{
    std::string fileName = "AOC31.dat";
    std::ifstream inFile;
    inFile.open(fileName);
    if (inFile.fail())
    {
        std::cout << "File open failure\n";
        return -1;
    }
    std::string lineIn;
    int numPatterns = 32;
    std::vector<std::vector<char>> landscape;
    std::vector<char> rowVec;
    while (getline(inFile, lineIn))
    {
        rowVec.clear();
        for (int i = 0; i < numPatterns; i++)
        {
            for (int j = 0; j < lineIn.size(); j++)
            {
                rowVec.push_back(lineIn[j]);
            }
        }
        landscape.push_back(rowVec);
    }
    char tree = '#';
    int nextR = 0;
    int treeCount = 0;
    for (int i = 1; i < landscape.size(); i++)
    {
        nextR = i * 3;
        if (landscape[i][nextR] == tree)
        {
            treeCount++;
        }
    }
    std::cout << "You encountered " << treeCount << " trees.\n";
    return 0;
}
