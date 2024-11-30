def  test_function():
   def inner_function():
      print("Я в области видимости функции test_function")
   inner_function()


test_function()
#inner_function() # при вызове функции внутри функции выходит ошибка так как она не работает за пределами функции.

