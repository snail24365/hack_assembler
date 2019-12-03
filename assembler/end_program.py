import sys

class EndProgram(object):
	@classmethod
	def success(cls, *messages):
		for message in messages:
			print(message)
		sys.exit(0)

	@classmethod
	def fail(cls, *messages):
		for message in messages:
			print(message)
		sys.exit(-1)