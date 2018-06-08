#!/usr/bin/env python3


import time


if __name__ == "__main__":
	print("What is your name?")
	response = input()
	time.sleep(0.5)

	print()
	print("Nice to meet you, {}.".format(response))
	print("How many times should we print your name?")
	num = int(input())
	time.sleep(0.5)

	print()
	print("{}\n".format(response) * num)
	time.sleep(0.5)

	print("Reading from file ...")
	time.sleep(0.5)
	try:
		file = open("index.html", "r")
		words = file.read().lower().split()
		file.close()
		print("Printing words in alphabetical order ...")
		time.sleep(0.5)
		for word in sorted(words):
			print(word)
			time.sleep(0.1)
	except FileNotFoundError:
		print("File not found!")
	print("END")
