import 'pract16.dart';

void main(List<String> arguments) {
  String name = arguments[0];
  int birthYear = int.parse(arguments[1]);
  calculateAge(name, birthYear);
}