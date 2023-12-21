#!/usr/bin/env python3

import pymsteams
import argparse
import sys


def send_message(url, subject, output, long_message=None):
    teams_message = pymstems.connectorcard(url)
    teams_message.title(subject)

    if long_message:
        teams_message.text(output + "\n\n" + long_message)
    else:
        teams_message.text(output)

    teams_message.send()


def main(args):
    url = args.get("url")
    if url is None:
        print("error no url")
        exit(2)

    subject = args.get("subject")
    output = args.get("output")
    long_message = args.get("long_message")

    send_message(url, subject, output, long)


if __name__ == "__main__":
    args = {}

    parser = argparse.ArguentParser()
    parser.add_argument("subject", action="store", help="subject")
    parser.add_argument("output", action="store", help="output of the check")
    parser.add_argument("url", action="store", help="teams webhook")

    parsedArgs = parser.parse_args()

    args["subject"] = parsedArgs.subject
    args["url"] = parsedArgs.url
    args["output"] = parsedArgs.output

    if not sys.__stdin__.isatty():
        args["long_message"] = sys.__stdin__.read()

    main(args)
