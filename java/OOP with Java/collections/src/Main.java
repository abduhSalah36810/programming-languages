import jdk.swing.interop.SwingInterOpUtils;

import java.lang.reflect.MalformedParameterizedTypeException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args)
    {
        // in this lesson we are going to be taking about collections

        // 1- Array list
         /*
        ArrayList<String> names = new ArrayList<>();
        names.add("wesam");
        names.add("soma");
        names.add("wesamy");
        names.remove(1);
        System.out.println(names.contains("soma"));
        System.out.println(names.get(1));
        names.clear();
        System.out.println(names.isEmpty());
        System.out.println(names.indexOf("wesamy"));
        for (int i = 0 ; i < names.size() ; i++ ){
            System.out.println(names.get(i));
        }*/

        // 2- maps :
        Map<String,String> contacts = new HashMap<>();
        contacts.put("abdulrahman" , "01144444121");
        System.out.println(contacts.get("abdulrahman"));

        // for each loop :

        ArrayList<students> students = new ArrayList<>();
        students.add(new students("abdularhman" , 42022026));
        students.add(new students("mostafa" , 42022001));
        for (students s : students){
            System.out.println(s.getName()+ " : " + s.getId());
        }


    }
}