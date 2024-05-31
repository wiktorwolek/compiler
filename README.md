# Język programowania
Opisany zostaną możliwości i ograniczenia utworzonego języka programowania. 
Język bazuje na przykładach zademonstrowanych na wykładzie. 
[TOC]

## Deklaracje zmiennych 
<!-- no toc -->#### Możliwości
Zmienne są deklarowane statycznie przy pierwszym przypisaniu wartości. 
Możliwe jest zadeklarowanie w ten sposób zmiennej typu ```int```,  ```real```, która jest 64-bitową liczbą zmiennoprzecinkową, a także ```string```.
```
myInt = 10
myReal = -100.01
myString = "Hello world"
```

<!-- no toc -->#### Ograniczenia
Wiąże się to z następującymi ograniczeniami: 
- nie jest możliwe uzskanie niezainicjalizowanej zmiennej poza [strukturą](#struktury)
- zmienna po pierwszym przypisaniu wartości nie może zmienić typu
```
myVariable 
int myInt

someValue = 1.90
someValue = 12
```

## Obsługa wejścia-wyjścia
<!-- no toc -->#### Możliwości
Język umożliwia wczytywanie zmiennych typu ```int``` oraz ```real```. Wykonywane jest to z pomoca słowa kluczowego ```read```:
```
read int year
read real time
```
Język umożliwia wypisanie zmiennych typu ```int```, ```real``` oraz ```string```. Wykonywane jest to z pomoca słowa kluczowego ```read```:
```
write myInt
write myReal
write myString
```
<!-- no toc -->#### Ograniczenia
Nie jest obecnie możliwe wczytywanie zmiennych znakowych. 

## Obsługa operacji arytemtycznych 
<!-- no toc -->#### Możliwości
Język obsługuje operacje arytmetyczne dodawania, odejmowania, mnożenia i dzielenia. 

<!-- no toc -->#### Ograniczenia
- Wynik dzielenia jest zawsze liczbą rzeczywistą, jeśli dzielna i dzielnik będą różnych typów. 
- Dodawanie, odejmowanie i mnożenie liczb dwóch różnych typów nie jest obsługiwane 

## Obsługa zmiennych tablicowych
<!-- no toc -->#### Możliwości
Możliwe jest utworzenie tablicy liczb typu ```int```. Inicjalizacja tablicy przebiega w następujący sposób:
```
myArray = {1, 2, 3, 4}
```
Do elementów tablicy można się odwoływać oraz przypisywać im wartości.
```
myElem = myArray[3]
myArray[1] = 10
```
<!-- no toc -->#### Ograniczenia
Nie jest obecnie możliwe utworzenie tablicy typu real oraz string.

## Obsługa macierzy
<!-- no toc -->#### Możliwości
Możliwe jest utworzenie macierzy liczb typu ```int```. Inicjalizacja macierzy przebiega w następujący sposób:
```
myArray = {1, 2, 3, 3 + 2 * (2 + 1); 5, 6, 7, 8}
```
Do elementów macierzy można się odwoływać oraz przypisywać im wartości.
```
myElem = myMatrix[3,1]
myMatrix[1,0] = 10
```

<!-- no toc -->#### Ograniczenia
Nie jest obecnie możliwe utworzenie macierzy typu real oraz string.

## Instrukcje warunkowe
<!-- no toc -->#### Możliwości
Język pozwala na stworzenie instrukcji warunkowych:
```
z = 1
if z == 1 then
    write z
    endif
```
<!-- no toc -->#### Ograniczenia
Język nie obsługuje instukcji else i elseif znanych z innych języków programowania.
Operator porównania może porównywać tylko zmienną typu ```Int``` z wartością typu ```Int```
## Pętle
<!-- no toc -->#### Możliwości
Język pozwala na stworzenie pętli. Pętla wykona kod znajdujący się między słowami kluczowymi ```repeat``` i ```endrepeat``` n razy gdzie n to wynik wyrażenia znajdującego się pezpośrednio po słowie kluczowym ```repeat```:
```
repeat 3
    x = x+1
   write x
  endrepeat
```
<!-- no toc -->#### Ograniczenia
Język nie pozwala na iterację po obiektach ani na znane z innych języków pętle, np.: while.
## Funkcje
<!-- no toc -->#### Możliwości
Język pozwala na stworzenie i wykonanie funkcji:
```
function fun
  x = 1
  fun = x + 1
endfunction


f = call fun()
```
Dodatkowo obsługiwane są zmienne lokalne w funkcjach.
<!-- no toc -->#### Ograniczenia
Nie da się wywołać funkcji z parametrami, jedynym sposobem na przekazanie wartości są zmienne globalne.

## Struktury
<!-- no toc -->#### Możliwości
Język pozwala na stworzenie struktur danych:
```
struct Person
    int age
    real height
    int id
endstruct

```
Dodatkowo można stworzyć instancje struktury i przypisywać wartości jej polom poprzez:
```
Person zosia

zosia.age = 12
zosia.height = 1.20
zosia.id = 12000012
```
<!-- no toc -->#### Ograniczenia
W języku nie ma operatora przypisania zdefiniowanego dla instancji struktur.
Pola struktury mogą być typu ```int``` lub ```real```.

## Klasy
<!-- no toc -->#### Możliwości
W języku można zdefiniować klasy wraz z metodami:
```
class Simple
    int year

    method Init
        this_year = 2024
        Init = 0
    endmethod
endclass
```
W celu odniesienia się do pola klasy wewnątrz metody zdefiniowany został operator ```this_```.
Język obsługuje tworzenie instancji klasy oraz umożliwia odnoszenie się do pól klasy i wywoływanie metod:
```
Simple simpleObject
simpleObject.year = 12000
a = call simpleObject.Init()
write simpleObject.year
```
<!-- no toc -->#### Ograniczenia
W języku nie ma operatora przypisania zdefiniowanego dla instancji klas.
Podobnie jak w przypadku struktur, obsługiwane są tylko pola typu ```int``` i ```real```.