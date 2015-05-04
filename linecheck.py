import re

class Checker(object):
    def __init__(self, comparison_dict):
        self.comparison_dict = comparison_dict

    def get_lines(self, lines):
        new_lines = []
        self.non_property_text = []
        self.prev_lines = []
        continue_pattern = re.compile("\\\r?\n$")
        for line in lines:
            if line.find("=") > -1:
                if self.prev_lines:
                    new_lines += self.get_new_lines(prop_name)
                if continue_pattern.search(line):
                    self.prev_lines.append(line)
                prop_name, prop_value = line.split("=")
            elif self.prev_lines:
                self.prev_lines.append(line)
                continue
            else:
                self.non_property_text.append(line)
                continue
            new_lines += self.get_new_lines(prop_name, line)
        return new_lines

    def get_new_lines(self, prop_name, line = ""):
        new_lines = []
        if prop_name not in self.comparison_dict:
            new_lines += self.non_property_text
            new_lines += self.prev_lines
            if line:
                new_lines.append(line)
            self.non_property_text = []
        return new_lines



