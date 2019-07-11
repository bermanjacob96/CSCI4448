#include <iostream>
 
using namespace std;

// Base class
class Shapes {
   public:
      void setWidth(int w) {
         width = w;
      }
      void setHeight(int h) {
         height = h;
      }
      void setRadius(int r) {
          radius = r;
      }
      void setCords(int x, int y, int z){
          xCord = x;
          yCord = y;
          zCord = z;
      }
      void setX(int x){
          xCord = x;
      }
      void setY(int y){
          yCord = y;
      }
      void setZ(int z){
          zCord = z;
      }
      
   protected:
      int width;
      int height;
      int radius;
      int xCord;
      int yCord;
      int zCord;
};

// Derived class
class Square: public Shapes {
   public:
      int getCords() { return (xCord, yCord, zCord); }
      int getX() { return (xCord); }
      int getY() { return (yCord); }
      int getZ() { return (zCord); }
      int getWidth() { return(width); }
};

class Circle: public Shapes {
   public:
      int getCords() { return (xCord, yCord, zCord); }
      int getX() { return (xCord); }
      int getY() { return (yCord); }
      int getZ() { return (zCord); }
      int getRadius() { return(radius); }
};

class Triangle: public Shapes {
   public:
      int getCords() { return (xCord, yCord, zCord); }
      int getX() { return (xCord); }
      int getY() { return (yCord); }
      int getZ() { return (zCord); }
      int getHeight() { return(height); }
};


int main(void) {
   Square sq;
   Circle cr;
   Triangle tr;
 
   sq.setWidth(5);
   sq.setX(5);
   sq.setY(10);
   sq.setZ(15);

   cr.setRadius(6);
   cr.setX(3);
   cr.setY(7);
   cr.setZ(12);

   tr.setHeight(5);
   tr.setX(6);
   tr.setY(11);
   tr.setZ(16);

   // Print
   cout << "Creating Database..." << endl;
   cout << "Three shapes in Database..." << endl;
   cout << "Circle at: "<< cr.getX() << ", " << cr.getY() << ", " << cr.getZ() << " with " << "radius: " << cr.getRadius() << endl;
   cout << "Square at: "<< sq.getX() << ", " << sq.getY() << ", " << sq.getZ() << " with " << "width: " << sq.getWidth() << endl;
   cout << "Triangle at: "<< tr.getX() << ", " << tr.getY() << ", " << tr.getZ() << " with " << "height: " << tr.getHeight() << endl;



   return 0;
}