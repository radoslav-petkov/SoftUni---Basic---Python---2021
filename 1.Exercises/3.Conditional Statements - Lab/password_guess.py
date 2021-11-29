# 1. Read input string
password = input()

# 2. Compare input with "s3cr3t!P@ssw0rd"
#   a: match - > print(Welcome)
#   b: not -> print(Wrong password!)

if password == "s3cr3t!P@ssw0rd":
    print("Welcome")
else:
    print("Wrong password!")