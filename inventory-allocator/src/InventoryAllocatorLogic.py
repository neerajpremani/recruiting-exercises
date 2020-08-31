
class InventoryAllocator:
    def cheapestOrderAllocator(self, orderDetails, warehouseDetails):
        # Checking condition whether order and warehouse details are 0
        if len(orderDetails) == 0 or len(warehouseDetails) == 0:
            return []
        # Creating a shipping order list to append orderDetails when condition is satisfied
        shipOrder = list()
        for warehouse in warehouseDetails:
            # Creating a dictionary to create Item:Quantity Pairs to append to the list
            maxOrderDict = dict()

            for name, orderQuantity in orderDetails.items():
                # Condition checking whether warehouse can fulfill the order request or not
                if warehouse["inventory"].get(name) and orderQuantity > 0:
                    if orderQuantity <= warehouse["inventory"][name]:
                        # Warehouse can fulfill, updating records as per
                        maxOrderDict[name] = orderQuantity
                        orderDetails[name] = 0
                    else:
                        # Warehouse has insufficient quantity to fulfill order request
                        maxOrderDict[name] = warehouse["inventory"][name]
                        orderDetails[name] -= warehouse["inventory"][name]

            # Appending the item:quantity pairs to the shipOrder list
            if len(maxOrderDict) > 0:
                shipOrder.append({warehouse["name"] : maxOrderDict})

        # Checking any order left
        for name, orderQuantity in orderDetails.items():
            if orderQuantity > 0:
                return []

        return shipOrder






