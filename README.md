# LSB Steganography

This tool allows for the secure encryption and encoding of text within an image using binary steganography, as well as the retrieval, decoding, and decryption of hidden messages.

## Getting Started

To get started, start by cloning this GitHub repository using the following:

```
git clone https://github.com/LoganSayles/LSB-Steganography.git
```

<p align="center"><img width="800" height="181" alt="1" src="https://github.com/user-attachments/assets/cd7bbfc3-7680-48e0-b430-b2ce3cb54a94" /></p>

### Prerequisites

To use this software you will need some required python modules, to quickly install the required modules use the following command:

```
pip3 install -r requirements.txt
```

<p align="center"><img width="800" height="181" alt="2" src="https://github.com/user-attachments/assets/d5fcdf80-74ba-4987-a058-8876cd21dfa5" /></p>

## Running the tests

To run the tests that come with this software run the following command:

```
python3 unit-tests.py
```

<p align="center"><img width="800" height="181" alt="3" src="https://github.com/user-attachments/assets/cb037699-86f6-44b4-8a35-8a997b91be38" /></p>

## Deployment

To begin, you will need an image to encode. For this tool any .png file format should work fine, anything else is not supported due to the lossy compression method used by JPEG

### Encoding

Once you have an image to encode the following parameters can be specified.

```
REQUIRED ARGUMENTS
-e, --encode      | to specify that you would like to encode an image
-i, --image       | to specify the image to encode
-t, --text        | to specify the text you would like to encode

OPTIONAL ARGUMENTS
-o, --ofset       | to specify the amount of bytes to offset the text by
-ck, --custom_key | to specify a custom key to be used
```
```
USAGE

python3 main.py -e -i image_name.png -t "enter text here" -o 300 -ck "Enter Key here"
```
![vmplayer_49E3bchDtp](https://github.coventry.ac.uk/storage/user/5742/files/5df929e6-ed89-4463-be16-63b8da3500b8)

### Decoding

Once you have an image to decode the following parameters can be specified

```
REQUIRED ARGUMENTS
-d, --decode      | to specify that you would like to decode an image
-i, --image       | to specify the image to decode
```
```
GROUPED ARGUMENTS

IMPORTANT: only one of these arguements should be specified

-k, --key         | to specify the key to decode the image
-ck, --custom_key | to specify a custom key to be used
```

![vmplayer_Ps7T72tKCa](https://github.coventry.ac.uk/storage/user/5742/files/8ebece51-ca3a-49c8-b7a7-3bfa4b02eb9b)

## Algorithm Justification

This software works by converting all the bytes in an image array to binary then selecting each least significant bit (LSB) of each byte and replacing it with a bit from the message the user has entered. The program currently goes through the image until the offset position has been reach. Altnernatively, I could have seperated the RGB values into their own respective arrays, however I believe that the efficiency of the program would have decreased as a result of more nested loops then I currently require. The method I chose of image steganography is LSB (least significant bit) I chose this method, as I knew it would be fast, simple and adaptable. Other methods include EBE (edge based embedding) this is where the software detects the edges of the image and encodes the data there as well as RPE (random pixel embedding) where the data is randomly entered into the image. These alternatives are more complex and also less efficient, the aim of them is to make it harder to find the message within the image however due to the human eye not being able to pickup the small change in pixel colour I believe that the method I chose best suited the software

## Authors

* **Logan Sayles** - *Primary and Only Contributer*
