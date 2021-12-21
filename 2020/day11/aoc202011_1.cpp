#include <iostream>
#include <vector>
#include <fstream>
#include <string>

char processSeat(const std::vector<std::string>& floorplanCurrent, int rowInd, int colInd, std::string whereToLook, long& numChanges)
{
    int count = 0;
    char subject = floorplanCurrent[rowInd][colInd];
    if (subject == '.')
    {
        return subject;
    }
    char looking;
    for (int i = 0; i < whereToLook.size(); i++)
    {
        looking = 'B';
        if (whereToLook[i] == 'A')
        {
            looking = floorplanCurrent[rowInd - 1][colInd - 1];
        }
        if (whereToLook[i] == 'B')
        {
            looking = floorplanCurrent[rowInd - 1][colInd];
        }
        if (whereToLook[i] == 'C')
        {
            looking = floorplanCurrent[rowInd - 1][colInd + 1];
        }
        if (whereToLook[i] == 'D')
        {
            looking = floorplanCurrent[rowInd][colInd - 1];
        }
        if (whereToLook[i] == 'E')
        {
            looking = floorplanCurrent[rowInd][colInd + 1];
        }
        if (whereToLook[i] == 'F')
        {
            looking = floorplanCurrent[rowInd + 1][colInd - 1];
        }
        if (whereToLook[i] == 'G')
        {
            looking = floorplanCurrent[rowInd + 1][colInd];
        }
        if (whereToLook[i] == 'H')
        {
            looking = floorplanCurrent[rowInd + 1][colInd + 1];
        }
        if (looking == '#')
        {
            count++;
        }
    }
    if (subject == 'L')
    {
        if (count == 0)
        {
            numChanges++;
            return '#';
        }
        else
        {
            return subject;
        }
    }
    if (subject == '#')
    {
        if (count >= 4)
        {
            numChanges++;
            return 'L';
        }
        else
        {
            return subject;
        }
    }
    return '!';
}

int main()
{
    std::string fileName = "AOC111.dat";
    std::ifstream inFile;
    inFile.open(fileName);
    if (inFile.fail())
    {
        std::cout << "File open failure\n";
        return -1;
    }
    std::string lineIn;
    std::vector<std::string> floorplanCurrent;
    std::vector<std::string> floorplanNext;
    while (getline(inFile, lineIn))
    {
        floorplanCurrent.push_back(lineIn);
    }
    floorplanNext = floorplanCurrent;
    long numberOfChanges = 1;
    std::string whereToLook;
    int iterations = 0;
    while (numberOfChanges != 0)
    {
        numberOfChanges = 0;
        for (int i = 0; i < floorplanCurrent.size(); i++)
        {
            for (int j = 0; j < floorplanCurrent[i].size(); j++)
            {
                if (i == 0) // top row
                {
                    if (j == 0) // top left corner
                    {
                        whereToLook = "EGH";
                    }
                    else if (j == floorplanCurrent[i].size() - 1) // top right corner
                    {
                        whereToLook = "DFG";
                    }
                    else // rest of the row
                    {
                        whereToLook = "DEFGH";
                    }
                }
                else if (i == floorplanCurrent.size() - 1) // bottom row
                {
                    if (j == 0) //bottom left corner
                    {
                        whereToLook = "BCE";
                    }
                    else if (j == floorplanCurrent[i].size() - 1) // bottom right corner
                    {
                        whereToLook = "ABD";
                    }
                    else // rest of bottom row
                    {
                        whereToLook = "ABCDE";
                    }
                }
                else // rest of the rows (ie all but top and bottom
                {
                    if (j == 0) // on left side
                    {
                        whereToLook = "BCEGH";
                    }
                    else if (j == floorplanCurrent[i].size() - 1) // on right side
                    {
                        whereToLook = "ABDFG";
                    }
                    else // all internal spots/ not on border
                    {
                        whereToLook = "ABCDEFGH";
                    }
                }
                floorplanNext[i][j] = processSeat(floorplanCurrent, i, j, whereToLook, numberOfChanges);
            }
        }
        iterations++;
        /*
        for (int i = 0; i < floorplanNext.size(); i++)
        {
            std::cout << floorplanNext[i] << "\n";
        }
        */
        std::cout << numberOfChanges << "\n";
        floorplanCurrent = floorplanNext;
    }
    std::cout << "It took " << iterations << " iterations\n";
    long occupiedSeats = 0;
    for (int i = 0; i < floorplanCurrent.size(); i++)
    {
        for (int j = 0; j < floorplanCurrent[i].size(); j++)
        {
            if (floorplanCurrent[i][j] == '#')
            {
                occupiedSeats++;
            }
        }
    }
    std::cout << occupiedSeats << " seats are occupied.\n";
    return 0;
}
