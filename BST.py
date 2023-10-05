# Ek list ko define karo jismein search karna hai
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# User se input lo jise wo number search karna chahta hai
target = int(input("Enter a number: "))

# Start aur end indices ko initialize karo
start = 0
end = len(L) - 1

# Binary search ka algorithm
while start <= end:
    # Middle index calculate karo
    middle = (start + end) // 2

    # Check karo ki middle element target hai ya nahi
    if L[middle] == target:
        print("Element found at index", middle)
        break
    # Agar middle element target se chhota hai, toh right half mein search karo
    elif L[middle] < target:
        start = middle + 1
    # Agar middle element target se bada hai, toh left half mein search karo
    else:
        end = middle - 1
else:
    print("Element not found")
