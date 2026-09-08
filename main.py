import os
import argparse
import numpy as np
from encode_image import Encoder
from decode_image import Decoder

np.set_printoptions(threshold=np.inf)  # Setting Print Options for numpy

parser = argparse.ArgumentParser()  # Initializing args parts arguments
group = parser.add_mutually_exclusive_group()
group.add_argument('-e', '--encode', action='store_true', help="encode")
group.add_argument('-d', '--decode', action='store_true', help="decode")

parser.add_argument('-i', '--image', type=str, help="specify a file name")
parser.add_argument('-t', '--text', type=str, help="specify text to encode")
parser.add_argument('-o', '--offset', type=str, help="specify the offset that the text will be entered")
parser.add_argument('-k', '--key', type=str, help="specify a key")
parser.add_argument('-ck', '--custom_key', type=str, help="specify a custom key")
# Initialising arguments for CLI functionality

args = parser.parse_args()

filename = None
text = None
key = None
custom_key = None
if args.encode is not False or args.decode is not False:  # If either args are fulfilled allow for args parse to be used
    if args.encode is not False:
        if args.image is not None:
            filename = args.image  # Setting filename
            if not (os.path.exists(filename)):  # Checking if file exists
                print("Error: Failed to find file")
                quit()
            elif not (filename.endswith(".png")):  # Checking if it is the correct file format
                print("Error: Non-png file types are not supported")
                quit()
            else:
                pass
        else:
            print("Error: Must specify a filename")
            quit()

        if args.text is not None:  # Checking if the user supplied any text
            text = args.text
        else:
            print("Error: Must specify text to encode")
            quit()

        if args.offset is not None:  # Checking if user supplied an offset
            offset = args.offset
        else:  # If no offset was supplied set to 0 by default
            offset = "0"

        if args.custom_key is not None:  # Checking if a custom key was set
            custom_key = args.custom_key
        else:
            custom_key = None

        encode = Encoder(filename, text, offset, custom_key)  # Initializing encoder class
        print(encode.set_byte())
    else:
        if args.image is not None:
            filename = args.image  # Setting filename
            if not (os.path.exists(filename)):  # Checking if file exists
                print("Error: Failed to find file")
                quit()
            elif not (filename.endswith(".png")):  # Checking if it is the correct file format
                print("Error: Non-png file types are not supported")
                quit()
            else:
                pass
        else:
            print("Error: Must specify a filename")
            quit()

        if args.custom_key is not None:  # Checking if a custom key was set
            custom_key = args.custom_key
        elif args.key is not None:
            key = args.key
        else:
            print("Error: Must enter a decryption key")
            quit()

        decode = Decoder(filename, key, custom_key)  # Initializing Decoder class
        print(decode.message_formatter())
else:
    answer = input("Would you like to encode or decode?: ")

    if answer.lower() == "encode":
        filename = input("Please enter a filename: ")
        if filename == "":
            print("Error: Must Specify filename")
            quit()
        elif not (os.path.exists(filename)):  # Checking if the file exists
            print("Error: Failed to find file")
            quit()
        elif not (filename.endswith(".png")):  # Checking if the correct file format was supplied
            print("Error: Non-png file types are not supported")
            quit()
        else:
            pass

        text = input("Please enter text to encode: ")

        if text == "":  # Checking if text was supplied
            print("Error: Must specify text to encode")
            quit()

        answer = input("Would you like to specify an offset?(y/n): ")

        if answer.lower() == "y":
            offset = input("Please enter offset: ")
        else:  # setting offset to 0 by default
            offset = "0"

        answer = input("Would you like to specify a custom key?(y/n): ")
        if answer.lower() == "y":
            custom_key = input("Please enter a custom key: ")
        else:
            custom_key = None

        encode = Encoder(filename, text, offset, custom_key)  # Initializing Encoder class
        print(encode.set_byte())
    else:
        filename = input("Please enter a filename: ")
        if filename == "":
            print("Error: Must specify filename")
            quit()
        elif not (os.path.exists(filename)):  # Checking if file exists
            print("Error: Failed to find file")
            quit()
        elif not (filename.endswith(".png")):  # Checking if the correct file format was supplied
            print("Error: Non-png file types are not supported")
            quit()
        else:
            pass

        answer = input("Would you like to specify a custom key?(y/n): ")
        if answer.lower() == "y":
            custom_key = input("Please enter a custom key: ")
            if custom_key == "":
                print("Error: Key not specified")
                quit()
        else:
            key = input("Please enter the key: ")
            if key == "":
                print("Error: Key not specified")
                quit()

        decode = Decoder(filename, key, custom_key)  # Initializing Decoder class
        print(decode.message_formatter())
