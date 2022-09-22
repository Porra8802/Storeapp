"""
Esta es una aplicación que te permite ingresar las ventas de un producto, con su cantidad, precio y 
hacer un cálculo del total de esa venta, ella será almacenada en un archivo plano que se guarda localmente
y este a la vez va a ser leído para obtener las ventas de los productos totales y el valor de las ventas totales
 """

#definir tu url local
from asyncore import file_wrapper


url="compras.txt"

#definición de función parametro o función decorador
def file(parameter_function):
    #definición de función de ejecución que nos va a retornar la función que pasemos al decorador
    def run_function(**kwargs):
        with open(url, "a+") as f:
            return parameter_function(f, **kwargs)

    return run_function

#aplicación de decorador a función agregar venta
@file
def add_purchase(obj_f, **kwargs):
    name=kwargs["prod_name"]
    quantity=kwargs["quantity"]
    unit_price=kwargs["unit_price"]
    total=kwargs["quantity"]*kwargs["unit_price"]
    row=(f'{name}, {quantity}, {unit_price}, {total}\n')
    obj_f.write(row)

#aplicación de decorador a función de listar productos
@file
def product_list(obj_f):
    obj_f.seek(0,0)
    print(obj_f.read())

#aplicación de decorador a función de obtener productos
@file
def get_products(obj_f):
    obj_f.seek(0,0)
    return (obj_f.readlines())

#funcion para obtener el total de las ventas
def total_sales():
    total_sales=0
    for product in get_products():
        product=product.strip("\n")
        total_product=product.split(",")[3]
        total_sales=total_sales+int(total_product)

    print("Las ventas totales del día son: " + str(total_sales) + " COP ")

#función para obtener el total de los productos vendidos
def total_products_sales():
    total_product_sales=0
    for product in get_products():
        product=product.strip("\n")
        total_product=product.split(",")[1]
        total_product_sales=total_product_sales+int(total_product)

    print("Se han vendido hasta el momento " + str(total_product_sales)+ " productos")


if __name__=="__main__":

    while True:
        selection=int(input("Seleccione la acción que deseas realizar (1-Agregar compra, 2-Listar productos, 3-Total de ventas, 4-Total de productos vendidos, 5-Cerrar) " ))

        if selection==1: 
            data={
                "prod_name": input("Cual es el nombre del producto: "),
                "quantity": int(input("Cuál es la cantidad del producto ")),
                "unit_price": int(input("Cuál es el precio del producto ")),
                }
            add_purchase(**data)

        elif selection==2:
            product_list()

        elif selection==3:
            total_sales()

        elif selection==4:      
            total_products_sales()
        
        elif selection==5:
            break

        else:
            print("Ingresas un valor invalido, por favor ingresar de nuevo")


