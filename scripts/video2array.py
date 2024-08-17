import cv2

video_path = "assets/bad_apple.mp4"
cap = cv2.VideoCapture(video_path)

frame_array = []
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_array.append(frame)

cap.release()

frame_store = []
for i, frame in enumerate(frame_array):
    # 转换为纯黑白
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 二值化
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    # 保存
    frame_store.append(binary)

# 帧采样 每隔 10 帧取一帧
frame_store = frame_store[::2]

# 像素采样 每隔 10 行取一行, 每隔 10 列取一列
frame_store = [frame[::5, ::5] for frame in frame_store]

print("frame count:", len(frame_store))
print("frame shape:", frame_store[0].shape)

# 保存新视频
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('assets/bad_apple_sampled.avi', fourcc, 30.0, frame_store[0].shape[::-1])

# 保存为JSON
import json

with open("assets/bad_apple.json", "w") as f:
    frame_store = [frame.tolist() for frame in frame_store]
    json.dump(frame_store, f)



    


