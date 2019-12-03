from syntax_exception import InvalidCommendType
from syntax_exception import InvalidClause


class Parser(object):

	A_TYPE = 'A_TYPE'
	L_TYPE = 'L_TYPE'
	C_TYPE = 'C_TYPE'
	IGNORE = 'IGNORE'

	@classmethod
	def command_type(cls, command):
		if command.startswith("@"):
			return Parser.A_TYPE
		if command.startswith("(") and command.endswith(")"):
			return Parser.L_TYPE
		if ("=" in command) or (";" in command):
			return Parser.C_TYPE
		if command == "":
			return Parser.IGNORE
		raise InvalidCommendType(command)


	@classmethod
	def addr(cls, command):
		if Parser.command_type(command) == Parser.A_TYPE:
			return command[1:]
		raise InvalidCommendType(command)


	@classmethod
	def symbol(cls, command):	
		if Parser.command_type(command) == Parser.L_TYPE:
			return command[1:-1]
		raise InvalidCommendType(command)

	
	@classmethod
	def dest(cls, command):
		if Parser.command_type(command) != Parser.C_TYPE:
			raise InvalidCommendType(command)
		return command.split("=")[0] if "=" in command else ""


	@classmethod
	def comp(cls, command):
		if Parser.command_type(command) != Parser.C_TYPE:
			raise InvalidCommendType(command)
		result = ""
		token = command.split("=")
		temp = token[1] if len(token) == 2 else token[0]

		result = temp.split(";")[0]
		return result


	@classmethod
	def jump(cls, command):
		if Parser.command_type(command) != Parser.C_TYPE:
			raise InvalidCommendType(command)
		return command.split(";")[1] if ";" in command else ""