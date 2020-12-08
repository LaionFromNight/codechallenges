import unittest
from parameterized import parameterized
import solution


class TestLeetCode(unittest.TestCase):

    @parameterized.expand([
        ("this is a string!!","dGhpcyBpcyBhIHN0cmluZyEh"),
        ("this is a test!","dGhpcyBpcyBhIHRlc3Qh"),
        ("now is the time for all good men to come to the aid of their country.",
         "bm93IGlzIHRoZSB0aW1lIGZvciBhbGwgZ29vZCBtZW4gdG8gY29tZSB0byB0aGUgYWlkIG9mIHRoZWlyIGNvdW50cnku"),
        ("1234567890  ", "MTIzNDU2Nzg5MCAg"),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ ", "QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVog"),
        ("the quick brown fox jumps over the white fence. ",
         "dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSB3aGl0ZSBmZW5jZS4g"),
        ("dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSB3aGl0ZSBmZW5jZS4",
         "ZEdobElIRjFhV05ySUdKeWIzZHVJR1p2ZUNCcWRXMXdjeUJ2ZG1WeUlIUm9aU0IzYUdsMFpTQm1aVzVqWlM0"),
        ("VFZSSmVrNUVWVEpPZW1jMVRVTkJaeUFna","VkZaU1NtVnJOVVZXVkVwUFpXMWpNVlJWVGtKYWVVRm5h"),
        ("TVRJek5EVTJOemc1TUNBZyAg","VFZSSmVrNUVWVEpPZW1jMVRVTkJaeUFn")
    ])
    def test_multiple(self, input, expect_result):
        # Assume

        # Action
        result = solution.to_base_64(input)
        decoding_result = solution.from_base_64(result)

        # Asert
        self.assertEqual(result, expect_result,
                         "The result for input {} should be {} but is {}".format(input, expect_result, result))

        self.assertEqual(decoding_result, input,
                         "The result for input {} should be {} but is {}".format(input, expect_result, result))
