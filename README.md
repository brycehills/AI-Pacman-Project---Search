# CS205 Aritifical Intelligence Pacman Project - Bryce Hills

<img src="pacman_search/screenshots/maze.png" alt="alt text" width="500" height="500">

## Motivation

* In this project, the Pacman agent will find paths through his maze world, both to reach a particular location and to collect food efficiently. We build general search algorithms and apply them to Pacman scenarios:
  - Breadth First Search
  - Depth First Search
  - Uniform Cost Search
  - A Star Algorithm
  - Implementing a Representation of the Corners Problem
  - Corners Problem Heuristic
  - Eating All Dots Heuristic
  - Greedy Search - (Finding out why this is suboptimal for the eating problem)
* Main Idea
  - Implement search algorithms and heuristics in a real world example to get a better idea of where each one can succeed or fail.
  - Understanding Admissibility vs. Consistency with respect to heuristics
  - Learning how to represent a game as a searchable set of states for search algorithms
 
## File Breakdown
* Main Files:
  * search.py - 	Where all of your search algorithms will reside.  
  * searchAgents.py - 	Where all of your search-based agents will reside.
* Files to Pay Attention to:
  * pacman.py	- The main file that runs Pacman games. This file describes a Pacman GameState type, which you use in this project.  
  * game.py -	The logic behind how the Pacman world works. This file describes several supporting types like AgentState, Agent, Direction, and Grid.  
  * util.py	- Useful data structures for implementing search algorithms.  
* Supporting files you can ignore:  
  * graphicsDisplay.py -	Graphics for Pacman  
  * graphicsUtils.py	- Support for Pacman graphics  
  * textDisplay.py	- ASCII graphics for Pacman  
  * ghostAgents.py	- Agents to control ghosts  
  * keyboardAgents.py	- Keyboard interfaces to control Pacman  
  * layout.py	- Code for reading layout files and storing their contents  
  * test_cases/	- Directory containing the test cases for each question  
  * searchTestClasses.py	- Project 1 specific autograding test classes  

## How To Use


```bash
After downloading the code (search.zip), unzipping it, and changing to the directory, you should be able to play a game of Pacman by typing the following at the command line:

python pacman.py

Run a pacman agent on a particular board by using 

python pacman.py --layout (maze) --pacman (agent)
```




## Credits

* http://ai.berkeley.edu/search.html#Q8


---

> GitHub [@brycehills](https://github.com/brycehills) &nbsp;&middot;&nbsp;
> LinkedIn [bryce hills]([https://twitter.com/amit_merchant](https://www.linkedin.com/in/brycehills1/)https://www.linkedin.com/in/brycehills1/)

