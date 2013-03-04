import re

with open("PrM.sublime-theme", "r") as f:
	w = open("PrM2.sublime-theme", "w")
	t = f.read().replace("\n", "@")
	s = "// transient property not needed"
	t = re.sub(r"\{[^{]+?transient.+?\},", s, t)
	t = t.replace("@", "\n")
	w.write(t)
	w.close()