# -------------Task 01 -------------
# Even Number Program


def even_numbers(arr):
    return [num for num in arr
            if num % 2 == 0]

arr = [1,2,3,4,5,6,7,8,9,10,12,14]
result = even_numbers(arr)
print("Even Numbers: ", result)




# ------------- Odd Number Program -------------
def odd_numbers(arr):
    return [num for num in arr
            if num % 2 != 0]

arr = [1,2,3,4,5,6,7,8,9,10,12,14]
result = odd_numbers(arr)

print("Odd Numbers: ", result)


# ------------- Prime Number Program -------------

def prime_numbers(arr):
    return [num for num in arr 
            if num > 1 and all(num % i for i in range(2, num)) ]

arr = [1,2,3,4,5,6,7,8,9,10,12,14]
result = prime_numbers(arr)
print ("Prime Numbers: ", result)


# ------------- Combine all the functions -------------


def numbers(arr):
    return {
        "even": even_numbers(arr),
        "odd": odd_numbers(arr),

        "prime": prime_numbers(arr)
    }

arr = [1,2,3,4,5,6,7,8,9,10,12,14]
result = numbers(arr)

print("Even Numbers: ", result["even"], '\n',
      "Odd Numbers: ", result["odd"], '\n',
      "Prime Numbers: ", result["prime"])
