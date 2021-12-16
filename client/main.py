import pose_module as pm
import tkinter as tk
from tkinter import ttk

'''
    # GUI 설명
    콤보박스에 있는 카메라와 동영상 두개의 방법 중 하나를 선택하여 VR 트래킹 영상인식이 가능하다.
    카메라를 선택할 경우 내장카메라와 자동연결되며,
    동영상을 선택할 경우 두번째 GUI 화면으로 넘어간다. 두번째 GUI 화면에서 인식할 영상의 동영상 경로를 입력하면 동영상 새 창이 표출된다.   
'''

def main():
    # 초기 화면
    win = tk.Tk()
    win.title("Full Traking 설정관리창")
    win.resizable(True, True)
    win.geometry('570x130')
    info = ttk.Label(win, text="\"카메라로 움직임을 인식하는 저비용 VR 풀트래킹\" ")
    info.grid(column=0, row=0)
    info = ttk.Label(win, text="고비용의 풀트래킹 기기를 카메라로 대체하고 \n "
                               "인공지능 기술을 이용하여 사용자의 움직임을 \n"
                               "인식하는 S/W로, 카메라로 즉시 움직임을\n"
                               "파악하기 때문에 VR기기 없이도 풀트래킹 구현 가능")
    info.grid(column=0, row=2)
    blank = ttk.Label(win, text="                   ")
    blank.grid(column=1, row=0)
    label = ttk.Label(win, text="인식할 영상선택")
    label.grid(column=2, row=0)

    # 콤보박스
    values = tk.StringVar()
    combobox = ttk.Combobox(win, width=20, textvariable=values)
    combobox['values'] = ('카메라', '동영상')
    combobox.grid(column=2, row=1)

    # 초기화면 '확인' 버튼 함수
    def btn_click():

        # 두번째 화면 (카메라 선택)
        if (values.get()=='카메라'):
            win.destroy()
            win2 = tk.Tk()
            win2.title("Full Traking 설정관리창")
            win2.resizable(True, True)
            win2.geometry('570x130')
            info = ttk.Label(win2, text="\"카메라로 움직임을 인식하는 저비용 VR 풀트래킹\" ")
            info.grid(column=0, row=0)
            info = ttk.Label(win2, text="고비용의 풀트래킹 기기를 카메라로 대체하고 \n "
                                       "인공지능 기술을 이용하여 사용자의 움직임을 \n"
                                       "인식하는 S/W로, 카메라로 즉시 움직임을\n"
                                       "파악하기 때문에 VR기기 없이도 풀트래킹 구현 가능")
            info.grid(column=0, row=2)
            blank = ttk.Label(win2, text="                   ")
            blank.grid(column=1, row=0)
            label = ttk.Label(win2, text="카메라 종류 선택")
            label.grid(column=2, row=0)

            # 콤보박스
            values_camera = tk.StringVar()
            combobox = ttk.Combobox(win2, width=20, textvariable=values_camera)
            combobox['values'] = ('내장 카메라', 'IP 카메라')
            combobox.grid(column=2, row=1)

            # 카메라 선택한 두번째 화면 '확인' 버튼
            def camera_btn_click():
                print(values_camera.get(), "버튼이 클릭되었습니다. 종료시에는 ESC키를 눌러주세요.")
                # 카메라 선택한 두번째 화면 '내장카메라' 선택시
                if (values_camera.get() == '내장 카메라'):
                    win2.destroy()
                    way = 0
                    pm.camera_input(way)

                # 카메라 선택한 두번째 화면 'IP카메라' 선택시
                else:
                    win2.destroy()
                    # IP 카메라 선택한 세번째 화면 생성
                    win3 = tk.Tk()
                    win3.title("VR 풀트래킹 설정관리창")
                    win3.resizable(True, True)
                    win3.geometry('260x160')
                    label = ttk.Label(win3, text="IP 카메라 경로")
                    label.grid(column=0, row=0)
                    path2 = tk.StringVar()  # path: 경로 저장변수
                    entry = ttk.Entry(win3, width=35, textvariable=path2)
                    entry.grid(column=0, row=1)
                    blank2 = ttk.Label(win3, text="                   ")
                    blank2.grid(column=0, row=2)

                    # IP 카메라 선택한 세번째 화면의 '확인' 버튼 함수
                    def btn3_click():
                        print(path2.get(), "입니다.")
                        win3.destroy()
                        way = path2.get()  # 'videos/example.mp4'
                        pm.camera_input(way)

                    # IP 카메라 선택한 세번째 화면의 '확인' 버튼
                    btn3 = ttk.Button(win3, text="확인", command=btn3_click)
                    btn3.grid(column=0, row=3)
                    blank3 = ttk.Label(win3, text="                   ")
                    blank3.grid(column=0, row=4)

                    # 예시 라벨(IP 카메라 경로)
                    info_ex = ttk.Label(win3, text="예시: http://192.168.0.10:8080/video")
                    info_ex.grid(column=0, row=5)


            # 카메라 선택한 두번째 화면의 '확인' 버튼
            camera_btn = ttk.Button(win2, text="확인", command=camera_btn_click)
            camera_btn.grid(column=2, row=2)
            win2.mainloop()

        # 두번째 화면 (동영상 선택)
        else:
            win.destroy()
            win2 = tk.Tk()
            win2.title("VR 풀트래킹 설정관리창")
            win2.resizable(True, True)
            win2.geometry('260x160')
            label = ttk.Label(win2, text="동영상 경로")
            label.grid(column=0, row=0)
            path = tk.StringVar()   # path: 경로 저장변수
            entry = ttk.Entry(win2, width=35, textvariable=path)
            entry.grid(column=0, row=1)
            blank2 = ttk.Label(win2, text="                   ")
            blank2.grid(column=0, row=2)

            # 동영상 선택한 두번째 화면의 '확인' 버튼 함수
            def btn2_click():
                print(path.get(), "입니다.")
                win2.destroy()
                way = path.get()  # '../videos/example.mp4'
                pm.camera_input(way)
            btn2 = ttk.Button(win2, text="확인",command=btn2_click)
            btn2.grid(column=0, row=3)
            blank3 = ttk.Label(win2, text="                   ")
            blank3.grid(column=0, row=4)
            # 예시 라벨(동영상경로)
            info_ex = ttk.Label(win2, text="예시: ../videos/example.mp4")
            info_ex.grid(column=0, row=5)

    # 초기화면 '확인' 버튼
    btn = ttk.Button(win, text="확인", command=btn_click)
    btn.grid(column=2, row=2)
    win.mainloop()


if __name__ == "__main__":
    main()
