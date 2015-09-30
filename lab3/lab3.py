import sys

thing = sys.argv[1]

if thing == thing[::-1]:
  print ("true")
else:
  print("false")
  
