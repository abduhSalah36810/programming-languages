import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        person patient = new person("ahmed" , 19);
     eye eye1 = new eye("right eye" , "normal" , "blue" , true);
     eye eye2 = new eye("left eye" , "normal" , "blue" , true);
     heart Heart = new heart("Heart" , "slow" , 58);
     stomach stomach = new stomach("Stomach", "PUD" , false);
     skin skin = new skin("skin", "burned" , "white" , 40);

        System.out.println("name : " + patient.getName());
        System.out.println("age : " + patient.getAge());

        Scanner scanner = new Scanner(System.in);

        boolean shouldfinish = false;
        while(!shouldfinish){
            System.out.println("choose an organ :" +
                    "\n\t 1. right eye" +
                    "\n\t 2. left eye" +
                    "\n\t 3. Heart" +
                    "\n\t 4. stomach" +
                    "\n\t 5. skin" +
                    "\n\t 6. Quit");
            int choice = scanner.nextInt();
            switch (choice)
            {
                case 1 :
                    eye1.getdetails();
                    if (eye1.isIs_open())
                    {
                        System.out.println("\t\t 1. close it");
                        if (scanner.nextInt() == 1){
                            eye1.close();
                        } else {
                            continue;
                        }
                    }
                    else {
                        System.out.println("\t\t 1. open it");
                        if (scanner.nextInt()== 1 ) {
                            eye1.open();

                        }else
                        {
                            continue;
                        }

                    }
                    break;


                case 2 :
                    eye2.getdetails();
                    if (eye2.isIs_open())
                    {
                        System.out.println("\t\t 1. close it");
                        if (scanner.nextInt() == 1){
                            eye2.close();
                        } else {
                            continue;
                        }
                    }
                    else {
                        System.out.println("\t\t 1. open it");
                        if (scanner.nextInt()== 1 ) {
                            eye2.open();

                        }else
                        {
                            continue;
                        }

                    }
                    break;
                case 3:
                    Heart.getdetails();
                    System.out.println("\t\t 1.change the heart rate ");
                    if (scanner.nextInt()==1){
                        System.out.println("enter the new heart rate");
                        int newheartrate = scanner.nextInt();
                        Heart.setHeart_rate(newheartrate);
                    }else {
                        continue;
                    }
                    break;
                case 4:
                    stomach.getdetails();
                    System.out.println("\t\t 1. digest");
                    if (scanner.nextInt()==1){
                        stomach.digest();
                    }else{
                        continue;
                    }
                    break;
                case 5:
                   skin.getdetails();
                   break;

                default:
                    shouldfinish =true;
                    break;

            }


        }



    }
}