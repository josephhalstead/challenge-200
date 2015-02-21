Program to solve the daily programmer challenge #200 by Joseph Halstead.
The specifics of the puzzle can be found at:

http://www.reddit.com/r/dailyprogrammer/comments/2uo3yf/20150204_challenge_200_intermediate_metro_tile/

Program flows as follows:

1) Import the puzzle data from a file
2) Loop through each character in the grid and check whether it is the beginning of
   a rectangle. If it is then get the dimensions of the rectangle and mark each character
   within the rectangle as visited.
3) Repeat until at the end of the grid.

