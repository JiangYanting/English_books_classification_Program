# English_books_classification_Program
英文文献的《中国图书馆分类法》自动标注小程序，帮助中国图书馆更方便地整理、管理英文图书文献，减轻图书馆员采访编目的负担。

![英文文献自动分类小程序](https://github.com/JiangYanting/English_books_classification_Program/blob/main/01.jpg)


# 环境依赖
farm  0.8.0

torch 1.8.1

transformers  4.6.1

Pillow  9.1.0

tkinter(python通常自带的库)

# 小程序的效果

  标注了中国图书馆分类号的英文图书十分稀缺。我们通过中文图书英译、英文图书回译（back translation）等文本增强方法，基于9万册英文图书训练了20类中图分类号的图书分类模型。
  在测试集上，总体的正确率（accuracy）达到90.69%。各类分类效果如下所示：
  
  |指标\类别|查准率precision|查全率recall|F1值|   
|-|-:|-:|-:| 
B哲学心理|0.9246|0.9191|0.9219|
C社会科学综合|0.7837|0.8418|0.8117|
D政治法律|0.9300|141317|12835787|
E军事|5820561|141317|12835787|
F经济|5820561|141317|12835787|
G文化科学教育|5820561|141317|12835787|
H语言文字|5820561|141317|12835787|
I文学|5820561|141317|12835787|
J艺术|5820561|141317|12835787|
K历史地理|5820561|141317|12835787|
N自然科学综合|5820561|141317|12835787|
O数理科学与化学|5820561|141317|12835787|
P天文地球科学|5820561|141317|12835787|
Q生物科学|5820561|141317|12835787|
R医学卫生|5820561|141317|12835787|
S农业科学|5820561|141317|12835787|
T工业技术|5820561|141317|12835787|
U交通运输|5820561|141317|12835787|
V航空航天|5820561|141317|12835787|
X环境、安全科学|5820561|141317|12835787|






# 使用方法
  1. 安装好环境依赖后，将app.py与模型文件夹book_bert_english放置在同一目录下。运行app.py程序，即出现英文图书分类小程序用户界面。

  2. 将待分类的英文图书信息（标题 关键词 摘要等）放置在一个txt文档中，点击小程序界面的“上传英文图书txt文件 每册书一行”按钮，选择上传该txt文档。稍等片刻，即可在窗口中出现自动分类结果。

  3. 点击“保存自动分类结果文档”按钮，将分类结果输出保存为txt文档。每行的格式为“图书文本  分类结果  分类概率”，字段之间用制表符分隔。可以直接复制粘贴到Excel文件中。
