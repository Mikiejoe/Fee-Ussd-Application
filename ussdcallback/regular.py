import re

pattern = r'[A-Z][A-Z][A-Z]/[A-Z]/[0-9][0-9]-\d{5}/\d{4}'
match = (re.match(pattern,"SIT/B/01-02664/2021"))
if match:
    print("matched!!")
    
else:
    print("no match")