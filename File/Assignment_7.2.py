fname = input("Enter file name: ")
fh = open(fname)
total = 0.0
count = 0.0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        total += float(line[line.find(":")+1:])
        count += 1
    else: continue

print ("Average spam confidence:", total/count)
