/**
localizer.cpp

Purpose : implements a 2 - dimensional histogram filter
for a robot living on a colored cyclical grid by
correctly implementing the "initialize_beliefs",
"sense", and "move" functions.

This file is incomplete!Your job is to make these
functions work.Feel free to look at localizer.py
for working implementations which are written in python.
*/

#include "helpers.cpp"
#include <stdlib.h>
#include "debugging_helpers.cpp"

using namespace std;

/**
    TODO - implement this function

    Initializes a grid of beliefs to a uniform distribution.

    @param grid - a two dimensional grid map (vector of vectors
           of chars) representing the robot's world. For example:

           g g g
           g r g
           g g g

           would be a 3x3 world where every cell is green except
           for the center, which is red.

    @return - a normalized two dimensional grid of floats. For
           a 2x2 grid, for example, this would be:

           0.25 0.25
           0.25 0.25

 *********************Python Code******************************

    def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

 *****************End Python Code*******************************
 */
 // Compilation Stages -> Precompiler (check syntax) -> generate obj files check for errors -> link objects and make an executable

// INITIALIZE BELIEFS
vector< vector <float> > initialize_beliefs(vector< vector <char> > grid) {
 
    int height = grid.size();
    int width = grid[0].size(); // grid[0] as each iteration of a row will return the full vector, grid[0] ensures we start in the first column
    int area = height * width;
    float belief_per_cell = 1.0 / area;

 // initializing all array elements with one value, 
    vector< vector <float> > newGrid(height, vector<float>(width,belief_per_cell));

    return newGrid;
}

/**
    TODO - implement this function

    Implements robot motion by updating beliefs based on the
    intended dx and dy of the robot.

    For example, if a localized robot with the following beliefs

    0.00  0.00  0.00
    0.00  1.00  0.00
    0.00  0.00  0.00

    and dx and dy are both 1 and blurring is 0 (noiseless motion),
    than after calling this function the returned beliefs would be

    0.00  0.00  0.00
    0.00  0.00  0.00
    0.00  0.00  1.00

    @param dy - the intended change in y position of the robot

    @param dx - the intended change in x position of the robot

    @param beliefs - a two dimensional grid of floats representing
            the robot's beliefs for each cell before sensing. For
            example, a robot which has almost certainly localized
            itself in a 2D world might have the following beliefs:

            0.01 0.98
            0.00 0.01

    @param blurring - A number representing how noisy robot motion
            is. If blurring = 0.0 then motion is noiseless.

    @return - a normalized two dimensional grid of floats
            representing the updated beliefs for the robot.

    *********************Python Code******************************

    def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    newGrid = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy ) % width
            new_j = (j + dx ) % height
            # pdb.set_trace()
            newGrid[int(new_i)][int(new_j)] = cell
    return blur(newGrid, blurring)

    *****************End Python Code*******************************
*/
// MOVE FUNCTION

vector< vector <float> > move(int dy, int dx,
    vector < vector <float> > beliefs,
    float blurring)
{

    int height = beliefs.size(); // rows
    int width = beliefs[0].size(); // columns
    int new_h = 0;
    int new_w = 0;
  
// declare size of newGrid
    vector<vector<float> > newGrid = zeros(height, width);

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            new_h = (i + dy + height) % height;
            new_w = (j + dx + width) % width;
            newGrid[new_h][new_w] = beliefs[i][j];
        }
    }
    return blur(newGrid, blurring);
}


/**
    TODO - implement this function

    Implements robot sensing by updating beliefs based on the
    color of a sensor measurement

    @param color - the color the robot has sensed at its location

    @param grid - the current map of the world, stored as a grid
            (vector of vectors of chars) where each char represents a
            color. For example:

            g g g
            g r g
            g g g

    @param beliefs - a two dimensional grid of floats representing
            the robot's beliefs for each cell before sensing. For
            example, a robot which has almost certainly localized
            itself in a 2D world might have the following beliefs:

            0.01 0.98
            0.00 0.01

    @param p_hit - the RELATIVE probability that any "sense" is
            correct. The ratio of p_hit / p_miss indicates how many
            times MORE likely it is to have a correct "sense" than
            an incorrect one.

    @param p_miss - the RELATIVE probability that any "sense" is
            incorrect. The ratio of p_hit / p_miss indicates how many
            times MORE likely it is to have a correct "sense" than
            an incorrect one.

    @return - a normalized two dimensional grid of floats
            representing the updated beliefs for the robot.
*/
// SENSE FUNCTION

vector< vector <float> > sense(char color,
    vector< vector <char> > grid,
    vector< vector <float> > beliefs,
    float p_hit,
    float p_miss)
{
    vector< vector <float> > newGrid;

    float normalizer = 0;
    int x = grid.size();
    int y = grid[0].size();

    //newGrid = zeros(x,y);

    for (int i = 0; i < x; i++) {
        vector<float> row;
        for (int j = 0; j < y; j++) {
            if (grid[i][j] == color) {
                row.push_back((beliefs[i][j]) * (p_hit));
                //normalizer += ((beliefs[i][j]) * (p_hit));
            }
            else {
                row.push_back((beliefs[i][j]) * (p_miss));
                //normalizer += ((beliefs[i][j]) * (p_miss));
            }
        }
        newGrid.push_back(row);
    }

    return normalize(newGrid);
}
