# Take input of a word
string = input("Please enter your own word : ")

# Take input of a character
char = input("Please enter your own character : ")

i = 0
count = 0

# Loop to find the occurrence of the character
while i < len(string):
    if string[i] == char:
        count = count + 1
    i = i + 1  # MUST be outside the if block

# Display the result
print("The total number of times",char,"has occured =",count)