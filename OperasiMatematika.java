public class OperasiMatematika {

    // Method penjumlahan
    public static int penjumlahan(int a, int b) {
        return a + b;
    }

    // Method pengurangan
    public static int pengurangan(int a, int b) {
        return a - b;
    }

    // Method perkalian
    public static int perkalian(int a, int b) {
        return a * b;
    }

    // Method pembagian
    public static double pembagian(int a, int b) {
        return (double) a / b;
    }

    public static void main(String[] args) {

        int angka1 = 20;
        int angka2 = 5;

        System.out.println("Hasil Penjumlahan : " + penjumlahan(angka1, angka2));
        System.out.println("Hasil Pengurangan : " + pengurangan(angka1, angka2));
        System.out.println("Hasil Perkalian   : " + perkalian(angka1, angka2));
        System.out.println("Hasil Pembagian   : " + pembagian(angka1, angka2));
    }
}