#input 1=" programming is fun"
#input 2= "m"
#output = [6,7]

sentence = "I decided to learn how to program"
letter= "m"
output= []

#enumerate will allow you to track the current location or idx
for  current_location, current_letter in enumerate(sentence):
    if current_letter == letter:
        output.append(current_location)

print (output)
