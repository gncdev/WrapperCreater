"""
    _____ _              _____      _____
  / ____(_)            / ____|    |  __ \
 | |  __ _  __ _ _ __ | |   ______| |  | | _____   __
 | | |_ | |/ _` | '_ \| |  |______| |  | |/ _ \ \ / /
 | |__| | | (_| | | | | |____     | |__| |  __/\ V /
  \_____|_|\__,_|_| |_|\_____|    |_____/ \___| \_/
      
      Coded By GianC-Dev
     https://github.com/GianC-Dev
     
"""

import os



def startwithh(string, fp):
	for line in fp:
		if line.startswith(string):
			return line


class WrapperCreater:
	
	def __init__(self, Path):
		self.oswalk(Path)
	
	def oswalk(self, Path):
		for i in os.walk(Path):
			listers = list(i)
			listersstr = str(listers)
			self.create(listers)
			break
	
	def create(self, listers):
		listers.pop(0)
		listener = list()
		for lan in listers[1]:
			lstr = str(lan)
			if lstr.endswith(".py"):
				listener.append("." + lstr.replace(".py", ""))
			else:
				continue
		file = open("__init__.py", "w")
		for i in listener:
			if i == ".idea":
				continue
			ifclassusinginfile = open(i.replace(".", "") + ".py", "r")
			if startwithh("class", ifclassusinginfile) is None:
				if i.replace(".", "") == "__init__":
					continue
				file.write("import " + i.replace(".", "") + " as " + i.replace(".", "") + "\n")
				continue
			else:
				fp = open(i.replace(".", "") + ".py", "r")
				for line in fp:
					if line.startswith("class"):
						classname = line.replace("class", "").replace(":", "")
						file.write("from " + i + " import " + classname.replace(" ", ""))
						continue


