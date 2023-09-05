# CS205 Aritifical Intelligence Pacman Project

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
  - 
 
## File Breakdown
* search.py	Where all of your search algorithms will reside.  
* searchAgents.py	Where all of your search-based agents will reside.  
* Files you might want to look at:  
* pacman.py	The main file that runs Pacman games. This file describes a Pacman GameState type, which you use in this project.  
* game.py	The logic behind how the Pacman world works. This file describes several supporting types like AgentState, Agent, Direction, and Grid.  
* util.py	Useful data structures for implementing search algorithms.  
* Supporting files you can ignore:  
* graphicsDisplay.py	Graphics for Pacman  
* graphicsUtils.py	Support for Pacman graphics  
* textDisplay.py	ASCII graphics for Pacman  
* ghostAgents.py	Agents to control ghosts  
* keyboardAgents.py	Keyboard interfaces to control Pacman  
* layout.py	Code for reading layout files and storing their contents  
* autograder.py	Project autograder  
* testParser.py	Parses autograder test and solution files  
* testClasses.py	General autograding test classes  
* test_cases/	Directory containing the test cases for each question  
* searchTestClasses.py	Project 1 specific autograding test classes  

## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com) and [Node.js](https://nodejs.org/en/download/) (which comes with [npm](http://npmjs.com)) installed on your computer. From your command line:

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

