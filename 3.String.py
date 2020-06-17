# sentence = 'I\'m a boy.'
# print(sentence)
# sentence2 = "Python is easy."
# print (sentence2)

# sentence3 = """
# I\'m a boy.
# And python is easy.
# """

# print(sentence3)

## slicing
# jumin = "990120-1234567"

# print("sex:" + jumin[7]) 
# print("year:" + jumin[0:2]) # 0~1
# print("month:"+jumin [2:4])
# print("day:"+ jumin[4:6])

# print("DOB:" + jumin[:6])
# print("last 7 digit:" + jumin[7:])
# print("last 7 digit:" + jumin[-7:])

## String function
python = "Python is Amazing"
print(python.lower())
print(python.upper())

print(python[0].isupper())
print(len(python))

print(python.replace("Python","Java"))

index = python.index("n")
print(index)
index = python.index("n", index+1)
print(index)
print(python.find("a"))

print(python.find("Java"))
#print(python.index("Java")) #error: compare to find

print(python.count("n"))