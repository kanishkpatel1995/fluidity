Point(1) = {0,0,0,0.025};
Point(2) = {0,1,0,0.025};
Point(3) = {1,1,0,0.025};
Point(4) = {1,0,0,0.025};
Line(1) = {1,4};
Line(2) = {4,3};
Line(3) = {3,2};
Line(4) = {2,1};
Physical Line(7) = {1};
Physical Line(8) = {2};
Physical Line(9) = {3};
Physical Line(10) = {4};
Line Loop(11) = {2,3,4,1};
Plane Surface(12) = {11};
Physical Surface(13) = {12};
