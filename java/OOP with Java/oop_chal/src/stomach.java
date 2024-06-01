public class stomach extends organ
{
    private boolean is_empty;
    public stomach(String name, String medical_condition , boolean is_empty) {
        super(name, medical_condition);
        this.is_empty = is_empty;
    }
    public void digest(){
        System.out.println("digesting began");
    }
    @Override
    public void getdetails() {
        super.getdetails();
        if(this.isIs_empty()){
            System.out.println("need food");
        }else
        {
            System.out.println("full");
        }
    }

    public boolean isIs_empty() {
        return is_empty;
    }

    public void setIs_empty(boolean is_empty) {
        this.is_empty = is_empty;
    }
}
