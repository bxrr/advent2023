#include <iostream>
#include <vector>

using namespace std;

long long run_simu(long long time, long long distance)
{
    long long total = 0;
    for(long long i = 1; i < time-1; i++)
    {
        long long your_time = i;
        long long speed = i;
        your_time += distance / speed;
        if(your_time < time) total++;
    }

    return total;
}

int main()
{
    long long times[] = {48938595};
    long long distances[] = {296192812361391};
    vector<long long> vals;

    long long result = 1;
    result *= run_simu(times[0], distances[0]);
    cout << result;
}
    