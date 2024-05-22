x = 1
function fun
  write x
  x = 1
  fun = x + 1
endfunction


zosia = call fun()
write zosia

ala = 1
write ala

function alax
  write ala
  alax = 15
endfunction

x = call alax()

write ala

write x