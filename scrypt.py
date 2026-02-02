purchases = [

    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},

    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},

    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},

    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},

]

#общая стоитмость покупок

def total_revenue(purchases):

    return sum (i["price"] * i["quantity"] for i in purchases)

print (f"Общая выручка: {total_revenue(purchases)}")

#продукты по категориям

def items_by_category(purchases):

    result = {}

    for i in purchases:

        category = i["category"]

        item = i["item"]

        if category not in result:

            result[category] =[]

        if item not in result[category]:

            result[category].append(item)

    return result

print (f"Товары по категориям:{items_by_category(purchases)}")

#покупки дороже определенной суммы

def expensive_purchases(purchases, min_price=1.0):

    if min_price is None:

        min_price = min(i["price"] for i in purchases )

    return min_price, [i for i in purchases if i["price"] > min_price]

   

min_price_value, result = expensive_purchases(purchases)

print (f"Покупки дороже {min_price_value}: {result}")

#Средняя цена товаров по категориям

def average_price_by_category(purchases):

    category_prices = {}

    category_counts = {}

    for i in purchases:

        category = i["category"]

        category_prices[category] = category_prices.get(category, 0) + i["price"]

        category_counts[category] = category_counts.get(category, 0) + 1

    return {category: round(category_prices[category] / category_counts[category], 2) for category in category_prices}

print (f"Средняя цена по категориям: {average_price_by_category(purchases)}")

#Категория наивысших продаж

def most_frequent_category(purchases):

    category_quantity = {}

    for i in purchases:

        category = i["category"]

        category_quantity[category] = category_quantity.get(category, 0) + i["quantity"]

    return max(category_quantity, key=category_quantity.get)

print (f"Категория с наибольшим количеством проданных товаров: {most_frequent_category(purchases)}")