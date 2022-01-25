name = input("Enter file: ")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    line = line.rstrip()
    word = line.split()
    if len(word)<1 or not line.startswith("From ") :continue
    s=word[1]
    counts[s]=counts.get(s,0)+1
bigcount = None
bigword= None
for key,val in counts.items() :
  if bigcount is None or bigcount<val:
      bigword = key
      bigcount = val

print (bigword,bigcount)
