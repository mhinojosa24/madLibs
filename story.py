'''
His mother scolds him about (climbing) to
high places and warns that his father (was)
cracked by (doing) the same thing. He then
courts (Easter) Egg, but the Bad Egg comes and
kidnaps her. Humpty must climb to death-defying
(heights) to rescue his beloved.

'''

def user_input(prompt):
     user = input(prompt)
     return user
# def user_fail(prompt):



u_1 = user_input("Pick a out door activity: skating, rollerblading, or running.\n")
u_2 = user_input("which is a past tense in English?: was or doing. \n")
u_3 = user_input("which is a present tense in English?: was or doing. \n")
u_4 = user_input("what holiday do you search for egg?: easter or christmas. \n")
u_5 = user_input("what's the most scariest, heights or walking? \n")



print("His mother scolds him about {} to high places and warns \n that his father {} cracked by {} the same thing. He \n then courts {} Egg, but the Bad Egg comes and kidnaps her. \n Humpty must climb to death-defying {} to rescue his beloved.".format(u_1.islower(),u_2.islower(),u_3.islower(),u_4,u_5))
