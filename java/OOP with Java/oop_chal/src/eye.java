public class eye extends organ
{
    private String color;
    private boolean is_open;
    public eye(String name, String medical_condition , String color, boolean is_open) {
        super(name, medical_condition);
        this.color = color;
        this.is_open = is_open;



    }

    @Override
    public void getdetails() {
        super.getdetails();
        System.out.println("color : " + this.color);
    }

    public void open(){
        this.setIs_open(true);
        System.out.println(this.getName() + "opened");
    }
    public void close(){
        this.setIs_open(false);
        System.out.println(this.getName() + "closed");
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public boolean isIs_open() {
        return is_open;
    }

    public void setIs_open(boolean is_open) {
        this.is_open = is_open;
    }
}
