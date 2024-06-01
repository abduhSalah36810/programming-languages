public class organ
{
    private String name;
    private String medical_condition;

    public organ(String name, String medical_condition) {
        this.name = name;
        this.medical_condition = medical_condition;

    }
    public void getdetails(){
        System.out.println("Name : " + this.getName());
        System.out.println("medical condition: " + this.getMedical_condition());
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getMedical_condition() {
        return medical_condition;
    }

    public void setMedical_condition(String medical_condition) {
        this.medical_condition = medical_condition;
    }
}
