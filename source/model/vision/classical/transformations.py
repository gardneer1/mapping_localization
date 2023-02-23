import cv2





def homography(p0, p1):
    num_pts = p0.shape[0]
    if num_pts >=4:

        for i, (cur_pt, old_pnt) in enumerate(zip(p1,p0))
            x1, y1 = new.ravel()
            x, y = old.ravel()

            a_row=np.array([-x, -y, -1, 0, 0, 0, x*x1, y*x1, x1], \
                           [0, 0, 0, -x, -y, -1, x*y1, y*y1, y1])
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