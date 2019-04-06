#tensorlink/tensor.py
import numpy as np

class Tensor:
    #あと、まともにコードを書いてなかったので忘れていたが、
    #クラスの中で定義された関数は全部最初の引数をselfにしないと動かない。
    def __init__(self,data):
        #Tensorが作られるときに呼ばれる関数。
        self.data = data#引数のdataを保持
        self.graph = None#計算グラフを保持、最初はNone
        self.grad = np.zeros_like(self.data)#データと同じ形の0で埋められた配列
        #こうすることで、dataが何次元でも対応できる。
    def backward(self,grad=None):
        if self.graph is None:
            #もし計算グラフがなかったら誤差逆伝播を終了
            #つまり、a = Tensor(5)って感じで定義されたTensorならば、
            return
        if grad is None:
            #もしgradがNone、つまり誤差逆伝播の最初ならgradをdataと同じ形で
            #1埋め。
            grad = np.ones_like(self.data)
        
        #誤差逆伝播スタート
        #self.graphって何かっていうと_addクラスとかなのでそいつらを定義していく
        self.graph.backward(grad)
