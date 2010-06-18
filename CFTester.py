import os
import tempfile

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

    def get_file1(self):
        return self.file1

    def set_file1(self,name):
        self.file1 = name
        return 0

    def get_file2(self):
        return self.file2

    def set_file2(self,name):
        self.file2 = name
        return 0

    def get_generator(self):
        return self.generator
    
    def set_generator(self,func):
        self.generator = func
        return 0

    def run_test1(self,input):
        return self.run_test(self.file1,input)

    def run_test2(self,input):
        return self.run_test(self.file2,input)

    def run_test(self,file,input):
        tf = tempfile.NamedTemporaryFile('r+w')
        tf2 = tempfile.NamedTemporaryFile('r+w')
        tf2.write(input + "\n")
        tf2.seek(0)
        os.system('python %s < %s > %s' % (file,tf2.name,tf.name))
        res = tf.read()[:-1]
        tf.close()
        tf2.close()
        return res
        
if __name__=="__main__":
    cft = CFTester()
    cft.set_file1('test1.py')
    cft.set_file2('test2.py')
    def f():
        yield "0 0 0"
        yield "1 2 3"
        yield "-1 -3 -5"
        yield "-2 -3 -5"
    cft.set_generator(f)
    cft.run()

