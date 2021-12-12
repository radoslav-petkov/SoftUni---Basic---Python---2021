# import java.util.Scanner;
#
# public
#
#
# class GrandpaStavri {
# public static void main(String[] args) {
# Scanner scanner = new Scanner(System.in );
#
# int days = Integer.parseInt(scanner.nextLine());
#
# double litersTotal = 0;
# double averageDegrees = 0;
# String outputRow3 = "";
#
# for (int i = 0; i < days; i++) {
# double liters = Double.parseDouble(scanner.nextLine());
# double degrees = Double.parseDouble(scanner.nextLine());
#
# litersTotal += liters;
# averageDegrees += liters * degrees;
# if (i == days - 1) {
# averageDegrees = averageDegrees / litersTotal;
# }
# }
# if (averageDegrees < 38) {
# outputRow3 = "Not good, you should baking!";
# } else if (averageDegrees <= 42) {
# outputRow3 = "Super!";
# } else {
# outputRow3 = "Dilution with distilled water!";
# }
# System.out.printf("Liter: %.2f%n",litersTotal);
# System.out.printf("Degrees: %.2f%n",averageDegrees);
# System.out.println(outputRow3);
# }
# }
#
#
#
