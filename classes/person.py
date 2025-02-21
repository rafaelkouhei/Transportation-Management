class Person:
	people = []
	def __init__(self, name, shift, address, city, state, remote_work, status, entry_line, exit_line):
		self.name = name.upper()
		self._shift = shift
		self.address = address
		self.city = city 
		self.state = state
		self.remote_work = remote_work
		self._status = status
		self.entry_line = entry_line
		self.exit_line = exit_line
		Person.people.append(self)

	def __str__(self):
		return f'{self.name} | {self.shift}'

	def changeStatus(self):
		self._status = not self._status

	@classmethod
	def printPeople(cls):
		for person in cls.people:
			print(f'{person.name} | {person.shift} | {person._status}')

	@property
	def shift(self):
		return "Adm." if self._shift == 4 else "Outros"

class Temp(Person):
	def __init__(self, name, shift, address, city, state, remote_work, status, entry_line, exit_line, cod_temp):
		super().__init__(name, shift, address, city, state, remote_work, status, entry_line, exit_line)
		self.cod_temp