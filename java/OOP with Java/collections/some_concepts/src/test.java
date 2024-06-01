public class test
{
    public static String  name ;
    public static int age;
    public String skincolor;

    public test(String skincolor) {
        this.skincolor = skincolor;
    }
    public static void print(){
        System.out.println("printing.....");
    }
    public static String getName() {
        return name;
    }

    public static void setName(String name) {
        test.name = name;
    }

    public static int getAge() {
        return age;
    }

    public static void setAge(int age) {
        test.age = age;
    }

    public String getSkincolor() {
        return skincolor;
    }

    public void setSkincolor(String skincolor) {
        this.skincolor = skincolor;
    }
}

