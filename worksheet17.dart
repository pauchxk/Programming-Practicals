void main() {
  List<String> posts = ['Learning #Dart and #Flutter is fun!','I love #working with #VSCode'];
  print(extractHashtags(posts));

  String name = 'john_smith';
  print(snakeToCamel(name));
}

/*8*/
Set extractHashtags(List<String> posts) {
  Set hashtags = {};

  for (int i = 0; i < posts.length; i++) {
    List temp = posts[i].split(' ');

    for (String j in temp) {
      if (j.contains('#')) {
        hashtags.add(j);
      }
    }
  }
  return hashtags;
}

/*10*/
String snakeToCamel(String name) {
  List temp = name.split('_');
  List assembly = [];
  for (String word in temp) {
    if (word != temp[0]) {
      word = word.substring(0,1).toUpperCase() + word.substring(1,word.length);
    }
    assembly.add(word);
  }
  String camel = assembly.join();
  return camel;
}