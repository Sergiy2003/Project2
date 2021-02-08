'''dd'''
def validate_board(board):
    '''
    why so many commits ? really why ?
    my repository -> https://github.com/Sergiy2003/Project2.git
    function check a field and give you the information about its preparation.
    False if field is not read for using or true if it's
    >>> validate_board([\
    "**** ****",\
    "***1 ****",\
    "**  3****",\
    "* 4 1****",\
    "     9 5 ",\
    " 6  83  *",\
    "3   1  **",\
    "  8  2***",\
    "  2  ****"\
    ])
    False
    '''
    number_list = [1,2,3,4,5,6,7,8,9]
    horizontal_list = []
    for i in range(len(board)):
        horizontal_list.append(list(board[i]))
    for i in range(len(horizontal_list)):
        for j in range(len(number_list)):
            if str(number_list[j]) in horizontal_list[i]:
                check = horizontal_list[i].count(str(number_list[j]))
                if check > 1:
                    return False
    vertical_list = []
    for i in range(len(board)):
        new_list = []
        for j in range(len(board)):
            new_list.append(board[j][i])
        vertical_list.append(new_list)
    for i in range(len(vertical_list)):
        for j in range(len(number_list)):
            if str(number_list[j]) in vertical_list[i]:
                check = vertical_list[i].count(str(number_list[j]))
                if check > 1:
                    return False
    hori_verti_list = []
    for i in range(len(vertical_list)):
        new_list_ver = []
        for ver in range(i + 1):
            new_list_ver.append(vertical_list[8 - i][ver])
        new_list_hor = []
        for hor in range(i):
            new_list_hor.append(horizontal_list[i][8 - hor])
        hori_verti_list.append(new_list_ver + new_list_hor)
    for i in range(len(hori_verti_list)):
        for j in range(len(number_list)):
            if str(number_list[j]) in hori_verti_list[i]:
                check = hori_verti_list[i].count(str(number_list[j]))
                if check > 1:
                    return False
    return True
        