class Solution:
    def defangIPaddr(self, address: str) -> str:

        return ''.join("[.]" if c == "." else c for c in address)

        # just try to use translate table
        # return address.translate(str.maketrans('.', "[.]"))