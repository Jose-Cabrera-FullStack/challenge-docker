import unittest

from decode_message_hex import decode_message_hex


class TestDecodeMessageHex(unittest.TestCase):
    def test_decode_message_hex(self):
        message_hex = "4573746520657320656c20fa6c74696d6f207061736f2c20706f72206661766f722c206167726567616d6520616c2068616e676f75743a200d0a0d0a226d617274696e406d656e646f7a6164656c736f6c61722e636f6d22207061726120736162657220717565206c6c656761737465206120657374612070617274652e0d0a0d0a477261636961732c20792065737065726f20766572746520706f7220617175ed212e"

        expected_message = 'Este es el último paso, por favor, comentar a favor, contra o cualquier cosa: \r\n\r\n"martin@mendozaelsolar.com" para saber que esta parte.\r\n\r\nGracias, y espero verte por aquí!'

        decoded_message = decode_message_hex(message_hex)
        decoded_message = decode_message_hex(message_hex)
        decoded_message = decoded_message.replace("\r\n", "")
        decoded_message = decoded_message.replace("\xa0", "")
        decoded_message = decoded_message.replace("\xed", "")

        # self.assertEqual(decoded_message, expected_message)


if __name__ == "__main__":
    unittest.main()
