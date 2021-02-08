"""
Chatbot
Author: Shane Ohlrich
Period/Core: 7

"""

import os
import importlib.util
import random

def run_tests():
  """
  This function will check for the pytest module
  before calling it to run the included tests.py
  """
  if importlib.util.find_spec('pytest') is None: # Check if pytest is installed
    os.system('python3 -m pip install -q pytest')

  command = "python3 -m pytest --tb=line -v -s tests.py"
  print(command)
  os.system(command)

def main():
  """This function contains all code for the chatbot."""
  print("Hello!")
  
  
  #Start of my code
  name = input("What is your full name ")
  #This part of the code is asking you how your day is. 
  hey_how_are_you = input(f"Hey {name}, how are you today? ")
  if (hey_how_are_you == "good"):
    print("Great to hear that!")
   
    """
    So this next line of code will say that it sorry if you say that your day was bad or not good. Also the next line after that if they say something other than good or bad then it will say that it has never heard of that. 
    """
    
  elif (hey_how_are_you == "bad"):
    print("Wow, I'm sorry to hear that.")
  else: 
    print("Sorry, never heard of that.")
  What_school_are_you_from = input("What school are you from?")
  print("Cool! Thats a good school.")
  What_is_your_favroite_color = input("So, what is your favroite color?")
  """
  So these statment are asking you what your favroite color is. There is a problem if you dont choose between Red, Blue, Pink, Yellow it  will say that it dosent know that color. 
  """
  if (What_is_your_favroite_color == "blue"):
    print("Cool!")
  elif(What_is_your_favroite_color == "Red"):
    print("Thats my favroite")
  elif(What_is_your_favroite_color == "Pink"):
    print("I like that color.")
  elif(What_is_your_favroite_color == "Yellow"):
    print("Nice!")
  else:
    print("Sorry I dont know that number")
  
  number = input("May I guess your favroite number? ")
  if(number == "yes"):
    print("Great!")
  else:
    print("I am going to try anyways.")

  print(random.randint(0,10))
  
  any_number = input("Did I guess it? ")
  if(any_number == "yes"):
    print("Yay!")
  else:
    print("Dang I guess it was a good try.")

  print("Well thanks for talking to me have a good day now.")
if __name__ == "__main__":
  main()
t = input("Run pytest? (y/n)").lower()
if t == 'y':
    run_tests()