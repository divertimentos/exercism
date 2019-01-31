def proteins(strand):
    if len(strand) % 3 == 0:

        for i in range(0, len(strand),3):
            pass
    else:
        print("Invalid RNA sequence")

proteins("123456")