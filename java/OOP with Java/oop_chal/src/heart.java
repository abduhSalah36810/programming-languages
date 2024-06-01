public class heart extends organ
{
    private int heart_rate;
    public heart(String name, String medical_condition , int heart_rate) {
        super(name, medical_condition);
        this.heart_rate = heart_rate;
    }
    public void change_heart_rate(int number){
        setHeart_rate(number);
        System.out.println(getHeart_rate());
    }

    @Override
    public void getdetails() {
        super.getdetails();
        System.out.println("rate : " + this.getHeart_rate());
    }

    public int getHeart_rate() {
        return heart_rate;
    }

    public void setHeart_rate(int heart_rate) {
        this.heart_rate = heart_rate;
    }
}
