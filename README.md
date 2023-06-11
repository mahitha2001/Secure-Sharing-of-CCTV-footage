# Secure Sharing of CCTV footage

This project aims to develop a technique for detecting, encrypting, and decrypting selected faces in CCTV feeds within a secure environment, efficiently.

## Setup
1. Run python app.py in the terminal.
2. Open the provided URL in any browser.

## Encryption

### How it works?
1. We utilize DNN (Deep Neural Network) to detect faces in the videos. Link: https://github.com/gopinath-balu/computer_vision/tree/master/CAFFE_DNN
2. Additionally, we add a specific colored border to form a rectangle around each of the detected faces.
3. After evaluating various encryption techniques, we employ Logistic Regression with key mixing to encrypt the region inside the rectangles using a common key, "abcdefghij" (temporary key for now).

## Decryption

### Challenges
Selectively detecting the encrypted portion in the videos poses a challenge, as this topic is still under research.

### How it works?
1. We detect the rectangles with the specific colored border.
2. Then, we decrypt the region inside using the encryption key we utilized.
3. Furthermore, we use pixel averaging to replace the pixels of that specific color within the rectangles.
