#!/usr/bin/env python
import sys
import traceback

def all_checks():
    try:
        import duckietown_utils
    except ImportError as e:
        sys.stderr.write('\nYou can use what-the-duck only *after* building the repository.\n')
        sys.stderr.write('\n\nError:\n\n\t%s\n\n\n' % traceback.format_exc(e))
        sys.stderr.write('Try again after building the repository.\n\n')
        #sys.stderr.write('Could not import duckietown_utils and what_the_duck packages:\n%s\n' % e)
        sys.exit(255)

    else:
        from what_the_duck.sanity_checks import do_all_checks

        do_all_checks()

if __name__ == '__main__':
    all_checks()
