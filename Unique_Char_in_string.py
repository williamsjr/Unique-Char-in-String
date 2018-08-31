class UniqueChars(object):
    """
    Return weather or not a string has all unique characters.
    
    None -> False
    '' -> True
    'foo' -> False
    'bar' -> True
    """
    
    def has_unique_chars(self, string):
        if string is None or '':
            return False
        return len(set(string) == len(string)
