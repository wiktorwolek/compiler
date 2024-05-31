#include <iostream>

extern "C"
{
    class Something
    {
        int day;
        double temperature;
        int year;

    public:
        Something()
        {
            this->year = 2024;
            this->day = 28;
            this->temperature = 28.90;
        }

        void incrementYear()
        {
            this->year += 1;
        }
    };

    int main()
    {
        Something thisYear;

        thisYear.incrementYear();

        return 0;
    }
}
