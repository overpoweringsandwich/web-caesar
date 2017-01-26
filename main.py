#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import sys
low_alpha = "abcdefghijklmnopqrstuvwxyz"
upper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"



def alphabet_position(letter):
    '''Takes a letter character and returns it's index value in the alphabet'''

    # Returns the index value of a capital letter
    if letter.isupper() == True:

        return upper_alpha.index(letter)
    # Returns the index value of a lower case letter
    elif letter.islower() == True:

        return low_alpha.index(letter)
    else:
        return letter
        sys.exit()


def rotate_character(char, rot):
    '''Takes a character, rotates it's index, and returns the new character'''

    # finds the index and rotates it, if non-alpha it is returned
    if char.isalpha() == False:
        return char
        sys.exit()

    idx_position = alphabet_position(char)
    new_index = idx_position + int(rot)

    # Wraps the index around the alphabet and returns new character
    if char.isupper():
        rotated_idx = (new_index % 26)
        return upper_alpha[rotated_idx]
    else:
        rotated_idx = (new_index % 26)
        return low_alpha[rotated_idx]


def encrypt(text, rot):
    '''Takes a string, rotates each character one by one, and returns the new string'''
    final = ""
    for i in text:
        newalpha = rotate_character(i, rot)
        final = final + newalpha
    return final

class MainHandler(webapp2.RequestHandler):
    def get(self):
        message = "Hi"
        encrypted_message = encrypt(message, 13)
        self.response.write(encrypted_message)
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
