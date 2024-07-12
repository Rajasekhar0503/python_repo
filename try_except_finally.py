try:
    print('raja')
    print(10/0)
except ZeroDivisionError:
    print('guru')
finally:
    print('mohan')

'''try:
    print('outertry')
    print(10/0)
    try:
        print('innertry')
    except:
        print('innerexcept')
    finally:
        print('innerfinally')
except:
    print('outerexcept')
finally:
    print('outerfinally')'''

'''try:
    print('raja')
    #print(10/0)
except:
    print('guru')
else:
    print('chinna')
finally:
    print('mohan')'''