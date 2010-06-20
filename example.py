import CFTester

def gen_input():
    start = -1
    end = 1
    for i in xrange(start,end):
        for j in xrange(start,end):
            for k in xrange(start,end):
                yield "%d %d %d" % (i,j,k)

CFTester.run_test(gen_input)
