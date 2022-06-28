# py.Processing-animations
Animations with Processing Python Mode

## 最初に
Processingはサイトからダウンロードしてきてインストールするだけで、プログラミング環境が整います。
以下サイトからダウンロードしてください。寄付の必要はありません。「No Donation」にチェックを入れてください。
https://processing.org/download/

<img src="image-processing/py.processing-consol.png" width="550px">

まずは初期設定です。Macならメニューバーの&#34;Processing&#34;のところをクリックして環境設定を選択してください。Windowsならファイル＞設定と進みます。
以下を設定してください。
- 言語を必要な言語に（日本語）にする
- エディタとコンソールのフォントをMacなら&#34;Osaka&#34;、Windowsなら&#34;Ms Gothic&#34;にする
- 複雑なテキスト入力を有効にするにチェックを入れる
- コード補完 Ctrl-spaceにチェックを入れる

設定したら、一度再起動して下さい。

## プログラムを実行してみよう
以下のプログラムをコード入力画面にコピー＆ペーストしてください。
```python=
#プログラムを実行したとき、始めに一回だけ実行されるブロック
def setup():
  size(500,500)  #ウィンドウのサイズを設定するメソッド。500x500に設定
  background(255,255,255) #背景色を設定する関数。白に設定
  fill(0,255,0) #図形の塗りつぶし色を設定するメソッド。緑に設定

#プログラムを実行したとき、ループして実行されるブロック
def draw():
    x = 250 #円の中心のx座標を表す変数、250を代入
    y = 250 #円の中心のy座標を表す変数、250を代入
    d = 300 #円の直径を表す変数、300を代入
    ellipse(x,y,d,d); #円（楕円）を描くメソッド
```
このプログラムを実行すると以下のような画像が表示されます。

<img src="image-processing/run-1.png" width="550px">

## 新規作成、保存、デバッグ

プログラムの新規作成、保存は、メニューの「ファイル」から項目を選んで実行します。もしくは、ショートカットキーでも行うことができます。  ファイルの保存場所ですが、書類フォルダの中に、Processing というフォルダがあります。例えば、`test1` という名前でプログラムを保存する場合、Processing フォルダの中に、`test1` フォルダができ、その中に `test1.pde` というプログラムファイルが保存されます。

<img src="image-processing/im-1.png" width="400px">

また、デバッグですが、下の「エラー」のタブをクリックすると、エラーメッセージとエラーの発生して いる行を確認することができます。
<img src="image-processing/error.png" width="550px">

## 線 (Line)

線の書き方です。line 関数を使います。変数は 4つあり、はじめの 2つは、線の端の座標、次の 2つは、 線のもう一方の端の座標を書きます。例えば、このプログラムを実行すると以下のようになります。端の座標は、(30, 40) と (200, 80)です。
```python=
def setup():
  size(240,120)
  line(30,40,200,80)
```
<img src="image-processing/run-2.png" width="400px">

## 実行の順序
Processing は、先頭の命令から順に実行されます。したがって、重なり合う図形を描く場合、プログラム の実行順序は重要です。例えば、これらの二つのプログラムはどうなるでしょうか。先に書かれた命令から 実行されます。
```python=
def setup():
  size(120,100)
  ellipse(0,0,90,90)
  rect(20,30,60,50)
```
<img src="image-processing/run-3.png" width="400px">
```python=
 def setup():
  size(120,100)
  rect(20,30,60,50)
  ellipse(0,0,90,90)
```
<img scr="image-pocessing/run-4/png" width="400px">
