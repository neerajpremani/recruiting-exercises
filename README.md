# recruiting-exercises-deliverr

InventoryAllocatorLogic.py 
- Business Logic behind order allocation to get the cheapest order

STEPS:
- Iterate through the warehouse list 
- For each warehouse check whether order can be fullfilled
- IF YES, append the warehouse name and the order details to a final shopping list
- IF NOT, append the quantity that can fullfilled and iterate through the warehouse list and append to the shopping list
- FINAL step: check whether any order is pending till the end, IF YES return empty list (Order cannot be fullfilled by any warehouse) 


InventoryAllocatorTestCases.py - Contains 15 test cases to verify different conditions on order and warehouse

TO RUN (from recruiting-exercises-master folder):

--  python .\inventory-allocator\src\InventoryAllocatorTestCases.py