#include <iostream>
#include <fstream>
#include <unordered_map>
#include <string>
#include <vector>

using namespace std;

int solve(int card, unordered_map<int, int> &data, const vector<int> &nums, int &total)
{   // failed attempt at memoization, will revisit if i feel like it. 
    // ends up being O(n!) without memoization
    total++;
    if(nums[card] == 0) 
    {
        data[card] = 0;
    }
    else
    {
        int temp = 0;
        for(int i = 1; i <= nums[card]; i++)
        {
            temp += solve(card+i, data, nums, total) + 1;
        }
        data[card] = temp;
    }
    return data[card];
}

int main()
{
    unordered_map<int, int> data;
    ifstream f("outputs");

    string line;
    vector<int> nums;
    int n = 0;
    while(getline(f, line))
    {
        n++;
        nums.push_back(stoi(line));
    }

    int sum = 0;
    int total = 0;
    for(int i = 0; i < n; i++)
    {
        sum += solve(i, data, nums, total);
    }

    cout << total;
}