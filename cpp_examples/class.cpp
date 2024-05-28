#include <iostream>

extern "C"
{
    class Something
    {
        int year;
        int day;
        double temperature;

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
