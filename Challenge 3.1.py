def linearsearchproduct(productlist,targetlist):
  indices=[]
  for index,product in enumerate(productlist):
    if product==target:
      indices.append(index)


  return indices
products=["shoes","slipper","sandal","slipper","slipper"]
target="slipper"
result=linearsearchproduct(products,target)
print(result)