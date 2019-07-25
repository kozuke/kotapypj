from janome.tokenizer import Tokenizer


def janome_analyze(text: str):
    # 形態素解析オブジェクト生成
    t = Tokenizer()

    word_dic = {}
    lines = text.split('\r\n')
    for line in lines:
        malist = t.tokenize(line)
        for w in malist:
            word = w.surface
            ps = w.part_of_speech
            print(w, word, ps, sep='■')
            if ps.find('名詞') < 0:
                continue
            if word not in word_dic:
                word_dic[word] = 0
            word_dic[word] += 1

    keys = sorted(word_dic.items(), key=lambda x: x[1], reverse=True)
    for word, cnt in keys[:50]:
        print('{0}({1})'.format(word, cnt), end='\n')
