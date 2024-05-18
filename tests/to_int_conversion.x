x = 1 
function fun
  fun = 3
endfunction

a = 1
write a
a = 1.1 + 1
write a
zosia = (call fun() + 4) * 2 + (int)((real)call fun() +1.6)
write zosia
