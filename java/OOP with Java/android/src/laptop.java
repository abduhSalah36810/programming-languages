public class laptop
{
       private String Brand;
       private String color;
       private int RAM_size;

    public laptop(String brand, String color, int RAM_size) {
        Brand = brand;
        this.color = color;
        this.RAM_size = RAM_size;
    }

    public void shutdown (){
           System.out.println("shutting down ....");
       }
       public void setBrand (String brand){
           this.Brand = brand;
       }
       public String getBrand (){
           return this.Brand;
       }

       public String getColor() {
        return color;
    }

      public void setColor(String color) {
        this.color = color;
    }

    public int getRAM_size() {
        return RAM_size;
    }

    public void setRAM_size(int RAM_size) {
        this.RAM_size = RAM_size;
    }
}
