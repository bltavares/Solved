import solved_conf, argparse, re

parser = argparse.ArgumentParser("Having troubles with clients? Try it!")
parser.add_argument('-s', '--section', help = "Set the section to use on the config file", default = "Default")
parser.add_argument('-f', '--file', help = "Set the config file", default = "solved.conf")
args = parser.parse_args()

config = solved_conf.SolvedConf( conf_file = args.file, section = args.section)

problem = config.random_data("Problems")
reason = config.random_data("Reasons")
solution = config.random_data("Solutions")

message = re.sub("{{[a-zA-Z]*}}","%s",config.get_message())

print(("\n" + message + "\n") % (problem, reason, solution)) 
