public class animal
{
    private String name;
    private String color;
    private int legs;
    private boolean hastale;

    public animal(String name, String color, int legs, boolean hastale) {
        this.name = name;
        this.color = color;
        this.legs = legs;
        this.hastale = hastale;
    }
    public void eat (String food)
    {
        System.out.printf("Eating" + food);
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public int getLegs() {
        return legs;
    }

    public void setLegs(int legs) {
        this.legs = legs;
    }

    public boolean isHastale() {
        return hastale;
    }

    public void setHastale(boolean hastale) {
        this.hastale = hastale;
    }
}
