from CFTester import CFTester
import unittest

class CFTesterTest(unittest.TestCase):
    
    def setUp(self):
        self.obj = CFTester()

    def test_run(self):
        self.obj.set_file1('test1.py')
        self.obj.set_file2('test2.py')

        def f():
            yield "0 0 0"
            yield "1 2 3"
            yield "-1 -3 -5"
            yield "-2 -3 -5"

        self.obj.set_generator(f)
        self.assertEqual(0,self.obj.run())

    def test_get_file1(self):
        self.obj.set_file1('test1.py')
        self.assertEqual('test1.py',self.obj.get_file1())

    def test_set_file1(self):
        self.assertEqual(0,self.obj.set_file1('set1.py'))

    def test_get_file2(self):
        self.obj.set_file2('test2.py')
        self.assertEqual('test2.py',self.obj.get_file2())

    def test_set_file2(self):
        self.assertEqual(0,self.obj.set_file2('set2.py'))

    def test_generate_input(self):
        f = 'function'
        self.assertEqual(0,self.obj.set_generator(f))
        self.assertEqual(f,self.obj.get_generator())

    def test_run_test1(self):
        self.assertEqual(0,self.obj.set_file1('test1.py'))
        self.assertEqual('0.0',self.obj.run_test1('0 0 0'))
        self.assertEqual('5.0',self.obj.run_test1('3 4 0'))

    def test_run_test2(self):
        self.assertEqual(0,self.obj.set_file2('test2.py'))
        self.assertEqual('0.0',self.obj.run_test2('0 0 0'))
        self.assertEqual('5.0',self.obj.run_test2('3 4 0'))
        
        

            

if __name__=='__main__':
    unittest.main()

    
