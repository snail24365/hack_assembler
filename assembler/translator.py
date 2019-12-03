from parser import Parser
from encoder import Encoder
from stream_manager import StreamManager
from symbol_table_factory import SymbolTableFactory
from syntax_exception import InvalidCommendType
from syntax_exception import InvalidClause

class Translator(object):
	def __init__(self, asm_file):
		self.stream_manager = StreamManager(asm_file)

	def get_machine_code(self):
		
		symbol_table = SymbolTableFactory.get_symbol_table(self.stream_manager)
		
		result = ""
		self.stream_manager.reset()
		command = self.stream_manager.advance()
		while True:
			if Parser.command_type(command) == Parser.A_TYPE:
				addr = Parser.addr(command)
				if addr.isdigit():
					code = Encoder.encode_addr(addr)
				elif addr in symbol_table.keys():
					addr = symbol_table[addr]
					code = Encoder.encode_addr(addr)
				else:
					raise InvalidCommendType()
				result += (code + '\n')

			elif Parser.command_type(command) == Parser.C_TYPE:
				dest = Parser.dest(command)
				comp = Parser.comp(command)
				jump = Parser.jump(command)
				
				code_dest = Encoder.encode_dest(dest)
				code_comp = Encoder.encode_comp(comp)
				code_jump = Encoder.encode_jump(jump)
				c_prefix = "111"
				code = c_prefix + code_comp + code_dest + code_jump				
				result += (code + '\n')

			elif Parser.command_type(command) in [ Parser.L_TYPE, Parser.IGNORE ]:
				pass
			else:
				raise InvalidCommendType()

			if not self.stream_manager.has_more_commands():
				break
			command = self.stream_manager.advance()
		return result		
