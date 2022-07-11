# English_books_classification_Program
英文文献的《中图法》自动分类、相似文献智能推荐小程序。帮助中国图书馆更方便地整理、管理英文图书文献，减轻图书馆员采访编目的负担。

本程序是下列科研论文的配套研究成果：

> 蒋彦廷,吴钰洁.英文文献的《中图法》分类号自动标注研究——基于文本增强与类目映射策略[J].数字图书馆论坛,2022(05):39-46.

> Jiang Yanting, Wu Yujie. Research on Automatic Chinese Library Classification Labeling for English Literature based on Text Data Augmentation and Classification Mapping Strategies[J]. Digital Library Forum, 数字图书馆论坛,2022(05):39-46.

![英文文献自动分类小程序1](https://github.com/JiangYanting/English_books_classification_Program/blob/main/00.png)

![英文文献自动分类小程序2](https://github.com/JiangYanting/English_books_classification_Program/blob/main/02.png)

![英文文献自动分类小程序3](https://github.com/JiangYanting/English_books_classification_Program/blob/main/03.png)


# 1. 基于Fasttext的英文文献归类与相似文献推荐小程序（已打包为exe小程序，可在Windows环境下直接下载使用）

## 小程序功能
  
   【功能1：英文文献归类】标注了中国图书馆分类号的英文图书十分稀缺。我们通过中文图书英译、英文图书回译（back translation）、近义词替换添加、噪声注入等文本增强方法，基于9万册英文图书训练了20类中图分类号的图书分类模型。在测试集上，20类英文图书分类的总体正确率在86%以上。
   
   【功能2：相似文献推荐】基于Fasttext文本向量，输入英文文献的名称、关键词，从59000多册英文文献中，推荐相似度高的20册文献。使用球树（ball tree）优化检索效率。
   
## 下载链接

  链接：https://pan.baidu.com/s/1mVG9xd9qbOGfgsB7CF6JIw 
  
  提取码：1234

  
  在Windows环境下，下载后解压，点击app.exe即可使用。




# 2. 基于BERT的英文图书文献分类小程序(尚未打包为.exe)

## 环境依赖
farm  0.8.0

torch 1.8.1

transformers  4.6.1

Pillow  9.1.0

tkinter(python通常自带的库)

## BERT图书分类小程序的效果

  标注了中国图书馆分类号的英文图书十分稀缺。我们通过中文图书英译、英文图书回译（back translation）等文本增强方法，基于9万册英文图书训练了20类中图分类号的图书分类模型。
  在测试集上，总体的正确率（accuracy）达到90.69%。除E军事类、N自然科学综合类分类效果稍差，其他类别的分类F1分数均在80%甚至90%以上。具体如下表所示。
  
  |指标\类别|查准率precision|查全率recall|F1值|   
|-|-:|-:|-:| 
B哲学心理|0.9246|0.9191|0.9219|
C社会科学综合|0.7837|0.8418|0.8117|
D政治法律|0.9300|0.9238|0.9269|
E军事|0.8571|0.7317|0.7895|
F经济|0.9138|0.9149|0.9144|
G文化科学教育|0.9118|0.8812|0.8962|
H语言文字|0.9333|0.9744|0.9534|
I文学|0.9211|0.8537|0.8861|
J艺术|0.9071|0.9300|0.9184|
K历史地理|0.8464|0.8435|0.8450|
N自然科学综合|0.6842|0.6667|0.6753|
O数理科学与化学|0.9163|0.9327|0.9244|
P天文地球科学|0.8984|0.9350|0.9163|
Q生物科学|0.8876|0.8815|0.8846|
R医学卫生|0.9431|0.9469|0.9450|
S农业科学|0.8788|0.9477|0.9119|
T工业技术|0.9307|0.8969|0.9135|
U交通运输|0.8072|0.9054|0.8535|
V航空航天|0.8727|0.9057|0.8889|
X环境、安全科学|0.8544|0.8800|0.8670|






## 使用方法
  1. 下载基于BERT的英文图书分类模型文件。链接：https://pan.baidu.com/s/11VY1mGjOsDvZT808f_1T7w   提取码：wq6l

  2. 安装好环境依赖后，将app.py与模型文件夹book_bert_english放置在同一目录下。运行app.py程序（最好使用命令行方式运行，速度更快一些），即出现英文图书分类小程序用户界面。

  3. 将待分类的英文图书信息（标题 关键词 摘要等）放置在一个txt文档中，点击小程序界面的“上传英文图书txt文件 每册书一行”按钮，选择上传该txt文档。稍等片刻，即可在窗口中出现自动分类结果。

  4. 点击“保存自动分类结果文档”按钮，将分类结果输出保存为txt文档。每行的格式为“图书文本  分类结果  分类概率”，字段之间用制表符分隔。可以直接复制粘贴到Excel文件中。
