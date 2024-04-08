def calculate_circle_area(radius):
    pi = 3.14159
    area = pi * (radius ** 2)
    return area

def main():
    radius = float(input("Введіть радіус кола: "))
    area = calculate_circle_area(radius)
    print("Площа кола з радіусом", radius, "дорівнює", area)

if __name__ == "__main__":
    main()
