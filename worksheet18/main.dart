import 'pract18.dart';

void main() {
  Student devki = Student('Devki', '07123456789');
  print(devki.name);
  print(devki.level);
  print(devki.phoneNumber); // gets the last 4 digits  
  devki.phoneNumber = ''; // should not set
  print(devki.phoneNumber); // gets the last 4 digits
  devki.phoneNumber = '0787654321'; // sets the phone number
  print(devki.phoneNumber); // gets the last 4 digits
}