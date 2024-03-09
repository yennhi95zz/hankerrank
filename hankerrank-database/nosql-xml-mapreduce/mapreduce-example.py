# This example calculates word frequencies 
# from a collection of documents.


from collections import Counter
from multiprocessing import Pool
from functools import reduce

def map_function(document):
    # Tokenize the document and count word frequencies
    words = document.lower().split()
    return Counter(words)

def reduce_function(counter1, counter2):
    # Combine word frequencies from two counters
    return counter1 + counter2

if __name__ == "__main__":
    # Sample documents
    documents = [
        "Hello world",
        "Hello from the other side",
        "World of programming",
        "Programming is fun",
    ]

    # Map phase
    with Pool() as pool:
        mapped_results = pool.map(map_function, documents)

    # Reduce phase
    final_result = reduce(reduce_function, mapped_results)

    # Display the final word frequencies
    print("Word frequencies:", final_result)
