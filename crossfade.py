"""
画像が徐々に変わるやつ
いわゆるクロスフェード

2024.11.11
Python3.13.0
Gemini 1.5 flash

どちらかというと画像Aからを画像Bに
フェードアウトしてフェードインするって感じ…

"haarcascade_frontalface_default.xml"のインストールを忘れずに
クロスフェードはOBSで実行して録画するのがいいかと…

"""

import cv2
import numpy as np
import os

# 画像を読み込みます (img2 から img1 へ流れる)
img1 = cv2.imread(".jpg")
img2 = cv2.imread(".jpg")

# 画像を同じサイズにリサイズします
img1 = cv2.resize(img1, (512, 512))
img2 = cv2.resize(img2, (512, 512))

# 画像をグレースケールに変換します
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# 顔検出器を初期化します
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# 顔を検出します
faces1 = face_cascade.detectMultiScale(gray1, 1.1, 4)
faces2 = face_cascade.detectMultiScale(gray2, 1.1, 4)

# 顔が検出されたかどうかを確認します
if len(faces1) == 0 or len(faces2) == 0:
    print("顔が見つかりませんでした")
    # 顔検出されなかった場合、イメージファイルのクロスフェードを実行
    crossed_images = []
    for i in range(0, 61):
        alpha = i / 60 # 60 = fps
        beta = 1 - alpha
        crossed_image = cv2.addWeighted(img1, alpha, img2, beta, 0.0)
        crossed_images.append(crossed_image)

        # 画像を保存
        folder_path = "crossed_images"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        image_path = os.path.join(folder_path, f"crossed_image_{i}.png")
        cv2.imwrite(image_path, crossed_image)

        # クロスフェード画像を表示
        cv2.imshow('Crossed Image', crossed_image)
        if cv2.waitKey(100) & 0xFF == 27: # (1000ミリ秒 = 1秒待機)
            break

else:
    # 最初の顔の座標を取得します
    x1, y1, w1, h1 = faces1[0]
    x2, y2, w2, h2 = faces2[0]

    # 顔の画像を切り取ります
    face1 = gray1[y1:y1+h1, x1:x1+w1]
    face2 = gray2[y2:y2+h2, x2:x2+w2]

    # 顔を同じサイズにリサイズします
    face1 = cv2.resize(face1, (512, 512))
    face2 = cv2.resize(face2, (512, 512))

    # 顔のクロスフェードを実行
    crossed_images = []
    for i in range(0, 61):
        # アルファ値とベータ値を計算
        # alpha = i - beta
        alpha = i / 60 # alpha = 1(完全に不透明) 画像の透過度を表す
        # beta = 1 - alpha
        beta = 1 - alpha # beta = 0(完全に暗い) 画像の明度を表す        
        crossed_image = cv2.addWeighted(face1, alpha, face2, beta, 0.0)
        crossed_images.append(crossed_image)

        # 画像を保存
        folder_path = "crossed_images"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        image_path = os.path.join(folder_path, f"crossed_image_{i}.png")
        cv2.imwrite(image_path, crossed_image)

        # クロスフェード画像を表示
        cv2.imshow('Crossed Image', crossed_image)
        if cv2.waitKey(100) & 0xFF == 27: # ミリ秒待機( 1000ミリ秒 = 1秒 )
            break

# すべてのウィンドウを閉じます
cv2.destroyAllWindows()
