a = {'A': 90, 'B': 0}

b = {'C': 50}
marks = {}
# Use to copy a dict
# marks = dict(a)
marks.update(a)
# update the marks
marks.update(b)
print(marks)
