#include "ros/ros.h"
#include "std_msgs/String.h" //not needed now, may need later?
#include <iostream>
using namespace std;
#include "math.h"  

float q0, q2, q3;
float cosine, sine;
float c12, s12; 
float transform_matrix[4][4];

float l1 = 1;
float l2 = 1;


int main(){
  cout<< "Joint 1: ";
  cin>> q0;

  cout<< "Joint 2: ";
  cin>> q2;

  cout<< "Joint 3: ";
  cin>> q3;

  cosine = cos(q0);
  sine = sin(q0);


  float transform_matrix[4][4] = {{c12, -s12, 0, l2*c12 + l2*cosine}, {s12, c12, 0, l2*s12 + l2*sine}, {0, 0, 1, q3+l1}, {0, 0, 0, 1}};
  
  for(int x=0;x<4;x++)  // loop 4 times for four lines
    {
        for(int y=0;y<4;y++)  // loop for the four elements on the line
        {
            cout <<transform_matrix[x][y] << ", ";  // display the current element out of the array
        }
    cout<<endl;  // when the inner loop is done, go to a new line
    }
    
    cout<< "x: " <<transform_matrix[0][3] <<endl;
    cout<< "y: " <<transform_matrix[1][3] <<endl;
    cout<< "z: " <<transform_matrix[2][3] <<endl;
    
    return 0;  // return 0 to the OS.
}
