import chardet
print(chardet.detect(b'Hello, world!'))

data = '离离原上草，一岁一枯荣'.encode('gbk')
print(chardet.detect(data))
dd=chardet.detect(data)
print(dd['encoding'])