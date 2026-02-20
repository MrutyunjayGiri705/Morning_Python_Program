import os
folders=os.listdir("data")
# print(folders)
# for f in folders:
#     print(f)
for f in folders:
    print(f)
    print(os.listdir(f"data/{f}"))