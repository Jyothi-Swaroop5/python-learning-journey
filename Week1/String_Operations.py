def string_operations_demo():
    text = "  Hello World 123!  "
    print("Original text:", repr(text))

    # Case Conversion
    print("\n--- Case Conversion ---")
    print("upper():", text.upper())
    print("lower():", text.lower())
    print("capitalize():", text.capitalize())
    print("title():", text.title())
    print("swapcase():", text.swapcase())
    print("casefold():", text.casefold())

    # Searching & Counting
    print("\n--- Searching & Counting ---")
    print("find('World'):", text.find("World"))
    print("rfind('l'):", text.rfind("l"))
    print("count('l'):", text.count("l"))

    # Checking Properties
    print("\n--- Checking Properties ---")
    print("isalnum():", text.isalnum())
    print("isalpha():", text.isalpha())
    print("isdigit():", text.isdigit())
    print("isspace():", text.isspace())
    print("isupper():", text.isupper())
    print("islower():", text.islower())
    print("istitle():", text.istitle())
    print("isascii():", text.isascii())
    print("isidentifier():", "variable1".isidentifier())
    print("isprintable():", text.isprintable())

    # Trimming & Padding
    print("\n--- Trimming & Padding ---")
    print("strip():", text.strip())
    print("lstrip():", text.lstrip())
    print("rstrip():", text.rstrip())
    print("center(30,'-'):", text.center(30, "-"))
    print("ljust(30,'*'):", text.ljust(30, "*"))
    print("rjust(30,'*'):", text.rjust(30, "*"))

    # Splitting & Joining
    print("\n--- Splitting & Joining ---")
    words = text.split()
    print("split():", words)
    print("rsplit():", text.rsplit())
    print("splitlines():", "Line1\nLine2\nLine3".splitlines())
    print("join():", "-".join(words))

    # Replacing & Partitioning
    print("\n--- Replacing & Partitioning ---")
    print("replace('World','Python'):", text.replace("World", "Python"))
    print("partition('World'):", text.partition("World"))
    print("rpartition('l'):", text.rpartition("l"))

    # Encoding & Formatting
    print("\n--- Encoding & Formatting ---")
    print("encode():", text.encode("utf-8"))
    print("format():", "My name is {name}".format(name="Alice"))
    print("expandtabs():", "Hello\tWorld".expandtabs(8))

    # String Constants (from string module)
    import string
    print("\n--- String Constants ---")
    print("ascii_letters:", string.ascii_letters[:26], "...")  # show first few
    print("digits:", string.digits)
    print("punctuation:", string.punctuation)
    print("whitespace:", repr(string.whitespace))


# Run the demo
string_operations_demo()
