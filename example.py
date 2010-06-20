import CFTester

def gen_input():
    for i in xrange(-2,2):
        for j in xrange(-2,2):
            for k in xrange(-2,2):
                yield "%d %d %d" % (i,j,k)

Cftester.run_test(gen_input)
