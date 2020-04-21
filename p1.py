fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    ln = line.lstrip()
    if(ln == ''):
    	continue
    word = ln.split()
    if word[0].find("From") >= 0 and word[0].find("From:") == -1:
        print(word[1])
        count = count + 1

print("There were", count, "lines in the file with From as the first word")
print("Hello World!")
print("Good")

