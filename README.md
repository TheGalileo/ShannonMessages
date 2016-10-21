# Shannon Messages
  
# What is it?  
A python program to encode and decode regular text messages using the concept of One Time Pad.  
  
# What does it do?  
  * Encodes the text message using a secret key (that is only shared between the sender and the receiver)  
  * Decodes the encoded text message using the same key  
 
# How to encode a message?
  * Find someone with whom you want to share a secret. 
  * Share a 4 digit key with him/her (example 1234) and do not share it with anyone else.  
  * Run `ShannonEncoder.py` and follow the instructions that appear.  
  * The encoded message will be saved as a .txt file in `~/Desktop/ShannonMessages/Encrypted`  
  * Send this .txt file to your friend over email or some IM application.  
    
# What do I do when I receive an encoded message?
  * Most probably yor received a .txt file containing 0s and 1s. Or you might have simlpy received a string of 0s and 1s.
  * Copy this string to your clipboard
  * Run `ShannnonDecoder.py` and follow the instructions that appear.
  * The decoded message will be saved as a .txt file in `~/Desktop/ShannonMessages/Decrypted`
  * Read the .txt file, it's in plain simple english.
  
# Contribute?
Yeah, go ahead. These are some of the things that you can work upon:  
  * Create GUI using Tkinter (or whatever)  
  * Directly send the encoded .txt file over email  
  * What if the entered filename already exists? (You'll have to go over the `ShannonEncoder.py` code to understand this)
  
# Why Shannon?
Because this is his centennial year. I wanted to do my `bit`.
