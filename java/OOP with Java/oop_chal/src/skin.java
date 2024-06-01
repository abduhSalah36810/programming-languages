public class skin extends organ
{
    private String color;
    private int softness;

    public skin(String name, String medical_condition, String color, int softness) {
        super(name, medical_condition);
        this.color = color;
        this.softness = softness;
    }

    @Override
    public void getdetails() {
        super.getdetails();
        System.out.println("skin color : " + this.getColor());
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public int getSoftness() {
        return softness;
    }

    public void setSoftness(int softness) {
        this.softness = softness;
    }
}
