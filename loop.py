# favorites = ["Creme Brulee", "Apple Pie","Churros","Tiramisu","Chocolate Cake"]

# # for idx, item in enumerate(favorites):
# #     print(idx, item)

# # count = 0

# # while count < len(favorites):
# #     print("I like this desert", favorites)
# # #     count += 1

# # for dessert in favorites:
# #     if dessert == "Churros":
# #         print("Yes! one of my favorite desserts is", dessert)
        

# # for dessert in favorites:
# #     if dessert == "Churros":
# #         print("Yes! one of my favorite desserts is", dessert)
# #         continue
# #     else:
# #         print("No sorry, that dessert is not on my list")            


# for dessert in favorites:
#     if dessert == "Churros":
#         print("Yes! one of my favorite desserts is", dessert)
#         continue
#     else:
#         print("Other desserts i like are", dessert)  

# list1 = [1,2,3,4,5,6,7,8,9]
# list2 = [1,2,3,4,5,6,7,8,9]

# count = 0

# for x in list1:
#     count += 1
    

# for y in list2:
#     count += 1    
    

# print(count)    
import time
start_time = time.time()

for i in range(1):
    for j in range(10):
      print(0, end= " ")
    print() 
    
print(round(time.time() - start_time))