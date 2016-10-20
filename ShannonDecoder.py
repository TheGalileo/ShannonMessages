import os, sys, binascii

print "Hello Galileo!"

def convert2binary(text, encoding='utf-8', errors='Nope. Somethiing went wrong.'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def convert2text(bits, encoding='utf-8', errors='Nope. Somethiing went wrong.'):
    n = int(bits, 2)
    return num2bytes(n).decode(encoding, errors)

def num2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

if not os.path.exists(os.path.expanduser('~/Desktop/ShannonMessages')):
	os.mkdir(os.path.expanduser('~/Desktop/ShannonMessages'))
if not os.path.exists(os.path.expanduser('~/Desktop/ShannonMessages/Encrypted')):
	os.mkdir(os.path.expanduser('~/Desktop/ShannonMessages/Encrypted'))
if not os.path.exists(os.path.expanduser('~/Desktop/ShannonMessages/Decrypted')):
	os.mkdir(os.path.expanduser('~/Desktop/ShannonMessages/Decrypted'))

original = raw_input('Please type in your message and then press enter: \n')

binary = convert2binary(original)
key = input('Please enter your key and then press enter: \n')
binary_key = bin(key)[2:]

j = 0
encrypt = ''
for b in range(len(binary)):
	if (j >= len(binary_key)):
		j = j % len(binary_key)
	encrypt = encrypt + str(int(binary[b])^int(binary_key[j]))
	j = j + 1

title = raw_input('Please give this message a one word title:\n')
filename = '~/Desktop/ShannonMessages/Encrypted/' + title + '.txt'
text_file = open(os.path.expanduser(filename), "w")
text_file.write(encrypt)
text_file.close()

print('_________________________\nYour message has been encoded.\n')
print('The encrypted message is stored in a text file, which can be found in the subdirectory titled "Encrypted" in the directory "ShannonMessages" on your *Desktop*')
print('Thank you.\nTake care!\n')
