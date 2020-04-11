def correctSubtitleEncoding(filename, newFilename, encoding_from, encoding_to='UTF-8'):
    with open(filename, 'r', encoding=encoding_from) as fr:
        with open(newFilename, 'w', encoding=encoding_to) as fw:
            for line in fr:
                fw.write(line[:-1]+'\r\n')

filename=input("Unesi naziv prevoda: ")
filename = filename +".srt"
newFilename=input("Unesi novi naziv prevoda: ")
newFilename = newFilename +".srt"
correctSubtitleEncoding(filename,newFilename,"Windows-1250")