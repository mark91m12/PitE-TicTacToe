<p align="center">
  <img width="460" height="300" src="https://github.com/Mario181091/Mario_content/blob/master/Senza%20titolo-3.jpg">
</p>

# PitE-TicTacToe

This is the second homework of the course "Python in the Enterprise", as requested has been implemented a personal version of the famous game Tic Tac Toe.    
Tic-tac-toe (also known as noughts and crosses or Xs and Os) is a paper-and-pencil game for two players, X and O, who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.

The following example game is won by the first player, X:

![alt text]( https://upload.wikimedia.org/wikipedia/commons/1/1b/Tic-tac-toe-game-1.svg)

## Features

* Artificial Intelligence
* 1 Vs PC mode

## Getting Started

**Prerequisites**
* In order to run this project is important to use python version 3 or upper.                                                    
  Install it with:
  
  ```shell
   $ sudo apt-get install python3
  ```
  now check your version: 
  ```shell
  $ python --version
  ```

**Basic usage**
* Running this command to start the game : 

  ```shell
   $ python3 Tic_tac_toe_game.py
  ```
  
* Once you have entered your name the following screen will be showed  
  
  ```
       |   |   
     7 | 8 | 9  
       |   |   
    -----------
       |   |   
     4 | 5 | 6  
       |   |   
    -----------
       |   |   
     1 | 2 | 3  
       |   |   
    
    chose an empty space for X.            
   
  ```
  
* To play simply choose a free keypad number corresponding to the grid (in this example 7 )

  ```
       |   |   
     X | 8 | 9  
       |   |   
    -----------
       |   |   
     4 | 5 | 6  
       |   |   
    -----------
       |   |   
     1 | 2 | 3  
       |   |    
      
  ```
* After the last movement one of the players (User or Pc) wins, in this example PC. 

  ```
       |   |   
     X | 8 | O  
       |   |   
    -----------
       |   |   
     X | X | O  
       |   |   
    -----------
       |   |   
     1 | 2 | O  
       |   |    
      
    Result: Computer Wins  
    
  ```
**Running the Tests**
In order to run all tests you simply need to write the following command :
  ```shell
    $ python3 Test_game_default.py
  ```
  
  
 [![Coverage Status](https://coveralls.io/repos/github/mark91m12/PitE-TicTacToe/badge.svg?branch=master)](https://coveralls.io/github/mark91m12/PitE-TicTacToe?branch=master) 
  
## Authors

* **Mario Egidio Carricato** - *Erasmus student AGH* - [other projects](https://github.com/mario181091)
* **Marco Amato** - *Erasmus student AGH* - [other projects](https://github.com/mark91m12)
