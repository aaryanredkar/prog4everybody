text = "X-DSPAM-Confidence: 0.8475";

dig = text.find(' ')

num = float(text[dig+1:])
print num,
