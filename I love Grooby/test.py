import this

def most_frequent_unigram(s):
    unique_unis = set(list(s))
    most_freq_uni = s[0]
    max_count = 1
    for unigram in unique_unis:
        if unigram == " ":
            continue 
        if s.count(unigram) > max_count:
            most_freq_uni = unigram
            max_count = s.count(unigram)
    return most_freq_uni, max_count 
        
def most_frequent_bigram(s):
    words = s.split(" ")
    bigrams = []
    for word in words:
        for i in range(len(word) - 1):
            bi = word[i] + word[i+1]
            if bi not in bigrams:
                bigrams.append(bi)
                
    most_freq_bi = bigrams[0]
    max_count = 1

    bigrams = list(map(lambda x: (x, s.count(x)), bigrams))
    return max(bigrams, key = lambda x: x[1])

    for bigram in bigrams:
        if s.count(bigram) > max_count:
            most_freq_bi = bigram
            max_count = s.count(bigram)
    return most_freq_bi, max_count


def contains(num1, num2):
    num1, num2 = str(num1), str(num2)
    l = len(num2)
    for i in range(len(num1)- l): 
        possible_string = num1[i:i+l]
        if possible_string == num2:
            return True 
    return False

#print(contains(123, 12))

def count_change(amt, lst):
    if amt == 0:
        return 1
    elif not lst or amt < 0:
        return 0
    else:
        return count_change(amt - lst[-1], lst) + count_change(amt, lst[:-1])


def cc_limited(n,d):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif d == {}:
        return 0
    else:
        max_v = max(d.keys())
        new_d = d.copy()
        new_d[max_v] -= 1
        if new_d[max_v] == 0:
            del new_d[max_v]
        del d[max_v]
        ans = cc_limited(n-max_v, new_d) + cc_limited(n, d)
        return ans 

#print(cc_limited(100, {1:30, 5:20, 10:5, 20:10, 50:1}))

a = 5/90 * (7.5)
b = 9/90 * (10.5)
c = 14/90 * (13.5)
d = 14/90 * (13.5)
e = 17/90 * (39 /2)
f = 9/90 * (45/2)
g = 11/90 * ( (24+27) / 2)
h = 7/90 * (57/2)
i = 3/90 * (63/2)

print(sum([a,b,c,d,e,f,g,h,i]))
##print(sum((5,9,14,14,17,9,11,7,3)))

def elevator(n):
    shortest = 10

    def helper(level, path):
        nonlocal shortest
        print(path)
        if level in path:
            return #lmao this would mean you went back to the same floor
        else:
            if level == n:
                if len(path) < shortest:
                    shortest = len(path)
            else:
                if level - 11 > 0:
                    new_path = path.copy()
                    new_path.append(level)
                    helper(level-11, new_path)
                if level+8 <= 65: 
                    newer_path = path.copy()
                    newer_path.append(level)
                    helper(level+8, newer_path)
                    
    helper(1, [])

    return shortest

#print(elevator(60))


def elevator(n):
    memo  = {}
    def helper(level, path):
        if level in memo:
            if len(memo[level]) <= len(path):
                return
            else:
                memo[level] = path

        if level == n:
            return len(path)
        else:
            if level + 8 not in path and level + 8 not in memo and level + 8 <= 65:
                new_path = path.copy()
                new_path.append(level)
                helper(level+8, new_path)
            if level - 11 not in path and level - 11 not in memo and level -11 > 0:
                new_path = path.copy()
                new_path.append(level)
                helper(level - 11, new_path)
                
                
        
##    
##    helper(1, [])
##    print(memo)
##
##print(elevator(6))

def fk1010(lst1, lst2):
    ## sums the items inside 2 lists
    ans = 0
    for i in range(lst1):
        ans += lst1[i]

    for i in range(lst2):
        ans += lst2[i]
    return ans


def tiowseng(plot, index, m):
    scores = []


    for i in range(1, m+1): #this i will determine how far to move left and/or right
        for j in range(i//2 - 1): #this is like the move left and move back to original pos, can only be max i//2
##        # start by moving left then back then right
##            left = 0
##            if index-j >= 0:
##                left += sum(plot[index:index-j:-1])
##            remainder = i - (j*2)
##            if index + remainder <= len(plot) - 1:
##                left += sum(plot[index + 1:index + remainder + 1]) #cannot overcount what you've already stepped on
##
##            right = 0
##
##            if index + j <= len(plot) - 1:
##                right += sum(plot[index:index + j])
##
##            if index - remainder >= 0:
##                right += sum(plot[index-1: index-remainder - 1:-1])
##
##            scores.extend([left, right])
            remainder = i - (j*2)
            print(remainder)
            left_patch  = sum(plot[ max(0, index - remainder) : min(len(plot), index + j + 1)])

            right_patch = sum(plot[ max(0, index - j) : min(len(plot), index + remainder + 1)])

            scores.extend([left_patch, right_patch])

    print(scores)
    return max(scores)

#print(tiowseng( (2, 3, 7, 5, 1, 3, 9), 1, 2))


a = [0,1,2,3,4,5,6]
for i in a:
    if i % 2:
        continue
    else:
        a.remove(i)
#print(a)

def count_change(amt, denom):
    if amt < 0 or len(denom) == 0:
        return 0
    elif amt == 0:
        return 1
    else:
        return count_change(amt - denom[0], denom) + count_change(amt, denom[1:])

##print(count_change(100, [5,10,25,50]))
##print(count_change(100, [50,25,10,5]))

def check(node):
    if left(node) == operator:
        l = check(left(node))
    elif type(left(node)) == int:
        l = False
    elif left(node) == None:
        l = True 

    if right(node) == operator:
        r = check(right(node))
    elif type(right(node)) == int:
        r = False

    elif right(node) == None:
        r = True

    return l or r

def insert(thing, node):
    if left(node) == None: #im assuming this is a branch
        left(node) = thing
    elif type(left(node)) == int:
        return 
    else:
        if type(left(node)) == operator:
            if check(left(node)):
                insert(thing, left(node))
            else:
                continue


    if right(node) == None:
        right(node) = thing
    elif type(right(node)) == int:
        return
    else: #the only way left is that the right node is an operator and you MUST be able to go down it!
        if type(right(node)) == operator:
            insert(thing, right(node))
        
            
        
print(1280678415822214057864524798453297819181910621573945477544758171055968245116423923 ** 0.5)
                
            








    
            
        
            
