def dfs(image,x,y,oldcolor,newcolor):
    if(x<0 or x>=len(image) or y<0 or y>=len(image[0])or image[x][y]!=oldcolor):
        return
    image[x][y]=newcolor
    dfs(image,x+1,y,oldcolor,newcolor)
    dfs(image,x-1,y,oldcolor,newcolor)
    dfs(image,x,y+1,oldcolor,newcolor)
    dfs(image,x,y-1,oldcolor,newcolor)
def floodfill(image,sr,sc,newcolor):
    if image[sr][sc]==newcolor:
        return image
    dfs(image,sr,sc,image[sr][sc],newcolor)
    return image
if __name__=="__main__":
    image=[[1,1,1,0],[0,1,1,1],[1,0,1,1]]
    print("Original Image:")
    for row in image:
        print(" ".join(map(str,row)))
    sr,sc,newcolor=1,2,2
    floodfill(image,sr,sc,newcolor)
    print("After floodfill")
    for row in image:
        print(" ".join(map(str,row)))