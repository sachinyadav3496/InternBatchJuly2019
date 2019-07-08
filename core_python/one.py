#this is a python script
import time
print("Welcome at ",time.ctime())
s = """     Hello--world--how--are--you--?      """
print("before processing ",s)
s = s.strip() # leading and traling spaces are trimmed 
print("After strip ",s)
# "Hello--world--how--are--you--?"
s = s.split("--") # [ "Hello","world","how","are","you","?"]
print("After Split ",s)
s = s[::-1] # ["?","you","are","how","world","Hello"]
print("After Reversing ",s)
s = " ".join(s)
print("final outupt = ",s)
