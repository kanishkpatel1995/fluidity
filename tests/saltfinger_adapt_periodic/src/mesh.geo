i=0.01;
Point(1) = {0,0,0,i};
Point(2) = {1, 0, 0,i};
Point(3) = {1, 2, 0,i};
Point(4) = {0, 2, 0,i};
Line(1) = {4, 3};
Line(2) = {3, 2};
Line(3) = {2, 1};
Line(4) = {1, 4};
Line Loop(5) = {1, 2, 3, 4};
Plane Surface(6) = {5};
Physical Line(7) = {1};//t
Physical Line(8) = {3};//b
Physical Line(9) = {4};//l
Physical Line(10) = {2};//r
Physical Surface(11) = {6};
