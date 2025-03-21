import fonts

tgt = "あ"
for tgt in "あいうえおフォント":
    #print(tgt)
    code = ord(tgt)
    #print(code)
    bitmap = fonts.access(code)
    #print(bitmap)
    for b in bitmap:
        print(
            "{:0>8b}"
            .format(b)
            .replace("1","■")
            .replace("0"," "))
