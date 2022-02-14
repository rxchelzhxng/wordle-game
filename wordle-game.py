# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 16:09:06 2022

@author: rxche
"""
import json
import random
from sys import exit

class Wordle:
    def __init__(self):
        # Reading in json file of all 5 letter words
        file = open("words.json")
        words = json.load(file)
        
        self.solutions = words["solutions"]
        self.invalid = words["invalid"]
        
        # Select 1 word from list as solution
        solution = self.selectSolution()
        
        # Play wordle game 
        self.createGame(solution)
        
        
    def selectSolution(self):
        """
        Function to select a random 5 letter word as the solution
        """
        solution = random.choice(self.solutions)
        return solution
    
    def createGame(self, solution):
        """
        Function to create game logic
        :param solution: string of solution
        None.

        """
        guess = 0
        # Iterate to query user for word attempt until 6 tries
        while guess < 7:
            attempt = input("Pick word: ")
            
            # If length of word is not 5, exit
            if len(attempt) != 5:
                print("Word must be five letters")
                continue
                
            # If word is in list of invalid solutions then inform it is not in the list
            elif attempt in self.invalid:
                print("Not in word list")
                continue
                
            # Check if attempt word is a valid five letter word
            elif attempt not in self.solutions:
                print("Not in word list")
                continue
                    
            # Calculate the attempted guess
            else:
                print(f"Guess {guess + 1}/6: {attempt}")
                result = Result.calculateAttempt(solution, attempt)
                print(f"Result: {result}")
                # Update counter
                guess += 1
                # Check if all letters match the correct spot in solution
                if all(result[letter] == Result.correct_spot for letter in range(len(attempt))):
                    print(f"Success! Got the solution in {guess} tries")
                    
                # Check if all 6 attempts have been used
                elif guess == 6:
                    next_step = input("Attempt was unsuccessful.\nHit enter to exit or type try again: ")
                    if next_step == "":
                        play = False
                        return
                    else:
                        play = True
                        self.__init__()
        
class Result():
    correct_spot = "Correct spot"
    wrong_spot = "Wrong spot"
    no_spot = "No spot"
        
    def calculateAttempt(solution, attempt):
        """
        Function to calculate the correct, wrong spot, and no spot letters in
        the attempted guess
        :param solution: string of solution
        :param attempt: string of guess attempt
        return: list of results 
        """
            
        def match_letter(solution, attempt, letter):
            """
            Function to match the letters in attempt to the solution
            :param solution: string of solution
            :param attempt: string of guess attempt
            :param i: integer of letter position
            return Result object 
            """
            # Check if letter is in the same position as the solution, return a correct spot status
            if attempt[letter] == solution[letter]:
                return Result.correct_spot
            # Check if the letter is in the solution, return a wrong spot status
            elif attempt[letter] in solution:
                return Result.wrong_spot
            # If not, return a no spot status
            else:
                return Result.no_spot
        
        if len(solution) == len(attempt):
            return [match_letter(solution, attempt, letter) for letter in range(len(attempt))] 
        
            

if __name__ == "__main__":
    Wordle()