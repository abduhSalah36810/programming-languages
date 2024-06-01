double info() {
  return double.parse('332cdf');
}

void main() {
  final f1 = Future(info);
  f1
      .then((value) => print("value = $value"))
      .catchError((Error) => print("error = $Error"));

  final f2 = Future.delayed(Duration(seconds: 1));
  final f3 = Future.value(2);
}
