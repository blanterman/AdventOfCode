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
	int numPatterns = 73;
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

	std::vector<std::vector<int>> slopes{ { 1, 1 },	{ 3, 1 }, { 5, 1 }, { 7, 1 }, { 1, 2 } };
	
	int nextR = 0;
	int nextD = 0;
	int treeCount = 0;
	long long answer = 1;
	for (int s = 0; s < slopes.size(); s++)
	{
		nextR = 0;
		treeCount = 0;
		for (int i = slopes[s][1]; i < landscape.size(); i = i + slopes[s][1])
		{
			nextR = (i  * slopes[s][0]) / slopes[s][1];
			if (landscape[i][nextR] == tree)
			{
				treeCount++;
			}
		}
		answer = answer * treeCount;
		std::cout << "You encountered " << treeCount << " trees.\n";
	}
	std::cout << "The answer is " << answer << ".\n";

	return 0;
}
