def say_hello():
    print("Hello!")

def add_numbers(a,b):
    return a+b

def run_system():
    total_additions = 0
    while True:
        print("1. Say Hello")
        print("2. Add Two Numbers")
        print("3. Exit")
        print("4. Show total additions performed")

        choice = input("Enter your choice:")
        if choice == "1":
            say_hello()
        elif choice == "2":
            a = input("Enter first number: ")
            b = input("Enter second number: ")

            if not (a.lstrip('-').isdigit() and b.lstrip('-').isdigit()):  #用于检查两个变量 a 和 b 是否都是有效的整数表示 #字符串方法 lstrip()，它返回原字符串去掉左侧指定字符（这里是 '-'）后的副本。如果 a 以负号开头（例如 "-123"），则去掉这个负号，得到 "123"。
                print("Invalid number input.")
                continue

            print("The sum is:", add_numbers(a,b))
            total_additions += 1
        elif choice == "4":
            print("Total additions performed: ", total_additions)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    run_system()