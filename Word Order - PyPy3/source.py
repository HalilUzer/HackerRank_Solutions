# Enter your code here. Read input from STDIN. Print output to STDOUT



word_count = int(input())

words = {}

for i in range(0,word_count):
    word = input()
    if word in words.keys():
        words[word] += 1
    
    else:
        words[word] = 1

print(len(words))

for word in words.values():
    print(word,end = " ")
