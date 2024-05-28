#include <iostream>

class Something
{
    int year;

public:
    Something()
    {
        this->year = 2024;
    }

    void incrementYear()
    {
        this->year += 1;
    }
};

int main()
{
    Something thisYear;

    return 0;
}
