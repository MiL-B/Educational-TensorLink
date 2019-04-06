#tensorlink/functions/__init__.py
#関数は死ぬほどたくさんあるので、tensorlink直下に.py作って書くのは狂気。
#なので新しいフォルダを作った。例のごとく僕は__init__.pyを書く。
#で、__init__.py内に大元のFunctionクラスを作る。
class Function:
    def __init__(self):
        self.graph = None
        #一見そんなに意味がないように見えるが後々多分大量にここに書くことになる。
    def __call__(self):
        pass #何もしない


#math.pyからadd関数をimportして、funcitons.add()のように使えるようにする
from tensorlink.functions.math import add
