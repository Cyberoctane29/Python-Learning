import random
import string

# Functions
def random_letters(n):
    letters = string.ascii_letters
    random_str = ''.join(random.choices(letters, k=n))
    return random_str

def reverse(word):
    reversed_string = ""
    for char in word:
        reversed_string = char + reversed_string
    return reversed_string

def encoding(word):
    a = word[0]
    word2 = word[1:] + a
    word2 = random_letters(3) + word2 + random_letters(3)
    return word2

def decoding(word):
    word2 = word[3:-3]
    a = word2[-1]
    word3 = a + word2[:-1]
    return word3

# Main body
message = input("Enter the message: ")

choice = input("Do you want to encode or decode? (encode/decode): ")

words = message.split(" ")

encoded_message = ""

if choice == 'encode':
    for word in words:
        if len(word) < 3:
            reversed_str = reverse(word)
            encoded_message += reversed_str + " "
        else:
            encoded_message += encoding(word) + " "

    # Strip the trailing space from the final encoded message
    encoded_message = encoded_message.strip()

    print("Original message: ", message)
    print("Encoded message: ", encoded_message)

elif choice == 'decode':
# pass
# note we can write pass in if blocks or other blocks if for the time being we dont have anything to fill for that block
    decoded_message=""
    for word in words:

     if len(word) < 3:
        reversed_str = reverse(word)
        decoded_message+= reversed_str + " "
     else:
        decoded_message+=decoding(word) + " "

     # Strip the trailing space from the final encoded message

    print("Original message: ", message)
    print("Decoded message: ", decoded_message)

else:
    raise ValueError("Choose from the given choices: 'encode' or 'decode'.")

#add the functionality that each word of a sentence will be turned into a code using print(" ".join(words)) and before it use words=st.split(" ")
#after st.split we can loop in the list and send each word to the function only if its a word of letters more than 3, in the function the word is encoded
#and sent back where we can concatenate them in another output string, we may not need to use join
#solved

#new problem in decoding      decoded_message = decoded_message.strip() gives an output of all the words joined into a sentence with no spaces

#assess this code which is possibly the solution
import random
import string

# Functions
def random_letters(n):
    letters = string.ascii_letters
    random_str = ''.join(random.choices(letters, k=n))
    return random_str

def reverse(word):
    reversed_string = ""
    for char in word:
        reversed_string = char + reversed_string
    return reversed_string

def encoding(word):
    a = word[0]
    word2 = word[1:] + a
    word2 = random_letters(3) + word2 + random_letters(3)
    return word2

def decoding(word):
    word2 = word[3:-3]
    a = word2[-1]
    word3 = a + word2[:-1]
    return word3

# Main body
message = input("Enter the message: ")

choice = input("Do you want to encode or decode? (encode/decode): ")

# Split the message into words based on spaces
words = message.split(" ")

decoded_message = ""

if choice == 'encode':
    for word in words:
        if len(word) < 3:
            reversed_str = reverse(word)
            decoded_message += reversed_str + " "
        else:
            decoded_message += encoding(word) + " "

    # Strip the trailing space from the final encoded message
    decoded_message = decoded_message.strip()

    print("Original message: ", message)
    print("Encoded message: ", decoded_message)

elif choice == 'decode':
    decoded_words = []
    for word in words:
        if len(word) < 3:
            reversed_str = reverse(word)
            decoded_words.append(reversed_str)
        else:
            decoded_words.append(decoding(word))

    # Join the decoded words back into the original message with spaces
    decoded_message = " ".join(decoded_words)

    print("Original message: ", message)
    print("Decoded message: ", decoded_message)

else:
    raise ValueError("Choose from the given choices: 'encode' or 'decode'.")

