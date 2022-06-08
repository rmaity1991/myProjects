package JavaProgramming.Polymorphism;

/*
 * Method Overloading: changing data type of arguments
 * In this example, we have created two methods that differs in data type
 * . The first add method receives two integer arguments and second add method
 * receives two double arguments.
 */
class Adder {
    static int add(int a, int b) {
        return a + b;
    }

    static double add(double a, double b) {
        return a + b;
    }
}

class TestOverloading2 {
    public static void main(String[] args) {
        System.out.println(Adder.add(11, 11));
        System.out.println(Adder.add(12.3, 12.6));
    }
}