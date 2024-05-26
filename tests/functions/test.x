function first
    x = 1

    y = call second()

    write x

    first = 0
endfunction

function second
    x = 42

    second = 0
endfunction

call first()