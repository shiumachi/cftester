import os
import tempfile
import sys

class CFTester():
    def __init__(self):
        pass

    def run(self):
        print "Case#|input|output1|output2"
        print "---------------------------"
        case = 1
        for input in self.generator():
            ans1 = self.run_test1(input)
            ans2 = self.run_test2(input)
            if ans1 != ans2:
                print "%d|%s|%s|%s" % (case,input,ans1,ans2)
            case += 1
        return 0

    def get_command1(self):
        return self.command1

    def set_command1(self,name):
        self.command1 = name
        return 0

    def get_command2(self):
        return self.command2

    def set_command2(self,name):
        self.command2 = name
        return 0

    def get_generator(self):
        return self.generator
    
    def set_generator(self,func):
        self.generator = func
        return 0

    def run_test1(self,input):
        return self.run_test(self.command1,input)

    def run_test2(self,input):
        return self.run_test(self.command2,input)

    def run_test(self,command,input):
        tf = tempfile.NamedTemporaryFile('r+w')
        tf2 = tempfile.NamedTemporaryFile('r+w')
        tf2.write(input + "\n")
        tf2.seek(0)
        os.system('%s < %s > %s' % (command,tf2.name,tf.name))
        res = tf.read()[:-1]
        tf.close()
        tf2.close()
        return res

def run_test(generator):
    argv = sys.argv
    argc = len(argv)
    if argc != 3:
        print "Usage:script.py <command1> <command2>"
        exit()
    cft = CFTester()
    cft.set_command1(argv[1])
    cft.set_command2(argv[2])
    cft.set_generator(generator)
    cft.run()
        
if __name__=="__main__":
        print "Error: you should write input data generator function"
        print "and run 'CFTester.run_test(generator)'"
    

