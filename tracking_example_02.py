"""
OpenCV のみを用いた最小のプログラム
〜dlibを使って顔を検知しよう〜

01からの追加↓　で検索して見てね！
"""

import cv2
import dlib

cap = cv2.VideoCapture(1)  # ウェブカメラの情報を取得（）内はカメラの選択、外部カメラなど

# 顔検知
faces_detector = dlib.get_frontal_face_detector()

# 顔と学習済みモデルの顔の部位別、68個の点を対応させるモデル
landmark_predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# 連続で画像を表示する事で動画にしている
while True:
    # 一コマ分の画像を取得
    ret, frame = cap.read()

    # メモリ削減のためグレースケールか
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 画面上の全ての顔検知(四隅の点の座標を取得)
    faces = faces_detector(gray)

    # 複数の顔全てに対して
    for face in faces:
        # 『顔の四隅』を描写する処理
        # 四隅の座標取得
        x, y = face.left(), face.top()
        x1, y1 = face.right(), face.bottom()
        # 四角形描写（GUIライブラリにありがちな方法やね）
        cv2.rectangle(frame, (x, y), (x1, y1), (0, 0, 255))

        # 『ランドマーク』を描写する処理
        landmarks = landmark_predictor(gray, face)
        # landmarks_numがshape_predictor_68_face_landmarks.datと対応（添付画像）

        for landmarks_num in range(48, 68):
            x = landmarks.part(landmarks_num).x
            y = landmarks.part(landmarks_num).y
            cv2.circle(frame, (x, y), 3, (0, 255, 0))

    # 画像の表示　("画像ウィンドウの名前", 表示する画像)
    cv2.imshow("テスト01", frame)

    # エスケープキーでループを抜ける処理
    key = cv2.waitKey(1)  # キーの入力を()の中msだけ受け取る and ウィンドウがぶつ切りになるのを防ぐ
    if key == 27:  # 27がエスケープキーに対応
        break

# while文から抜けたらウィンドウを閉じる
cap.release()
cv2.destroyAllWindows()
