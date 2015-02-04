# perf script event handlers, generated by perf script -g python
# Licensed under the terms of the GNU GPL License version 2

# The common_* event handler fields are the most useful fields common to
# all events.  They don't necessarily correspond to the 'common_*' fields
# in the format files.  Those fields not available as handler params can
# be retrieved using Python functions of the form common_*(context).
# See the perf-trace-python Documentation for the list of available functions.

import os
import sys

sys.path.append(os.environ['PERF_EXEC_PATH'] + \
  '/scripts/python/Perf-Trace-Util/lib/Perf/Trace')

from perf_trace_context import *
from Core import *


def trace_begin():
  pass

def trace_end():
  pass

def trace_unhandled(event_name, context, event_fields_dict):
  print event_name
  pass

def probe_ax__a(event_name, ctx, cpu, secs, nsecs, pid,
    comm, callchain, unknown):
  # print_header(event_name, cpu, secs, nsecs, pid, comm)
  pass

# def print_header(event_name, cpu, secs, nsecs, pid, comm):
#   print "%-20s %5u %05u.%09u %8u %-20s" % \
#     (event_name, cpu, secs, nsecs, pid, comm),