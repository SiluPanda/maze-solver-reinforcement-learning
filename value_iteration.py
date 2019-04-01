import math
import sys


class markov_desicion_problem:

    #init function to inilialize number of states and number of actions
    def __init__(self,t_s,t_a):
        self.total_states = t_s
        self.total_actions = t_a

    #helper function to retrun all values in the form of a list
    def return_all_values(self):
        return [self.total_states,self.total_actions,self.transition,self.gamma,self.start,self.end]

    #defining all the necessary values for a transistion
    def tansistion_values(self,start,end,transition,gamma):
        self.start = start
        self.end = end
        self.transition = transition
        self.gamma = gamma

    
    """
    Main Value interation function:
    Takes all self vaaribles and calculates the utility (V) values. It is calculated in a always true while loop
    until it reaches convergence. convergence constant is defined as 1e-16
    """   


    def val_iter(self):
        [total_states,total_actions,transition,gamma,start,end] = self.return_all_values()

        iterator = 0

        convergence_constant = 1e-16

        previous_utilities = [0] * (total_states)

        updated_utilities  = [0] * (total_states)
        
        Action = [-1 for i in range(total_states)]
        Action[end]=-1

        def isconverged(list1, list2, convergence_const):
            maxi = abs(list1[1] - list2[1])
            for i in range(len(list1)):
                if abs(list1[i] - list2[i]) > maxi:
                    maxi = abs(list1[i] - list2[i])

            if maxi < convergence_constant:
                return True
            else:
                return False

        #looping until it reaches the convergence
        while True:
            iterator += 1

            for state in range(total_states):
                if state == end:
                    continue


                max_util = -100000000000

                for curr_action in range(total_actions):

                    myaction = transition[state][curr_action]
                    if len(myaction)!=0:

                        curr_sum = sum([act[1] * (act[2] + gamma * previous_utilities[act[0]]) for act in myaction])

                        if max_util < curr_sum:

                            max_util = curr_sum

                            Action[state] = curr_action

                            updated_utilities[state] = max_util

                
            if isconverged(previous_utilities, updated_utilities, convergence_constant) == True:
                break
            previous_utilities = [ele for ele in updated_utilities]
        return [updated_utilities,Action, iterator]

    """Helper function to print the path of the solver"""

    def detect_the_path(self,V,Action):

        state_iter = self.start

        destination = self.end

        possible_directions = ['N','S','E','W']

        
        width = int(math.sqrt(self.total_states))

        while state_iter != destination:

            action_current = Action[state_iter]

            #prints the first letter of the direction of the action.
            print(possible_directions[action_current],end = ' ')

            p1 = state_iter/width
            p2 = state_iter%width

            
            if action_current == 0:

                states_around =  (p1-1,p2)  

            elif action_current == 1:

                states_around =  (p1+1,p2)

            elif action_current == 2:

                states_around =  (p1,p2+1) 

            elif action_current ==3:  

                states_around =  (p1,p2-1)
            state_iter = width*states_around[0] + states_around[1]
        print("",end = "\n")
            
def read_mdp_file(file_name):

    with open(file_name) as opened_file:

        for curr_line in opened_file:
            #splitting the line with white space
            all_ele = curr_line.split()

            #extracting values w.r.t to the tag
            if all_ele[0] == 'numStates':

                total_states = int(all_ele[1])

            elif all_ele[0]=='numActions':

                total_actions = int(all_ele[1])

                decision_model = markov_desicion_problem(total_states,total_actions)

                chance_of_trans = []
                reward_trans = []

                #initializing a matrix
                for i in range(total_states):

                    reward_trans.append([])

                    chance_of_trans.append([])

                    for j in range(total_actions):

                        reward_trans[i].append([])

                        chance_of_trans[i].append([])

            #extracting values and assigning them to the corresponding variables

            elif all_ele[0]=='start':

                start = int(all_ele[1])

            elif all_ele[0]=='end':

                end = int(all_ele[1])

            elif all_ele[0]=='discount':

                gamma = float(all_ele[1])
            else:

                all_ele = [all_ele[0]] + [int(num) for num  in all_ele[1:4]] + [float(num) for num in all_ele[4:6]]
                #probababilty
                chance_of_trans[all_ele[1]][all_ele[2]].append((all_ele[3],all_ele[5],all_ele[4]))

        decision_model.tansistion_values(start,end,chance_of_trans,gamma)  

        return decision_model

if __name__ == "__main__":

    file_name = sys.argv[1]

    decision_model = read_mdp_file(file_name)

    [V,Action,t] = decision_model.val_iter()
    
    total_states = len(V)
    for i in range(total_states):
        print("%f %d "%(V[i],Action[i]))
    print("iterations \t %d"%t)

   