from solved_conf import *

config = SolvedConf()

problem = config.random_data("Problems")
reason = config.random_data("Reasons")
solution = config.random_data("Solutions")

msg = "\nYou got %s, caused by %s and you MUST %s to solve it\n" % (problem, reason, solution) 
print(msg)


