import cv2 as cv
import numpy as np

# 초기 설정
canvas = np.ones((600, 900, 3), dtype=np.uint8) * 255  # 흰색 캔버스 생성

drawing = False  # 그림 그리기 여부 확인용 변수
mode = None  # 현재 그리기 모드를 나타내는 변수. 직선, 직사각형, 원 그리기 등을 결정
color, filled_color = (0, 0, 0), (0, 255, 0)  # 색상 설정 (검정색), 채워진 색상 설정 (초록색)
start_point = None  # 그리기 시작점 저장


# 마우스 이벤트 콜백 함수
def draw(event, x, y, flags, param):
    global drawing, mode, color, filled_color, start_point

    if event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON:
        cv.circle(canvas, (x, y), 5, (255, 0, 0), -1)  # 왼쪽 버튼 클릭하고 이동하면 파란색
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_RBUTTON:
        cv.circle(canvas, (x, y), 5, (0, 0, 255), -1)  # 오른쪽 버튼 클릭하고 이동하면 빨간색

    if event == cv.EVENT_LBUTTONDOWN:
        if flags & cv.EVENT_FLAG_SHIFTKEY:  # Shift 키가 눌렸을 때
            mode = 'line'
        elif flags & cv.EVENT_FLAG_ALTKEY:  # Alt 키가 눌렸을 때
            mode = 'rectangle'
        elif flags & cv.EVENT_FLAG_CTRLKEY:  # Ctrl 키가 눌렸을 때
            mode = 'circle'
        drawing = True
        start_point = (x, y)  # 그리기 시작점 저장

    elif event == cv.EVENT_RBUTTONDOWN:
        if flags & cv.EVENT_FLAG_ALTKEY:  # Alt 키가 눌렸을 때
            mode = 'filled_rectangle'
        elif flags & cv.EVENT_FLAG_CTRLKEY:  # Ctrl 키가 눌렸을 때
            mode = 'filled_circle'
        drawing = True
        start_point = (x, y)  # 그리기 시작점 저장

    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            end_point = (x, y)  # 현재 마우스 위치 저장
            canvas_copy = canvas.copy()  # 캔버스의 복사본 생성
            if mode == 'line':
                cv.line(canvas_copy, start_point, end_point, color, 2)
            elif mode == 'rectangle':
                cv.rectangle(canvas_copy, start_point, end_point, color, 2)
            elif mode == 'circle':
                radius = int(np.sqrt((end_point[0] - start_point[0]) ** 2 + (end_point[1] - start_point[1]) ** 2))
                cv.circle(canvas_copy, start_point, radius, color, 2)
            elif mode == 'filled_rectangle':
                cv.rectangle(canvas_copy, start_point, end_point, filled_color, cv.FILLED)
            elif mode == 'filled_circle':
                radius = int(np.sqrt((end_point[0] - start_point[0]) ** 2 + (end_point[1] - start_point[1]) ** 2))
                cv.circle(canvas_copy, start_point, radius, filled_color, cv.FILLED)

            cv.imshow('Drawing', canvas_copy)

    elif event == cv.EVENT_LBUTTONUP:  # 왼쪽 마우스 버튼을 놓았을 때
        drawing = False
        end_point = (x, y)  # 그리기 종료점 저장
        if mode == 'line':
            cv.line(canvas, start_point, end_point, color, 2)
            mode = None
        elif mode == 'rectangle':
            cv.rectangle(canvas, start_point, end_point, color, 2)
            mode = None
        elif mode == 'circle':
            radius = int(np.sqrt((end_point[0] - start_point[0]) ** 2 + (end_point[1] - start_point[1]) ** 2))
            cv.circle(canvas, start_point, radius, color, 2)
            mode = None
        cv.imshow('Drawing', canvas)

    elif event == cv.EVENT_RBUTTONUP:  # 오른쪽 마우스 버튼을 놓았을 때
        drawing = False
        end_point = (x, y)  # 그리기 종료점 저장
        if mode == 'filled_rectangle':
            cv.rectangle(canvas, start_point, end_point, filled_color, -1)  # 내부가 칠해진 직사각형 그리기
            mode = None
        elif mode == 'filled_circle':
            radius = int(np.sqrt((end_point[0] - start_point[0]) ** 2 + (end_point[1] - start_point[1]) ** 2))
            cv.circle(canvas, start_point, radius, filled_color, -1)  # 내부가 칠해진 원 그리기
            mode = None


# 창 생성 및 마우스 콜백 함수 연결
cv.namedWindow('Drawing')
cv.imshow('Drawing', canvas)
cv.setMouseCallback('Drawing', draw)

while True:
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
