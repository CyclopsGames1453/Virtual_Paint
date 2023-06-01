# Virtual_Paint
Virtual Paint is an application developed using Python and OpenCV2. It allows you to create digital paintings on your computer screen by tracking the movements of an object, typically a colored marker, in front of a camera.

# Here's how the application works:
-The program uses the OpenCV library to capture video frames from the camera connected to your computer.

-The program uses the numpy library for mathematical operations.

-Identify the color range of the pen using the Find_Color_Area code.

-Add the colors you detect to the myColors list in Virtual_Paint and add the color you want to draw in that color range to the myColorValues list

![Ekran görüntüsü 2023-06-01 125632](https://github.com/CyclopsGames1453/Virtual_Paint/assets/77069289/108b0530-6165-4524-980e-b4b451d9527b)

-It applies image processing techniques to detect the desired object, usually a colored marker, based on its color or shape.

-Once the object is detected, the program tracks its movements in real-time.

-As you move the object in front of the camera, the application continuously updates the object's position.

-Based on the object's position, the program maps it to the corresponding location on the computer screen.

-As you move the object, the program creates a trail of brushstrokes, resulting in a digital painting on the screen.

![Ekran görüntüsü 2023-06-01 125852](https://github.com/CyclopsGames1453/Virtual_Paint/assets/77069289/e1c6f0f8-0e22-4d6f-9fed-66c83257b1ea)
