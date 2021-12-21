
                if (reqs[j] == "byr")
                {
                    if (value.size() < 4 || 1920 > stoi(value) || 2002 < stoi(value))
                    {
                        std::cout << "passport number " << i + 1 << " is invalid\n";
                        invalid++;
                        j = reqs.size();
                        stillGood = false;
                    }
                }
                if (reqs[j] == "iyr" && stillGood)
                {
                    if (value.size() < 4 || 2010 > stoi(value) || 2020 < stoi(value))
                    {
                        std::cout << "passport number " << i + 1 << " is invalid\n";
                        invalid++;
                        j = reqs.size();
                        stillGood = false;
                    }
                }
                if (reqs[j] == "eyr" && stillGood)
                {
                    if (value.size() < 4 || 2020 > stoi(value) || 2030 < stoi(value))
                    {
                        std::cout << "passport number " << i + 1 << " is invalid\n";
                        invalid++;
                        j = reqs.size();
                        stillGood = false;
                    }
                }
                if (reqs[j] == "hgt" && stillGood)
                {
                    heightUnits = value.substr(value.size() - 2, 2);
                    if (heightUnits == "cm")
                    {
                        height = value.substr(0, value.size() - 2);
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
                        height = value.substr(0, value.size() - 2);
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
