function funt
  x = 10
  write x
  funt = x
endfunction

function fun
  x = 1
  write x
  y = call funt()
  write x
  fun = x
endfunction


x = call fun()