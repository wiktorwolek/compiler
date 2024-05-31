class Simple
    int x
    method getValue
        this_x = 1212
        x = 1111
        write this_x
        write x 
        getValue = x
    endmethod
endclass

x = 1010

Simple object
a = call object.getValue()
write x 
write a
