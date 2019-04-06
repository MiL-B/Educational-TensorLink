#じゃあ始めてく。JKのパンツ見たい。
#とりあえず、Tensorクラスを実装してく。
#Tensorクラスというのは、「計算グラフ（どういう計算を辿ってきたか）を保持した変数」
#chainerで言うところのVariableクラスに相当する。
#で具体的にどういうことをしたいのかコードで表すと
#やっぱフォルダ名mirukumaは謎いので変えといた（）
from tensorlink import Tensor
#from tensorlink.tensor import Tensor #__init__.pyを書かなくてもこれで動く

import tensorlink.functions as F

test_tensor = Tensor(5)#5という値を持ったTensorクラスを作ってtest_tensorに代入


print(test_tensor.data) #test_tensorのデータを表示。（つまり5が表示されるはず）
print(test_tensor.graph)#計算グラフを表示。計算何もやってないので多分None.

#これで計算グラフと値の二つを保持する機構が整った。


test_tensor_2 = Tensor(3)

#というわけで、addって関数を作ってく（Tensorの要素ごとの足し算）

#二つのTensorを足し合わせた結果をtest_tensor_3に入れる。
#F.add()っていう関数は後で作る（ていうか確か開発した時同時に作った？）
test_tensor_3 = F.add(test_tensor,test_tensor_2)

print(test_tensor_3.data)#8が表示される
print(test_tensor_3.graph)

#ということで、誤差逆伝播実装してくぜー

#これを実行したら、test_tensor_3ができるまでに関わったTensor全部の勾配用の変数
#に勾配が入れられるようにしたい
test_tensor_3.backward()
print(test_tensor_2.grad)
print(test_tensor.grad)
