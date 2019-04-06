#tensorlink/functions/math.py
#ここに数学関連のFunctions達を置く。
#色々importしないといけなかった
from tensorlink import Tensor
from tensorlink.functions import Function

class _add(Function):
#funciton一個ごとにクラス一個なので、Functionクラス（後で作る）を継承して作る
    def __init__(self):
        #親クラスの__init__を呼ぶ
        super().__init__()
    def __call__(self,tensor_1,tensor_2):
        #これをかくとクラスが関数みたいに扱える
        #a = _add()
        #b = a(1,2)#これはb = a.__call__(1,2)と同じ
        new_tensor = Tensor(tensor_1.data + tensor_2.data)
        #このままでは計算グラフを保持していない

        #使われた変数を保持
        self.graph = [tensor_1,tensor_2]
        new_tensor.graph = self#自分自身を新しいtensorの計算グラフとする。
        return new_tensor
    def backward(self,grad):
        #new_tensorのgradを受け取って、それをそのままtensor_1,tensor_2
        #に流せば良い（これは当然関数によって処理が異なる。）
        #フレームワーク実装で一番頭使うのは多分ここ（とあと高速化周り）
        self.graph[0].grad += grad
        self.graph[1].grad += grad

        #再帰的にbackwardを実装（伝播していく）
        self.graph[0].backward(self.graph[0].grad)
        self.graph[1].backward(self.graph[1].grad)


def add(tensor_1,tensor_2):
    #で、こいつの大変なところは、計算結果だけじゃなくて、どういう計算でそうなったか
    #を記録しなきゃならんので大変。
    #どうやって解決するかというと、使い捨て的なクラスを作って、それを計算グラフに記録する。
    return _add()(tensor_1,tensor_2)
    #何やってんのか初見では分かりづらいけど、_add()でクラス作って、それの__call__
    #を呼んでるだけ。