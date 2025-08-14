import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


#Numpy

# array = np.array([1,2,3,4,5,])
# print(array)
# print(array[1])
# print(array[1:])
# print(array[:-2])
# print(type(array))


# mul_array = np.array([[[[1,2,3],
#                       [4,5,6],
#                       [7,8,9]],
#                      [[1,2,3],
#                       [4,5,6],
#                       [7,8,9]],
#                      [[1,2,3],
#                       [4,5,6],
#                       [7,8,9]]]])
# print(mul_array)
# print("---------------------------")
# print(mul_array[0])
# print(mul_array[0, 1])
# print("---------------------------")
# print(mul_array[1: ,0])

# print(mul_array.shape)
# print(mul_array.ndim)
# print(mul_array.size)



# lst_1 = np.array([1,2,3])
# lst_2 = np.array([4,5,6])
# print(lst_1 * lst_2)


# all_zeroes = np.zeros((3,3))
# print(all_zeroes)


# all_1 = np.full((3, 3), 0)
# print(all_1)


# random_array = np.random.randint(10, size=(3,3))
# print(random_array)


# array = np.arange(0, 11, 2)
# print(array)



# array_1 = np.array([1, 2, 3])
# number = 4
# print(array_1 * number)





#Pandas

#Series:
# scores = pd.Series(
#                    [18, 20, 15, 17],
#                    index= ["Ali", "Sara", "Reza", "Nika"]
#                    )
# print(scores)



#DataFrames:
# scores = {
#     "Ali" : [18, 14, 12, 13],
#     "Sara" : [11, 10, 12, 15],
#     "Reza" : [20, 9, 19, 16],
#     "Nika" : [17, 18, 11, 20]
# }
# df = pd.DataFrame(scores)
# print(df)



# math_scores = {
#     "name": ["Ali", "Sara", "Reza", "Maryam",
#              "Nima", "Ava", "Omid", "Fatemeh",
#              "Hassan", "Laleh", "Kia", "Pari",
#              "Shahab", "Neda", "Aria", "Mina"],
#     "score": [18, 14, 12, 13,
#               11, 10, 12, 15,
#               20, 9, 19, 16,
#               17, 18, 11, 20]
# }
# df = pd.DataFrame(math_scores)
# # under_18 = df[df["score"] < 18]
# # under_18 = under_18.reset_index(drop=True)
# # print(under_18)
# df["status"] = np.where(df["score"] < 10, "Failed", "Passed")
# print(df)




#Matplotlib

# x_data = np.random.random(50) * 100    #50 values beetween 0 and 1 * 100  -> 100 values for the x axes
# y_data = np.random.random(50) * 100    #same thing for y
# plt.scatter(x_data,y_data, marker="*")
# plt.show()



# years = [2006, 2007, 2008, 2009, 2010, 2011, 2012]
# weights = [50, 53, 49, 54, 58, 59, 61]
# plt.plot(years, weights)
# plt.xticks(years)
# plt.title("Ali weight in 3 years")
# plt.xlabel("Years")
# plt.ylabel("weights")
# plt.show()



# chocolate_milk = [100, 200, 80, 90, 300]
# milk = [30, 50, 10, 90, 100]
# strawberry_milk = [120, 300, 500, 300, 90 ]
# plt.plot(chocolate_milk, label="chocolate milk")
# plt.plot(milk, label="milk")
# plt.plot(strawberry_milk, label="strawberry milk")
# plt.legend()
# plt.show()



# poupularity_df = pd.DataFrame({
#     "language" : ("python", "c++", "java", "c#"),
#     "votes"    : (100, 40, 80, 20)
# })
# plt.pie(
#     poupularity_df["votes"],
#     labels=poupularity_df["language"],
#     autopct="%.2f%%"
#     )
# plt.show()



# poupularity_df = pd.DataFrame({
#     "language" : ("python", "c++", "java", "c#"),
#     "votes"    : (100, 40, 80, 20)
#     })
# plt.bar(
#     poupularity_df["language"],
#     poupularity_df["votes"],
#     color="blue",
#     align="edge"
#     )
# plt.show()



# ages = np.random.normal(20, 1.5, 1000)    #creats random samples from a normal (gaussian) distribution, which looks like a bell
# plt.hist(ages,bins=20)
# plt.show()



# random_xnums = np.random.random(50)   
# random_ynums = np.random.random(50) 
# random_ages = np.random.normal(30, 2, 100)
# plt.figure(1)
# plt.scatter(random_xnums, random_ynums)
# plt.figure(2)
# plt.hist(random_ages)
# plt.show()





