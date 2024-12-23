import matplotlib.pyplot as plt

def main():
    print("Добро пожаловать в Архитектурный планировщик!")

    # Ввод размеров квартиры (дома)
    width = float(input("Введите ширину квартиры (в метрах): "))
    height = float(input("Введите длину квартиры (в метрах): "))

    rooms = []  # Список для хранения информации о комнатах

    while True:
        print("\nДобавление комнаты:")
        room_name = input("Введите название комнаты: ")
        room_width = float(input("Введите ширину комнаты (в метрах): "))
        room_height = float(input("Введите длину комнаты (в метрах): "))

        # Проверка на соответствие размеру квартиры
        if room_width > width or room_height > height:
            print("Размеры комнаты превышают размеры квартиры. Попробуйте снова.")
            continue

        room_area = room_width * room_height
        print(f"Площадь комнаты {room_name}: {room_area:.2f} кв. м")

        rooms.append({
            "name": room_name,
            "width": room_width,
            "height": room_height,
            "area": room_area
        })

        more = input("Хотите добавить еще одну комнату? (да/нет): ").lower()
        if more != "да":
            break

    # Визуализация плана
    visualize_plan(width, height, rooms)

    print("\nПроект завершен. Спасибо за использование Архитектурного планировщика!")

def visualize_plan(width, height, rooms):
    fig, ax = plt.subplots()
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.set_aspect('equal')
    
    current_x = 0
    current_y = 0

    for room in rooms:
        room_width = room["width"]
        room_height = room["height"]
        rect = plt.Rectangle((current_x, current_y), room_width, room_height, edgecolor='black', facecolor='lightblue', alpha=0.5)
        ax.add_patch(rect)
        ax.text(current_x + room_width / 2, current_y + room_height / 2, room["name"],
                color='black', ha='center', va='center')

        current_x += room_width
        if current_x >= width:  # Перенос на следующую "строку" плана
            current_x = 0
            current_y += room_height

    ax.set_title("План квартиры (дома)")
    ax.set_xlabel("Ширина (м)")
    ax.set_ylabel("Длина (м)")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
