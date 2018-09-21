import re

def parse(man_page_str):
    parse_usages(man_page_str)

def parse_usages(man_page_str):
    synopsis_re = re.compile('SYNOPSIS([\s\S]*)DESCRIPTION\n')
    print synopsis_re.search(man_page_str).group(1)