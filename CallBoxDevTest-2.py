def find_frequency (letter, sentence):
    count = 0
    for l in sentence:
        if l == letter:
            count = count+1
    
    return count

my_count = find_frequency("t", "tooth fairy stole my tooth")
print my_count
