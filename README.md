# 腾讯视频弹幕分析
《非凡仪式》纪录片 2018 英国 人文

## 环境配置
Python 3.x
requests, collections, re, jieba, matplotlib, wordcloud

## 代码说明
#### get.py
**目的**：获取腾讯视频播放弹幕
**方法**：分析弹幕来源等参数，使用GET方法获取json格式的弹幕资源，再筛选出content部分，即弹幕文本
**结果**：输出至content_x.txt文件，按行逐条分隔弹幕，作为分析备用

#### worldcloud.py
**目的**：清洗分析弹幕文本、生成词云
**方法**：使用jieba分词将弹幕分拆成单词形式，按标点正则式、固有停用词和用户停用词屏蔽部分无意义符号或单词，最终使用wordcloud库生成词云图片
**结果**：输出至figure_x.png图片