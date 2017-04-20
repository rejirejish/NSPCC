#import numpy as np
#import os
#from step_parser import *
#from CAD_processVstep import *
#from CAD_kernel import *
import sys
sys.path.append("/home/rejish/PhD/project/NSPCC/NSPCC_reader")


from step_reader import *
#from face_reader import *
#from eval_connection import *
#import sys
#import h5py
from read_writeh5 import *



name1 = "testing_ownM.stp"
#name1="m6.stp"
#name1="ubend_1.stp"
#name1="ubend_0-5.stp"
#name1="ubend_1-0-1-1.stp"
#name1 ="ubend_4-6.stp"
#name1="ubend_4.stp"
#name1="ubend_6.stp"
#name1="halfcylinder.stp"
#name1="sbend.stp"
#name1='testing_ownS.stp'
#name1='half_S.stp'
#name1='Final_S.stp'
#name1 = 'ubend.stp'
#name1='main2.stp'
#degree_u, degree_v, Mu, Mv, knots_u, knots_v, all_CP = step_read(name1, details=False)
#print all_CP
#name1 = 'M6_CADopt.stp'
#name1 = 'testing_new.stp'




#degree, edge_mulu, edge_knots, all_edges = step_edgeRead(name1)
#print 'edges', all_edges

#name1 = "testing_own07.stp"
#print ' '
#print len(all_edges[1])
#print len(all_edges[0])


patch_type, degree_u, degree_v,mul_u, mul_v, knots_u, knots_v, all_CP = step_surfaceRead(name1)
print 'hi', degree_u
no_of_patch = len(all_CP)

patch1 = all_CP
print all_CP


        
                   
get = create_NSPCCBRep(degree_u, degree_v,mul_u, knots_u, mul_v, knots_v, all_CP)   
                    
    


ID1 = -1
ID2 = -1
connecting = []




#print all_CP[0]





#patchID = ['12','13']
#get = get_step(patchID, name1, 1, degree_u, deg/ree_v, mul_u, mul_v, knots_u, knots_v, all_CP)
#free_patch = [0, 1, 3, 6]
free_patch = [0]
#print 'surface' , all_CP
#print 'number of patch', len(all_CP)
#print all_CP
#print all_CP
#print all_CP[1]




#design_type,degree_ud, degree_vd, Mud, Mvd, knots_ud, knots_vd, all_CPd = design_patch(patch_type, degree_u, degree_v, mul_u, mul_v, knots_u, knots_v, all_CP, free_patch)

#get = get_patchCon(all_CP, design_type ,details=True)



name11 = 'new_s.stp'
name22 = '/home/rejish/Reya_sep29/test/'+name11

no_of_axis = 1

#get = step_writer(name11, name22, no_of_axis, degree_u, degree_v, mul_u, mul_v, knots_u, knots_v, all_CP)
   



'''
p = 0

print degree_u
print np.size(all_CP[p])
get = get_edge(degree_u[p], degree_v[p], Mu[p], Mv[p], knots_u[p], knots_v[p], all_CP[p])
print ' Edge of single patch', len(get)
a = get[0]

print a[0]

com = eval_compare_patch(all_CP[3], all_CP[11])
'''
#check = connecting_patch(degree_u, degree_v, Mu, Mv, knots_u, knots_v, all_CP)
'''
6#patchID = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
patchID = [0,5]
#split = split_step(patchID, name1, 1, degree_u, degree_v, Mu, Mv, knots_u, knots_v, all_CP )
patchID = ['1','5']
get = get_step(patchID, name1, 1, degree_u, degree_v, Mu, Mv, knots_u, knots_v, all_CP)
'''
