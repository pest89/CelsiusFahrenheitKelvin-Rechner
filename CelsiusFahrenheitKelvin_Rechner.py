# Zweck Programieren leren


import pytemperature

print ("Autor: Cem\nErstellt: 22.09.2023\nVersion: 0.2\nPython 3.10 64 bit\n")
print ("#########################################\n\n+++ Celsius Fahrenheit Kelvin Rechner +++\n\n#########################################\n")
print ("Press 1 'C --> 'F\nPress 2 'F --> 'C\nPress 3 'C --> 'K\nPress 4 'K --> 'C\nPress 5 'F --> 'K\nPress 6 'K --> 'F\n" )
select = int (input ('your chois: '))
if select == 1:
    print()
    wehrt = float (input ('Welcher Wehrt soll umgerechnet werden: ')) # variable wird als Fliesskommazahl eingelehsen
    print ()
    print (wehrt, "Grad Celsius entsprechen", pytemperature.c2f(wehrt), "Grad Fahrenheit\n") 
    input ("Press any Key to close...") 
    
if select == 2:
    print()
    wehrt = float (input ('Welcher Wehrt soll umgerechnet werden: ')) # variable wird als Fliesskommazahl eingelehsen
    print ()
    print (wehrt, "Grad Fahrenheit entsprechen", pytemperature.f2c(wehrt), "Grad Celsius\n") 
    input ("Press any Key to close...") 

if select == 3:
    print()
    wehrt = float (input ('Welcher Wehrt soll umgerechnet werden: ')) # variable wird als Fliesskommazahl eingelehsen
    print ()
    print (wehrt, "Grad Celsius entsprechen", pytemperature.c2k(wehrt), "Grad Kelvin\n") 
    input ("Press any Key to close...") 

if select == 4:
    print()
    wehrt = float (input ('Welcher Wehrt soll umgerechnet werden: ')) # variable wird als Fliesskommazahl eingelehsen
    print ()
    print (wehrt, "Grad Kelvin entsprechen", pytemperature.k2c(wehrt), "Grad Celsius\n") 
    input ("Press any Key to close...") 

if select == 5:
    print()
    wehrt = float (input ('Welcher Wehrt soll umgerechnet werden: ')) # variable wird als Fliesskommazahl eingelehsen
    print ()
    print (wehrt, "Grad Fahrenheit entsprechen", pytemperature.f2k(wehrt), "Grad Kelvin\n") 
    input ("Press any Key to close...")
     
if select == 6:
    print()
    wehrt = float (input ('Welcher Wehrt soll umgerechnet werden: ')) # variable wird als Fliesskommazahl eingelehsen
    print ()
    print (wehrt, "Grad Kelvin entsprechen", pytemperature.k2f(wehrt), "Grad Fahrenheit\n") 
    input ("Press any Key to close...") 
