# import re

# pattern = r'[A-Z][A-Z][A-Z]/[A-Z]/[0-9][0-9]-\d{5}/\d{4}'
# match = (re.match(pattern,"SIT/B/01-02664/2021"))
# if match:
#     print("matched!!")
    
# else:
#     print("no match")
    
lang = input("What's the programming language you want to learn? ")

match lang:
    case "JavaScript":
        print("You can become a web developer.")

    case "Python":
        print("You can become a Data Scientist")

    case "PHP":
        print("You can become a backend developer")
    
    case "Solidity":
        print("You can become a Blockchain developer")

    case "Java":
        print("You can become a mobile app developer")
    case _:
        print("The language doesn't matter, what matters is solving problems.")