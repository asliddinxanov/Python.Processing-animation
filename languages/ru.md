# py.Processing-animations
Animations with Processing Python Mode


## First Contributions
Processing can be downloaded from the site and simply installed to create a programming environment.
Please download it from the site below. No donation is required. Please check the box (No Donation).
https://processing.org/download/

<img src="image-processing/py.processing-consol.png" width="550px">

The initial setup:
For Mac: click on &#34;Processing&#34; in the menu bar and select Preferences.

For Windows: go to File > Preferences.
Set up the following:
- Set the language
- Set editor and console fonts to &#34;Osaka&#34; for Mac or &#34;Ms Gothic&#34; for Windows
- Check Enable complex text input
- Check Code completion Ctrl-space

After setup is complete, Reboot the system.

## Let's run the program.
Copy and paste the following program into the code.
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
When you run this program, will see the image.

<img src="image-processing/run-1.png" width="550px">

## New, Save, Debug

To create a new program or save a program, select an item from the menu "File" and execute it. Alternatively, you can use the shortcut keys.  As for where to save the file, there is a folder called `Processing` in the Documents folder. For example, if you save a program named `test1`, a folder named `test1` will be created in the Processing folder, and the program file `test1.pde` will be saved there.

<img src="image-processing/im-1.png" width="400px">

Also, debugging, you can see the error message and the line where the error is occurring by clicking on the "Errors" tab below.

<img src="image-processing/error.png" width="550px">

## Line

The line function is used to draw a line. The first two variables are the coordinates of the end of the line, and the next two are the coordinates of the other end of the line. For example, the following is the result of executing this program. The end coordinates are (30, 40) and (200, 80).
```python=
def setup():
  size(240,120)
  line(30,40,200,80)
```
<img src="image-processing/run-2.png" width="400px">

## Execution order
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

## Color

Processing is, you can add color to shapes and backgrounds. There are two types of color that can be set: grayscale and RGB. First, we explain the grayscale setting. Gray color is represented by a value from `0` to `255`. Smaller values represent darker colors, and larger values represent lighter color. These values are written to variables in the background and shape fill functions.
For example, let's create a window that is 120 by 240 and specify the background color with the background function. In this case, the value is set to 0, which represents pitch black. Next, specify the fill color of the shape with the `fill` function. We set it to 200, which is a light gray color. Next, we write a function to draw a circle, which reflects the previous color specification, so a light gray circle is drawn. Next, we again specify 100 as the dark gray color in the fill function. Then, the next circle drawn will be filled with dark gray. Try writing the following program.

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

RGB colors are specified by three numbers: `Red`, `Green`, and `Blue`. Each number has a value from 0 to 255, and as with grayscale, the smaller the value, the darker the color. This program draws four different colored circles.
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

## Checking color values

When you want to know the value of the color you want to specify, it is convenient to use the color selector. Click on your favorite color to see the RGB value corresponding to that color.

<img src="image-processing/selectColor.png" width="400px">

## Transparency

Color settings, you can also add transparency. After the number representing the color, add a number representing the transparency. Values range from 0 to 255, with smaller values indicating transparency and larger values opaqueness. In the case of grayscale, the color and transparency are specified by two numbers, one for the color and one for the transparency. In the case of `RGB` color, there are three values for the color and four values for the transparency. Let's look at an example of this program, which draws three circles, and the result looks like this: Each of the three circles has a color and a transparency value specified. Since they are semi-transparent, the colors of the overlapping areas are mixed.

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
  
  ## Variables

  Processing is, like other programming languages, allows the use of variables. This makes it easy to represent repetitive processes. You can also perform operations such as addition on variables. The following program will draw three circles. These circles are the same height, equal distance, and the same size with respect to the y-axis. By making these same values variables, it is not necessary to write the same numbers each time in the instructions for drawing the circles.

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

## 特Another variable

Processing has several special variables. For example, width and height, which represent the width and height of the window. You do not need to declare these variables; they are automatically assigned to the variables of the `size` function, which specifies the size of the window. Using these values, consider the following program that draws a circle around the diagonal and center of the window. First, create a window with the `size` function. Then, 400 is assigned to `width` and 200 to `height`. Using these variables, we can represent the diagonals and the center of the circle.

```python=
size(400,200)
line(0,0,width,height)
line(width,0,0,height)
ellipse(width/2, height/2, 100, 100)
```
 <img src="image-processing/run-7.png" width="400px">
 
## input `setup()` and `draw()`

The programs we have described so far were programs that executed from the top to the bottom and ended when they were executed to the end. If you want to create an animation that changes its motion based on external input, such as a mouse click, the program needs to keep running. So we use the `setup` function and the `draw` function: the setup function is a function that is executed only once, and the draw function is a function that is executed repeatedly until the stop button is pressed. Let's see how these functions are executed. The print function prints a string or the value of a variable to the console at the bottom of the screen, and the variable called frame count in the draw function is a special variable that stores the number of frames in which the draw function is executed from top to bottom, which is called a frame. By the way, if you do not specify anything, it is 60 frames per second, and this number can be changed. Now, press the Run button, and then press the Stop button immediately. And if you go back up to the top with the scroll bar next to the console, you will see that the setup function is only shown once, while the draw function is executed many times.

```python=
def setup():
  print("setup")
def draw():
  print(frameCount)
```
<img src="image-processing/run-8.png" width="400px">

## Iterative process

You can use variables and `for` to iterate. Here are two examples of programs that use the variables `width` and `height` and the repetitive process: the first program creates a black background and repeatedly writes white circles and gray lines in a double `for` loop. When executed, this produces the following graphic.

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

## Position

In the previous program, the circle goes out of the screen in the middle of the program because the value of x keeps getting larger and larger. To keep it on the screen, the position of the object must be adjusted so that it fits in the window. For example, to the previous program, add a conditional branch as shown in the following program: If the value of x exceeds the width of the window, the instruction is to return the value of x to the left edge. The outgoing circle will then reappear from the left.

## PixelArt

Although pixel art has strong ties to gaming, pixel art is no longer confined to the inner workings of gaming culture. People may enjoy it in different ways: some may enjoy it for its nostalgia, others for its new graphic style, and still others for its pure cuteness, but in any case, drawing and viewing pixel art is a culture in and of itself. This time, let's try drawing `Pixelart` images on processin.

<img src="Pixel_art(image)/pokeball.png" width="300px">

Let's write this Pokeball image

[Pixle_Art_code](https://github.com/asliddinxanov/py.Processing-animations/blob/main/Pixel_art(image)/art_pixel.pyde)

## Let's write various animations using the functions we have studied so far.

## example 1

### Array

ソースコード：[array](https://github.com/asliddinxanov/py.Processing-animations/blob/main/array/array/anim-1.pyde)

Result

<img src="array/array/run_anim-1.png" width="500px">

### array_animation

ソースコード：[array_animation](https://github.com/asliddinxanov/py.Processing-animations/blob/main/array/array_animation/kadai1_2.pyde)

Result

<img src="array/array_animation/kadai1_2(gif).gif" width="600px">

## example 2

### Mouse Vector

ソースコード：[Mouse Vector](https://github.com/asliddinxanov/py.Processing-animations/blob/main/mouse%20vector/mouse%20vector/kadai2_2.pyde)

Result

<img src="mouse vector/mouse vector/Untitled.gif" width="600px">

## example 3

### Array Animation

ソースコード：[array_animation_pixart](https://github.com/asliddinxanov/py.Processing-animations/blob/main/pixArt_animation/pixArt_animation.pyde)

Result

<img src="pixArt_animation/Untitled.gif" width="600px">

## example 4

### Click Mouse Animation (PokeBall)

This animation uses `OOP` (Object Oriented Programming). `Poke_main.pyde`, `PokePix.py`.

Poke_main：[Poke_main.pyde](https://github.com/asliddinxanov/py.Processing-animations/blob/main/PokeBall(click%20mouse)/Poke_main.pyde)

PokePix：[PokePix.py](https://github.com/asliddinxanov/py.Processing-animations/blob/main/PokeBall(click%20mouse)/PokePix.py)

Result

<img src="PokeBall(click mouse)/Untitled.gif" width="620px">

## example 5

### Bounce(PockeBall)
Animation of an object moving diagonally and bouncing back when it reaches the edge of the screen.

ソースコード：[Bounce](https://github.com/asliddinxanov/py.Processing-animations/blob/main/Bounce(PokeBall)/sketch_220611b/sketch_220611b.pyde)

Result

<img src="Bounce(PokeBall)/Untitled.gif" width="620px">

## example 6

### Bounce2
An animation in which an object is moved in a diagonal direction, and when it comes to the edge of the screen, the screen changes color at the moment it bounces back.
Add the following code for an animation similar to Example 5.
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

Result

<img src="Bounce2/Untitled.gif" width="620px">

### example 7



### Cube Color Animation_01

Source	code
：[color-animation](https://github.com/asliddinxanov/py.Processing-animations/blob/main/cube-color-animation/sketch_220619a/sketch_220619a.pyde)

Result

<img src="cube-color-animation/sketch_220619a/cube-ran.png" width="600px">


### 2D Grid Animation

ソースコード：[2D grid animation](https://github.com/asliddinxanov/py.Processing-animations/blob/main/2D%20grid-animation/sketch_220729a/sketch_220729a.pyde)

Result

<img src="2D%20grid-animation/2D-anim.png" width="620px">
