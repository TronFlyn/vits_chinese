""" from https://github.com/keithito/tacotron """

'''
Defines the set of symbols used in text input to the model.
'''
_punctuation = ';:,.!?¡¿—…"«»“” '

# chinese_cleaners
_pad        = '_'
_punctuation_zh = '；：，。！？-“”《》、（）ＢＰ…— '
_letters = 'ㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄏㄐㄑㄒㄓㄔㄕㄖㄗㄘㄙㄚㄛㄜㄝㄞㄟㄠㄡㄢㄣㄤㄥㄦㄧㄨㄩˉˊˇˋ˙ '


# Export all symbols:
symbols = [_pad] + list(_punctuation) + list(_letters) + list(_letters_ipa)

symbols_zh = [_pad] + list(_punctuation_zh) +  list(_letters)

# Special symbol ids
SPACE_ID = symbols.index(" ")