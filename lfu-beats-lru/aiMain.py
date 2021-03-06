from performai import make, TestCase
import sys

def main():
	p1 = 'lfu_perform'
	p2 = 'lru_perform'

	try:
		make(p1,p2)
	except:
		return

	t = TestCase(p1, p2, 'lfu_beats_lru.txt')

	if t.score2() >= t.score1():
		sys.stderr.write('LFU replacement did not outperform LRU on your data.\n')
	else:
		print 'Correct!'
main()