import os

#print(os.listdir('.')) # List directory with a non-ASCII filename
#print(os.listdir(b'.')) # Let's pretend we do not know the encoding and get filenames as bytes

pi_name_bytes = os.listdir(b'.')[1]
print(pi_name_bytes) 
pi_name_str = pi_name_bytes.decode('ascii', 'surrogateescape')
print(pi_name_str)
print(pi_name_str.encode('ascii', 'surrogateescape'))

