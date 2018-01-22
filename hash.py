import hashlib
import time
import re

# validate user input
while (True):
	user_input = input("Type a password | len >= 6 & contains numbers: ")
	if len(user_input) < 6:
		print("Type a password with at least 6 characters")
	elif re.match('[0-9]', user_input) is None:
	 	print("Type a password that contains at least one number")
	else:
	 	break 

encoded_input = user_input.encode('utf-8')

# SHA-1
start = time.time()
hash_sha1 = hashlib.sha1(encoded_input)
end = time.time()
print ("SHA-1", hash_sha1.hexdigest(), "Time Elapsed: ", end - start) 

# SHA-256
start = time.time()
hash_sha256 = hashlib.sha256(encoded_input)
end = time.time()
print ("SHA-256", hash_sha256.hexdigest(), "Time Elapsed: ", end - start) 

# SHA-512
start = time.time()
hash_sha512 = hashlib.sha512(encoded_input)
end = time.time()
print ("SHA-512", hash_sha512.hexdigest(), "Time Elapsed: ", end - start) 

# MD5
start = time.time()
hash_md5 = hashlib.md5(encoded_input)
end = time.time()
print("MD-5", hash_md5.hexdigest(), "Time Elapsed: ", end - start)
