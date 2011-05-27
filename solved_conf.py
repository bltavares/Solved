import configparser, random, sys, os.path

class SolvedConf:

  def __init__(self, conf_file = "solved.conf", section = "Default"):
    if not(os.path.isfile(conf_file)):
      sys.exit("File not found")
    self.conf_file = configparser.ConfigParser()
    try:
      self.conf_file.read(conf_file)
      self.section = section
    except configparser.ParsingError:
      sys.exit("Malformed configuration file: " + conf_file)

  def data_array(self, data):
    try:
      return self.conf_file.get(self.section, data).replace("\n","").split(",")
    except configparser.NoSectionError:
      sys.exit("Section not found: " + self.section)
    except configparser.NoOptionError:
      sys.exit("No option found: " + data)

  def random_data(self, data):
    return random.choice(self.data_array(data)).strip()

  def get_message(self):
    try:
      return self.conf_file.get(self.section,"Message")
    except configparser.NoOptionError:
      sys.exit("Missing message option")
    except configparser.NoSectionError:
      sys.exit("Missing message data for the section " + self.section)
