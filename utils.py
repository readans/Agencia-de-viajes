def alter(x, y):
  return (y, x)

def key2value(d):
  return {y:x for x, y in d.items()}

mydict= {
  "a": "b",
  "b": "a"
}
# print(mydict)
# print(key2value(mydict))

# a= 10
# b= 20
# a= a+b
# b= a-b
# a= a-b
# print(a, b)

print([].append(10))