import 'dart:io';
import 'dart:math';

void main() {
  pizzaOrder();
}

String getPizzaType() {
  print('What type of pizza do you want?');
  String? input = stdin.readLineSync();
  return input!;
}

int getPizzaSize() {
  print('Enter the diameter of the pizza:');
  String? input = stdin.readLineSync();
  return int.parse(input!);
}

double getPizzaPrice(int radius) {
  double pricePerSquareInch = 0.05;
  double area = pi * pow(radius / 2, 2);
  return area * pricePerSquareInch;
}

void pizzaOrder() {
  String pizzaType = getPizzaType();
  int pizzaSize = getPizzaSize();
  double pizzaPrice = getPizzaPrice(pizzaSize);
  print('A $pizzaSize inch $pizzaType pizza costs ${pizzaPrice.toStringAsFixed(2)}');
}