import string
import os
os.system('cls')
def InputNumber(condition, str):
    check = True
    # x: int
    while check:
        try:
            if condition == 'int':
                x = int(input(str))
            elif condition == 'float':
                x = float(input(str))
        except: check = True
        else:
            if x < 0 or x == 0 and condition == 'int': check = True
            else:
                # check = False
                return x
    # return x
check = True
while check:
    option = InputNumber('int', '''1. Xem danh sách các học sinh
2. Tìm học sinh theo mã
3. Thêm học sinh
4. Sửa học sinh
5. Xóa học sinh
6. Thoát
Bạn chọn số mấy? ''')
    match option:
        case 1:
            f = open('pupil.txt', 'r', encoding='utf-8')
            for x in f:
                print(x.strip())
            # print(f.read())
            f.close()
        case 2:
            wantedId = InputNumber('int', 'Nhập mã học sinh mà bạn muốn tìm: ')
            f = open('pupil.txt', 'r', encoding='utf-8')
            for x in f:
                # if len(x.strip()) != 0:
                try:
                    if int(x.split()[0]) == wantedId:
                        print(x)
                        break
                except IndexError: pass
            f.close()
        case 3:
            numberOfPupils = InputNumber('int', 'Nhập số học sinh mà bạn muốn nhập liệu: ')
            numberOfGoodPupils = numberOfRatherPupils = numberOfAveragePupils = 0
            summary = 'Có tổng cộng'
            spaces = ' ' * len(summary)
            for i in range (1, numberOfPupils + 1):
                id = InputNumber('int', 'Nhập mã học sinh: ')
                f = open('pupil.txt', 'r', encoding='utf-8')
                checkExistPupil = False
                for x in f:
                    l = x.split()
                    try:
                        if int(l[0]) == id:
                            print('Mã học sinh này đã tồn tại')
                            checkExistPupil = True
                            break
                        else: checkExistPupil = False
                    except IndexError: pass
                f.close()
                if checkExistPupil: continue
                # name = input('Nhập tên học sinh: ').capitalize()
                name = string.capwords(input('Nhập tên học sinh: '))
                science = InputNumber('float', 'Nhập điểm khoa học: ')
                social = InputNumber('float', 'Nhập điểm xã hội: ')
                softSkill = InputNumber('float', 'Nhập điểm kỹ năng mềm: ')
                average = (science + social + softSkill) / 3
                print(f'Điểm trung bình của {name} là: {average:.2f}')
                f = open('pupil.txt', 'a', encoding='utf-8')
                f.write(f'{id} {name} {average:.2f}\n')
                f.close()
                if average >= 8:
                    numberOfGoodPupils += 1
                    print(name, 'xuất sắc thật')
                elif average >= 5.5 and average < 8:
                    numberOfRatherPupils += 1
                    print(name, 'làm tốt lắm')
                else:
                    numberOfAveragePupils += 1
                    print(name, 'cố lên')
                print('-' * 10)
            print(f'''{summary} {numberOfGoodPupils} HSG
            {spaces} {numberOfRatherPupils} HSK
            {spaces} {numberOfAveragePupils} HSTB
            ''')
            # print('Có tổng cộng', numberOfGoodPupils, 'HSG')
            # print(spaces, numberOfRatherPupils, 'HSK')
            # print(spaces, numberOfAveragePupils, 'HSTB')
        case 4:
            wantedId = InputNumber('int', 'Nhập mã học sinh mà bạn muốn sửa: ')
            f = open('pupil.txt', 'r', encoding='utf-8')
            newF = ''
            for x in f:
                l = x.split()
                try:
                    if int(l[0]) == wantedId:
                        name = string.capwords(input('Nhập tên mới: '))
                        average = InputNumber('float', 'Nhập điểm trung bình mới: ')
                        x = f'{wantedId} {name} {average}'
                        # newF.join(f'{x}\n')
                        newF += f'{x}\n'
                    else: newF += f'{x}\n'
                except IndexError: pass
            f = open('pupil.txt', 'w', encoding='utf-8')
            f.write(newF)
            f.close()
        case 5:
            wantedId = InputNumber('int', 'Nhập mã học sinh mà bạn muốn xóa: ')
            f = open('pupil.txt', 'r', encoding='utf-8')
            newF = ''
            for x in f:
                l = x.split()
                try:
                    if int(l[0]) == wantedId:
                        # newF += ''
                        break
                    else: newF += f'{x}\n'
                except IndexError: pass
            f = open('pupil.txt', 'w', encoding='utf-8')
            f.write(newF)
            f.close()
        case 6:
            check = False