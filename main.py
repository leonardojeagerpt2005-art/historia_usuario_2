list_product = []

def add_product():
            print("="*50)
            product_name = input("ingrese el nombre del producto: ")
            print("="*50)
            unit_price = float(input("ingrese el precio del producto: "))
            print("="*50)
            quantity = int(input("ingrese la cantidad del producto: "))
            print("="*50)

            product = {
                "name": product_name,
                "price": unit_price,
                "quantity": quantity
            }

            list_product.append(product)
            print("="*50)
            print("✅ su producto a sido agregado con exito")
            print("="*50)

def show_inventory():
    print("="*50)
    for product in list_product:
        print("="*50)
        print(f"producto: {product['name']} | price: {product['price']} | quantity {product['quantity']}")
        print("="*50)

def calculate_statistics():
    print("="*50)
    print("📊 INVENTORY STATISTICS 📊")
    print("="*50)

    for product in list_product:
        if not list_product:
            print("⚠️ No data available to calculate statistics.")
        else:
            total_value = 0
            total_items = 0

            total_value +=  product['price'] * product['quantity']
            total_items += product['quantity']

            print(f"Total value of inventory: ${total_value:,.2f}")
            print(f"Total units in stock: {total_items}")
            print(f"Total types of products: {len(list_product)}")

        print("="*50)
         


opcion = None

while opcion != 4:
    print(f"""
    ╔═══════════════════════════════════════════════════════════╗
                    🥑 RIWIMART RETAIL CHAIN 🥑
    🌷 Welcome to the Customer Order Management System! 🌷
            
            1) 🤵 add Product
            2) 🔍 show inventory
            3) 🧾 calculate statistics
            4) 💀 Exit
    ╚═══════════════════════════════════════════════════════════╝
    """)
    print("="*50)
    opcion = int(input("ingrese la opcio que desea realizar: "))
    
    if opcion == 1:
        add_product()
    elif opcion == 2:
        show_inventory()
    elif opcion == 3:
        calculate_statistics()
    else:
         print("fin del programa")