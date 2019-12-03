from __future__ import with_statement
from __future__ import print_function

import os
import sys
from syntax_exception import InvalidCommendType
from syntax_exception import InvalidClause
from translator import Translator
from end_program import EndProgram
from user_message import UserMessage


if __name__ == '__main__':
	if len(sys.argv) != 2:
		EndProgram.fail(UserMessage.INVALID_ARGUMENT_NUMBER)

	translated = ""
	path_asm_file = sys.argv[1]
	try:
		with open(path_asm_file) as asm_file:
			translated = Translator(asm_file).get_machine_code()		

	except FileNotFoundError as e:
		EndProgram.fail(UserMessage.ASM_FILE_NOT_FOUND, str(e))

	except InvalidClause as e:
		EndProgram.fail(UserMessage.INVALID_CLAUSE, str(e))

	except InvalidCommendType as e:
		EndProgram.fail(UserMessage.INVALID_COMMEND_TYPE, str(e))

		
	if translated == "":
		EndProgram.success(UserMessage.EMPTY_HACK_FILE)
	try:
		file_name = os.path.basename(path_asm_file).split(".")[0]
		hack_file_path = os.path.join(os.path.dirname(path_asm_file), f"{file_name}.hack")
		with open(hack_file_path, "w") as hack_file:
			hack_file.write(translated)
		EndProgram.success(UserMessage.JOB_SUCCEED)			

	except OSError as e:
		EndProgram.success(UserMessage.OS_ERROR, str(e))