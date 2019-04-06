#tensorlink/__init__.py
#これは例えばsample.pyで、import tensorlinkとかを行なった場合実行されるファイル。
#書かなくても別に動くけど、例えばTensorクラスを読みこみたくなった場合
#form tensorlink import Tensor
#じゃなくて、
#from tensorlink.tensor import Tensor 
#って感じで定義してるファイル名をimportするときにつけなくちゃいけなくなって、
#使う側としてはめんどいことになるので__init__.pyを書く。

#これをかくと、うまいこと動く、はず
from tensorlink.tensor import Tensor

