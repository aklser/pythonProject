import queue
import sys
import threading
import time

msg = []


class MsgLoop(object):
    def __init__(self):
        super(MsgLoop, self).__init__()

    def do_clicked(self):
        time.sleep(10)
        print("do clicked")

    def do_keydown(self):
        print("do keydown")

    def getmsg(self):
        try:
            newmsg = msg[0]
            del msg[0]
            return newmsg
        except:
            return

    def check_msg(self):
        while True:
            msg_i = input("请输入：")
            msg.append(msg_i)
            get_msg = self.getmsg()
            if get_msg == "clicked":
                t = threading.Thread(target=self.do_clicked)
                t.start()
            elif get_msg == "keydown":
                self.do_keydown()
            else:
                print(get_msg)


class Application(object):
    def __init__(self, argv):
        super(Application, self).__init__()
        self.msgloop = MsgLoop()

    def exec(self):
        self.msgloop.check_msg()


app = Application(sys.argv)
print("!!!!!!!!!!!")
app.exec()
