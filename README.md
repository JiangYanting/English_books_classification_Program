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

  标注了中国图书馆分类号的英文图书十分稀缺。我们通过中文图书英译、英文图书回译（back translation）等文本增强方法，基于9万册英文图书训练了图书分类模型。
  在测试集上的各类分类效果如下所示：

# 使用方法
  1. 安装好环境依赖后，将app.py与模型文件夹book_bert_english放置在同一目录下。运行app.py程序，即出现英文图书分类小程序用户界面。

  2. 将待分类的英文图书信息（标题 关键词 摘要等）放置在一个txt文档中，点击小程序界面的“上传英文图书txt文件 每册书一行”按钮，选择上传该txt文档。稍等片刻，即可在窗口中出现自动分类结果。

  3. 点击“保存自动分类结果文档”按钮，将分类结果输出保存为txt文档。每行的格式为“图书文本  分类结果  分类概率”，字段之间用制表符分隔。可以直接复制粘贴到Excel文件中。
