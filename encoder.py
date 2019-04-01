import sys

possible_directions = ['N','S','E','W']
all_directions = len(possible_directions)


"""
Function to find the next position.
It takes, the map_of_grid, position points (i,j) of the current position, and current action
return thr nect position

"""	
def find_the_position(map_of_grid, i, j, current_action):

	W = len(map_of_grid)

	if current_action == 0:
		if i == 0:
			return (-1,-1)
		if map_of_grid[i-1][j] == 1:
			return (-1,-1)
		else:
			return (i-1,j)	

	elif current_action == 1:
		if i == W-1:
			return (-1,-1)
		if map_of_grid[i+1][j]==1:
			return (-1,-1)
		else:
			return (i+1,j) 	

	elif current_action == 2:
		if j == W-1:
			return (-1,-1)
		if map_of_grid[i][j+1]==1:
			return (-1,-1)
		else:
			return (i,j+1)

	elif current_action == 3:							
		if j == 0:
			return (-1,-1)
		if map_of_grid[i][j-1]==1:
			return (-1,-1)
		else:
			return (i,j-1)	
	return 1	

"""
Funtion to print the path
It taked the map_of_grid as the input and prints the path and other info (such as number of states
and number of directions) as the output.
It does not return anything explicitly
"""		

def show_path(map_of_grid):

	W = len(map_of_grid[0])

	
	total_states = W*W

	print("numStates" , total_states)

	print("numActions", all_directions)

	start = [(i,j) for i in range(W) for j in range(W) if map_of_grid[i][j]==2]

	end = [(i,j) for i in range(W) for j in range(W) if map_of_grid[i][j]==3]

	start = start[0]

	end = end[0] 

	start = W*start[0] + start[1]

	end = W*end[0] + end[1]

	print("start %d"%start)
	print("end %d"%end)

	for i in range(W):

		for j in range(W):
			
			if map_of_grid[i][j] != 1 or map_of_grid[i][j] != 3:
				s = W*i + j
				for current_action in range(4):
					near_states = find_the_position(map_of_grid,i,j,current_action)
					
					if near_states[0]==-1:
						continue
					s1 = W * near_states[0] + near_states[1]

					print("transitions ", s, current_action, s1, -1, 1)


	print("discount", 1)	

"""
Helper function to read a grid file
Takes a file name as input and return  map_of_grid
"""	

def read_map_of_grid_file(file_name):

	with open(file_name) as f:

		curr_row = 0

		for single_line in f:

			all_words = single_line.split()

			if curr_row == 0:

				map_of_grid = [[0 for i in range(len(all_words))] for j in range(len(all_words))]

			for col in range(len(all_words)):

				map_of_grid[curr_row][col] = int(all_words[col])	

			curr_row = curr_row + 1
		return map_of_grid


if __name__ == "__main__":
	file_name = sys.argv[1]
	map_of_grid = read_map_of_grid_file(file_name)
	show_path(map_of_grid)