# -*- coding: utf-8 -*-
"""
Compare the translatable properties of VIVO/Vitro to the
German property file. Output the original file minus the 
existing keys, with line breaks/comments intact.
"""

import linecheck

read_vitro = open("vitro_all.properties", "r")
read_all = open("all_de_DE.properties", "r")
writefile = open("new.properties", "w")

dict_all = {}
for dall in read_all:
    dall = dall.strip().split('=')
    if len(dall) == 1:
        continue
    dict_all[dall[0]] = dall[1]

# for testing
# dict_all = {}

checker = linecheck.Checker(dict_all)
writefile.write("".join(checker.get_lines(read_vitro)))

