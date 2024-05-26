#---T♠ - 25/05/2020: 'SORTING ALGORITHMS'

import time
import keyboard
import sys

array = []

def intro():
    print("\n")
    print("Hello there! This program is a sorting algorithm program. Currently, there are two options: bubble sort and shuttle sort.")
    time.sleep(1)
    selection()

def bubble():
    print("You have selected: bubble sort.")
    elements = int(input("How many elements do you want to have sorted?\n"))
    for item in range(elements):
        array.append(int(input("Enter an integer for the array to be sorted. ")))
    print("\n")
    print(array)
    print("The above shows your array.")
    time.sleep(1)
    print("Bubble sort is a simple sorting algorithm that works by simply comparing two adjacent values in an array, and swapping them if they are in the wrong order, starting at the left hand side. After every swap, the array is read from the position prior.")
    time.sleep(1)
    print("We shall now apply bubble sort to the given array.")
    print("\n")
    print("Please press the 'a' key when you are satisfied with the result, and want to end the program.")
    print("Press the 'b' key if you get the result, but want to restart the program.")
    print("Press the 'c' key if you have a problem with the result.")
    print("\n")
    time.sleep(1)
    print(array)
    n = 0
    while True:
        if array[n] > array[n+1]:
            swap1 = array[n] 
            swap2 = array[n+1]
            array[n] = swap2
            array[n+1] = swap1
            print(array)
            n = n+1
            while n+1 >= len(array):
                n = 0
                break
        elif array[n] < array[n+1]:
            n = n+1
            while n+1 >= len(array):
                n = 0
                break
        elif array[n] == array[n+1]:
            n = n+1
            while n+1 >= len(array):
                n = 0
                break
            
        if keyboard.is_pressed("a"):
            time.sleep(0.5)
            print("You pressed the 'a' key. This means that you are satisfied with the result.")
            end()
        if keyboard.is_pressed("b"):
            time.sleep(0.5)
            print("You pressed the 'b' key. This means that you want to run the program again.")
            time.sleep(1)
            print("\n")
            selection()
        if keyboard.is_pressed("c"):
            time.sleep(0.5)
            print("You have pressed the 'c' key. This means that you have found a problem with the result.")
            time.sleep(0.5)
            print("Please email me at {talha.hussa2014@st-pauls.me.uk}, with a screenshot of the issue attached. I will look into the problem and make corrections as necessary.")
            end()
            
        
            
  

def shuttle():
    print("You have selected: shuttle sort.")
    elements = int(input("How many elements do you want to have sorted?\n"))
    for item in range(elements):
        array.append(int(input("Enter an integer for the array to be sorted. ")))
    print("\n")
    print(array)
    print("The above shows your array.")
    time.sleep(1)
    print("Shuttle sort is a simple sorting algorithm that works by simply comparing two adjacent values in an array, and swapping them if they are in the wrong order, starting at the left hand side. After every swap, the array is read from the start once again.")
    time.sleep(1)
    print("We shall now apply bubble sort to the given array.")
    print("\n")
    print("Please press the 'a' key when you are satisfied with the result, and want to end the program.")
    print("Press the 'b' key if you get the result, but want to restart the program.")
    print("Press the 'c' key if you have a problem with the result.")
    print("\n")
    time.sleep(1)
    print(array)
    n = 0
    while True:
        if array[n] > array[n+1]:
            swap1 = array[n] 
            swap2 = array[n+1]
            array[n] = swap2
            array[n+1] = swap1
            print(array)
            n = n+1
            n = 0
            while n+1 >= len(array):
                n = 0
                break
        elif array[n] < array[n+1]:
            n = n+1
            while n+1 >= len(array):
                n = 0
                break
        elif array[n] == array[n+1]:
            n = n+1
            while n+1 >= len(array):
                n = 0
                break

                    
        if keyboard.is_pressed("a"):
            time.sleep(0.5)
            print("You pressed the 'a' key. This means that you are satisfied with the result.")
            end()
        if keyboard.is_pressed("b"):
            time.sleep(0.5)
            print("You pressed the 'b' key. This means that you want to run the program again.")
            time.sleep(1)
            print("\n")
            selection()
        if keyboard.is_pressed("c"):
            time.sleep(0.5)
            print("You have pressed the 'c' key. This means that you have found a problem with the result.")
            time.sleep(0.5)
            print("Please email me at [REDACTED], with a screenshot of the issue attached. I will look into the problem and make corrections as necessary.")
            end()

    

def selection():
    array.clear()
    mode = input("Choose a sorting algorithm. (bubble or shuttle)\n")
    while mode != "Bubble" and mode != "bubble" and mode != "BUBBLE" and mode != "Shuttle" and mode != "shuttle" and mode != "SHUTTLE":
            print("Invalid input. Try again.")    
            mode = input("Choose a sorting algorithm. (bubble or shuttle)\n")
    if mode == "Bubble" or mode == "bubble" or mode == "BUBBLE":
        bubble()
    else:
        if mode == "Shuttle" or mode == "shuttle" or mode == "SHUTTLE":
            shuttle()
        else:
            print("Error encountered: Terminating program.")
            end()
    

def end():
    time.sleep(1)
    print("[Terminating]...")
    time.sleep(0.5)
    print(".\n")
    time.sleep(0.5)
    print(".\n")
    time.sleep(0.5)
    print(".\n")
    time.sleep(0.5)
    sys.exit()
    

intro()
    


