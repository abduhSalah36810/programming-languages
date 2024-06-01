public class innerclasses

{
    private class innerclass
    {
        // you can always have access to the private fields and methods
        // inside the main class
        private String name;


        public innerclass(String name) {
            this.name = name;
        }

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }
    }
}
