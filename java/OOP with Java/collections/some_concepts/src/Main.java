public class Main {
    public static void main(String[] args) {

        //static keyword
        test test1 = new test("white");
        test.name = "wesam";
        System.out.println(test.getName());
        test.print();


    }
}