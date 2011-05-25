import configparser, random

def getDataArr(config,data):
  return config.get("Default",data).replace("\n","").split(",")

def getRandomData(config, data):
  """docstring for getRandomData"""
  return random.choice(getDataArr(config, data))

Config = configparser.ConfigParser()
Config.read("solved.conf")

problem = getRandomData(Config,"Problems").strip() 
reason = getRandomData(Config, "Reasons").strip()
solution = getRandomData(Config, "Solutions").strip()

msg = "\nYou got %s, caused by %s and you MUST %s to solve it\n" % (problem, reason, solution) 
print(msg)


