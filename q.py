from collections import Counter
def counting(s):

    str1 =  s.lower()

    words = str1.split()
    letters = [char for char in str1 if char.isalpha()]
    
 
    word_count = Counter(words)
    letter_count = Counter(letters)
    
  
    print("Word Occurrence")
    for word, count in word_count.items():
        print(f"{word}-{count}")
    
   
    print("\nLetter Occurrence")
    for letter, count in letter_count.items():
        print(f"{letter}-{count}")


s = "TCS is the largest IT service company in India, headquartered in Mumbai, and also the largest employee base."
counting(s)

    


