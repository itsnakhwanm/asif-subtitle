import re
punctuations=[".",",",":",";","!"]
quotes=["\"","\'"]

words = "I just want to let you here, you know, I'm here'"
print(re.findall(f"[\\b\\w']+[{"".join(punctuations)}]|[\\b\\w']+",words))
