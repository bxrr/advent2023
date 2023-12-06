#include <iostream>
#include <vector>

using namespace std;

int run_simu(int time, int distance)
{
    int total = 0;
    for(int i = 1; i < time-1; i++)
    {
        int your_time = i;
        int speed = i;
        your_time += distance / speed;
        if(your_time < time) total++;
    }

    return total;
}

int main()
{
    int times[] = {48, 93, 85, 95};
    int distances[] = {296, 1928, 1236, 1391};
    vector<int> vals;

    int result = 1;
    for(int i = 0; i < 4; i++) result *= run_simu(times[i], distances[i]);
    cout << result;
}
    