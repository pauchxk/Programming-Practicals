/*import 'dart:math';

void main(List<String> arguments) {
  int passlength = int.parse(arguments[0]);
  print(password(passlength));
}

String password(int input) {
  String fullpass = '';
  for (int i = 1; i <= input; i++) {
    var passnum = Random().nextInt(93) + 33;
    fullpass += String.fromCharCodes([passnum]);
  }
  return fullpass;
}*/

import 'dart:math';

void main(List<String> arguments) {

  int passlength = 8; // Default value

  if (arguments.isNotEmpty) {
    int length = int.parse(arguments[0]);

    if (length > 0) {
      passlength = length;

    }
  }

  print(password(passlength));
}

String password(int input) {

  String fullpass = '';

  for (int i = 0; i < input; i++) {

    var passnum = Random().nextInt(93) + 33;
    fullpass += String.fromCharCode(passnum);

  }
  
  return fullpass;
}