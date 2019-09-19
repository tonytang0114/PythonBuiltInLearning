class MySeq:
    def __getitem__(self, index):
        return index # return whatever is passed to it

s = MySeq()
print(s[1])
print(s[1:4])
print(s[1:4:2])
print(s[1:4:2, 9])
print(s[1:4:2, 7:9])
print(slice)
print(dir(slice))