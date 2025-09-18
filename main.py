
import sys

def get_book_text(filepath):
	with open(filepath) as file:
		book = file.read()
		return book

from stats import get_book_words 

from stats import count_charts

from stats import sort_dict     #takes a dictionary, returns a list 

def main(filepath):

    new_dict={}
    try:
        book_len = get_book_text(filepath[1])
    except Exception as e:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print(f"----------- Word Count ----------")
    print(f"Found {get_book_words(book_len)} total words")
    print(f"--------- Character Count -------")
    new_dict = count_charts(book_len)
    new_dict = sort_dict(new_dict)
    for i in range(0,len(new_dict)):
        if(new_dict[i]["char"].isalpha()):
            print(f"{new_dict[i]["char"]}: {new_dict[i]["num"]}")
    print("============= END ===============")



main(sys.argv)
#main(f"books/frankenstein.txt")
