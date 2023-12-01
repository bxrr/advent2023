#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
    fstream f;
    f.open("input_new", ios::in);
    
    int sum = 0;
    int left, right;
    int lval, rval;

    string line;
    while(getline(f, line))
    {
        left = 0;
        right = line.length()-1;
        lval = -1;
        rval = -1;
        for(int i = 0; i < line.length(); i++)
        {
            char curl, curr;
            if(lval == -1)
            {
                curl = line.at(left);
                if(curl >= '0' && curl <= '9')
                {
                    lval = curl - '0';
                }
                left++;
            }
            if(rval == -1)
            {
                curr = line.at(right);
                if(curr >= '0' && curr <= '9')
                {
                    rval = curr - '0';
                }
                right--;
            }
        }
        sum += lval * 10 + rval;
    }

    cout << sum;
}