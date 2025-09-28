# 在此处编写代码
try:
    year = int(input("请输入一个年份："))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} 是闰年")
    else:
        print(f"{year} 不是闰年")
except ValueError:
    print("输入错误！请输入一个有效的整数年份。")
