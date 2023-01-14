#!/usr/bin/env python

import os
import sys
import argparse
import traceback
import json
import ndex2
import cdapsutil


class Formatter(argparse.ArgumentDefaultsHelpFormatter,
                argparse.RawDescriptionHelpFormatter):
    pass


def _parse_arguments(desc, args):
    """
    Parses command line arguments
    :param desc:
    :param args:
    :return:
    """
    parser = argparse.ArgumentParser(description=desc,
                                     formatter_class=Formatter)
    parser.add_argument('input',
                        help='JSON')

    return parser.parse_args(args)


def run_cxtoedgelist(theargs, out_stream=sys.stdout,
                     err_stream=sys.stderr):
    """
    Converts CX file set via theargs.input to EDGE LIST of format
    The optional weight is set if theargs.weight is not ``None``
    and matches a node column in CX

    ..code-block::

        SOURCE\tTARGET\t(optional weight)\n


    :param theargs: Holds attributes from argparse
    :type theargs: `:py:class:`argparse.Namespace`
    :param out_stream: stream for standard output
    :type out_stream: file like object
    :param err_stream: stream for standard error output
    :type err_stream: file like object
    :return: 0 upon success otherwise error
    :rtype: int
    """
    if theargs.input is None or not os.path.isfile(theargs.input):
        err_stream.write(str(theargs.input) + ' is not a file')
        return 3

    if os.path.getsize(theargs.input) == 0:
        err_stream.write(str(theargs.input) + ' is an empty file')
        return 4
    try:

        with open(theargs.input, 'r') as f:
            raw_json = json.load(f)
            if 'communitydetectresultv2' not in raw_json:
                return 5
            if 'cx' not in raw_json:
                return 6

            raw_json_to_load = raw_json['cx']
            net = ndex2.create_nice_cx_from_raw_cx(raw_json_to_load)

            cd = cdapsutil.CommunityDetection(runner=cdapsutil.ExternalResultsRunner())
            cd.

        return 0
    finally:
        err_stream.flush()
        out_stream.flush()


def main(args):
    """
    Main entry point for program
    :param args: command line arguments usually :py:const:`sys.argv`
    :return: 0 for success otherwise failure
    :rtype: int
    """
    desc = """
    Takes COMMUNITYDETECTRESULTV2 with CX and outputs a CDAPS compatible
    hierarchy
    
    """
    theargs = _parse_arguments(desc, args[1:])
    try:
        return run_cxtoedgelist(theargs, sys.stdout, sys.stderr)
    except Exception as e:
        sys.stderr.write('\n\nCaught exception: ' + str(e))
        traceback.print_exc()
        return 2


if __name__ == '__main__':  # pragma: no cover
    sys.exit(main(sys.argv))
