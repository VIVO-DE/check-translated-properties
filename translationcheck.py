# -*- coding: utf-8 -*-
"""
Merge the translatable properties of VIVO and Vitro and compare to the
German property file. Output all missing dictionary keys.
"""

read_vitro = open("vitro_all.properties", "r")
read_vivo = open("vivo_all.properties", "r")
read_all = open("all_de_DE.properties", "r")
writefile = open("new.properties", "w")

### Vitro Properties ###
dict_vitro = {}
for dvit in read_vitro:
    dvit = dvit.strip().split('=')
    if len(dvit) == 1:
        continue
    dict_vitro[dvit[0]] = dvit[1]
    #print dvit                                                                 # For Testing
#print dict_vitro                                                               # For Testing

### Vivo Properties ###
dict_vivo = {}
for dviv in read_vivo:
    dviv = dviv.strip().split('=')
    if len(dviv) == 1:
        continue
    dict_vivo[dviv[0]] = dviv[1]
    #print dviv                                                                 # For Testing
#print dict_vivo                                                                # For Testing


### All Properties ###
dict_all = {}
for dall in read_all:
    dall = dall.strip().split('=')
    if len(dall) == 1:
        continue
    dict_all[dall[0]] = dall[1]
    #print dall                                                                 # For Testing
#print dict_all                                                                 # For Testing

# Merge vitro and vivo dicts
dict_merged = dict_vitro.copy()
dict_merged.update(dict_vivo)

### Checking the entries, generate a dict with the missing entries ###
missing = {entry: dict_merged[entry] for entry in dict_merged if entry not in dict_all }

#print missing                                                                 # For Testing

## print properties
for entry in missing:
    property_pair = "{}={}".format(entry, missing[entry])
    # print property_pair
    writefile.write(property_pair + "\n")

read_vitro.close()
read_vivo.close()
read_all.close()
writefile.close()
