import read

df = read.load_data()

text = []

for each in df:
    text.append(each['headline'])
    
print(len(text))