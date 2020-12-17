
with open('file','r') as f:
    cipher = f.read()

out=''
for c in cipher[::-1]:
    out = out[:int(len(out)/2)]+c+out[int(len(out)/2):]

print(out)
