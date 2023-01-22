#include <iostream>            //Leap Year Code
int main() {
  
  int year;
  std::cout<<"Enter Year\n";
  std::cin>>year;
  if (!(year> 1000 and year < 9999)){
    std::cout<<"Invalid Entry";
  }
  else if (year%4==0 and year%100!=0 or year%400==0 ){
      std::cout<<"Year is Leap";
  }
  else {
      std::cout<<"Not a leap year";
  }
   
 }
  