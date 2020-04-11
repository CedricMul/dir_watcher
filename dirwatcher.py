#!/user/bin/env python
# -*- coding: utf-8 -*-
import signal
import logging
import os
import sys
import argparse
import datetime
import time

__author__ = "Cedric Mulvihill"

logger = logging.getLogger(__file__)
def signal_handler(sig_num, frame):
    signames = dict((k, v) for v, k in reversed(
        sorted(signal.__dict__.items())
    )
    if v.startswith('SIG') and not v.startswith('SIG_'))
    logger.warn('Received ' + signames[sig_num])

def watch_dir(args):
    logger.info(
        '\nWatching Directory: {}'
        '\nFile Extension: {}'
        '\nKey Phrase: {}'
        .format(args.path, args.ext, args.magic_key)
    )
    while True:
        try:
            logger.info('LOOPING...')
            """If the directory does not exist, the program will let you know
            and update every interval that the directory does not exist until
            it does. Then it reads every file with the matching extension within
            that directory. If the string is contained in the file, the reader 
            return true, points to the file and exits"""
            try:
                for f in os.listdir(args.path):
                    ex = os.path.splitext(f)[1]
                    if ex == args.ext:
                        with open('{}/{}'.format(args.path, f), 'r') as r:
                            for i in r:
                                call = file_reader(i, args.magic_key)
                                if call:
                                    logger.info("\n\n"
                                        "^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^\n"
                                        "Magic Key Word Discovered in: {}\n"
                                        "v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v\n"
                                        .format(f)
                                    )
                                    uptime = datetime.datetime.now() - app_start_time
                                    logger.info(
                                        '\n'
                                        '------------------------------------\n'
                                        '   Stopped: {0}\n'
                                        '   Uptime:  {1}\n'
                                        '------------------------------------\n'
                                        .format(__file__, str(uptime))
                                    )
                                    sys.exit()
            except OSError:
                logger.info(
                    '\n'
                    '************************************************\n'
                    'File and/or directory does not currently exist\n'
                    '************************************************\n'
                )
            time.sleep(args.interval)
        except KeyboardInterrupt:
            logger.info(
                "\n\n"
                "<><><><>><>><>><><><><<<<><>\n"
                "USER EXIT THE PROGRAM\n"
                "<><><><>><>><>><><><><<<<><>\n"
                "\n\n")
            break
    uptime = datetime.datetime.now() - app_start_time
    logger.info(
        '\n'
        '------------------------------------\n'
        '   Stopped: {0}\n'
        '   Uptime:  {1}\n'
        '------------------------------------\n'
        .format(__file__, str(uptime))
    )

def dir_read_loop(args):
    """If the directory does not exist, the program will let
            you know and update every interval that the directory
            does not exist until it does. Then it reads every file
            with the matching extension within that directory.
            If the string is contained in the file, the reader
            return true, points to the file and exits"""
    try:
        for f in os.listdir(args.path):
            ex = os.path.splitext(f)[1]
            if ex == args.ext:
                with open('{}/{}'.format(args.path, f), 'r') as r:
                    for i in r:
                        call = file_reader(i, args.magic_key)
                        if call:
                            logger.info("\n\n"
                                "^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^"
                                "v^v^v^v^\n"
                                "Magic Key Word Discovered in: {}\n"
                                "v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^"
                                "v^v^v^v^v\n"
                                .format(f)
                            )
                            return False
    except OSError:
        logger.info(
            '\n'
            '************************************************\n'
            'File and/or directory does not currently exist\n'
            '************************************************\n'
        )

def file_reader(line, magic):
    if magic in line:
        return True
    else:
        return False

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-e', '--ext',
        type=str, default='.txt',
        help='Text extension to watch for'
    )
    parser.add_argument(
        '-i', '--interval',
        type=float, default=2.0,
        help='Time interval between status checks'
    )
    parser.add_argument('path', help='Directory path to watch')
    parser.add_argument('magic_key', help='Key phrase to watch for')
    return parser

app_start_time = datetime.datetime.now()
def main():
    logging.basicConfig(
        format='%(asctime)s.%(msecs)03d %(name)-12s %(levelname)-8s'
        '[%(threadName)-12s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    logger.setLevel(logging.DEBUG)
    logger.info(
        '\n'
        '------------------------------------\n'
        '  Running {0}\n'
        '  Started on {1}\n'
        '------------------------------------\n'
        .format(__file__, app_start_time.isoformat())
    )
    parser = create_parser()
    args = parser.parse_args()
    watch_dir(args)
    uptime = datetime.datetime.now() - app_start_time
    logger.info(
        '\n'
        '------------------------------------\n'
        '   Stopped: {0}\n'
        '   Uptime:  {1}\n'
        '------------------------------------\n'
        .format(__file__, str(uptime))
    )

if __name__ == "__main__":
    main()
