""" from https://github.com/keithito/tacotron """

'''
Defines the set of symbols used in text input to the model.
'''

'''# chinese_cleaners
_pad        = '_'
_punctuation_zh = '；：，。！？-“”《》、（）ＢＰ…— '
_letters = 'ㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄏㄐㄑㄒㄓㄔㄕㄖㄗㄘㄙㄚㄛㄜㄝㄞㄟㄠㄡㄢㄣㄤㄥㄦㄧㄨㄩˉˊˇˋ˙ '
'''

# zh_ja_mixture_cleaners
_pad        = '_'
_punctuation = ',.!?-~…'
_letters = 'AEINOQUabdefghijklmnoprstuvwyzʃʧʦɯɹəɥ⁼ʰ`→↓↑ '

# Export all symbols:
symbols = [_pad] + list(_punctuation) + list(_letters)

# Special symbol ids
SPACE_ID = symbols.index(" ")
