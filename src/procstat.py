import os.path
import argparse
import logging

logging.basicConfig(level=logging.DEBUG)


class Procstat():
	PROCSTATPATH = '/proc/%d/stat'
	STATLIST = (
		'pid',
		'comm',
		'state',
		'ppid',
		'pgrp',
		'session',
		'tty_nr',
		'tpgid',
		'flags',
		'minflt',
		'cminflt',
		'mjflt',
		'cmajflt',
		'utime',
		'stime',
		'cutime',
		'cstime',
		'priority',
		'nice',
		'num_threads',
		'itrealvalue',
		'starttime',
		'vsize',
		'rss',
		'rsslim',
		'startcode',
		'endcode',
		'startstack',
		'kstkesp',
		'kstkeip',
		'signal',
		'blocked',
		'sigignore',
		'sigcatch',
		'wchan',
		'nswap',
		'cnswap',
		'exit_signal',
		'processor',
		'rt_priority',
		'policy',
		'delayacct_blkio_ticks',
		'guest_time',
		'cguest_time')

	def __init__(self, pid):
		fstat = self.PROCSTATPATH % args.pid

		if not os.path.exists(fstat):
		    logging.error('PID is not valid')
		    return None

		with open(fstat, 'r') as f:
		    procStat = f.readline().split()

		self.stat = {}
		for i in range(len(self.STATLIST)):
		    self.stat[self.STATLIST[i]] = procStat[i]

		strComm = self.stat['comm']
		self.stat['comm'] = str(strComm[1:len(strComm) - 1])

	def __str__(self):
		rl = ''
		for i in self.STATLIST:
		    rl += '%s(%s)' % (i, self.stat[i])

		return rl

	def getStat(self, name):
		return self.stat[name] if self.stat[name] else ''

	def printStat(self, readable=False):
		l = ''
		for i in self.STATLIST:
			v = self.stat[i]
			
			l += '%-12s : %s\n' % (i, v)

		print(l)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Process stat information parser')
	parser.add_argument('pid', type=int, help='Pid')

	args = parser.parse_args()

	pstat = Procstat(args.pid)
	pstat.printStat()
