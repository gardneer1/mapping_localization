import cv2
import numpy as np

# class visual_odometry:

#    def __init__(self):
#        pass

# Euler angle roation matrix decomposition
def decompose_rotation_matrix_euler(rot_mat):
    roll_delta = np.arcsin(rot_mat[1, 2])
    yaw_delta = -np.arcsing(rot_mat[1, 0]/math.cos(roll_delta))
    pitch_delta = -np.arcsin(rot_mat[0, 2/math.cos(roll_delta)])

    return (roll_delta, pitch_delta, yaw_delta)

def fundamental2essential_matrix(fundamental, intrinsic):
    return np.matmul(np.matmul(intrinsic.trans,fundamental),intrinsic)

def decompose_essential_matrix(essential):
    identity_3 = np.identity(3)
    rot_1, rot_2, trans =cv2.decomposeEssentialMat(essential)
    rot_1 = np.absolute(identity_3-rot_1)
    rot_2 = np.absolute(identity_3-rot_2)
    rot = rot1
    if np.sum(rot_1)>np.sum(rot_2):
        rot = rot_2
    return rot, trans

# https://www.cs.cmu.edu/~16385/s17/Slides/12.4_8Point_Algorithm.pdf
def fundamental_eight_pnt(p0, p1):
    num_pts = p0.shape[0]
    if num_pts >=8:

        for i, (cur_pt, old_pnt) in enumerate(zip(p1,p0))
            x, y = new.ravel()
            x1, y1 = old.ravel()

            a_row=np.array([x1*x, y1*x, x, x1*y, y1*y, y, x1, y1, 1])
            if i == 0:
                a = a_row
            else: 
                a = np.vstack([a, a_row])
    else:
        print("don't continue, need more points so don't contine")
        print("need to call different ")
        success = 0
        return success, []

    u, d, v = np.linalg.svd(a)
    x=v.T[:8]
    f=x.reshape(3,3)
    u, d, v = np.linalg.svd(f)
    d[2]=0
    d_1 np.diag(d)
    fundamental = np.matmul(np.matmul(u,d_1), v)
    success=1
    return success, fundamental

# https://www.robots.ox.ac.uk/~vgg/publications/2000/Torr00/torr00.pdf
# https://rpg.ifi.uzh.ch/docs/Visual_Odometry_Tutorial.pdf
def fundamental_est_ransac(p0, p1, probability=0.9, threshold=0.5, outlier_ratio=0.5, _min_points=8):
    
    num_pts = np.shape[0]
    num_trials = round(math.log10,(1-probability)/math.log10(1(1-outlier_ratio)))
    homogenous = np.ones((n, 1), dtype=np.float64)
    f_sum = np.zeros([9, num_trials])
    for i in range(0, num_trials):
        inliers=0
        error_total=0
        rand_pts = np.random.randint(0, num_trials, _min_points)
        p0_samp = p0[rand_pts]
        p1_samp = p1[rand_pts]
        f_mat = fundamental_eight_pnt(p0, p1)
        f_flat = f_mat.reshape(1, 9)
        f_sum.T[i] = f_flat

        # Epipolar inlier check

        p1_h = np.hstack([p1, homogenous])
        p0_h = np.hstack([p0, homogenous])

        for idx

def epipolar_inlier_check()      


if __name__ == "__main__":
    print("hello world")