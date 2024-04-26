void main() {
  Person alice = Person('Alice', 20);
  alice.age = 21;
  print('Alice is ${alice.age} years old');
  print('Next year, Alice will be ${alice.ageNextYear()} years old.');
  print('Alice has a valid name: ${alice.hasValidName()}');
  print(alice);
}

class Person {
  String name = 'unknown';
  int age = 0;

  Person(this.name, this.age) {
    this.name = name;
    this.age = age;
  }

  int ageNextYear() {
    return age + 1;
  }

  bool hasValidName() {
    if (name.length > 2 && name.length < 100) {
      return true;
    } else {
      return false;
    }
  }

  String toString() {
    return 'Person(name: $name, age: $age)';
  }
}

class Student {
  String? name;
  int level = 4;
  String? _phoneNumber;

  Student(this.name, this._phoneNumber);

  void graduate() {
    level++;
  }

  String greet() => 'Hello, $name!';

  String get phoneNumber {
    String lastFourDigits = _phoneNumber!.substring(6);
    return '***-***-$lastFourDigits';
  }

  void set phoneNumber(String phoneNumber) {
    if (phoneNumber.length == 10) {
      _phoneNumber = phoneNumber;
    }
  }
}