
class illness():
    cls_name=""
    Questions_com={}
    Questions_unqi={}
    clicks=int(0)

        


ptsd=illness()
ptsd.Questions_com={}
ptsd.Questions_unqi={}
adhd=illness()
adhd.Questions_com={}
adhd.Questions_unqi={}
sleepness=illness()
sleepness.Questions_com={}
sleepness.Questions_unqi={}
stress=illness()
stress.Questions_com={}
stress.Questions_unqi={}
depression=illness()
depression.Questions_com={}
depression.Questions_unqi={}




def adder(results):
    dep={1,3,4,10,14}
    sleep={14,5,7,2,11}
    strs={5,12,8,10}
    ptsd={5,12,8,10}
    ADHD={14,12,8,2}
    print("asdasd")
    for c in results:
        print(c)
        if c in dep:
            depression.clicks+=1
            print("yes")
        if c in sleep:
            sleepness.clicks+=1
        if c in strs:
            stress.clicks+=1
        if c in ptsd:
            ptsd.clicks+=1
        if c in ADHD:
            adhd.clicks+=1