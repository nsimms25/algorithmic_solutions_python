'''
Find the capital of a state entered by the user, not all states are included. 

Param
State: The state to be looked up, entered by the user. 

Print the capital of the state inputted. 
'''

state_dictionary = {'Colorado': 'Denver', 'Alaska': 'Juneau',
                    'California': 'Sacramento', 'Georgia': 'Atlanta',
                    'Kansas': 'Topeka', 'Nebraska': 'Lincoln',
                    'Oregon': 'Salem', 'Texas': 'Austin', 'New York': 'Albany'}

state_input = input('Please input the state to be looked up. ')

state = str.lower(state_input)
new_input = str.title(state)

if(new_input not in state_dictionary):
    print('Capital unknown')
else:
    print(state_dictionary[new_input])
