sentence = "I like how cats like to nap in sunny spots, just like my lazy neighbor Bob likes to do on weekends."

# Program 1
count = 0

for i in sentence.lower():
    if i == "e":
        count += 1

print(count)

# Pogram 2

like_count = 0
for word in sentence.lower().split():
    if word == "like":
        like_count += 1

print(like_count)

# Program 3

word_count = 0
seperate_words = sentence.split()

word_count = len(seperate_words)
print(word_count)
