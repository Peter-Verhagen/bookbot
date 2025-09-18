
def get_book_words(book_file):
        list_words = book_file.split()
        return len(list_words)

def count_charts(book_file):

	char_dict = {}
	book_file = book_file.lower()

	for char in book_file:
		if(char not in char_dict):
			char_dict[char] = 1
		elif(char in char_dict):
			char_dict[char]+=1
	return char_dict

def sort_on(items):
    return items["num"]


def sort_dict(dictionary):
    
    sorted_dict={}
    list_dict=[]

    for key in dictionary:
        sorted_dict["char"] = key
        sorted_dict["num"] = dictionary[key]
        list_dict.append(sorted_dict)
        sorted_dict={}
    list_dict.sort(reverse=True,key=sort_on)
    return list_dict

        #sorted_dict[key] = dictionary[key]
        #list_dict.append(sorted_dict)
        #sorted_dict={}




#sort_dict({"h":19176,"t":29493,"e":44538,"g":5795}) 
