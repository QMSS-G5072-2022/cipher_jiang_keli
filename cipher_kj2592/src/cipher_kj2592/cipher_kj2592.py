def cipher(text, shift, encrypt=True):
    """
    Enciphers is a function that takes in a string and shifts the letters by a fixed number of positions in the alphabet.
    Parameters 
    ----------
    text : str
        A string input that you want to encrypt or decrypt.
    shift : int
        An integer input that defines the number of positions to shift the letters by.
    encrypt : bool
        A boolean input that decides whether to encrypt your input string (True: encrypt; False: decrypt).
    Returns
    -------
    str
        The encrypted or decrypted string.
    Examples
    -------
    >>> text = "toys"
    >>> shift = 26
    >>> cipher_cjc2279.cipher(text, shift, encrypt = True)
    "TOYS"
    >>> text1 = "traffic"
    >>> shift1 = 1
    >>> cipher_cjc2279.cipher(text1, shift1, encrypt = False)
    "sqZeehb"
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text