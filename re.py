#!/usr/bin/python
"""usage: re regex [replacement]"""
import getopt
import re
import sys


if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hc", ["help", "capture"])
        inf = sys.stdin
    except getopt.GetoptError:
        print __doc__
        sys.exit(1)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print __doc__
            sys.exit()
        elif opt in ("-c", "--capture"):
            for line in inf:
                for pattern in args:
                    matches = re.findall(pattern, line)
                    for match in matches:
                        print ''.join(match)
            sys.exit()
    try:
        replacement = args[1] if len(args) >= 2 else ''
        print re.sub(args[0], replacement, inf.read()),
    except IndexError:
        print __doc__
        sys.exit(1)
