class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        cleaned_key = key.replace(" ", "")
        table = dict()
        position = 0
        a_ascii_num = ord("a") 
        for letter in cleaned_key:
            ascii_num = ord(letter)
            if not ascii_num in table:
                table[ascii_num] = a_ascii_num + position
                position += 1
        return message.translate(table)
