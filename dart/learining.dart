import 'dart:ffi';
import 'dart:io';
import 'dart:mirrors';
import 'foo_lib.dart';

main() {
  // data types
  String name = 'hu';
  int n = 1;
  double m = 1.2;
  bool b = true;
  List<int> nums = [1, 2, 3, 4, 5];
  Map UserInfo = {"number": 01141656121, "password": "!@#123"};
  // a symbol let you store the name of the library and its class
  Symbol lib = new Symbol('foo_lib');
  Symbol clsToSearch = new Symbol('foo');
  //if (checkIf_classAvailableInlibrary(lib, clsToSearch))
  // searches Foo class in foo_lib library
  //  print("class found..");
  // runes let you store the unicode
  Runes input = new Runes(' \u{1f602} ');
  // print(new String.fromCharCodes(input));
  var names = ["hamdi", "mahamed"];
  final anything = [true, false, 12, 21.3];
}
