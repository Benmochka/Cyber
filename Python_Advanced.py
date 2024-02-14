def most_common(fyle_path, n):
    with open(fyle_path,'w') as f:
        data = f.read()
    data.split()
    words_count = {}
    for word in data:
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1        
    sorted_words = sorted(words_count.item(),key = lambda x: x[1], reverse = True)  
    for i in range(n):
        return sorted_words[i]
    