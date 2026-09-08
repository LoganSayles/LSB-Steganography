import unittest
from encode_image import Encoder
from decode_image import Decoder


class MyTestCase(unittest.TestCase):

    @unittest.expectedFailure
    def test_key_gen(self):  # Testing to see if the key generated is different each time
        self.my_class_instance = Encoder("sample.png", "Test Text 123", 20, None)
        result_one = self.my_class_instance.key_gen()
        result_two = self.my_class_instance.key_gen()
        self.assertEqual(result_one, result_two)  # Test is expected to fail

    @unittest.expectedFailure
    def test_custom_key(self):  # Testing to see if key generated from custom key is different each time
        self.my_class_instance = Encoder("sample.png", "Test Text 123", 20, "Test key")
        result_one = self.my_class_instance.key_gen()
        result_two = self.my_class_instance.key_gen()
        self.assertEqual(result_one, result_two)  # Test is expected to fail

    @unittest.expectedFailure
    def test_message_generator(self):  # Checking to see if message generated is different each time
        self.my_class_instance = Encoder("sample.png", "Test Text 123", 20, None)
        result_one = self.my_class_instance.message_generator()
        result_two = self.my_class_instance.message_generator()
        self.assertEqual(result_one, result_two)  # Test is expected to fail

    @unittest.expectedFailure
    def test_set_byte(self):  # Checking to see if the image has been altered by the method
        self.my_class_instance = Encoder("sample.png", "Test Text 123", 20, None)
        image_one = self.my_class_instance.binary_img_
        self.my_class_instance = Encoder("sample.png", "Test Text 123", 20, None)
        self.my_class_instance.set_byte()
        image_two = self.my_class_instance.binary_img_
        self.assertEqual(image_one, image_two)

    def test_bit_interpreter(self):  # Testing to see if the message found is the same each time
        #  For this test to run there is required to have a sample.png present
        self.my_class_instance = Encoder("sample.png", "This is a test", 20, "TestKey")
        self.my_class_instance.set_byte()

        self.my_class_instance = Decoder("sample_encoded.png", "", "TestKey")
        result_one = self.my_class_instance.bit_interpreter()
        result_two = self.my_class_instance.bit_interpreter()
        self.assertEqual(result_one, result_two)

    def test_message_formatter(self):  # Testing to see if the decoded message is the correct message
        self.my_class_instance = Decoder("sample_encoded.png", "", "TestKey")
        result = self.my_class_instance.message_formatter()
        self.assertEqual(result, "This is a test")

if __name__ == '__main__':
    unittest.main()
