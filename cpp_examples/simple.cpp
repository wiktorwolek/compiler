#include <iostream>

class Simple
{
public:
    int year;

    Simple()
    {
        this->year = 2024;
    }

    void increment()
    {
        this->year += 1;
    }
};

int main()
{

    Simple s;

    s.increment();

    return 0;
}