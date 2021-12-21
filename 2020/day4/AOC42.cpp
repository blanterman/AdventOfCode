#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <map>
#include<sstream>

int main()
{
    std::string fileName = "AOC41.dat";
    std::ifstream inFile;
    inFile.open(fileName);
    if (inFile.fail())
    {
        std::cout << "File open failure\n";
        return -1;
    }
    std::string lineIn;
    std::vector<std::map<std::string, std::string>> passports;
    std::map<std::string, std::string> passportInfo;
    int totalLines = 0;
    int blankLines = 0;
    std::string entry;
    std::string key;
    std::string value;
    while (getline(inFile, lineIn))
    {
        if (lineIn != "")
        {
            std::istringstream instr(lineIn);
            while(instr >> entry)
            {
                key = entry.substr(0, 3);
                value = entry.substr(4, entry.size() - 4);
                passportInfo[key] = value;
            }
        }
        else
        {
            passports.push_back(passportInfo);
            passportInfo.clear();
        }
    }
    passports.push_back(passportInfo);
    std::vector<std::string> reqs{ "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid" };
    std::map<std::string, std::string>::iterator current;
    int invalid = 0;
    int valid = 0;
    std::string height;
    std::string heightUnits;
    bool stillGood = true;
    for (int i = 0; i < passports.size(); i++)
    {
        for (int j = 0; j < reqs.size(); j++)
        {
            current = passports[i].find(reqs[j]);
            if (current == passports[i].end() && reqs[j] != "cid")
            {
                std::cout << "passport number " << i + 1 << " is invalid\n";
                invalid++;
                j = reqs.size();
            }
            else
            {
                if (reqs[j] == "byr")
                {
                    if ((current->second).size() < 4 || 1920 > stoi((current->second)) || 2002 < stoi((current->second)))
                    {
                        std::cout << "passport number " << i + 1 << " is invalid\n";
                        invalid++;
                        j = reqs.size();
                        stillGood = false;
                    }
                }
                if (reqs[j] == "iyr" && stillGood)
                {
                    if ((current->second).size() < 4 || 2010 > stoi((current->second)) || 2020 < stoi((current->second)))
                    {
                        std::cout << "passport number " << i + 1 << " is invalid\n";
                        invalid++;
                        j = reqs.size();
                        stillGood = false;
                    }
                }
                if (reqs[j] == "eyr" && stillGood)
                {
                    if ((current->second).size() < 4 || 2020 > stoi((current->second)) || 2030 < stoi((current->second)))
                    {
                        std::cout << "passport number " << i + 1 << " is invalid\n";
                        invalid++;
                        j = reqs.size();
                        stillGood = false;
                    }
                }
                if (reqs[j] == "hgt" && stillGood)
                {
                    heightUnits = (current->second).substr((current->second).size() - 2, 2);
                    if (heightUnits == "cm")
                    {
                        height = (current->second).substr(0, (current->second).size() - 2);
                        if (150 > stoi(height) || 193 < stoi(height))
                        {
                            std::cout << "passport number " << i + 1 << " is invalid\n";
                            invalid++;
                            j = reqs.size();
                            stillGood = false;
                        }
                    }
                    else if (heightUnits == "in")
                    {
                        height = (current->second).substr(0, (current->second).size() - 2);
                        if (59 > stoi(height) || 76 < stoi(height))
                        {
                            std::cout << "passport number " << i + 1 << " is invalid\n";
                            invalid++;
                            j = reqs.size();
                            stillGood = false;
                        }
                    }
                    else
                    {
                        std::cout << "passport number " << i + 1 << " is invalid\n";
                        invalid++;
                        j = reqs.size();
                        stillGood = false;
                    }
                }
            }
        }
    }
    valid = passports.size() - invalid;
    std::cout << valid << " valid passports.\n";
    /*
    std::cout << passports.size() << "\n";
    std::map<std::string, std::string> toPrint;
    toPrint = passports[passports.size() - 1];
    std::map<std::string, std::string>::iterator current = toPrint.begin();
    while (current != toPrint.end())
    {
        std::cout << current->first << ":" << current->second << "\n";
        ++current;
    }
    */
    return 0;
}
