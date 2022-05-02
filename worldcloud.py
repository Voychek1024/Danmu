import collections
import re
import numpy as np
import jieba.posseg
import matplotlib.pyplot as plt
import wordcloud

string_data = open("content_1.txt", 'r', encoding="utf-8").read()

pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"|，|。|？|！')
string_data = re.sub(pattern, '', string_data)

seg_list_exact = jieba.cut(string_data, cut_all=False, HMM=True)
object_list = []
user_stop_words = ['[', ']', '😂', '没人', '哈哈哈', 'VIP', '确实', '一句', '17', '好好', '有没有', '哈哈哈哈', '略略', '16', '弹幕', '鸡腿',
                   '手机', '有人', '回复', '女生']

with open('stopwords/baidu_stopwords.txt', 'r', encoding='UTF-8') as meaninglessFile:
    stopwords = set(meaninglessFile.read().split('\n'))
stopwords.add(' ')
for word in seg_list_exact:
    if word not in stopwords:
        if word not in user_stop_words:
            if word.__len__() != 1:
                object_list.append(word)

word_counts = collections.Counter(object_list)
word_counts_top = word_counts.most_common(100)
print(word_counts_top)

cloud = wordcloud.WordCloud(
    width=1920,
    height=1080,
    mode='RGBA',
    background_color=None,
    font_path='SIMYOU.TTF',
    # mask=mask,
    max_words=100,
    # max_font_size=100,
    # min_font_size=50
)


def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl({},100%, {}%)".format(np.random.randint(270, 330), np.random.randint(35, 65))


cloud.generate_from_frequencies(word_counts)
cloud.recolor(color_func=grey_color_func)
cloud.to_file("figure_1.png")
plt.imshow(cloud, interpolation='bilinear')
plt.axis('off')
plt.show()
