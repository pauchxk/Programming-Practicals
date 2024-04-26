void main() {
  //int x = 5;
  //int result = multiplyBy2(x);
  //print('Result: $result');
  int distance = 100;
  double time = 9.58;
  speedCalculator(distance, time);
  int x = 5;
  double y = 10;
  print(secret(x, y));
  typeConversion();
}

int multiplyBy2(int number) {
  return number * 2;
}

void speedCalculator(int distance, double time) {
  double speed = distance / time;
  print('Speed: $speed');
}

double secret(int x, double y) {
  x += 5;
  y /= 5;
  x ~/= 3;
  y *= 2;
  x++;
  double result = x * y;
  return result;
}

void typeConversion() {
  int i = 5;
  double d = 10.65;
  // to integer
  int dAsInt = d.toInt();
  int dFloor = d.floor();
  int dCeil = d.ceil();
  int dRounded = d.round();
  print("dAsInt: $dAsInt, dFloor: $dFloor, dCeil: $dCeil, dRounded: $dRounded");
  // to double
  double iAsDouble = i.toDouble();
  print("iAsDouble: $iAsDouble");
  // to string
  String iAsString = i.toString();
  String dAsString = d.toString();
  String dAsFixed = d.toStringAsFixed(1);
  print("iAsString: $iAsString, dAsString: $dAsString, dAsFixed: $dAsFixed");
  // from string
  i = int.parse(iAsString);
  d = double.parse(dAsString);
  print("i: $i, d: $d");
}