import urllib.request
import os
import re

meme_url = input("dis aí... CUAL péque tu ké? ")
meme_pack = urllib.request.Request(meme_url, headers={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"})
meme_pack = urllib.request.urlopen(meme_pack)
meme_pack = meme_pack.read().decode("utf-8")
folder_name = input("en cual pazta eu tenhu ki sauva, talkei? ")
os.mkdir(folder_name)
finded = re.findall(r'meme/\S+jpg', meme_pack);
print("\nachamu "+str(len(finded))+" meme pa vosse, talkei?\n")

for meme in finded:
    urllib.request.urlretrieve("http://packdememes.com/"+meme, folder_name+"/"+str(finded.index(meme)+1)+".jpg")
    print(meme + " foi abaixado cum sussesso! ["+str(finded.index(meme)+1)+"]")

print("terminamu o servicu bixo! talkei?")
