list_of_name = ['Sana Eslami', 'Raha Eslami', 'Rose Samadi', 'Soodeh Parsa']

def seprate_name(full_name):
    return full_name.split()[0]

# print(seprate_name(list_of_name[0]))
print(list(map(seprate_name, list_of_name)))