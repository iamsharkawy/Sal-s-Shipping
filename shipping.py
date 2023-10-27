weight = 41.5

# Ground Shipping
if weight <= 2:
  cost = weight * 1.50 + 20
elif weight > 2 and weight < 6:
  cost = weight * 3 + 20
elif weight > 6 and weight < 10:
  cost = weight * 4 + 20
else:
  cost = weight * 4.75 + 20

print("Ground Shipping Cost: ", cost, "$")

# Premium Ground Shipping
Premium_shipping_cost = 125
print("Premium Ground Shipping Cost: ", Premium_shipping_cost , "$")

# Drone Shipping

if weight <= 2:
  cost = weight * 4.50
elif weight > 2 and weight < 6:
  cost = weight * 9
elif weight > 6 and weight < 10:
  cost = weight * 12
else:
  cost = weight * 14.25

print("Drone Shipping Cost: ", cost, "$")


