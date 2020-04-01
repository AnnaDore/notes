dodo = int(input("print an integer: ").strip())

counts = str(bin(dodo)[2:]).split('0')
print(counts)
lens = [len(counts) for count in counts]
print(max(lens))