import 'dart:math';

void main() {
  print(maxNumbers(4, 5));
  print(daysInMonth(6));
  print(gcd(40, 40));
}

/*1*/
int maxNumbers(int x, int y) {
  return max(x, y);
}

/*2*/
int daysInMonth(int month) {
  switch (month) {
    case 1:
      return 31;
    case 2:
      return 28;
    case 3:
      return 31;
    case 4:
      return 30;
    case 5:
      return 31;
    case 6:
      return 30;
    case 7:
      return 31;
    case 8:
      return 31;
    case 9:
      return 30;
    case 10:
      return 31;
    case 11:
      return 30;
    case 12:
      return 31;
    default:
      return -1;
  }
}

/*7*/
int gcd(int a, int b) {
  while (a != b) {
    if (a > b) {
      a = a - b;
    } else {
      b = b - a;
    }
  }
  return a;
}