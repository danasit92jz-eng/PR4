
# Project: Data Analyzer and Transformer
a = []
b = []
total = 0
avg = 0

def input_data():
    """Take 1D or 2D list input from the user."""
    global a, b

    print("\n1. Enter 1D List")
    print("2. Enter 2D List")

    c = int(input("Enter choice: "))

    if c == 1:
        a = list(map(int, input("Enter numbers: ").split()))
        b = []
        print("Data saved successfully!")

    elif c == 2:
        b = []
        n = int(input("Enter number of rows: "))

        for i in range(n):
            x = list(map(int, input("Enter row: ").split()))
            b.append(x)

        a = []
        print("2D data saved successfully!")

    else:
        print("Invalid choice")


def get_data():
    """Return all numbers as a single list."""
    if len(a) > 0:
        return a

    x = []
    for i in b:
        for j in i:
            x.append(j)

    return x


def show_summary():
    """Display basic statistics using built-in functions."""
    x = get_data()

    if len(x) == 0:
        print("Please enter data first.")
        return

    print("\nTotal elements:", len(x))
    print("Sum:", sum(x))
    print("Minimum:", min(x))
    print("Maximum:", max(x))
    print("Average:", round(sum(x) / len(x), 2))


def average(x):
    """Calculate average of list values."""
    if len(x) == 0:
        return 0

    return sum(x) / len(x)


def find_duplicate(x):
    """Display duplicate values in a list."""
    y = []

    for i in x:
        if x.count(i) > 1 and i not in y:
            y.append(i)

    print("Duplicate values:", y)


def find_unique(x):
    """Display unique values in a list."""
    y = []

    for i in x:
        if x.count(i) == 1:
            y.append(i)

    print("Unique values:", y)


def show_args(*args):
    """Accept and display multiple values using args."""
    print("Values:", args)


def show_kwargs(**kwargs):
    """Display dataset information using keyword arguments."""
    for i, j in kwargs.items():
        print(i, ":", j)


def factorial(n):
    """Calculate factorial using recursion............"""
    if n <= 1:
        return 1

    return n * factorial(n - 1)


def filter_data():
    """Filter values using lambda and filter."""
    x = get_data()

    if len(x) == 0:
        print("Please enter data first.")
        return

    n = int(input("Enter threshold: "))

    y = list(filter(lambda i: i < n, x))
    print("Values below threshold:", y)

    z = list(map(lambda i: i * 2, x))
    print("Values multiplied by 2:", z)


def sort_data():
    """Sort 1D list or rows of a 2D list......."""
    if len(a) > 0:
        print("1. Ascending")
        print("2. Descending")

        c = int(input("Enter choice: "))

        if c == 1:
            a.sort()
        elif c == 2:
            a.sort(reverse=True)
        else:
            print("Invalid choice")
            return

        print("Sorted list:", a)

    elif len(b) > 0:
        print("1. Sort rows by first value (ascending)")
        print("2. Sort rows by first value (descending)")

        c = int(input("Enter choice: "))

        if c == 1:
            x = sorted(b, key=lambda i: i[0])
        elif c == 2:
            x = sorted(b, key=lambda i: i[0], reverse=True)
        else:
            print("Invalid choice")
            return

        print("Sorted 2D list:")
        for i in x:
            print(i)

    else:
        print("Please enter data first.")


def show_data():
    """Display 1D or 2D list."""
    if len(a) > 0:
        print("1D List:", a)

    elif len(b) > 0:
        print("2D List:")
        for i in b:
            print(i)

    else:
        print("No data available.")


def show_statistics():
    """Return minimum, maximum, and average."""
    x = get_data()

    if len(x) == 0:
        return None, None, None

    return min(x), max(x), average(x)


def show_menu():
    """Display project menu."""
    print("\n===== DATA ANALYZER =====")
    print("1. Input Data")
    print("2. Display Data")
    print("3. Data Summary")
    print("4. Calculate Average")
    print("5. Find Duplicates")
    print("6. Find Unique Values")
    print("7. Factorial")
    print("8. Filter Data using Lambda")
    print("9. Sort Data")
    print("10. Dataset Statistics")
    print("11. Display Function Documentation")
    print("12. Display *args and **kwargs")
    print("13. Exit")


while True:
    show_menu()

    c = input("Enter your choice: ")

    if c == "1":
        input_data()

    elif c == "2":
        show_data()

    elif c == "3":
        show_summary()

    elif c == "4":
        x = get_data()

        if len(x) > 0:
            print("Average:", round(average(x), 2))
        else:
            print("Please enter data first.")

    elif c == "5":
        x = get_data()

        if len(x) > 0:
            find_duplicate(x)
        else:
            print("Please enter data first.")

    elif c == "6":
        x = get_data()

        if len(x) > 0:
            find_unique(x)
        else:
            print("Please enter data first.")

    elif c == "7":
        n = int(input("Enter a number (0 to 20): "))

        if 0 <= n <= 20:
            print("Factorial:", factorial(n))
        else:
            print("Enter a number between 0 and 20.")

    elif c == "8":
        filter_data()

    elif c == "9":
        sort_data()

    elif c == "10":
        x, y, z = show_statistics()

        if x is not None:
            print("Minimum:", x)
            print("Maximum:", y)
            print("Average:", round(z, 2))
        else:
            print("Please enter data first.")

    elif c == "11":
        print(show_menu.__doc__)
        print(input_data.__doc__)
        print(show_summary.__doc__)
        print(factorial.__doc__)

    elif c == "12":
        x = get_data()

        if len(x) > 0:
            show_args(*x)
            show_kwargs(
                total=len(x),
                sum=sum(x),
                average=round(average(x), 2)
            )
        else:
            print("Please enter data first.")

    elif c == "13":
        print("Thank you! Goodbye.")
        break

    else:
        print("Invalid choice. Try again.")
