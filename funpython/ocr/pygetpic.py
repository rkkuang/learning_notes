#按c保存图片，按q退出
import cv2
cap = cv2.VideoCapture(1)
# cap.set(3,1600) #设置分辨率
# cap.set(4,1200)
cap.set(15, -6)
cap.set(10, -64)
cap.set(11, 64)

# print(cap.get(15))#-1.0 曝光
# print(cap.get(14))# 0 增益
# print(cap.get(13))# 0 图像的色相
# print(cap.get(12))#64.0 图像的饱和度
# print(cap.get(11))#32.0 图像的对比度
# print(cap.get(10))# 0 图像的亮度



# cap.set(3,1280) #设置分辨率跑一趟hi哦那
# cap.set(4,960)
cap.set(3,2592) #设置分辨率
cap.set(4,1944)
# cap.set(15, 0.01)




'''
设置曝光
https://blog.csdn.net/zmdsjtu/article/details/72864828


https://codeday.me/bug/20171101/90657.html
> 1CV_CAP_PROP_POS_FRAMES接下来要解码/捕获的帧的基于0的索引。
> 2CV_CAP_PROP_POS_AVI_RATIO视频文件的相对位置
> 3CV_CAP_PROP_FRAME_WIDTH视频流中的帧的宽度。
> 4CV_CAP_PROP_FRAME_HEIGHT视频流中帧的高度。
> 5CV_CAP_PROP_FPS帧速率。
> 6CV_CAP_PROP_FOURCC编解码器的4个字符代码。
> 7CV_CAP_PROP_FRAME_COUNT视频文件中的帧数。
> 8CV_CAP_PROP_FORMAT retrieve()返回的Mat对象的格式。
> 9CV_CAP_PROP_MODE指示当前捕获模式的后端特定值。
> 10CV_CAP_PROP_BRIGHTNESS图像的亮度(仅适用于相机)。
> 11CV_CAP_PROP_CONTRAST图像的对比度(仅适用于相机)。
> 12CV_CAP_PROP_SATURATION图像的饱和度(仅适用于相机)。
> 13CV_CAP_PROP_HUE图像的色相(仅适用于相机)。
> 14CV_CAP_PROP_GAIN图像的增益(仅适用于相机)。
> 15CV_CAP_PROP_EXPOSURE曝光(仅适用于相机)。
> 16CV_CAP_PROP_CONVERT_RGB指示图像是否应转换为RGB的布尔标志。
> 17CV_CAP_PROP_WHITE_BALANCE目前不支持
> 18CV_CAP_PROP_RECTIFICATION立体摄像机的校正标志(注意：目前仅支持DC1394 v 2.x后端)
'''




win = cv2.namedWindow('capture', flags=0)
# flags为0表示窗口可以用鼠标来改变大小，此时显示的图像也跟着窗口大小变化，需要注意的是它可能会导致图像的变

# prefix = input('前缀,eg: size1_>>>')
# afterfix = input('后缀,eg: .bmp>>>')

prefix = 'img'
afterfix = '.bmp'

while(1):
    # get a frame
    ret, frame = cap.read()
    # show a frame
    # cv2.imshow("capture", frame)
    cv2.imshow("capture", frame)
    # if cv2.waitKey(1) & 0xFF == ord('n'):
        # prefix = input('前缀,eg: size1_>>>')
        # afterfix = input('后缀,eg: .bmp>>>')
    if cv2.waitKey(1) & 0xFF == ord('c'):
        name = input("Img_name,eg: 1>>>")
        # name = name + '.png'
        name = prefix + name + afterfix
        cv2.imwrite(name, frame)
        # break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # cv2.imwrite("fangjian2.jpeg", frame)
        break
cap.release()
cv2.destroyAllWindows()

