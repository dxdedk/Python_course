vid_1=12

def global_func():
    print('')

print(vid_1)

def func_two():
    vid_1 = "Local value"
    print(vid_1)

func_two()

print(vid_1)

def func_three():
    global vid_1
    vid_1="Local to global"

func_three()
print(vid_1)