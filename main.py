#!/usr/bin/env python3


if __name__ == "__main__":
	print("What is your name?")
	response = input()
	print("Nice to meet you, {}.".format(response))
	print("How many times should we print your name?")
	num = int(input())
	print("{}\n".format(response) * num)
