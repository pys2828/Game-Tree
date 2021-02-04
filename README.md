# Game-Tree

The Game Tree represents the possible choices of moves that might be made by a player or computer during a game. In these trees, the root of a tree represents the
initial configuration of the game and each lower level represents all possible moves from the current state (node).

For this tree, we focus on the movement of a knight.  The knight's move always creates an L shape: two squares in one direction and one square at a right angle to the first direction or one square in one direction and two square at a right angle to the first direction. We want to see if a knight can capture all the 16 pawns in 16 moves or not. The goal is to have the knight eat all the pawns in k moves. The initial state will be the root of the tree and goal state is one possibility for a leaf in case of success.
