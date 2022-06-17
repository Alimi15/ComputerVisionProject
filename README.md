# ComputerVisionProject

A rock, paper, scissors game that uses a camera to detect the user's choice.

## Milestone 1

Using a TeachableMachine image model, four classes are trained; "Rock", "Paper", "Scissors" and "Nothing". The model is then downloaded and stored in the local repository for this project.

## Milestone 2

A new virtual environment is created and all libraries needed for this project are installed using conda and pip. The dependencies are then compiled into a single text file.

```bash
conda install pip

pip install opencv-python
pip install tensorflow
pip install ipykernel

pip list > requirements.txt
```

## Milestone 3

The logic for deciding who won is coded in a separate python script file. 

```python
import random

def get_computer_choice():
    rps = random.randrange(1,4)
    if rps == 1:
        return "Rock"
    elif rps == 2:
        return "Paper"
    elif rps == 3:
        return "Scissors"

def get_user_choice():
    while True:
        user_rps = input("Rock, Paper or Scissors?").lower()
        if user_rps == "rock" or user_rps == "r":
            return "Rock"
        elif user_rps == "paper" or user_rps == "p":
            return "Paper"
        elif user_rps == "scissors" or user_rps == "s":
            return "Scissors"

def get_winner(computer_choice, user_choice):
    if computer_choice == "Rock":
        if user_choice == "Rock":
            return "Draw"
        elif user_choice == "Paper":
            return "User wins"
        elif user_choice == "Scissors":
            return "Computer wins"
        else:
            return "None"
    elif computer_choice == "Paper":
        if user_choice == "Rock":
            return "Computer wins"
        elif user_choice == "Paper":
            return "Draw"
        elif user_choice == "Scissors":
            return "User wins"
        else:
            return "None"
    elif computer_choice == "Scissors":
        if user_choice == "Rock":
            return "User wins"
        elif user_choice == "Paper":
            return "Computer wins"
        elif user_choice == "Scissors":
            return "Draw"
        else:
            return "None"

def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    win = get_winner(computer_choice, user_choice)
    print(win)

if __name__ == "__main__":
    play()
```

## Milestone 4

A function is created to output a prediction based on the output from the models.

```python
def get_prediction(prediction):
    if prediction[0][0] > 0.5:
        return "Rock"
    elif prediction[0][1] > 0.5:
        return "Paper"
    elif prediction[0][2] > 0.5:
        return "Scissors"
    else:
        return "Nothing"
```

The above code is then all put together and completed in a python notebook file using the virtual environment created above for its kernel.

```python
import cv2
from keras.models import load_model
import numpy as np
import time
import camera_rps
import manual_rps
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
startTime = time.time()
integerTime = 0
userWins = 0
computerWins = 0

while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    #print(prediction)
    timeSinceStart = time.time() - startTime
    #print(timeSinceStart)
    if integerTime != int(timeSinceStart):
        integerTime = int(timeSinceStart)
        if integerTime % 5 == 0:
            user_choice = camera_rps.get_prediction(prediction)
            print(user_choice)
            computer_choice = manual_rps.get_computer_choice()
            print(computer_choice)
            win = manual_rps.get_winner(computer_choice, user_choice)
            print(win)
            if win == "User wins":
                userWins += 1
            elif win == "Computer wins":
                computerWins += 1
    if userWins == 3 or computerWins == 3:
        print(f"{win}: {userWins}-{computerWins}")
        break

    # Press q to close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
```
