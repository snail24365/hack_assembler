from syntax_exception import InvalidCommendType
from syntax_exception import InvalidClause
from parser import Parser

class StreamManager(object):
	
	def __init__(self, stream):
		self.stream = stream
		self.line_counter = 0
		self.__has_more_commands = True


	def has_more_commands(self):
		return self.__has_more_commands


	def reset(self):
		self.stream.seek(0)
		self.__has_more_commands = True
		self.line_counter = 0


	def advance(self):
		if not self.has_more_commands():
			raise Exception("No more commands")
		skip = True
		while skip:
			line = self.stream.readline()
			if not line: 
				break

			ann_idx = line.find("//")
			if ann_idx != -1:
				line = line[:ann_idx]
			line = line.strip(" \t\n\r")
			skip = (line == "\n") or (line == "")
		
		self.__has_more_commands = (line != "")

		if Parser.command_type(line) in [Parser.A_TYPE, Parser.C_TYPE]:
			self.line_counter += 1

		return line
