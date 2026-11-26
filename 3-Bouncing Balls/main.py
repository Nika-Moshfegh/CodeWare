def bouncing_ball(h, bounce, window):
    if not(h>0 and bounce>0 and bounce<1 and window<h):return -1
    
    count=1
    h = bounce*h
    while h > window:
        count+=2
        h=bounce*h

    return count

print(bouncing_ball(3,0.66,1.5))
        