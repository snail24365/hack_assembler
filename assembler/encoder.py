from syntax_exception import InvalidCommendType
from syntax_exception import InvalidClause

class Encoder(object):
	def __init__(self):
		pass

	@classmethod
	def encode_addr(cls, clause):
		return bin(int(clause))[2:].rjust(16, "0")


	@classmethod
	def encode_comp(cls, clause):
		pre_code = "1" if "M" in clause else "0"

		other_code = None
		if clause == "0":  		    other_code = "101010"
		if clause == "1":  		    other_code = "111111"
		if clause == "-1": 		    other_code = "111010"
		if clause == "D":  		    other_code = "001100"
		if clause in ["A","M"]:     other_code = "110000"
		if clause == "!D":          other_code = "001101"
		if clause in ["!A","!M"]:   other_code = "110001"
		if clause == "-D":          other_code = "001111"
		if clause in ["-A","-M"]:   other_code = "110011"
		if clause == "D+1":         other_code = "011111"
		if clause in ["A+1","M+1"]: other_code = "110111"
		if clause == "D-1":         other_code = "001110"
		if clause in ["A-1","M-1"]: other_code = "110010"
		if clause in ["D+A","D+M"]: other_code = "000010"
		if clause in ["D-A","D-M"]: other_code = "010011"
		if clause in ["A-D","M-D"]: other_code = "000111"
		if clause in ["D&A","D&M"]: other_code = "000000"
		if clause in ["D|A","D|M"]: other_code = "010101"

		if other_code == None:
			raise InvalidClause(clause)

		comp = pre_code + other_code
		return comp

	
	@classmethod
	def encode_dest(cls, clause):
		if clause in ["", "null"]: return "000"
		if clause == "M": return "001"
		if clause == "D": return "010"
		if clause == "MD": return "011"
		if clause == "A": return "100"
		if clause == "AM": return "101"
		if clause == "AD": return "110"
		if clause == "AMD": return "111"
		raise InvalidClause(clause)


	@classmethod
	def encode_jump(cls, clause):
		if clause in ["", "null"]: return "000"
		if clause == "JGT": return "001"
		if clause == "JEQ": return "010"
		if clause == "JGE": return "011"
		if clause == "JLT": return "100"
		if clause == "JNE": return "101"
		if clause == "JLE": return "110"
		if clause == "JMP": return "111"
		raise InvalidClause(clause)