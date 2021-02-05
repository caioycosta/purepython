##initial commit with prototypes of some operations
##pure python libraries: sqlalchemy, pg8000, suds

#creating matrixes
Z = ([ [0 for x in range(0,144)] for x in range(0,40)])

#matrix minima 
min([min(x) for x in Z]

# convolution
def convolve(Z, kernelX, center, GZx):    
    for row in range(0,len(Z)):
        for pix in range(0,len(Z[row])):
            acc = 0
            for Krow in range(0,len(kernelX)):
                for Kpix in range(0,len(kernelX[Krow])):
                    off_kx = Krow - center[0]
                    off_ky = Kpix - center[1]
                    if row+off_kx >= 0 and row+off_kx < len(Z) and pix+off_ky >= 0 and pix+off_ky < len(Z[row]):
                        try:
                            acc += Z[row+off_kx][pix+off_ky] * kernelX[Krow][Kpix]
                        except:
                            print (row, pix, off_kx, off_ky, Krow, Kpix)
                            raise                        
            GZx[row][pix] = acc  
            
# kmeans
mn = min([min([j for j in k ]) for k in Z])
mx = max([max([j for j in k ]) for k in Z])
ct = sum([sum([1 for j in k ]) for k in Z])
lst = [q for q in it.chain.from_iterable([[j for j in k ] for k in Z])]
clusters = [i for i in range(int(mn), int(mx)+1, (int(mx)-int(mn))  // 3)]
print(clusters)
for zz in range(0,15):    
    new_clusters = [(0,0) for i in clusters]
    for l in lst:
        cp = None
        for c in range(0, len(clusters)):
            if cp is None or abs(clusters[c] - l) < abs(clusters[cp] - l):
                cp = c
        new_clusters[cp] = ( (new_clusters[cp][0] * new_clusters[cp][1] + l) / (new_clusters[cp][1] + 1), new_clusters[cp][1] + 1 )    
    clusters = [p[0] for p in new_clusters]
    print(clusters)

boundaries = [None for i in clusters]
for l in lst:
    cp = None
    for c in range(0, len(clusters)):
        if cp is None or abs(clusters[c] - l) < abs(clusters[cp] - l):
                cp = c
    if boundaries[cp] is None:
        boundaries[cp] = (l,l)
    else:
        boundaries[cp] = (min(l, boundaries[cp][0]), max(l, boundaries[cp][1]) )
    
cl = [a for a in it.chain.from_iterable([ [ b[1] ] for b in boundaries])]
print(cl)      



#thresholding and others
#for row in range(0,len(GZ)):
#    for pix in range(0,len(GZ[row])):
#        GZ[row][pix] = 0 if GZ[row][pix] < cl[1] else 127
#            
#for row in range(0,1):
#    for pix in range(0,len(Z[row])):
#        Z[row][pix] = 0 
#
#
#for pix in range(0,len(GZ[0])):  
#    prim_pix = -1
#    for row in range(0, len(GZ)): 
#        if prim_pix < 0 and GZ[row][pix] > 0:
#            prim_pix = row
#        elif GZ[row][pix] > 0 and prim_pix >= 0:
#            GZ[row][pix] = 0
    #x = 0            
    #for row in range(0,len(GZ)):
    #    GZ[row][pix] = x
    #    x = x + 0.05
        #fpix = 0
        #if fpix == 0 and GZ[row][pix] > 0:
        #    fpix = row
        #if row > fpix:
        #    GZ[row][pix] = 0

    
#erosion
mtx = [[1],
       [1],
       [1]]
       
ct = (1,0)

for row in range(0,len(Z)):
    for pix in range(0,len(Z[row])):
        new_px = None
        for mtxrow in range(0, len(mtx)):
            for mtxpix in range(0, len(mtx[mtxrow])):
                offx = mtxpix - ct[1]
                offy = mtxrow - ct[0]
                if row+offy >= 0 and row+offy < len(Z) and pix+offx >= 0 and pix+offx < len(Z[row]):
                    new_px = Z[row+offy][pix+offx] if new_px is None else min(Z[row+offy][pix+offx], new_px)
        Ze[row][pix] = new_px
    #min per column
    for pix in range(0,len(Z[0])):  
    prim_pix = -1
    for row in range(0, len(Z)): 
        if prim_pix < 0 and Z[row][pix] > 0:
            prim_pix = row
        elif Z[row][pix] > 0 and prim_pix >= 0:
            Z[row][pix] = 0
