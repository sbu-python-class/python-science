"""
  A very simple profiling class.  Define some timers and methods
  to start and stop them.  Nesting of timers is tracked so we can
  pretty print the profiling information.

  # define a timer object, labeled 'my timer'
  a = timer('my timer')

  This will add 'my timer' to the list of keys in the 'my timer'
  dictionary.  Subsequent calls to the timer class constructor
  will have no effect.

  # start timing the 'my timer' block of code
  a.begin()

  ... do stuff here ...

  # end the timing of the 'my timer' block of code
  a.end()

  for best results, the block of code timed should be large
  enough to offset the overhead of the timer class method
  calls.

  Multiple timers can be instantiated and nested.  The stackCount
  global parameter keeps count of the level of nesting, and the
  timerNesting data structure stores the nesting level for each
  defined timer.

  timeReport() is called at the end to print out a summary of the
  timing.

  At present, no enforcement is done to ensure proper nesting.

"""

from __future__ import print_function

import time

timers = {}

# keep basic count of how nested we are in the timers, so we can do some
# pretty printing.
stack_count = 0

timer_nesting = {}
timer_order = []

class Timer(object):

    def __init__ (self, name):
        global timers, stack_count, timer_nesting, timer_order

        self.name = name

        keys = timers.keys()

        if name not in keys:
            timers[name] = 0.0
            self.startTime = 0.0
            timer_order.append(name)
            timer_nesting[name] = stack_count


    def begin(self):
        global stack_count

        self.startTime = time.time()
        stack_count += 1


    def end(self):
        global timers, stack_count

        elapsedTime = time.time() - self.startTime
        timers[self.name] += elapsedTime

        stack_count -= 1


def time_report():
    global timers, timer_order, timer_nesting

    spacing = '   '
    for key in timer_order:
        print(timer_nesting[key]*spacing + key + ': ', timers[key])



if __name__ == "__main__":
    a = Timer('1')
    a.begin()
    time.sleep(10.)
    a.end()

    b = Timer('2')
    b.begin()
    time.sleep(5.)

    c = Timer('3')
    c.begin()

    time.sleep(20.)

    b.end()
    c.end()

    time_report()
