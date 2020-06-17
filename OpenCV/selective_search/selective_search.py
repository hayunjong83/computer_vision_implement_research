#!/usr/bin/env python
'''
Usage:
    ./selctive_search.py input_image (f|q)
    f = fast, q = quality
Use 'l' to display less rects, 'm' to display more rects,
'x' to exit
'''
import sys
import cv2

if __name__ == '__main__':
    if len(sys.argv) < 3 :
        print(__doc__)
        sys.exit(1)

    # Speed-up using multi-threads
    cv2.setUseOptimized(True)
    cv2.setNumThreads(4)

    img = cv2.imread(sys.argv[1])
    # resize
    newHeight = 200
    newWidth = int(img.shape[1] * newHeight / img.shape[0])
    img = cv2.resize(img, (newWidth, newHeight))

    # create Selective search Segmentation Object
    #                   with default parameter
    ss = cv2.ximgproc.segmentation.createSelectiveSearchSegmentation()
    ss.setBaseImage(img)

    # "f" mode
    # Switch to fast but low recall Selective Search method
    if ( sys.argv[2] == 'f'):
        ss.switchToSelectiveSearchFast()

    # "q" mode
    # Switch to high recall but slow Selective Search method
    elif ( sys.argv[2] == 'q'):
        ss.switchToSelectiveSearchQuality()

    else:
        print(__doc__)
        sys.exit(1)

    # run Selective Search segmentation on input image
    rects = ss.process()
    print('Total Number of Region Proposals:{}'.format(len(rects)))

    # number of region proposals to show
    numShowRects = 100
    # increment to increase/decrease total number of region proposals to be shown
    increment = 50

    while True:
        dest = img.copy()

        # iterate over all the region proposals
        for i, rect in enumerate(rects):
            if (i < numShowRects):
                x, y, w, h = rect
                cv2.rectangle(dest, (x,y), (x+w, y+h), (255,0,0), 1, cv2.LINE_AA)
            else:
                break
        
        # show output
        cv2.imshow("SELECTIVE SEARCH RESULT", dest)

        # record the key press
        k = cv2.waitKey(0) & 0xFF

        # 'm(more)' is pressed
        if  k == ord('m'):
            numShowRects += increment

        # 'l(less)' is pressed
        elif k == ord('l') and numShowRects > increment:
            numShowRects -= increment

        # 'x' is pressed
        elif k == ord('x'):
            break

    # close image show window
    cv2.destroyAllWindows()

