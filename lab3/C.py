import re, sys
print(*sorted(list(set(re.findall('[a-zA-Z]+', sys.stdin.read().lower())))), sep='\n')