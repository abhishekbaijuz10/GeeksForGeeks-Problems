def check_if_empt(string, sub):
    while len(string)!=0:
        index_of_sub = string.find(sub)

        if index_of_sub == -1:
            return False

        string = string[0:index_of_sub] + string[index_of_sub+len(sub):]

    return True

my_str = 'geegeeksks'
sub_string = 'geeks'
print(check_if_empt(my_str, sub_string))
