# -*- coding: utf-8 -*-
"""
Compare the translatable properties of VIVO/Vitro to the
German property file. Output the original file minus the 
existing keys, with line breaks/comments intact.
"""

import linecheck
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("original_file", help="Original all.properties file from Vitro or VIVO theme folder", metavar="ORIGINAL_FILE")
parser.add_argument("translation_file", help="Properties file with translation from languages/themes/wilma/i18n folder", metavar="TRANSLATED_FILE")
parser.add_argument("output_file", default="missing.properties", nargs='?', metavar="OUTPUT_FILE")
args = parser.parse_args()

original = open(args.original_file, "r")
translation = open(args.translation_file, "r")
output_file = open(args.output_file, "w")

def get_properties_dict(lines):
    """ Get property => value dict from an iterable.
        Comments, blank lines and multiline properties are ignored.
    """
    dict_all = {}
    for line in lines:
        items = line.strip().split('=', 1)
        if len(items) < 2:
            continue
        dict_all[items[0]] = items[1]
    return dict_all

checker = linecheck.Checker(get_properties_dict(translation))
output_file.write("".join(checker.get_lines(original)))

