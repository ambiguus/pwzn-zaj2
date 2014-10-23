# -*- coding: utf-8 -*-


def xrange(start_stop, stop=None, step=None):
	if stop is None:
		stop = start_stop
		start_stop = 0
	if step is None:
		step = 1
	it=start_stop
	while (it < stop and step > 0) or (it > stop and step < 0):
		yield it
		it = it+step
