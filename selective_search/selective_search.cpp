#include "opencv2/ximgproc/segmentation.hpp"
#include "opencv2/highgui.hpp"
#include "opencv2/core.hpp"
#include "opencv2/imgproc.hpp"
#include <iostream>

using namespace std;
using namespace cv;

static void help() {
	cout << "Usage: " << endl;
	cout << "./ssearch input image (f|q)" << endl;
	cout << "f = fast, q = quality" << endl;
	cout << "Use l to display less rects..." << endl;
	cout << "...m to display more rects..." << endl;
	cout << "...x to quit." << endl;
}

int main(int argc, char** argv) {
	
	if (argc < 3) {
		help();
		return -1;
	}

	// Speed-up using multi-threads
	setUseOptimized(true);		// enable the optimized code
	setNumThreads(4);

	Mat img = imread(argv[1]);
	
	//resize
	int newHeight = 200;
	int newWidth = img.cols * newHeight / img.rows;
	resize(img, img, Size(newWidth, newHeight));

	// Create Selective Search Segmentation Object
	//                  with defautl parameter 
	Ptr<ximgproc::segmentation::SelectiveSearchSegmentation> ss =
		ximgproc::segmentation::createSelectiveSearchSegmentation();
	ss->setBaseImage(img);

	// "f" mode
	// Switch to fast but low recall Selective Search method
	if (argv[2][0] == 'f') {
		ss->switchToSelectiveSearchFast();
	}
	// "q" mode
	// Switch to high recall but slow Selective Search method
	else if (argv[2][0] == 'q') {
		ss->switchToSelectiveSearchQuality();
	}
	else {
		help();
		return -2;
	}

	// run Selective Search Segmentation on input image
	vector<Rect> rects;
	ss->process(rects);

	cout << "Total Number of Region Proposals : " <<
		rects.size() << endl;

	// number of region proposals to show
	int numShowRects = 100;
	// increment to increase/decrease total number of 
	// region proposals to be shown
	int increment = 50;

	while (1) {
		// create a copy of original image
		Mat dest = img.clone();

		// iterate over all the region proposals
		for (int i = 0; i < rects.size(); i++) {
			if (i < numShowRects) {
				rectangle(dest, rects[i], Scalar(255,0,0));
			}
			else {
				break;
			}
		}

		// show output
		imshow("SELECTVIE SEARCH RESULT", dest);

		// record the key press
		int k = waitKey();

		// "m (more) " is pressed
		if (k == 'm') {
			// increase total number of rectangles to show 
			numShowRects += increment;
		}
		// "l (less)" is pressed
		else if (k == 'l' && numShowRects > increment) {
			// decrease total number of rectangles
			numShowRects -= increment;
		}
		// "q" is pressed
		else if (k == 'x') {
			break;
		}
	}
	return 0;
}