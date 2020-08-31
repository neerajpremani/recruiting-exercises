from InventoryAllocatorLogic import InventoryAllocator

def getBestShipment(orderDetail, warehouseCollection):
    print("Orders Details: ", orderDetail)
    print("Warehouse Details: ", warehouseCollection)
    inventory = InventoryAllocator()
    print("Result are: ",inventory.cheapestOrderAllocator(orderDetail, warehouseCollection))
    print("")

if __name__ == '__main__':

    # Test Case 1
    print("Test Case 1")
    orderDetail = {"apple": 7, "orange": 12}
    warehouseStore = [{"name": "owd", "inventory": {"apple": 5, "orange": 10}},
                  {"name": "dm", "inventory": {"apple": 10, "orange": 15}}]
    getBestShipment(orderDetail, warehouseStore)
    print("------------------------------------------------------------")

    # Test Case 2
    print("Test Case 2")
    orderDetail = {"apple": 5, "orange": 10}
    warehouseStore = [{"name": "owd", "inventory": {"apple": 5, "orange": 10}},
                  {"name": "dm", "inventory": {"apple": 5, "orange": 10}}]
    getBestShipment(orderDetail, warehouseStore)
    print("------------------------------------------------------------")

    # Test Case 3
    print("Test Case 3")
    orderDetail = {"apple": 6, "orange": 10, "watermelon": 4}
    warehouseStore = [{"name": "owd", "inventory": {"apple": 5, "orange": 10}},
                  {"name": "dm", "inventory": {"apple": 5, "orange": 10}}]
    getBestShipment(orderDetail, warehouseStore)
    print("------------------------------------------------------------")

    # Test Case 4
    print("Test Case 4")
    orderDetail = {"apple": 11, "orange": 30 }
    warehouseStore = [{"name": "owd", "inventory": {"apple": 5, "orange": 10}},
                  {"name": "dm", "inventory": {"apple": 5, "orange": 10}}]
    getBestShipment(orderDetail, warehouseStore)
    print("------------------------------------------------------------")

    # Test Case 5
    print("Test Case 5")
    orderDetail = {"apple": 6, "orange": 10, "watermelon": 4}
    warehouseStore = []
    getBestShipment(orderDetail, warehouseStore)
    print("------------------------------------------------------------")

    # Test Case 6
    print("Test Case 6")
    orderDetail = {"apple": 6, "orange": 10, "watermelon": 4}
    warehouseStore = [{"name": "owd", "inventory": {"apple": 5, "orange": 10}},
                  {"name": "dm", "inventory": {"apple": 5, "orange": 10}},
                  {"name": "ck", "inventory": {"watermelon": 10, "banana": 10}}]
    getBestShipment(orderDetail, warehouseStore)
    print("------------------------------------------------------------")

    # Test Case 7
    print("Test Case 7")
    orderDetail = { "apple": 1 }
    warehouseStore = [{ "name": "owd", "inventory": { "apple": 1 } }]
    getBestShipment(orderDetail, warehouseStore)
    print("------------------------------------------------------------")

    # Test Case 8
    print("Test Case 8")
    orderDetail = {"apple": 1}
    warehouseStore = [{"name": "owd", "inventory": {"apple": 0}}]
    getBestShipment(orderDetail, warehouseStore)
    print("------------------------------------------------------------")

     # Test Case 9
    print("Test Case 9")
    orderDetail = {}
    warehouseStore = [{"name": "owd", "inventory": {"apple": 0}}]
    getBestShipment(orderDetail, warehouseStore)
    print("------------------------------------------------------------")

     # Test Case 10
    print("Test Case 10")
    orderDetail = {"apple": 1}
    warehouseStore = []
    getBestShipment(orderDetail, warehouseStore)
    print("------------------------------------------------------------")

    # Test Case 11
    print("Test Case 11")
    orderDetail = {"apple": 11}
    warehouseStore = [{"name": "owd", "inventory": {"apple": 5, "orange": 10}},
                  {"name": "dm", "inventory": {"apple": 5, "orange": 10}}]
    getBestShipment(orderDetail, warehouseStore)
    print("------------------------------------------------------------")

    # Test Case 12
    print("Test Case 12")
    orderDetail = {"orange": 20}
    warehouseStore = [{"name": "owd", "inventory": {"apple": 5, "orange": 10}},
                  {"name": "dm", "inventory": {"apple": 5, "orange": 10}}]
    getBestShipment(orderDetail, warehouseStore)
    print("------------------------------------------------------------")

    # Test Case 13
    print("Test Case 13")
    orderDetail = {"apple": 1, "orange":5}
    warehouseStore = [{"name": "owd", "inventory": {"apple": 5, "orange": 10}},
                  {"name": "dm", "inventory": {"apple": 5, "orange": 10}}]
    getBestShipment(orderDetail, warehouseStore)
    print("------------------------------------------------------------")

    # Test Case 14
    print("Test Case 14")
    orderDetail = {"watermelon": 1}
    warehouseStore = [{"name": "owd", "inventory": {"apple": 5, "orange": 10}},
                  {"name": "dm", "inventory": {"apple": 5, "orange": 10}}]
    getBestShipment(orderDetail, warehouseStore)
    print("------------------------------------------------------------")

       # Test Case 15
    print("Test Case 15")
    orderDetail = {"apple": 10, "orange":20}
    warehouseStore = [{"name": "owd", "inventory": {"apple": 5, "orange": 10}},
                  {"name": "dm", "inventory": {"apple": 5, "orange": 10}}]
    getBestShipment(orderDetail, warehouseStore)
    print("------------------------------------------------------------")