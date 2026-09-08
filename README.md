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

To begin, you will need an image to encode. For this tool, any .png file format should work fine; anything such as JPEG is not supported due to the lossy compression method

### Encoding

Once you have an image to encode, the following parameters can be specified.

```
REQUIRED ARGUMENTS
-e, --encode      | to specify that you would like to encode an image
-i, --image       | to specify the image to encode
-t, --text        | to specify the text you would like to encode

OPTIONAL ARGUMENTS
-o, --offset       | to specify the number of bytes to offset the text by
-ck, --custom_key | to specify a custom key to be used
```
```
USAGE

python3 main.py -e -i image_name.png -t "enter text here" -o 300 -ck "Enter Key here"
```
<p align="center"><img width="800" height="181" alt="4" src="https://github.com/user-attachments/assets/75f67e44-a82c-427a-a8a0-c3ed80788fb7" /></p>

### Decoding

Once you have an image to decode, the following parameters can be specified

```
REQUIRED ARGUMENTS
-d, --decode      | to specify that you would like to decode an image
-i, --image       | to specify the image to decode
```
```
GROUPED ARGUMENTS

IMPORTANT: only one of these arguments should be specified

-k, --key         | to specify the key to decode the image
-ck, --custom_key | to specify a custom key to be used
```

<p align="center"><img width="800" height="181" alt="5" src="https://github.com/user-attachments/assets/471863a8-a61c-490e-bb7b-28996d087ddb" /></p>

## Algorithm Justification

This application works by converting all the bytes in an image array to binary, then selecting the least significant bit (LSB) of each byte and replacing it with a bit from the message the user has entered. The program currently goes through the image until the offset position has been reached. Alternatively, I could have separated the RGB values into their own respective arrays; however, I believe that the efficiency of the application would have decreased as a result of containing more nested loops than I reasonably require. The method I chose for image steganography is LSB (least significant bit). I chose this method, as I knew it would be fast, simple, and adaptable. Other methods include EBE (edge-based embedding), where the application detects the edges of the image and encodes the data there instead, as well as RPE (random pixel embedding), where the data is randomly entered into the image. These alternatives are more complex and less efficient. The aim of the alternatives is to make it harder to find the message within the image. However, due to the human eye not being able to pick up the small change in pixel colour, I believe that the method I chose best suited the software

**UPDATE:** After graduating, LLMs have become much more prominent; I believe now that RPE (random pixel embedding) would be the most effective solution. This is due to the inhuman ability of LLMs to be able to see the smallest of variations within an image and thus a string of every-so-slightly changed pixels would easily be detectable.

## Authors

* **Logan Sayles** - *Primary Contributer*
