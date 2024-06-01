public class Main {
    public static void main(String[] args) {
     engine engine = new engine("renault" , 8000 );
     car mercedes = new car("mercedes AMG" , "Silver", 4 , engine );
        System.out.printf(mercedes.getName());


    }
}