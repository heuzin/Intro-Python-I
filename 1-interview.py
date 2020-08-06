words = ["Joe", "2", "Ted", "4.98", "14", "Sam", "void *", "42", "float", "pointers", "5006"]
for el in words:
    print(el)

words2 = ['Bob', 'Slack', ['reddit', '89', 101, ['alacritty', '(brackets)', 5, 375]], 0, ['{slice, owned}'], 22]

s = 0
for i in range(len(words2)):
    for j in range(len(words2[i])):
        str(s) += str(words2[i][j])
print(s)