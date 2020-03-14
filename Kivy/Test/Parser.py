file = open('../src/conf/kottak.txt', mode = 'r', encoding = 'utf-8-sig')
lines=file.read().splitlines() 
file.close()
songs = []
tunes = {}
rythm = {}

for i in range(len(lines)):
    if lines[i] == str("--Title--"):
        songs.append(lines[i+1])
        tunes[lines[i+1]] = lines[i+3].split()
        rythm[lines[i+1]] = lines[i+5]
        
print(len(tunes["Boci, boci, tarka"]))