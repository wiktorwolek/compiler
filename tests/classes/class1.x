class Something
    int year
    int month
    method Init
        this_year = 2024
        this_month = 5
    endmethod

    method getYear
        getYear = this_year
    endmethod

    method increment
        this_year = this_year + 1
    endmethod
endclass


Something object
a = call object.Init()
b = call object.increment()
c = call object.getYear()

write a
write b
write c