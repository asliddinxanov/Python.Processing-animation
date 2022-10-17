# py.Processing-animations
Processing Анимации с помощью Python.


## Первый процесс.
Processing можно загрузить с сайта и просто установить для создания среды программирования, скачайте его с сайта: https://processing.org/download/

<img src="https://github.com/asliddinxanov/Python.Processing-animation/blob/main/image-processing/py.processing-consol.png" width="550px">

Начальная настройка:
Для Mac: нажмите на &#34;Processing&#34; в строке меню и выберите Preferences.

Для Windows: перейдите в меню File > Preferences.
Настройте следующее:
- Установите язык
- Установите шрифты редактора и консоли на &#34;Osaka&#34; для Mac или &#34;Ms Gothic&#34; для Windows.
- Установите флажок включить ввод текста
- Проверьте завершение кода Ctrl-пробел

После завершения настройки перезагрузите систему.

## Давайте запустим программу.

Скопируйте и вставьте код следующую программу.

```python=
#Blocks that are executed only once at the beginning when the program is executed
def setup():
  size(500,500)
  background(255,255,255)
  fill(0,255,0)

#Blocks that loop and run when the program is executed
def draw():
    x = 250 #variable representing the x-coordinate the center of the circle, assigned 250
    y = 250 #variable representing the y-coordinate the center of the circle, assigned 250
    d = 300 #variable representing the diameter of the circle, assigned 300
    ellipse(x,y,d,d); #method to draw a circle (ellipse)
```
Когда вы запустите эту программу, увидите изображение.

<img src="image-processing/run-1.png" width="550px">

## Новый(New), Сохранить(Save), Отладка(Debug).

Чтобы создать новую программу или сохранить программу, выберите пункт в меню "File" и выполните его. В качестве альтернативы можно использовать клавиши быстрого доступа.  Что касается места сохранения файла, то в папке Documents folder `Processing`. Например, если вы сохраните программу с именем `test1`, в папке Processing будет создана папка `test1`, и в ней будет сохранен файл программы `test1.pde`.

<img src="image-processing/im-1.png" width="400px">


Кроме того, при отладке вы можете увидеть сообщение об ошибке и строку, в которой происходит ошибка, перейдя на вкладку "Ошибки(Errors)" ниже.

<img src="image-processing/error.png" width="550px">

## Линия(Line).

Функция line используется для построения линии. Первые две переменные - это координаты конца линии, а следующие две - координаты другого конца линии. Например, результат выполнения этой программы следующий. Координаты конца линии - (30, 40) и (200, 80).

```python=
def setup():
  size(240,120)
  line(30,40,200,80)
```
<img src="image-processing/run-2.png" width="400px">

## Порядок исполнения.
Processing executes instructions in order, starting with the first instruction. Therefore, when drawing overlapping figures, the order in which the programs are executed is important. For example, what happens to these two programs? The first instruction is executed first.

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

## Цвет(Color)

Обработка заключается в том, что можно добавить цвет к фигурам и фонам. Существует два типа цвета, которые можно задать: градации серого и RGB. Сначала мы объясним настройку оттенков серого. Серый цвет представлен значением от `0` до `255`. Меньшие значения представляют более темные цвета, а большие - более светлые. Эти значения записываются в переменные в функциях background и shape fill.
Например, давайте создадим окно размером 120 на 240 и зададим цвет фона с помощью функции background. В данном случае значение установлено в 0, что означает абсолютно черный цвет. Затем зададим цвет заливки фигуры с помощью функции `fill`. Мы установили значение 200, что представляет собой светло-серый цвет. Далее мы пишем функцию для рисования окружности, которая отражает предыдущую цветовую спецификацию, поэтому рисуется светло-серый круг. Далее мы снова задаем 100 в качестве темно-серого цвета в функции заливки. Тогда следующий нарисованный круг будет заполнен темно-серым цветом. Попробуйте написать следующую программу.

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

Цвета RGB задаются тремя числами: `красный`, `зеленый` и `синий`. Каждое число имеет значение от 0 до 255, и, как и в случае с градациями серого, чем меньше значение, тем темнее цвет. Эта программа рисует четыре разных цветных круга.

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

## Проверка значений цвета.

Когда вы хотите узнать значение цвета, который хотите задать, удобно использовать селектор цветов. Нажмите на понравившийся цвет, чтобы увидеть значение RGB, соответствующее этому цвету.

<img src="image-processing/selectColor.png" width="400px">

## Транспарентность

В настройках цвета можно также добавить прозрачность. После числа, обозначающего цвет, добавьте число, обозначающее прозрачность. Значения варьируются от 0 до 255, при этом меньшие значения означают прозрачность, а большие - непрозрачность. В случае с градациями серого цвет и прозрачность задаются двумя числами, одно для цвета, другое для прозрачности. В случае с цветом `RGB` есть три значения для цвета и четыре значения для прозрачности. Рассмотрим пример этой программы, которая рисует три окружности, и результат выглядит следующим образом: Для каждого из трех кругов заданы цвет и значение прозрачности. Поскольку они полупрозрачны, цвета перекрывающихся областей смешиваются.

```python=
def setup():
  size(400,200)
  noStroke ()                 #remove outlines
  background (200, 226 , 225) #change background color
  fill (255, 0, 0, 160)       #specify color and transparency of a shape
  ellipse (150, 110, 90,90)   #drive a circle
  fill (0, 255, 0, 160)
  ellipse(200, 60, 90, 90)
  fill (0, 0, 255, 160)
  ellipse (210, 130, 90, 90)
  ```
 <img src="image-processing/RGB.png" width="400px">
  
  ## Переменные.

  Processing, как и другие языки программирования, позволяет использовать переменные. Это позволяет легко представлять повторяющиеся процессы. Над переменными также можно выполнять такие операции, как сложение. Следующая программа нарисует три окружности. Эти окружности имеют одинаковую высоту, одинаковое расстояние и одинаковый размер относительно оси y. Благодаря тому, что эти одинаковые значения являются переменными, нет необходимости каждый раз писать одни и те же числа в инструкциях по рисованию окружностей.

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

## Другая переменная

Processing имеет несколько специальных переменных. Например, width и height, которые представляют собой ширину и высоту окна. Вам не нужно объявлять эти переменные; они автоматически присваиваются переменным функции `size`, которая задает размер окна. Используя эти значения, рассмотрим следующую программу, которая рисует круг вокруг диагонали и центра окна. Сначала создайте окно с помощью функции `size`. Затем, 400 присваивается `width`, а 200 - `height`. Используя эти переменные, мы можем представить диагонали и центр окружности.

```python=
size(400,200)
line(0,0,width,height)
line(width,0,0,height)
ellipse(width/2, height/2, 100, 100)
```
 <img src="image-processing/run-7.png" width="400px">
 
## ввод `setup()` и `draw()`

Программы, которые мы описывали до сих пор, выполнялись сверху вниз и заканчивались, когда были выполнены до конца. Если вы хотите создать анимацию, которая меняет свое движение в зависимости от внешнего воздействия, например, щелчка мыши, программа должна работать постоянно. Поэтому мы используем функцию `setup` и функцию `draw`: функция setup - это функция, которая выполняется только один раз, а функция draw - это функция, которая выполняется многократно до тех пор, пока не будет нажата кнопка stop. Давайте посмотрим, как выполняются эти функции. Функция print выводит строку или значение переменной на консоль внизу экрана, а переменная frame count в функции draw - это специальная переменная, которая хранит количество кадров, в которых выполняется функция draw сверху вниз, что называется кадром. Кстати, если ничего не указывать, то это 60 кадров в секунду, и это число можно изменить. Теперь нажмите кнопку Run, а затем сразу же нажмите кнопку Stop. И если вы вернетесь наверх с помощью полосы прокрутки рядом с консолью, то увидите, что функция setup отображается только один раз, в то время как функция draw выполняется много раз.

```python=
def setup():
  print("setup")
def draw():
  print(frameCount)
```
<img src="image-processing/run-8.png" width="400px">

## Итеративный процесс.

Для итерации можно использовать переменные и `for`. Вот два примера программ, использующих переменные `width` и `height` и повторяющийся процесс: первая программа создает черный фон и многократно пишет белые круги и серые линии в двойном цикле `for`. При выполнении получается следующий график.

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

## Позиция(Position).

В предыдущей программе круг выходит за пределы экрана в середине программы, потому что значение x становится все больше и больше. Чтобы удержать его на экране, необходимо изменить положение объекта так, чтобы он поместился в окне. Например, к предыдущей программе добавьте условную ветвь, как показано в следующей программе: Если значение x превышает ширину окна, то инструкция возвращает значение x к левому краю. После этого выходящая окружность снова появится слева.

## PixelArt

Хотя пиксель-арт тесно связан с играми, пиксель-арт больше не ограничивается внутренним миром игровой культуры. Людям он нравится по-разному: кому-то он нравится из-за ностальгии, кому-то из-за нового графического стиля, а кому-то из-за чистой миловидности, но в любом случае, рисование и просмотр пиксель-арта - это целая культура. На этот раз давайте попробуем нарисовать изображения в стиле `Pixelart` на processin.

<img src="Pixel_art(image)/pokeball.png" width="300px">

Давайте напишем код изображение Pokebal

[Pixle_Art_code](https://github.com/asliddinxanov/py.Processing-animations/blob/main/Pixel_art(image)/art_pixel.pyde)

## Давайте напишем различные анимации, используя функции, которые мы изучили до сих пор.

## например (1)

### Массив(Array)

Source code：[array](https://github.com/asliddinxanov/py.Processing-animations/blob/main/array/array/anim-1.pyde)

Результат

<img src="array/array/run_anim-1.png" width="500px">

### массив_анимации

Source code：[array_animation](https://github.com/asliddinxanov/py.Processing-animations/blob/main/array/array_animation/kadai1_2.pyde)

Результат

<img src="array/array_animation/kadai1_2(gif).gif" width="600px">

## например (2)

### Вектор мыши

Source code：[Mouse Vector](https://github.com/asliddinxanov/py.Processing-animations/blob/main/mouse%20vector/mouse%20vector/kadai2_2.pyde)

Результат

<img src="mouse vector/mouse vector/Untitled.gif" width="600px">

## например (3)

### Анимация массива

Source code：[array_animation_pixart](https://github.com/asliddinxanov/py.Processing-animations/blob/main/pixArt_animation/pixArt_animation.pyde)

Результат

<img src="pixArt_animation/Untitled.gif" width="600px">

## например (4)

### Анимация нажатия кнопки мыши (PokeBall)

В этой анимации используется`OOP` (Object Oriented Programming). `Poke_main.pyde`, `PokePix.py`.

Poke_main：[Poke_main.pyde](https://github.com/asliddinxanov/py.Processing-animations/blob/main/PokeBall(click%20mouse)/Poke_main.pyde)

PokePix：[PokePix.py](https://github.com/asliddinxanov/py.Processing-animations/blob/main/PokeBall(click%20mouse)/PokePix.py)

Результат

<img src="PokeBall(click mouse)/Untitled.gif" width="620px">

## например (5)

### Bounce(PockeBall)
Анимация объекта, движущегося по диагонали и отскакивающего назад, когда он достигает края экрана.

Source code：[Bounce](https://github.com/asliddinxanov/py.Processing-animations/blob/main/Bounce(PokeBall)/sketch_220611b/sketch_220611b.pyde)

Результат

<img src="Bounce(PokeBall)/Untitled.gif" width="620px">

## например (6)

### Bounce2
Анимация, в которой объект перемещается в диагональном направлении, и когда он подходит к краю экрана, экран меняет цвет в момент его отскока.
Добавьте следующий код для анимации, аналогичной (примеру 5).

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

Source code：[Bounce2](https://github.com/asliddinxanov/py.Processing-animations/blob/main/Bounce2/sketch_220611c/sketch_220611c.pyde)

Результат

<img src="Bounce2/Untitled.gif" width="620px">

### например (7)



### Анимация цвета куба_01

Source code
：[color-animation](https://github.com/asliddinxanov/py.Processing-animations/blob/main/cube-color-animation/sketch_220619a/sketch_220619a.pyde)

Результат

<img src="cube-color-animation/sketch_220619a/cube-ran.png" width="600px">


### 2D Grid Анимация

Source code：[2D grid animation](https://github.com/asliddinxanov/py.Processing-animations/blob/main/2D%20grid-animation/sketch_220729a/sketch_220729a.pyde)

Результат

<img src="2D%20grid-animation/2D-anim.png" width="620px">
