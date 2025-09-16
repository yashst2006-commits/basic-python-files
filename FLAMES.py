def flames(name1, name2):
    # Remove spaces and convert to lowercase
    name1 = name1.replace(" ", "").lower()
    name2 = name2.replace(" ", "").lower()

    # Cancel out common letters
    for ch in name1[:]:
        if ch in name2:
            name1 = name1.replace(ch, "", 1)
            name2 = name2.replace(ch, "", 1)

    # Remaining count
    count = len(name1) + len(name2)

    flames_list = ["F", "L", "A", "M", "E", "S"]

    while len(flames_list) > 1:
        split_index = (count % len(flames_list)) - 1
        if split_index >= 0:
            flames_list = flames_list[split_index+1:] + flames_list[:split_index]
        else:
            flames_list = flames_list[:len(flames_list)-1]

    result_map = {
        "F": "Friends😎",
        "L": "Love😘",
        "A": "Affection🥰",
        "M": "Marriage😍",
        "E": "Enemies😠",
        "S": "Siblings🐒"
    }

    return result_map[flames_list[0]]


# Example run
if __name__ == "__main__":
    print('Welcome to FLAMES...!')
    n1 = input("Enter first name: ")
    n2 = input("Enter second name: ")
    print("Relationship is:", flames(n1, n2))
