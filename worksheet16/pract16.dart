void main() {
  print(calculateArea(side1: 5, side2: 10));
  print(calculateArea(side1: 5));
  print(factorial(5));
}

int calculateArea({required int side1, int? side2}) => side1 * (side2 ?? 1);


void calculateAge(String name, int birthYear) {
  int currentYear = DateTime.now().year;
  int age = currentYear - birthYear;
  print("Hello, $name! You are $age years old.");
}

int factorial(int n) {
  int result = 1;
  for (int i = 1; i <= n; i++) {
    result = result * i;
  }
  return result;
}
