def groundShip(weight=1):
  if weight<=2:
    cost = 1.5*weight+20
  elif weight>2 and weight<=6:
    cost = 3*weight+20
  elif weight>6 and weight<=10:
    cost = 4*weight+20
  else:
    cost = 4.75*weight+20

  return cost

package1 = groundShip(8.4)
print(package1)
premiumGround = 125

def droneShip(weight):
  if weight<=2:
    cost = 4.5*weight
  elif weight>2 and weight<=6:
    cost = 9*weight
  elif weight>6 and weight<=10:
    cost = 12*weight
  else:
    cost = 14.25*weight

  return cost

package2 = droneShip(1.5)
print(package2)