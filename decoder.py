
import sys
import math

possible_directions = ['N','S','E','W']

"""
Helper function to read a file
It takes a file name a input and populates a list with the all_actions values.
It returns a list of number of states and all actions
"""

def fun_file_read(file_name):

	curr_line = 0

	all_actions = []

	with open(file_name) as f:

		for line in f:
			#iterating for all lines
			curr_line = curr_line + 1
			#splitting a line to extract values
			all_words = line.split()

			if all_words[0]=='iterations':
				number_of_states = curr_line-1

				return [number_of_states,all_actions]

				continue
			else:

				all_actions.append(int(all_words[1]))

"""
Helper function to read a grid from a file.
It takes the file name as the only argument.
It returns a grid as output.
"""

def extract_grid(file_name):

	with open(file_name) as f:
		line_no = 0
		for line in f:

			all_words = line.split()

			if line_no == 0:
				#define a matrix of size all_words * all_words
				grid = [[0 for i in range(len(all_words))] for j in range(len(all_words))]
			for col in range(len(all_words)):
				#populating the values
				grid[line_no][col] = int(all_words[col])

			line_no = line_no + 1
		return grid

"""
Function to print the path of the agent
It takes start position, end position, number of states and all actions as input
and print the path.
It does not explicitly return anything
"""

def extract_map(start_position, end_position, number_of_states, all_actions):
		curr_state = start_position
		end_state = end_position
		
		W = int(math.sqrt(number_of_states))

		while curr_state != end_state:

			curr_action = all_actions[curr_state]

			print(possible_directions[curr_action], end = " ")

			i = int(curr_state / W)
			j = int(curr_state % W)

			#checking for the action and assigning the nearby state with the value
			if curr_action == 0:

				nearby_state =  (i-1, j)

			elif curr_action == 1:

				nearby_state =  (i+1,j) 

			elif curr_action == 2:

				nearby_state =  (i,j+1)

			elif curr_action == 3:

				nearby_state =  (i,j-1)

			curr_state = W * nearby_state[0] + nearby_state[1]

		print(" ", end = "\n")





if __name__ == "__main__":

	input_grid = sys.argv[1]

	file_name = sys.argv[2]

	grid = extract_grid(input_grid)

	W = len(grid[0])

	start_position = [(i,j) for i in range(W) for j in range(W) if grid[i][j]==2]

	end = [(i,j) for i in range(W) for j in range(W) if grid[i][j]==3]

	start_position = start_position[0]

	end = end[0] 
	start_position = W * start_position[0] + start_position[1]

	end = W*end[0] + end[1]

	[number_of_states,all_actions] = fun_file_read(file_name)

	extract_map(start_position,end,number_of_states,all_actions)