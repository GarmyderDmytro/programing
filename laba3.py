ADMIN_PASSWORD = "admin123"

catalog: dict[str, dict] = {
    "products": {
        "1": {"name": "Хліб", "price": 35.50, "quantity": 20},
        "2": {"name": "Молоко", "price": 42.00, "quantity": 15},
        "3": {"name": "Сир", "price": 210.75, "quantity": 8},
        "4": {"name": "Яблука", "price": 55.20, "quantity": 30},
    }
}

cart: dict = {}


format_price = lambda value: f"{value:.2f} грн"


def get_price(item: tuple) -> float:
    return item[1]["price"]


def sort_by_price() -> dict:
    return dict(sorted(catalog["products"].items(), key=get_price))


def filter_in_stock(products: dict) -> dict:
    return {pid: product for pid, product in products.items() if product["quantity"] > 0}


def find_by_name(products: dict, name: str) -> dict:
    name = name.lower()
    return {
        pid: product
        for pid, product in products.items()
        if name in product["name"].lower()
    }


def cart_total(cart: dict) -> float:
    total: float = 0
    for product_id, quantity in cart.items():
        total += catalog["products"][product_id]["price"] * quantity
    return total


def ask() -> str:
    print("\nМАГАЗИН")
    print("1. Переглянути каталог товарів")
    print("2. Додати товар у кошик")
    print("3. Видалити товар з кошика")
    print("4. Переглянути кошик")
    print("5. Купити товари з кошика")
    print("6. Увійти як адміністратор")
    print("0. Вийти з програми")
    choice = input("Введіть номер дії: ")
    return choice.strip()


def show_catalog() -> None:
    print("\nКАТАЛОГ ТОВАРІВ")
    for product_id, product in catalog["products"].items():
        status = "в наявності" if product["quantity"] > 0 else "немає в наявності"
        print(
            f"{product_id:<8}{product['name']:<10}"
            f"{format_price(product['price']):<14}{status}"
        )


def find_product(product_id: str) -> dict:
    return catalog["products"].get(product_id)


def create_cart() -> dict:
    return {}


def add_to_cart() -> None:
    show_catalog()
    product_id = input("Введіть номер товару, який хочете додати: ").strip()
    product = find_product(product_id)

    if product is None:
        print("Товар з таким номером не знайдено.")
        return

    try:
        quantity = int(input("Введіть кількість: "))
    except ValueError:
        print("Помилка: введіть коректне число.")
        return

    if quantity <= 0:
        print("Кількість повинна бути більшою за нуль.")
        return

    already_in_cart = cart.get(product_id, 0)

    if product["quantity"] < already_in_cart + quantity:
        print(f"Недостатньо товару на складі. В наявності: {product['quantity']}.")
        return

    cart[product_id] = already_in_cart + quantity
    print(f"Товар '{product['name']}' додано в кошик. У кошику: {cart[product_id]} шт.")


def remove_from_cart() -> None:
    if not cart:
        print("\nКошик порожній.")
        return

    show_cart()
    product_id = input("Введіть номер товару для видалення з кошика: ").strip()

    if product_id in cart:
        del cart[product_id]
        print("Товар видалено з кошика.")
    else:
        print("Такого товару немає в кошику.")


def show_cart() -> None:
    if not cart:
        print("\nКошик порожній.")
        return

    print("\nВАШ КОШИК")
    for product_id, quantity in cart.items():
        product = catalog["products"][product_id]
        subtotal = product["price"] * quantity
        print(
            f"{product_id:<8}{product['name']:<10}"
            f"{format_price(product['price']):<14}{quantity:<5}"
            f"{format_price(subtotal)}"
        )
    print(f"Загальна сума: {format_price(cart_total(cart))}")


def buy() -> None:
    if not cart:
        print("Кошик порожній, купувати нічого.")
        return

    for product_id, quantity in cart.items():
        product = catalog["products"].get(product_id)
        if product is None or product["quantity"] < quantity:
            print(f"Товару з номером '{product_id}' недостатньо на складі. Купівлю скасовано.")
            return

    total = cart_total(cart)

    for product_id, quantity in cart.items():
        catalog["products"][product_id]["quantity"] -= quantity

    print("\nЧЕК")
    for product_id, quantity in cart.items():
        product = catalog["products"][product_id]
        subtotal = product["price"] * quantity
        print(f"{product['name']} x{quantity} = {format_price(subtotal)}")
    print(f"ДО СПЛАТИ: {format_price(total)}")
    print("Дякуємо за покупку!")

    cart.clear()


def show_stock() -> None:
    print("\nЗАЛИШКИ ТОВАРІВ")
    for product in catalog["products"].values():
        print(f"{product['name']:<10}{product['quantity']} шт.")


def admin_login() -> None:
    password = input("Введіть пароль адміністратора: ")
    if password == ADMIN_PASSWORD:
        print("Вхід виконано успішно.")
        show_stock()
    else:
        print("Невірний пароль.")


def main() -> None:
    while True:
        choice = ask()

        if choice == "1":
            show_catalog()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            remove_from_cart()
        elif choice == "4":
            show_cart()
        elif choice == "5":
            buy()
        elif choice == "6":
            admin_login()
        elif choice == "0":
            print("До побачення!")
            break
        else:
            print("Такого пункту меню немає, спробуйте ще раз.")


if __name__ == "__main__":
    main()
