sentence = input("Enter a sentence: ")

words = sentence.split()
word_count = len(words)

if words:
    longest_word = max(words, key=len)
else:
    longest_word = "No words"

reverse_sentence = sentence[::-1]

print("Word Count:", word_count)
print("Longest Word:", longest_word)
print("Reversed Sentence:", reverse_sentence)

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
