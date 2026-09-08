import cv2
import base64
import hashlib
import numpy as np
from cryptography.fernet import Fernet


class Decoder:  # Initialising class attributes#
    """
    This class is responsible for finding and decoding the message hidden within the image
    """

    def __init__(self, filename_, key_, custom_key_):
        """
        Initializing a decoder with filename, key(optional) and custom_key(optional)

        filename_ (str): The filename of the image to decode
        key_ (str)(optional): The key that will be used to decrypt the message
        custom_key_(str)(optional): The custom key set by the user to decrypt the message
        """
        self.code = ""
        self.key_ = key_
        self.start_byte = "1010101010101010"
        self.stop_byte = "1111111010111110"
        self.custom_key_ = custom_key_

        self.img = cv2.imread(filename_)
        self.binary_img_ = (np.vectorize(np.binary_repr, otypes=[str])(self.img, width=8))  # Converting img to binary
        self.array_shape_ = np.shape(self.binary_img_)  # Obtaining shape of binary image array

    def bit_interpreter(self):  # Responsible for finding the start and end of the message
        """
        Returns the binary string that was originally encoded in the image

        return check_byte (str)
        """
        check_byte = ""

        for y in range(self.array_shape_[0]):  # Incrementing for Y axis of pixels
            for x in range(self.array_shape_[1]):  # Incrementing for X axis of pixels
                for byte in range(self.array_shape_[2]):  # Incrementing for each byte within an RGB series
                    check_byte += (self.binary_img_[y, x, byte][7])  # Storing the current bytes LS

                    if check_byte[-16:] == self.stop_byte:  # Checks the last 16 bits for the stop byte
                        return check_byte[check_byte.find(self.start_byte) + 16:check_byte.find(self.stop_byte)]
                        # Returns the binary string sequence to decode

    def message_formatter(self):
        """
        Responsible for converting the binary message to ascii and then decrypting it with the key set


        Returns the ascii version of the originally encoded message
        return decrypted_message (str)
        """
        byte = ""
        new_message = ""
        found_code = self.bit_interpreter()
        for char in found_code:  # Extracting individual bits
            byte += char  # Storing extracted bits
            if (len(byte)) == 8:
                new_message += chr(int(byte, 2))  # Turning every 8 bits (byte) into its ascii value
                byte = ""

        if self.custom_key_ is not None:
            hlib = hashlib.md5()
            hlib.update(self.custom_key_.encode())

            self.key_ = base64.urlsafe_b64encode(hlib.hexdigest().encode())

        f = Fernet(self.key_)  # Preparing decryption key
        decrypted_message = f.decrypt(new_message)  # Decrypting encrypted message

        return decrypted_message.decode()
