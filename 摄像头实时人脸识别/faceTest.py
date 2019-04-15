# 读入相关库
# cv2即 OpenCV(cv和cv2 有点类似 py2和py3)，用来读取摄像头
# face_recognition 进行人脸识别

import face_recognition as fr
import cv2

# 保存在本地的待比较图片
# image是numpy三维数组
image = fr.load_image_file(r'C:\SecurityMonitor\FaceRecognition\img\face.jpg')
# 对已知图片进行编码，由于face_encodings是元组列表，并且我们已知的图片中只有一个人，所以获取索引0即目标编码
Admin_encoding = fr.face_encodings(image)[0]

# 调用OpenCV获取摄像头，VideoCapture(0)是后置摄像头，VideoCapture(1)是前置摄像头
cap = cv2.VideoCapture(1)

# 让摄像头一直进行拍摄
while True:
    # 由于摄像头中会出现很多人脸，设置index为编码列表中识别成功的元素下标值
    index = -1
    # 进行摄像头的拍摄，read()是按帧拍摄
    # 返回值1：ret是bool值，拍摄成功与否
    # 返回值2：frame是该帧的numpy数组
    ret,frame = cap.read()
    # 对图像进行resize()缩小，提高速度
    smallFrame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    # 定位摄像头该帧中的人脸，face_locations(top，right，bottom，left)是元组列表，可能有多个人脸
    face_locations = fr.face_locations(smallFrame)
    # 在该帧图像中定位人脸位置，并进行人脸编码
    face_encodings = fr.face_encodings(smallFrame,face_locations)

    # 对每一个编码进行与已知编码进行比较，识别成功则记录下标并退出
    for i,face_encoding in enumerate(face_encodings):
        result = fr.compare_faces([Admin_encoding],face_encoding)
        if result:
            index = i
            break
    # 识别成功则进行矩形框标记，需要将该帧图像恢复原图，因为上面的比例因子为0.25，所以这里扩大四倍
    if index != -1:
        face_location = face_locations[index]
        top = face_location[0] * 4
        right = face_location[1] * 4
        bottom = face_location[2] * 4
        left = face_location[3] * 4
        # 矩形框标记
        cv2.rectangle(frame,(left,top),(right,bottom),(0,0,255),2)

    # 显示摄像头图像
    cv2.imshow('Identification',frame)
    # 按 q 退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()