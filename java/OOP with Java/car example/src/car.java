public class car
{
    private String name;
    private String color;
    private int doors;
    private engine engine ;

    public car(String name,String color ,  int doors ,engine engine )
    {
        this.name = name;
        this.color = color;
        this.doors = doors;
        this.engine = engine;
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

    public int getDoors() {
        return doors;
    }

    public void setDoors(int doors) {
        this.doors = doors;
    }

    public engine getEngine() {
        return engine;
    }

    public void setEngine(engine engine) {
        this.engine = engine;
    }
}
