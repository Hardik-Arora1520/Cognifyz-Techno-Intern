'''This is a program of a Python program that reads a text
file and counts the occurrences of each
word in the file. Display the results in
alphabetical order along with their
respective counts.'''
print('Task of file manupulation')
def inspect(file):
    f=open(file)
    f.read()
    count={}
    for  line in file:
           word = line.strip()
           for w in word:
               count[w] = count.get(w,0)+1
    sort_w=sorted(count.items())
    
    for w,count in sort_w:
        print(f"{w}:{count}") 
           
file="D:/Code/Cognifyz/Python Dev/Level 2/Task5.txt"
inspect(file)