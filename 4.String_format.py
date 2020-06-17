##1.
print("I\'m %dyears old." % 20)
print("I like %s very much." % "Python")
print("Apple starts with %c" % "A")

print("I like %s color and %s color" % ("blue","red"))

#2. 
print("--------------------------------------")
print("I\'m {} years old.".format(20))
print("I like {} color and {} color". format("blue","red"))
print("I like {1} color and {0} color". format("blue","red"))

#3. 
print("--------------------------------------")
print("I\'m {age} years old, and I like {color} color.".format(age=20, color="red"))

#4.
print("--------------------------------------")
age = 20
color = "red"
print(f"I\'m {age} years old, and I like {color} color.")

########### exit charactor ###########################
print("--------------------------------------")
# \n : line change
print("백문이 불여일견\n백견이 불여일타")

# \"" or \ ''
print("저는 \"내맘대로 코딩\"입니다.")

# \\
print("C:\\Users\\yohko\\OneDrive")

# \r : move cursor at front
print("Red Apple\rPine")

# \b : back space - remove one char
print("Redd\b Apple")

# \t
print("Red\tApple")

#Quiz
print("--------------------------------------")
site_address = "http://naver.com"
naver = site_address[7:site_address.find(".")]
password = naver[:3]+str(len(naver))+str(naver.count("e"))+"!"
print(password)