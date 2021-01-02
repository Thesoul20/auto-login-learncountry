import pyautogui
import time
import os
import re
def open_software():
    #open xuexiqiangguo
    # qiangguo = subprocess.Popen('/home/choose/Desktop/fuck-xuexiqiangguo/learncountry')
    with open('/home/choose/PycharmProjects/untitled1/xuexiqiangguo/login.txt', mode='w') as f:
        pass
    os.system('cd /home/choose/Desktop/fuck-xuexiqiangguo && ./learncountry >> /home/choose/PycharmProjects/untitled1/xuexiqiangguo/login.txt &')

    print("open software success")
    time.sleep(3)
    # return qiangguo

def maxisoftware():
    print('begin to maxium the software')

    # note: must sure the software was the only software in desktop

    '''
    maxium the software
    '''
    # get the list of the maxium img button site
    addresses = list(pyautogui.locateOnScreen('/home/choose/PycharmProjects/untitled1/xuexiqiangguo/maxium.png'))
    # get the center of button sites
    max_center = pyautogui.center((addresses[0], addresses[1], addresses[2], addresses[3]))
    # click to maxium the software
    pyautogui.click(max_center)
    pyautogui.click(max_center)
    print('maxium success!')

def exit_account():
    print('begin to exit account')
    '''
    exit the account now
    '''
    # the opreation too quick we must wait the software for a while
    for i in range(0, 6):
        exit_button = pyautogui.locateCenterOnScreen('/home/choose/PycharmProjects/untitled1/xuexiqiangguo/exit.png', grayscale=False)
        # exit_button_sites = list(pyautogui.locateOnScreen('exit.png'))
        # exit_button = pyautogui.center((exit_button_sites[0], exit_button_sites[1], exit_button_sites[2], exit_button_sites[3]))
        if exit_button != None:
            pyautogui.click(exit_button)

            print('exit success!')
            break
        else:
            print("False")
            continue
    # the sites of exit button are 1447,391
    pyautogui.click(1447, 391)

def screen_shot():

    # wait software begining
    time.sleep(3)

    #screenshot
    pyautogui.screenshot('qingguodenglu.jpg', region=(79, 79, 1699, 539))
    print("screenshot success")
    # img = Image.open('qingguodenglu.jpg')
    # img.show()

def close_software():
    '''
    close the software by terminal command pa aux | grep learncountry and kill the soft ware num
    :return:
    '''
    '''
    the command grep can only operate the line of input instead of part of input
    It's simple but powful for us.
    But how to do complex operate like select one part from one line? -- awk is viable
    awk '{print $2}' means print the second column in operated data

    '''
    # the thought of use command to get the num of software is not viable for the grep only show the line of input
    # instead of a part of one line

    # But after search article we find the command of awk can do this work

    # creat the logout.txt to store the output of ps aux | grep learncountry
    logout_file = '/home/choose/PycharmProjects/untitled1/xuexiqiangguo/logout.txt'
    with open(logout_file, mode='w') as f:
        pass

    # output the command information to the logout file
    # the command os.system("ps aux | grep learncountry | grep app-path | awk '{print $2}' >> {}".format(logout_file))
    # can't running raise by KeyError: 'print $2'

    # this error is about  which software_num to kill in the terminal command
    # the software number is not precise, so it's just to try
    os.system("ps aux | grep learncountry | awk '{print $2}' > /home/choose/PycharmProjects/untitled1/"
              "xuexiqiangguo/logout.txt")

    # read the least line of the login.txt
    with open('/home/choose/PycharmProjects/untitled1/xuexiqiangguo/logout.txt', mode='r') as f:
        rows = len(f.readlines())
        # software_num = f.readlines()[-1]
    for i in range(rows):
        with open('/home/choose/PycharmProjects/untitled1/xuexiqiangguo/logout.txt', mode='r') as f:
            software_num = f.readlines()[i][:-2]
            print(software_num)
    # kill the software by software_num
    os.system('kill {}'.format(software_num))


open_software()
maxisoftware()
exit_account()
screen_shot()
with open('/home/choose/PycharmProjects/untitled1/xuexiqiangguo/login.txt', mode='r') as f:
    least_line_in_login = f.readlines()[-1]

today_score = re.findall('今日积分: (\d+)', least_line_in_login)[0]
if today_score == '25':
    close_software()