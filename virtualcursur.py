import cv2
import mediapipe as mp
import pyautogui
capture_hand = mp.solutions.hands.Hands()
drawing_option = mp.solutions.drawing_utils
screen_width , screen_height = pyautogui.size()
x1 = y1 = x2 = y2 =0



camera = cv2.VideoCapture(0)

while True:
    _,image = camera.read()
    image_height, image_width,_=image.shape
    image = cv2.flip(image,1)
    rgb_image = cv2.cvtColor(image,cv2.COLOR_BGRA2RGB)
    output_hands = capture_hand.process(rgb_image)
    all_hands = output_hands.multi_hand_landmarks
    if all_hands:
        for hand in all_hands:
            drawing_option.draw_landmarks(image,hand)
            one_handland_marks = hand.landmark
            for id , lm in enumerate(one_handland_marks):
                x = int(lm.x * image_width)
                y = int(lm.y * image_height)
                
                if id == 8:
                    mouse_x = int(screen_width / image_width * x)
                    mouse_y = int(screen_height/ image_height * y)
                    cv2.circle(image,(x,y),15,(0,255,255))
                    pyautogui.moveTo(mouse_x,mouse_y)
                    x1=x
                    y1=y
                    
                if id == 4:
                    x2=x
                    y2=y
                    cv2.circle(image,(x,y),15,(0,255,255))
        
        dist = y2 -y1
        if (dist < 20):
            pyautogui.click()

    
    cv2.imshow("Hand movement",image)
    
    
    key = cv2.waitKey(100)
    if key == 27: ## if escape key is pressed then it will terminate the program
        break

camera.release()
cv2.destroyAllWindows()    