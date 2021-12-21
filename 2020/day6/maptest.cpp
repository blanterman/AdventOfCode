#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <map>
#include <sstream>

int main()
{
    std::map<char, int> testMap;
    testMap['a'] = 1;
    testMap['a'] = (testMap.find('a')->second) + 1;
    std::cout << testMap.size() << "\n";
    std::map<char, int>::iterator current = testMap.begin();
    while (current != testMap.end())
    {
        std::cout << current->first << ":" << current->second << "\n";
        ++current;
    }
    return 0;
}
