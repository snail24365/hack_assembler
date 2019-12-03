from parser import Parser
from stream_manager import StreamManager

class SymbolTableFactory():

	@classmethod
	def get_symbol_table(cls, stream_manager):
		symbol_table = {}
		R_SIZE = 16
		for i in range(R_SIZE):
			symbol_table["R" + str(i)] = i
		symbol_table["SCREEN"] = 16384
		symbol_table["KBD"] = 24576
		symbol_table["SP"] = 0
		symbol_table["LCL"] = 1
		symbol_table["ARG"] = 2
		symbol_table["THIS"] = 3
		symbol_table["THAT"] = 4
		variable_addr = 16

		stream_manager.reset()
		command = stream_manager.advance()

		while True:
			if Parser.command_type(command) == Parser.L_TYPE:
				symbol = Parser.symbol(command)
				symbol_table[symbol] = stream_manager.line_counter
			if not stream_manager.has_more_commands():
				break
			command = stream_manager.advance()
		
		stream_manager.reset()
		command = stream_manager.advance()
		while True:
			if Parser.command_type(command) == Parser.A_TYPE:
				addr = Parser.addr(command)
				if not addr.isdigit() and addr not in symbol_table.keys():
					symbol_table[addr] = variable_addr
					variable_addr += 1
			if not stream_manager.has_more_commands():
				break
			command = stream_manager.advance()
		stream_manager.reset()
		return symbol_table