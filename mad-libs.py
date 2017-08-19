''' mad-libs.py by Devin Carter
this is a simple program to take words the user inputs and place them into a preformatted string
'''

answer1 = input("Type a color: ")
answer2 = input("Type an animal: ")
answer3 = input("Give the animal something to do: ")

print("The %s %s %s over the log, into the water" % (answer1, answer2, answer3))