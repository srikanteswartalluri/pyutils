__author__ = 'talluri'

def change_ordinal(letter):
    num = ord(letter)
    if num <= 120 and num >= 95:
        return chr(ord(letter) + 2)
    elif num <= 122 and num > 120:
        return chr(ord(letter) - 24)
    else:
        return letter


text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb " \
       "rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
text = "map"

newtext = ""
print text
i = 0
for letter in text:
    newtext += change_ordinal(letter)

print newtext
