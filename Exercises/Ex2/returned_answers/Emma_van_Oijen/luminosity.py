import re

file = "../../../brilcalc.log"

with open(file, 'r') as f:
	lines = f.readlines()

pattern = re.compile(r"\|\s\d+\s+\|\s\d+\s+\|\s\d+\s\|\s\d+\s+\|\s\d+\.\d+\s+\|\s(\d+\.\d+)\s+\|")
pattern_extra = re.compile(r"\|\s\d+:\d+\s\|\s\d+/\d+/\d+\s\d+:\d+:\d+\s\|\s\d+\s+\|\s\d+\s+\|\s\d+\.\d+\s+\|\s(\d+\.\d+)\s+\|")

luminosity_summed = 0

for i,line in enumerate(lines):
	match = re.search(pattern, line)
	if match:
		print(f"The total recorded luminosity is {float(match.group(1))/1000:.1f} /fb.")
	match_extra = re.search(pattern_extra, line)
	if match_extra:
		luminosity_summed += float(match_extra.group(1))

print(f"The manually summed total recorded luminosity is {luminosity_summed/1000:.1f} /fb.")
