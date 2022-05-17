import re, sys
print(*sorted(list(set(re.findall('[a-zA-Z]+[-]*[a-zA-Z]*[-]*[a-zA-Z]*[-]*[a-zA-Z]*[-]*[a-zA-Z]*[-]*[a-zA-Z]*[-]*[a-zA-Z]*', sys.stdin.read().lower().replace('-\n', ''))))), sep='\n')