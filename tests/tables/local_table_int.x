function myScope

    myArray = {12, 13, 14}

    x = 1

    arrElem = myArray[1]
    
    myScope = arrElem
endfunction


something = call myScope()

write something