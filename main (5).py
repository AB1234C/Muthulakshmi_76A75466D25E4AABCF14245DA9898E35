#linear search program

def linear_search_product(productList , targetProduct):
  indices=[]
  for index, product in enumerate(productList):
    if product==targetProduct:
      indices.append(index)
  return indices
products=["shoes","boot","loafer","shoes","sandal","shoes"]
target1="shoes"
target2="apple"
result=linear_search_product(products,target1)
print(result)