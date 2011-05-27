import configparser, random

class SolvedConf:

  def __init__(self, conf_file = "solved.conf", section = "Default"):
    self.conf_file = configparser.ConfigParser()
    self.conf_file.read(conf_file)
    self.section = section

  def data_array(self, data):
    return self.conf_file.get(self.section, data).replace("\n","").split(",")

  def random_data(self, data):
    return random.choice(self.data_array(data)).strip()


