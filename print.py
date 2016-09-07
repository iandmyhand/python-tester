import sys

# print 'This is %s...' % 'test'
sys.stdout.flush()

sys.stdout.write('This is %s...' % 'test')
sys.stdout.flush()

sys.stdout.write('\n\n')
sys.stdout.write('This is %s...' % 'test')
sys.stdout.write('\n\n')
sys.stdout.flush()

print
print "Active SQS queues"
print "-----------------"
print
