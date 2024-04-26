import 'password.dart';

class User {
  String username;
  String _password = Password(10);

  User(String this.username) {
    this.username = username;
  }

  void changePassword(String currentPassword, String newPassword) {
    if (currentPassword == _password) {
      _password = newPassword;
    }
  }

  String get password => _password;

  bool login(pass) {
    if (pass == _password) {
      return true;
    } else {
      return false;
    }
  }
}