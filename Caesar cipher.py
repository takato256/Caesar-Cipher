import string
import time


print("これはシーザー暗号のプログラムです。\n\'ひらがな\' または \'アルファベット\' のメッセージを暗号化できます。\n\n")


print("暗号化・復号するメッセージの言語を選択します。")
language = input("\'ひらがな\' または \'アルファベット\' を入力してください>>")

while not language.startswith(('ひ', 'ヒ', '平', 'h', 'H', 'あ', 'ア', 'A', 'a')):
    print('\"注意\": \'ひらがな\' または \'アルファベット\' が入力されていません。')
    language = input("\'ひらがな\' または \'アルファベット\' を入力してください>>")
    
if language.startswith(('ひ', 'ヒ', '平', 'h', 'H')):
    SYMBOLS = "あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをんがぎぐげござじずぜぞだちづでどばびぶべぼぱぴぷぺぽ"
else:
    SYMBOLS = string.ascii_letters
                        

message = input('暗号化・復号するメッセージを入力してください>>')


print('メッセージの暗号化・復号を行います。\n\'encrypt\' で暗号化  \'decrypt\' で復号  ができます')
mode = input('\'encrtpt\' または \'decrypt\' を入力してください>>')

while not mode.startswith(('e','E', 'd', 'D')):
    print("\"注意\": \'encrypt\' または \'decrypt\' が入力されていません。")
    mode = input('\'encrtpt\' または \'decrypt\' を入力してください>>')

if mode.startswith(('e', 'E')):
    mode = "encrypt"
else:
    mode = "decrypt"



while True:
    key = input('鍵となる自然数を入力してください>>')
    while not key.isdecimal():
        print("\"注意\": 自然数が入力されていません。")
        key = input("鍵となる自然数を入力してください>>") 
    
    key = int(key)

    if key % len(SYMBOLS) == 0:
        print("この鍵は脆弱性を抱えている場合があります。")
        check = input('このまま実行してもよろしいですか？[y/n]>>')
        if check.startswith(('y', 'Y')):
            break
        else:
            continue
    break
        
    



output_text = ''

start_time = time.time()

for symbol in message:
    if symbol in SYMBOLS:
        index_before = SYMBOLS.find(symbol)
        
        if mode == "encrypt":
            index_after = index_before + key
        elif mode == "decrypt":
            index_after = index_before - key
            
        while index_after >= len(SYMBOLS):  
            index_after -= len(SYMBOLS)
        while index_after < 0:
            index_after += len(SYMBOLS)
            
        output_text += SYMBOLS[index_after]
        
    else:
        output_text += symbol

take_time = round(time.time() - start_time, 3)
print(len(SYMBOLS))     
print(output_text)
print('掛かった時間: {}秒'.format(take_time))