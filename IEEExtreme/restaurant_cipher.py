
while True:
    n = int(input())
    if 1 <= n <= 20:
        break
    else:
        print("Invalid input.")

messages = []
for i in range(n):
    while True:
        message = input()
        if all(c.islower() or c.isspace() or c in '.,!?;:' for c in message) and len(message) <= 50000:
            messages.append(message)
            break
        else:
            print("Invalid message. Messages should consist of lowercase letters, spaces, and punctuation, and be at most 50,000 characters.")


def most_frequent_lowercase_to_uppercase(text):
    lowercase = 'abcdefg'
    uppercase = 'ABCDEFG'
    f = {}

    for c in text:
        if c.islower() and c in lowercase:
            if c in f:
                f[c] += 1
            else:
                f[c] = 1

    if not f:  # No lowercase letters found
        return None

    most_frequent_lower = max(f, key=f.get)
    most_frequent_upper = uppercase[lowercase.index(most_frequent_lower)]

    return most_frequent_upper


for i in range(n):
    result = most_frequent_lowercase_to_uppercase(messages[i])
    print(result)