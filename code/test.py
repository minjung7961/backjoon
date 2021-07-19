def main():
    count = 0
    x = int(input())
    while x != 1:


        if x % 3 == 0:
            x = int(x/3)
        elif x % 3 != 0:
            x -= 1
        elif x % 2 != 0:
            x = int(x/2)
                
        count += 1 

    return count

if __name__ == '__main__':
    print(main()) # 1을 만들기위한 연산 갯수를 출력하자