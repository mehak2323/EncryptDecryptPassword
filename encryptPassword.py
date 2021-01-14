# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 15:15:51 2021

@author: mehak
"""
import base64

password_raw =input("Enter your password: ")

#Encode a password string into a UTF-8 string
password = password_raw.encode("utf-8")

#Encode utf-8 string into a base64 string
encoded = base64.b64encode(password)
#Decoding utf-8 string to remove letter b specifying it's a bytes-like object
encoded = encoded.decode("utf-8")
print("Encoded password is: ",encoded)

#Decode base64 string into a utf-8 string
decoded = base64.b64decode(encoded)
#Decoding utf-8 string to remove letter b specifying it's a bytes-like object
decoded = decoded.decode("utf-8")
print("Decoded password is: ",decoded)