import fileinput

def word_count(words):
   splited = words.split()
   return len(splited)

if __name__=="__main__":
   words = input("input sentences: ")
   print("words:", word_count(words))