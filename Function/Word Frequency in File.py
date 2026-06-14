def freq(filepath):
    word_count={}
    with open(filepath,'r') as file:
        for line in file:
          words=line.split()
          for char in words:
                  char = char.lower().strip('.,?!')
                  word_count[char]=word_count.get(char,0)+1
    return word_count


file_path = 'sample.txt'
frequency = freq(file_path)
print(frequency)
