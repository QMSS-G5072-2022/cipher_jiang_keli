from cipher_kj2592 import cipher_kj2592
    
def test_cipher():
    example = 'abcd'    
    expected = 'ABCD'
    actual = cipher_kj2592.cipher(example, 26)
    assert actual == expected
