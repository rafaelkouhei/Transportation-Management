from classes.person import Person

def printMain():
	print("Welcome to Main!")

def main():
	printMain()

	fulano = Person("Rafael", 4, "Rua João Bonat 1385", "Curitiba", "PR", 2, True, 403, 403)
	ciclao = Person("Isabela", 4, "Rua Eneas Marques 444", "São José dos Pinhais", "PR", 2, True, 404, 404)

	# Person.printPeople()

	print(fulano)

if __name__ == "__main__":
	main()