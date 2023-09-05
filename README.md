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

## Question 1
#### Screenshots of successful runs:
```python
python pacman.py -l tinyMaze -p SearchAgent
```
![Q1_tinymaze_success](https://user-images.githubusercontent.com/11414055/138003625-cc982f44-3af3-443b-a755-cea5e05249af.png)
```python
python pacman.py -l mediumMaze -p SearchAgent
```
![](https://user-images.githubusercontent.com/11414055/138004166-03f9bafc-165d-4180-8d42-380ad06d5925.png)
```bash
$ python pacman.py -l mediumMaze -p SearchAgent
[SearchAgent] using function depthFirstSearch
[SearchAgent] using problem type PositionSearchProblem
Path found with total cost of 130 in 0.0 seconds
Search nodes expanded: 144
Pacman emerges victorious! Score: 380
Average Score: 380.0     
Scores:        380.0     
Win Rate:      1/1 (1.00)
Record:        Win  
```
```python
python pacman.py -l bigMaze -z .5 -p SearchAgent
```
![Q1_bigmaze_success](https://user-images.githubusercontent.com/11414055/138004726-fd081c22-98a3-47ec-afe6-f932f5084540.png)
#### Answers to questions posted in [Question 1](http://ai.berkeley.edu/search.html#Q1):
The exploration of the board using DFS is slightly surprising in that in general, PacMan searches along the desired parth, ignoring a series of states (e.g. positions on the board) that would never lead him to the goal state.  The return from DFS is the path Pacman must take to reach the goal state, so he does not actually move to the explored states on his path to the goal, although the board provides an overlay of the states that were explored.

DFS provides a sub-optimal solution (e.g. not the shortest path), in that it returns the "first" path it encounters that reaches the goal state.  If this path is at the very bottom of the search tree, but happens to be the first path explored, then this path is returned, regardless of the path depth. 

## Question 2
#### Screenshots of successful runs:
```python
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
```
![Q2_mediummaze_success](https://user-images.githubusercontent.com/11414055/138005250-bc1097b9-b5d6-40ef-af6c-342890d63b8b.png)
```bash
$ python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
[SearchAgent] using function bfs
[SearchAgent] using problem type PositionSearchProblem
Path found with total cost of 68 in 0.0 seconds
Search nodes expanded: 269
Pacman emerges victorious! Score: 442
Average Score: 442.0     
Scores:        442.0     
Win Rate:      1/1 (1.00)
Record:        Win     
```
```python
python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
```
![Q2_bigmaze_success](https://user-images.githubusercontent.com/11414055/138005394-d79821e8-9f27-400d-b7a9-4bb9fcd20dee.png)


## Question 3
#### Screenshots of successful runs:
```python
python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
```
![Q3_mediummaze_success](https://user-images.githubusercontent.com/11414055/138021564-0b30f2c7-7a64-4d11-8fb2-0f39a0a3d4a2.png)
```bash
$ python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
[SearchAgent] using function ucs
[SearchAgent] using problem type PositionSearchProblem
Path found with total cost of 68 in 0.0 seconds
Search nodes expanded: 269
Pacman emerges victorious! Score: 442
Average Score: 442.0     
Scores:        442.0     
Win Rate:      1/1 (1.00)
Record:        Win   
```
```python
python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
```
![Q3_mediumdottedmaze_success](https://user-images.githubusercontent.com/11414055/138021789-9146d8e4-7b14-412e-ac58-736a50183597.png)
```bash
$ python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
Path found with total cost of 1 in 0.0 seconds
Search nodes expanded: 186
Pacman emerges victorious! Score: 646
Average Score: 646.0     
Scores:        646.0     
Win Rate:      1/1 (1.00)
Record:        Win 
```
```python
python pacman.py -l mediumScaryMaze -p StayWestSearchAgent
```
![Q3_mediumscarymaze_success](https://user-images.githubusercontent.com/11414055/138021994-34bbaae3-b872-4526-a22a-83d33d32aef9.png)
```bash
$ python pacman.py -l mediumScaryMaze -p StayWestSearchAgent --frameTime 0
Path found with total cost of 68719479864 in 0.0 seconds
Search nodes expanded: 108
Pacman emerges victorious! Score: 418
Average Score: 418.0
Scores:        418.0     
Win Rate:      1/1 (1.00)
Record:        Win 
```

## Question 4
#### Screenshots of successful runs:
```python
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```
![Q4_bigmaze_success](https://user-images.githubusercontent.com/11414055/138022285-d200b3c7-e1a0-4930-8d9d-72c1ae895f88.png)


## Question 5
#### Screenshots of successful runs:
```python
python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
```
![05 tiny corners](https://user-images.githubusercontent.com/57783476/139521327-8d1cec50-f0c8-48bc-ad53-edca210c66b5.png)
```bash
Path found with total cost of 28 in 0.0 seconds
Search nodes expanded: 435
Pacman emerges victorious! Score: 512
Average Score: 512.0
Scores:        512.0
Win Rate:      1/1 (1.00)
Record:        Win
```

```python
python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
```
![05 medium corners](https://user-images.githubusercontent.com/57783476/139521445-71aec2f9-a430-4935-972d-b5f8afd524a7.png)
```bash
Path found with total cost of 106 in 0.2 seconds
Search nodes expanded: 2448
Pacman emerges victorious! Score: 434
Average Score: 434.0
Scores:        434.0
Win Rate:      1/1 (1.00)
Record:        Win
```

## Question 6
#### Screenshots of successful runs:
```python
python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
```
![06 mediumcorners heuristic](https://user-images.githubusercontent.com/57783476/139521541-941b37f2-8a1a-4194-bca1-fe8250194bf0.png)
```bash
Path found with total cost of 106 in 9.9 seconds
Search nodes expanded: 978
Pacman emerges victorious! Score: 434
Average Score: 434.0
Scores:        434.0
Win Rate:      1/1 (1.00)
Record:        Win
```

## Question 7
#### Screenshot of successful runs:
```python
python pacman.py -l trickySearch -p AStarFoodSearchAgent
```
![07 trickysearch astarfoodsearch](https://user-images.githubusercontent.com/57783476/140805058-ca8cad35-c8ec-4740-bf5a-0a4fb5c9b525.png)
```bash
Path found with total cost of 60 in 36.5 seconds
Search nodes expanded: 4137
Pacman emerges victorious! Score: 570
Average Score: 570.0
Scores:        570.0
Win Rate:      1/1 (1.00)
Record:        Win
```

## Question 8
#### Screenshot of successful runs
```python
python pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5 
```
![08 bigsearch closestdotsearch](https://user-images.githubusercontent.com/57783476/140805834-f8c511a9-dc88-4452-91a8-b26985502606.png)
```bash
Path found with cost 350.
Pacman emerges victorious! Score: 2360
Average Score: 2360.0
Scores:        2360.0
Win Rate:      1/1 (1.00)
Record:        Win
```




## Credits

* http://ai.berkeley.edu/search.html#Q8


---

> GitHub [@brycehills](https://github.com/brycehills) &nbsp;&middot;&nbsp;
> LinkedIn [@brycehills](https://www.linkedin.com/in/brycehills1/)

