def most_common(fyle_path,n):
    with open(fyle_path, 'w+') as f:
        f.seek(0)
        data = f.read()
    words = data.split(' ')
    words_count = {}
    for word in set(words):
        words_count[word] = words.count(word)     
    sorted_words = sorted(words_count.items(),key = lambda x: x[1], reverse = True)
    print(sorted_words)  
    for i in range(n):
        print(sorted_words[i])

print(most_common(2))    