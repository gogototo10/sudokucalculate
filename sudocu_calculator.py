import copy



Recursive_function_end_flag=False

def first_list(sudocu_mat):
    for i in range(0, 9):
        for j in range(0, 9):
            if sudocu_mat[i][j] == 0:
                sudocu_mat[i][j] = [1, 2, 3, 4, 5, 6, 7, 8,
                                    9]  # 처음에 실행되면 빈곳은 0을 입력되어있어서 0으로 되어있는 곳을 리스트형으로 변경하고 리스트에 들어갈수있는 수만 집어넣는다.


def horizontal_mat(sudocu_mat):  # 가로줄 계산
    for i in range(0, 9):
        for j in range(0, 9):
            if type(sudocu_mat[i][j]) == type([]):  # 해당칸이 리스트형이면 어떤수가 들어가는지 몰라서 리스트형으로 들어갈수있는것을 집어넣기 위해서 하는것
                for k in range(0, 9):  # 여기서 주로 리스트형에 들어갈수를 정한다.
                    if type(sudocu_mat[i][k]) == type(0) and (
                            sudocu_mat[i][k] in sudocu_mat[i][j]):  # 각각의 칸을 검사 (int형이고 해당리스트에 값이 중복되지 않아야한다.)
                        sudocu_mat[i][j].remove(sudocu_mat[i][k])
    for i in range(0, 9):
        for j in range(0, 9):
            if type(sudocu_mat[i][j]) == type([]) and len(
                    sudocu_mat[i][j]) == 1:  # 리스트형에서 들어갈수 있는 수가 1개이면 그수를 집어넣을 수 밖에 없으므로 그렇게 실행 한다.
                sudocu_mat[i][j] = sudocu_mat[i][j][0]
                for ii in range(0, 9):
                    for jj in range(0, 9):
                        if type(sudocu_mat[ii][jj]) == type(
                                []):  # 해당칸이 리스트형이면 어떤수가 들어가는지 몰라서 리스트형으로 들어갈수있는것을 집어넣기 위해서 하는것
                            for k in range(0, 9):  # 여기서 주로 리스트형에 들어갈수를 정한다.
                                if type(sudocu_mat[ii][k]) == type(0) and (
                                        sudocu_mat[ii][k] in sudocu_mat[ii][
                                    jj]):  # 각각의 칸을 검사 (int형이고 해당리스트에 값이 중복되지 않아야한다.)
                                    sudocu_mat[ii][jj].remove(sudocu_mat[ii][k])


def vertical_mat(sudocu_mat):  # 세로줄 계산
    for i in range(0, 9):
        for j in range(0, 9):
            if type(sudocu_mat[j][i]) == type([]):  # 해당칸이 리스트형이면 어떤수가 들어가는지 몰라서 리스트형으로 들어갈수있는것을 집어넣기 위해서 하는것
                for k in range(0, 9):  # 여기서 주로 리스트형에 들어갈수를 정한다.
                    if type(sudocu_mat[k][i]) == type(0) and (
                            sudocu_mat[k][i] in sudocu_mat[j][i]):  # 각각의 칸을 검사 (int형이고 해당리스트에 값이 중복되지 않아야한다.)
                        sudocu_mat[j][i].remove(sudocu_mat[k][i])
    for i in range(0, 9):
        for j in range(0, 9):
            if type(sudocu_mat[j][i]) == type([]) and len(sudocu_mat[j][i]) == 1:  # 리스트형에서 들어갈수 있는 수가 1개이면 그수를 집어넣을 수 밖에 없으므로 그렇게 실행 한다.
                sudocu_mat[j][i] = sudocu_mat[j][i][0]
                for ii in range(0, 9):
                    for jj in range(0, 9):
                        if type(sudocu_mat[jj][ii]) == type(
                                []):  # 해당칸이 리스트형이면 어떤수가 들어가는지 몰라서 리스트형으로 들어갈수있는것을 집어넣기 위해서 하는것
                            for k in range(0, 9):  # 여기서 주로 리스트형에 들어갈수를 정한다.
                                if type(sudocu_mat[k][ii]) == type(0) and (
                                        sudocu_mat[k][ii] in sudocu_mat[jj][
                                    ii]):  # 각각의 칸을 검사 (int형이고 해당리스트에 값이 중복되지 않아야한다.)
                                    sudocu_mat[jj][ii].remove(sudocu_mat[k][ii])

def block_mat(sudocu_mat):  # 블럭 단위로 계산
    for x in range(0, 3):  # x,y는 블럭을 이동하기 위해 사용
        for y in range(0, 3):

            for i in range(0, 3):
                for j in range(0, 3):
                    sudocu_mat[i + x * 3][j + y * 3]
                    if type(sudocu_mat[i + x * 3][j + y * 3]) == type(
                            []):  # 해당칸이 리스트형이면 어떤수가 들어가는지 몰라서 리스트형으로 들어갈수있는것을 집어넣기 위해서 하는것
                        for a in range(0, 3):
                            for b in range(0, 3):
                                if type(sudocu_mat[a + x * 3][b + y * 3]) == type(0) and (
                                        sudocu_mat[a + x * 3][b + y * 3] in sudocu_mat[i + x * 3][j + y * 3]):
                                    sudocu_mat[i + x * 3][j + y * 3].remove(sudocu_mat[a + x * 3][b + y * 3])

def sudocu_mat_list_clear(sudocu_mat):  # sudocu_mat_calculation에서 계산이 끝나고 정리할려고 사용
        horizontal_mat(sudocu_mat)
        vertical_mat(sudocu_mat)
        block_mat(sudocu_mat)

def sudocu_mat_calculation(sudocu_mat):  # 계산이 필요한것은 이곳에서 계산
    first_list(sudocu_mat)
    pre_mat = sudocu_mat
    sudocu_mat_list_clear(sudocu_mat)
    while pre_mat != sudocu_mat:
        pre_mat = sudocu_mat
        # VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVvv 리스트에 1개만 있으면 그수를 집어넣는다
        for i in range(0, 9):
            for j in range(0, 9):
                if type(sudocu_mat[i][j]) == type([]) and len(sudocu_mat[i][j]) == 1:  # 리스트형에서 들어갈수 있는 수가 1개이면 그수를 집어넣을 수 밖에 없으므로 그렇게 실행 한다.
                    sudocu_mat[i][j] = sudocu_mat[i][j][0]
                    sudocu_mat_list_clear(sudocu_mat)

        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        sudocu_mat_list_clear(sudocu_mat)

        # VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV 가로줄에서 해당 줄에 1개씩 꼭 들어가야하나 해당줄의 리스트들에서 딱 1개만 잇으면 무조건 그게 들어가야 하므로 그걸 계산하는것

        for num in range(1, 10):

            for i in range(0, 9):
                count = 0
                temp_list = [0, 0, 0]
                for j in range(0, 9):
                    if type(sudocu_mat[i][j]) == type([]):  #
                        for k in sudocu_mat[i][j]:
                            if k == num:
                                count = count + 1
                                temp_list[0] = i
                                temp_list[1] = j
                                temp_list[2] = num
                if count == 1:
                    sudocu_mat[temp_list[0]][temp_list[1]] = temp_list[2]
                    sudocu_mat_list_clear(sudocu_mat)
        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        sudocu_mat_list_clear(sudocu_mat)

        # VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV 세로줄에서 해당 줄에 1개씩 꼭 들어가야하나 해당줄의 리스트들에서 딱 1개만 잇으면 무조건 그게 들어가야 하므로 그걸 계산하는것
        for num in range(1, 10):

            for i in range(0, 9):
                count = 0
                temp_list = [0, 0, 0]
                for j in range(0, 9):
                    if type(sudocu_mat[j][i]) == type([]):  #
                        for k in sudocu_mat[j][i]:
                            if k == num:
                                count = count + 1
                                temp_list[0] = j
                                temp_list[1] = i
                                temp_list[2] = num
                if count == 1:
                    sudocu_mat[temp_list[0]][temp_list[1]] = temp_list[2]
                    sudocu_mat_list_clear(sudocu_mat)
        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        sudocu_mat_list_clear(sudocu_mat)

        # VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV 블럭에서 해당 줄에 1개씩 꼭 들어가야하나 해당줄의 리스트들에서 딱 1개만 잇으면 무조건 그게 들어가야 하므로 그걸 계산하는것
        for num in range(1, 10):

            for x in range(0, 3):  # x,y는 블럭을 이동하기 위해 사용
                for y in range(0, 3):
                    count = 0
                    temp_list = [0, 0, 0]
                    for i in range(0, 3):
                        for j in range(0, 3):
                            sudocu_mat[i + x * 3][j + y * 3]
                            if type(sudocu_mat[i + x * 3][j + y * 3]) == type(
                                    []):  # 해당칸이 리스트형이면 어떤수가 들어가는지 몰라서 리스트형으로 들어갈수있는것을 집어넣기 위해서 하는것
                                for k in sudocu_mat[i + x * 3][j + y * 3]:
                                    if k == num:
                                        count = count + 1
                                        temp_list[0] = i + x * 3
                                        temp_list[1] = j + y * 3
                                        temp_list[2] = num
                    if count == 1:
                        sudocu_mat[temp_list[0]][temp_list[1]] = temp_list[2]
                        sudocu_mat_list_clear(sudocu_mat)
        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        sudocu_mat_list_clear(sudocu_mat)

    #print_sudocu_mat(sudocu_mat)


def print_sudocu_mat(sudocu_mat):
    for i in range(0, 9):
        temp_str = ''
        for j in range(0, 9):
            if (j + 1) % 3 == 0:
                temp_str += str(sudocu_mat[i][j]) + "\t\t\t\t"
            else:
                temp_str += str(sudocu_mat[i][j]) + " "
        print(temp_str)
        if (i + 1) % 3 == 0:
            print()
    print()


def mat_complete(sudocu_mat):
    mat_working = True
    return_val = False
    for i in range(0, 9):
        for j in range(0, 9):
            if type(sudocu_mat[i][j]) == type([]):
                mat_working = False

    if mat_working:
        return_val = True
        for i in range(0, 9):
            num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for j in range(0, 9):
                if sudocu_mat[i][j] in num_list:
                    num_list.remove(sudocu_mat[i][j])
            if len(num_list) > 0:
                return_val = False

        for i in range(0, 9):
            num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for j in range(0, 9):
                if sudocu_mat[i][j] in num_list:
                    num_list.remove(sudocu_mat[i][j])
            if len(num_list) > 0:
                return_val = False

        for x in range(0, 3):  # x,y는 블럭을 이동하기 위해 사용
            for y in range(0, 3):
                num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

                for i in range(0, 3):
                    for j in range(0, 3):
                        if sudocu_mat[i + x * 3][j + y * 3] in num_list:
                            num_list.remove(sudocu_mat[i + x * 3][j + y * 3])
                if len(num_list) > 0:
                    return_val = False
    return [mat_working, return_val]

def list_in_empty_mat(sudocu_mat):
    for i in range(0, 9):
        for j in range(0, 9):
            if type(sudocu_mat[i][j]) == type([]):
                if sudocu_mat[i][j]==[]:
                    return True
                else:
                    return False

def case_mat_calculation(sudocu_mat, count=0):  ##빈칸에 들어갈수 있는 수들을 저장한다음 그수들을 하나 하나씩 대입하고 계산(스도쿠의 조건을 계산한다.)

    if mat_complete(sudocu_mat)[1]:
        global sudocu_mat_1
        sudocu_mat_1=copy.deepcopy(sudocu_mat)

        return True


    for_break_flag=False
    temp_count=count+1
    mat_list_side = []

    for i in range(0, 9):#첫 리스트형을 발견하면 mat_list_side에 저장후 바로 for 문을 나간다.
        if for_break_flag:
            break
        for j in range(0, 9):
            if type(sudocu_mat[i][j]) == type([]):
                mat_list_side.append(i)
                mat_list_side.append(j)
                mat_list_side.append(sudocu_mat[i][j])
                for_break_flag=True
                break

    try:
        for mat_list_side_i in mat_list_side[2]:
            temp_mat=copy.deepcopy(sudocu_mat)
            temp_mat[mat_list_side[0]][mat_list_side[1]]=mat_list_side_i
            sudocu_mat_calculation(temp_mat)


            if not list_in_empty_mat(temp_mat):  # 빈리스트가 없으면 작동

                if case_mat_calculation(temp_mat,temp_count) :

                    return True
    except:
        pass



def sudocu_calculation_final(mat):
    sudocu_mat_calculation(mat)
    case_mat_calculation(mat, 0)

    print_sudocu_mat(sudocu_mat_1)
    return sudocu_mat_1

