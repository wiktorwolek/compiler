class Simple
    int year

    method Init
        this_year = 2024
        Init = 0
    endmethod
endclass


Simple simpleObject
simpleObject.year = 12000
a = call simpleObject.Init()
write simpleObject.year