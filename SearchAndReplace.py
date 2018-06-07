f = open('/path/to/file/file.txt','r')  # Open file with Read permissions, so we can keep the original.
filedata = f.read()
f.close()

newdata1 = filedata.replace("StringToReplace", "StringToInput")


f = open('/path/to/file/Newfile.txt','w')
f.write(newdata1)
f.close()
