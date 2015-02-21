"""
Program to solve the daily programmer challenge #200 by Joseph Halstead.
The specifics of the puzzle can be found at:

http://www.reddit.com/r/dailyprogrammer/comments/2uo3yf/20150204_challenge_200_intermediate_metro_tile/

Program flows as follows:

1) Import the puzzle data from a file
2) Loop through each character in the grid and check whether it is the beginning of
   a rectangle. If it is then get the dimensions of the rectangle and mark each character
   within the rectangle as visited.
3) Repeat until at the end of the grid.

"""
def import_data(filepath):

    data =[]

    f = open(filepath, "r")
    length =0
    for line in f:
        data.append(list(line.strip())+["."])
        length = len(line.strip())+1
        
    data.append((". "*length).split())
        
    return data
    
    
def get_rectangle_dimensions(board,row,col):

    start_row = row #stores beginning value as row will change
    start_col = col #stores beginning value as col will change

    length =1
    height =1
    
    while board[row][col+1] <> ".": #go to right end corner of rectangle

        length = length +1
        col=col+1

    while board[row+1][col] <> ".": #go to bottom of rectangle
    
        board[row][start_col:start_col +length] = ["."] * (start_col-start_col +length)
        #above line changes all chars in the row within the rectangle to "."
        #to prevent the program from visiting them again.
        height = height +1
        row=row+1
    
    else:
        board[row][start_col:start_col +length] = ["."] * (start_col-start_col +length)
        #catches last row of the rectangle
            

        
    return [length,height]
       
def main():

    board = import_data("tests/test3.txt")
    
    for row_num,row in enumerate(board):
        
        for char_num,char in enumerate(row):
        
            if char == ".": #if char is "." we can ignore
            
                pass
                
            else:
                #print information on the rectangle
                rectangle_info = get_rectangle_dimensions(board,row_num, char_num)

                length = rectangle_info[0]
                height = rectangle_info[1]
                
                print str(length) +"x"+ str(height) +" tile of character " + char + \
                        " located at (" + str(char_num) + "," + str(row_num) + ")."
                        
                        
    

main()