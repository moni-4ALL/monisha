interface rectangle
{
int rect_length=10;int rect_breadth=20;
public void area();
}
interface triangle
{
int tri_breadth=10;int tri_height=20;
public void area();
}
class Shapes implements rectangle,triangle
{
public void area();
{
System.out.println("Length="+rect_length+"Breadth="+rect_breadth);
int area=int rect_length*int rect_breadth;
System.out.println("Area of rectangle="+area_rect);
System.out.println("Breadth="+tri_breadth+"Height="+tri_height);
int area=(int tri_breadth*int height)/2;
System.out.println("Area of triangle="+area_tri);
}
public static void main(String []args)
{
Shapes obj=newShapes();
obj.area();
}
}