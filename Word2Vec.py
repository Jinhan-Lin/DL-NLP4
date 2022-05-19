import jieba
import os  # 用于处理文件路径
import re
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
#获取预料内容
def getCorpus(txt_path):
    corpus = []
    path = txt_path
    output = 'corpus.txt'
    Character = u'[a-zA-Z0-9’!"#$%&\'()*+,-./:：;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'  # 去除文字外所有字符
    ad = ['本书来自www.cr173.com免费txt小说下载站\n更多更新免费电子书请关注www.cr173.com', '----〖新语丝电子文库(www.xys.org)〗', '新语丝电子文库',
          '\u3000', '\n', '。', '？', '！', '，', '；', '：', '、', '《', '》', '“', '”', '‘', '’', '［', '］', '....', '......',
          '『', '』', '（', '）', '…', '「', '」', '\ue41b', '＜', '＞', '+', '\x1a', '\ue42b', '她', '他', '你', '我', '它', '这']   # 去除广告和无意义字符
    for line in open(path, "r", encoding='utf-8'):
        line.strip('\n')
        line = re.sub(Character, "", line)
        line = line.replace("\n", '')
        line = line.replace(" ", '')
        for i in ad:
            line = line.replace(i, '')
        con = jieba.cut(line, cut_all=False)  # 结巴分词
        corpus.append(" ".join(con))
    with open(output, "w", encoding='utf-8') as f:
        f.writelines(corpus)


if __name__ == '__main__':   ##
    txt_path = "datasets/天龙八部.txt"
    #getCorpus(txt_path)
    test_name = ['乔峰']
    sentences = LineSentence('corpus.txt')
    #训练模型
    #model = Word2Vec(sentences, sg=0, vector_size=200,  window=5,  min_count=5,  sample=0.001, hs=1, epochs=100, workers=4)
    model = Word2Vec(sentences, sg=0, vector_size=200, window=5, min_count=10, hs=1,  workers=4)
    #测试结果
    sim = model.wv.most_similar('江湖', topn=6)  #获取相似词
    print(sim)
    # sim = model.wv.most_similar('段誉', topn=6)  #获取相似词
    # print(sim)
    # sim = model.wv.similarity('段正淳', '乔峰') #判断相关性a
    # print(sim)




