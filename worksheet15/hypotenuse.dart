import 'dart:io';
import 'dart:math';

void main() {
  print('Enter length of first side:');
  String? input1 = stdin.readLineSync();
  print('Enter length of second side:');
  String? input2 = stdin.readLineSync();
  int x = int.parse(input1!);
  int y = int.parse(input2!);
  print('The hypotenuse is ${hypotenuseOfTriangle(x, y)}');
}

num hypotenuseOfTriangle(int x, int y) {
  num hypotenuse = sqrt(pow(x, 2) + pow(y, 2));
  return hypotenuse;
}
