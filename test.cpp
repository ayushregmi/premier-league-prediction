#include<iostream>
#include<vector>
#include<string>

using namespace std;

int main()
{
    vector<char> chars = {' ','a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x'
    ,'y','z','1','2','3','4','5','6','7','8','9','0', 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T'
    ,'U','V','W','X','Y','Z', '@', '_', '-'};

    string pass = "";

    for(int i1 = 0; i1 < chars.size(); i1++)
    {
        for(int i2 = 0; i2 < chars.size(); i2++)
        {
            for(int i3 = 0; i3 < chars.size(); i3++)
            {
                for(int i4 = 0; i4 < chars.size(); i4++)
                {
                    for(int i5 = 0; i5 < chars.size(); i5++)
                    {
                        for(int i6 = 0; i6 < chars.size(); i6++)
                        {
                            for(int i7 = 0; i7 < chars.size(); i7++)
                            {
                                for(int i8 = 0; i8 < chars.size(); i8++)
                                {
                                    for(int i9 = 1; i9 < chars.size(); i9++)
                                    {
                                        for(int i10 = 1; i10 < chars.size(); i10++)
                                        {
                                            for(int i11 = 1; i11 < chars.size(); i11++)
                                            {
                                                for(int i12 = 1; i12 < chars.size(); i12++)
                                                {
                                                    for(int i13 = 1; i13 < chars.size(); i13++)
                                                    {
                                                        for(int i14 = 1; i14 < chars.size(); i14++)
                                                        {
                                                            for(int i15 = 1; i15 < chars.size(); i15++)
                                                            {
                                                                for(int i16 = 1; i16 < chars.size(); i16++)
                                                                {
                                                                    pass = "";
                                                                    pass.push_back(chars[i16]);
                                                                    pass.push_back(chars[i15]);
                                                                    pass.push_back(chars[i14]);
                                                                    pass.push_back(chars[i13]);
                                                                    pass.push_back(chars[i12]);
                                                                    pass.push_back(chars[i11]);
                                                                    pass.push_back(chars[i10]);
                                                                    pass.push_back(chars[i9]);
                                                                    pass.push_back(chars[i8]);
                                                                    pass.push_back(chars[i7]);
                                                                    pass.push_back(chars[i6]);
                                                                    pass.push_back(chars[i5]);
                                                                    pass.push_back(chars[i4]);
                                                                    pass.push_back(chars[i3]);
                                                                    pass.push_back(chars[i2]);
                                                                    pass.push_back(chars[i1]);
                                                                    cout << pass << endl;
                                                                }
                                                            }           
                                                        }
                                                    }
                                                }
                                            }           
                                        }
                                    }
                                }
                            }           
                        }
                    }
                }
            }           
        }
    }
}