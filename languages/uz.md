# py.Processing-animations
Animations with Processing Python Mode

## Kirish

Iltimos, quyidagi saytdan Processingni yuklab oling va o'rnating, shunda dasturlash muhiti tayyor bo'ladi. Donat talab qilinmaydi. Iltimos, "No Donation" bandini tekshiring.
https://processing.org/download/

<img src="image-processing/py.processing-consol.png" width="550px">

Dastlabki sozlash. MacOSda menyu satrida &#34;Processing&#34;-ni bosing va Preferences-ni tanlang. Windows-da File>Settings-ga o'ting.
Quyidagilarni o'rnating。
- エMonitor va konsol shriftini Mac-da &#34;Osaka&#34; va Windows-da &#34;Ms Gothic&#34;ga o'zgartiring.
- Murakkab matn kiritishni yoqish-ni belgilang
- Kodning bajarilishini tekshiring : Ctrl-space

Sozlagandan so'ng, bir marta PCni qayta yoqing.

## Dasturni ishga tushirib ko'ramiz.
Quyidagi dasturdan nusxa ko'chiring va kod kiritish ekraniga joylashtiring.

```python=
#Dasturning bajarilishi boshida faqat bir marta bajariladigan blok
def setup():
  size(500,500)
  background(255,255,255)
  fill(0,255,0)

#Dasturni ishga tushirganda siklda bajariladigan blok
def draw():
    x = 250 #円の中心のx座標を表す変数、250を代入
    y = 250 #円の中心のy座標を表す変数、250を代入
    d = 300 #円の直径を表す変数、300を代入
    ellipse(x,y,d,d); #円（楕円）を描くメソッド
```
Ushbu dasturni ishga tushirganingizda quyidagi rasmni ko'rasiz.

<img src="image-processing/run-1.png" width="550px">

## New, Save, Debug

Yangi dastur yaratish va saqlash uchun “Fayl” menyusidan biror bandni tanlang va uni bajaring. Yoki buni shortcut key bilan ham qilishingiz mumkin. Faylni saqlash joyiga kelsak, hujjat papkasida Processing deb nomlangan papka mavjud. Masalan, dasturni `test1` nomi bilan saqlasangiz, Processing papkasida `test1.pde` nomli dastur fayli bo`lgan `test1` jildi bo`ladi.

<img src="image-processing/im-1.png" width="400px">

Bundan tashqari, "Error" tugmasini bosish orqali xato xabari va xatolik yuzaga kelgan qatorni tekshirishingiz mumkin.

<img src="image-processing/error.png" width="550px">

## Line

Chizish chiziq funksiyasidan to'rtta o'zgaruvchi mavjud, birinchi ikkitasi chiziq oxiri koordinatalari, keyingi ikkitasi chiziqning boshqa uchi koordinatalari. Masalan, ushbu dasturni ishga tushirish quyidagicha ko'rinadi: Chet koordinatalari (30, 40) va (200, 80).

```python=
def setup():
  size(240,120)
  line(30,40,200,80)
```
<img src="image-processing/run-2.png" width="400px">

## Amalga oshirish tartibi.(Run)

(Run)ni ishlash birinchi buyruqdan boshlab ketma-ket amalga oshiriladi. Shuning uchun, bir-biriga o'xshash shakllarni chizishda dasturni bajarish tartibi muhim ahamiyatga ega. Misol uchun, bu ikki dastur bilan nima sodir bo'ladi? Avval yozilgan ko'rsatmalar birinchi navbatda bajariladi.

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
<img src="image-processing/run-4.png" width="400px">

## Rang (Color).

Processingda shakllar va fonlar rangli bo'lishi mumkin. O'rnatish mumkin bo'lgan ikki xil rang mavjud, kulrang rang va RGB tomonidan belgilangan ranglar. Birinchidan, kulrang shkala sozlamalari haqida gapiraylik. Kulrang ranglar "0" dan "255" gacha bo'lgan qiymatlar bilan ifodalanadi. Pastroq qiymat ochroq rangni, yuqoriroq qiymat esa yorqinroq rangni bildiradi. Bu raqam fon va shaklni to'ldirish funksiyasining o'zgaruvchisiga yoziladi.
Misol uchun, 240 marta 120 bo'lgan oyna yarating va fon rangini fon funktsiyasi bilan belgilang. Bu erda 0 sof qora rangni ifodalaydi. Keyin, “to'ldirish” funksiyasi bilan shaklning to'ldirish rangini belgilang. Ochiq kul rang sifatida men uni 200 ga qo'ydim. Keyinchalik, men doira chizadigan funktsiyani yozdim, lekin oldingi rang spetsifikatsiyasi aks ettirilgan, shuning uchun ochiq kulrang doira chizilgan. Keyin, shuningdek, to'ldirish funksiyasida 100 ni quyuq kulrang sifatida belgilang. Keyin chizilgan keyingi doira quyuq kulrang rang bilan to'ldiriladi. Quyidagi dasturni yozishga harakat qiling.

```python=
def setup():
  size(240,120)
  background(0)
  fill(200)
  ellipse(70,60,80,80)
  fill(100)
  ellipse(10,60,80,80)
```
## RGB

RGB ranglar, rangni uchta raqam bilan belgilanadi, "Qizil", "Yashil" va "Moviy". Har bir raqam 0 dan 255 gacha bo'lgan qiymatga ega va kulrang rangdagi kabi, qiymat qanchalik past bo'lsa rang quyuqroq bo'ladi. Bu dastur to'rt xil rangdagi doiralarni chizadigan dasturdir.

```python=
def setup():
  size(450,150)
  background(255)
  fill(255,0,0)
  rect(50,50,50,50)
  fill(0,255,0)
  rect(150,50,50,50)
  fill(0,0,255)
  rect(250,50,50,50)
  fill(100,20,80)
  rect(350,50,50,50)
```
<img src="image-processing/run-5.png" width="400px">

## 色の数値の確認

指定したい色が、どのような数値になるのか知りたいとき、カラーセレクターを使うと便利です。Processing のメニューの、「Tools」から、「color selector」を選択すると、以下の図のような画面が出てきます。自分の好きな色をクリックすると、その色に対応する RGBの値がわかります。

<img src="image-processing/selectColor.png" width="400px">

## 透明度

色の設定では、透明度も追加することができます。色を表す数値の後に、透明度を表す数値を追加します。値は 0から 255で、値が小さいほど透明、値が大きいほど不透明であることを表します。グレースケールの場合、色を表す数値と透明度を表す数値の、2つの数値で指定します。また、`RGB`のカラーの場合は、色を表す 3つの数値と透明度を表す数値の、全部で 4つの数値で指定します。このプログラムの例を見てみましょう。3つの円を描くプログラムですが、実行結果は以下のようになります。3つの円それぞれに色と透明度を指定しました。半透明なので、重なっているところの色が混ざっています。

```python=
def setup():
  size(400,200)
  noStroke ()                 #輪郭線を消す
  background (200, 226 , 225) #背景の色を変更する
  fill (255, 0, 0, 160)       #図形の色と透明度を指定する
  ellipse (150, 110, 90,90)   #円を描く
  fill (0, 255, 0, 160)
  ellipse(200, 60, 90, 90)
  fill (0, 0, 255, 160)
  ellipse (210, 130, 90, 90)
  ```
 <img src="image-processing/RGB.png" width="400px">
  
  ## 変数
  Processingは、他のプログラミング言語のように、変数を使うことができます。これにより、繰り返しの処理が簡単に表せるようになります。また、変数に対して足し算などの演算をすることもできます。この以下のプログラムを実行すると、3つの円が描かれます。これらの円は、y 軸に関して同じ高さ、等間隔、また、同じ大きさです。これらの同じ値を変数にすると、円を描く命令で毎回同じ数字を書く必要がなく、また、数値の変更も簡単になります。
```python=
size(400, 200)
#変数
x = 80
y = 100
d = 120
s = 80
ellipse(x, y, s, s)
ellipse(x+d, y, s, s)
ellipse(x+d∗2, y, s, s)
```

## 特別な変数
Processingには、いくつかの特別な変数があります。例えば、ウィンドウの幅と高さを表す、widthと heightです。これらの変数は宣言する必要はなく、ウィンドウのサイズを指定する `size` 関数の変数が自動的に代入されます。これらの値を使って、以下のようにウィンドウの対角線と中心に円を描くプログラムを考えます。まず、size関数でウィンドウを作ります。すると、`width`に 400、`height`に 200 が代入されます。これらの変数を使い、対角線や円の中心を表すことができます。

```python=
size(400,200)
line(0,0,width,height)
line(width,0,0,height)
ellipse(width/2, height/2, 100, 100)
```
 <img src="image-processing/run-7.png" width="400px">
 
## 入力 `setup()` と `draw()`

今まで説明してきたプログラムは、上から順に実行し、最後まで実行すると終わるプログラムでした。マウスのクリックなど、外からの入力によって動きが変わるアニメーションを作りたい場合、そのプログラムはずっと動いている必要があります。そこで、`setup` 関数と`draw` 関数を使います。setup関数は、一度だけ実行される関数で、draw関数は、ストップボタンが押されるまで繰り返し実行される関数です。これらの関数が実行される様子を確認してみましょう。 print関数は、画面の下にあるコンソールに文字列や変数の値を表示する関数です。draw関数の方のフレームカウントという変数は、draw関数が上から下まで実行されることをフレームというのですが、そのフレームの数が格納されている特別な変数です。ちなみに、何も指定しない場合、1秒間に 60フレームで、この数は変更することができます。では、実行ボタンを押して、すぐ止めるボタンを押しましょう。そして、コンソールの横のスクロールバーで上まで戻ると、setup 関数は 一度だけしか表示されていないのに対して、draw 関数は何度も実行されているのが確認できます。
```python=
def setup():
  print("setup")
def draw():
  print(frameCount)
```
<img src="image-processing/run-8.png" width="400px">

## 繰り返し処理

変数と `for`を使って繰り返しの処理ができます。変数 `width`と `height`の変数と、繰り返しの処理を使ったプログラムの例を二つ示します。1つ目のプログラムは、黒い背景を作って、二重の `for`ループで白い円とグレーの線を繰り返し書いています。これを実行すると、以下のようなグラフィックが出来上がります。

```pyhton=
size(400,200)
background(0)

for x in range(20, width-20, 10):
    for y in range(20, height-20, 10):
        fill(255,0,0)
        ellipse(x, y, 4, 4)
        stroke(100)
        line(x, y, width/2, height/2)
```
<img src="image-processing/run-9.png" width="600px">

## 位置

先ほどのプログラムは、xの値がどんどん大きくなるので、途中から円は画面の外へ出て行ってしまいます。画面の中で表示し続けるには、物体の位置をウィンドウに収まるように調整する必要があります。例えば、先ほどのプログラムに、次に示すプログラムのように条件分岐を追加します。x の値がウィンドウの横幅を超えたら、左端に xの値を戻すという命令です。そうすると、出て行った円は再び左から現れるようになります。

## PixelArt

ピクセルアートはゲームとの結びつきが強いとはいえ、ピクセルアートはもはやゲーム文化の内部にとどまるものではありません。懐しさを楽しむ人、新しいグラフィック・スタイルとして楽しむ人、純粋にかわいいという点で楽しむ人、といったように楽しみ方は人それぞれだろうが、いずれにしろピクセルアートを描いたり鑑賞したりすることは、それ自体でひとつのカルチャーとして成り立っています。今回はprocessin上で`Pixelart`(ピクセルアート)画像を描いてみましょう。

<img src="Pixel_art(image)/pokeball.png" width="300px">
このポケモンボールの画像をを書いてみましょう

[Pixle_Art_code](https://github.com/asliddinxanov/py.Processing-animations/blob/main/Pixel_art(image)/art_pixel.pyde)

## 今まで勉強してきた関数を使って様々なアニメーションを書いてみましょう。

## 例題1

### Array

ソースコード：[array](https://github.com/asliddinxanov/py.Processing-animations/blob/main/array/array/anim-1.pyde)

実効結果

<img src="array/array/run_anim-1.png" width="500px">

### array_animation

ソースコード：[array_animation](https://github.com/asliddinxanov/py.Processing-animations/blob/main/array/array_animation/kadai1_2.pyde)

実行結果

<img src="array/array_animation/kadai1_2(gif).gif" width="600px">

## 例題2

### Mouse Vector

ソースコード：[Mouse Vector](https://github.com/asliddinxanov/py.Processing-animations/blob/main/mouse%20vector/mouse%20vector/kadai2_2.pyde)

実行結果

<img src="mouse vector/mouse vector/Untitled.gif" width="600px">

## 例題3

### Array Animation

ソースコード：[array_animation_pixart](https://github.com/asliddinxanov/py.Processing-animations/blob/main/pixArt_animation/pixArt_animation.pyde)

実行結果

<img src="pixArt_animation/Untitled.gif" width="600px">

## 例題4

### Click Mouse Animation (PokeBall)

こちらのアニメーションは　`OOP` (オブジェクト指向プログラミング)を使っています。`Poke_main.pyde`, `PokePix.py` です。

Poke_mainのソースコード：[Poke_main.pyde](https://github.com/asliddinxanov/py.Processing-animations/blob/main/PokeBall(click%20mouse)/Poke_main.pyde)

PokePixのソースコード：[PokePix.py](https://github.com/asliddinxanov/py.Processing-animations/blob/main/PokeBall(click%20mouse)/PokePix.py)

実行結果

<img src="PokeBall(click mouse)/Untitled.gif" width="620px">

## 例題5

### Bounce(PockeBall)
物体をななめ方向へ移動させ、画面の端へ来ると跳ね返るアニメーション。

ソースコード：[Bounce](https://github.com/asliddinxanov/py.Processing-animations/blob/main/Bounce(PokeBall)/sketch_220611b/sketch_220611b.pyde)

実行結果

<img src="Bounce(PokeBall)/Untitled.gif" width="620px">

## 例題6

### Bounce2
物体をななめ方向へ移動させ、画面の端へ来ると跳ね返る瞬間に画面の色が変わるアニメーション。
例題5に似ているようなアニメーションで、以下のコードを追加します。
```python=
r = 0
g = 0
b = 0

xdi = 0
ydi = 0

def draw():
  background(r, g, b)
  if (x < z) or (width - z*16 < x):
  xdi *= -1
  r = random(255)
  g = random(255)
  b = random(255)
  
  if (y < z) or (height - z*16 < y):
  ydi *= -1
  r = random(255)
  g = random(255)
  b = random(255)
```

ソースコード：[Bounce2](https://github.com/asliddinxanov/py.Processing-animations/blob/main/Bounce2/sketch_220611c/sketch_220611c.pyde)

実行結果

<img src="Bounce2/Untitled.gif" width="620px">

## 例題7

### PixArt(method "keyPressed")

ソースコード：[keyPressed](https://github.com/asliddinxanov/py.Processing-animations/blob/main/PressKey/sketch_220612d/sketch_220612d.pyde)

```Python=
if keyPressed:
  if key == "d":
    x += 5
  elif key == "a":
    x -= 5
  elif key == "s":
    y += 5
  elif key == "w":
    y -= 5
```
実行結果

<img src="PressKey/sketch.gif" width="620px">
### Cube Color Animation_01

ソースコード：[color-animation](https://github.com/asliddinxanov/py.Processing-animations/blob/main/cube-color-animation/sketch_220619a/sketch_220619a.pyde)

実行結果

<img src="cube-color-animation/sketch_220619a/cube-ran.png" width="600px">


### 2D Grid Animation

ソースコード：[2D grid animation](https://github.com/asliddinxanov/py.Processing-animations/blob/main/2D%20grid-animation/sketch_220729a/sketch_220729a.pyde)

実行結果

<img src="2D%20grid-animation/2D-anim.png" width="620px">
