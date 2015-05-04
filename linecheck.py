import re

class Checker(object):
    def __init__(self, comparison_dict):
        self.comparison_dict = comparison_dict

    def get_lines(self, lines):
        self.new_lines = []
        self.non_property_text = []
        self.prev_lines = []
        self.current_prop = ""
        for line in lines:
            if self.line_has_property(line):
                self.handle_property_line(line)
            else:
                self.handle_non_property_line(line)
        return self.new_lines

    def line_has_property(self, line):
        return line.find("=") > -1 and not re.match("\s*#", line)

    def handle_property_line(self, line):
        continue_pattern = re.compile(r"\\\r?\n$")
        if self.prev_lines:
            self.new_lines += self.get_new_lines(self.current_prop)
            self.prev_lines = []
        if continue_pattern.search(line):
            self.prev_lines.append(line)
        self.current_prop, prop_value = line.split("=", 1)
        self.new_lines += self.get_new_lines(self.current_prop, line)

    def handle_non_property_line(self, line):
        if self.prev_lines:
            self.prev_lines.append(line)
        else:
            self.non_property_text.append(line)

    def get_new_lines(self, prop_name, line = ""):
        new_lines = []
        if prop_name not in self.comparison_dict:
            new_lines += self.non_property_text
            new_lines += self.prev_lines
            if line:
                new_lines.append(line)
            self.non_property_text = []
        return new_lines



