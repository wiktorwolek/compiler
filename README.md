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

<!-- no toc -->#### Ograniczenia

## Obsługa ciągu znaków
<!-- no toc -->#### Możliwości
<!-- no toc -->#### Ograniczenia

## Instrukcje warunkowe
<!-- no toc -->#### Możliwości
<!-- no toc -->#### Ograniczenia

## Funkcje
<!-- no toc -->#### Możliwości
<!-- no toc -->#### Ograniczenia

## Struktury
<!-- no toc -->#### Możliwości
<!-- no toc -->#### Ograniczenia

## Klasy
<!-- no toc -->#### Możliwości
<!-- no toc -->#### Ograniczenia