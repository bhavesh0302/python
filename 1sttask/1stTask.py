#1.string reverse
inputString ="this is string example"
print("1.string reverse:",inputString[::-1])


#2.string reverse by words
inputString="this is string example"
splitString=inputString.split(' ')
print("2.string reverse by words:",splitString[0][::-1],splitString[1][::-1],splitString[2][::-1],splitString[3][::-1])


#3. 2 char interchange
splitString=inputString.split(" ")
print(splitString[0][0:2][-1::-1]+splitString[0][2:4][::-1]+" "+splitString[1][0:2][::-1]+" "+splitString[2][0:2][::-1]+splitString[2][2:4][::-1]+splitString[2][4:6][::-1]+" "+splitString[3][0:2][::-1]+splitString[3][2:4][::-1]+splitString[3][4:6][::-1]+splitString[3][6:8][::-1])

#4.space with split and join by *
inputString4="this is string example"
splitString=inputString4.split(' ')
joinSign="*"
print("4.space with split and join by *:",joinSign.join(splitString))

#5.replace is with was
inputString5="this is string example"
replaceString=inputString5.replace(" is"," was")
print("5.replace is with was:",replaceString)

