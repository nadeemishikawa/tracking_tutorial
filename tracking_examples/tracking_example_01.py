"""
OpenCV のみを用いた最小のプログラム
〜ウェブカメラを起動しよう〜
"""

import cv2

cap = cv2.VideoCapture(1)  # ウェブカメラの情報を取得（）内はカメラの選択、外部カメラなど

# 連続で画像を表示する事で動画にしている
while True:

    # 一コマ分の画像を取得
    ret, frame = cap.read()

    # 画像の表示　("画像ウィンドウの名前", 表示する画像)
    cv2.imshow("テスト01", frame)

    # エスケープキーでループを抜ける処理
    key = cv2.waitKey(1)  # キーの入力を()の中msだけ受け取る and ウィンドウがぶつ切りになるのを防ぐ
    if key == 27:  # 27がエスケープキーに対応
        break

# while文から抜けたらウィンドウを閉じる
cap.release()
cv2.destroyAllWindows()
