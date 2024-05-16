x = 1 
function fun
  fun = 3
endfunction


zosia = (call fun() + 4) * 2 + (int)((real)call fun() +1.6)
write zosia
