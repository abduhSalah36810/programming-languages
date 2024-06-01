import 'dart:io';

void main() async {
  await Future.delayed(Duration(seconds: 1), () => 2)
      .then((value) => print("value = $value"))
      .catchError((Error) => print("error = $Error"));

  print("value 1");
  try {
    final value = await Future.delayed(Duration(seconds: 1), () => 1);
    print(value);
  } catch (e) {
    print('error = $e');
  }

  final s1 = Stream.periodic(Duration(milliseconds: 500), (count) => count);
  //final sub = s1.listen((_) => _);
  // sub.onData((data) {
  //   data > 10 ? sub.cancel() : print(data);
  //});

  await for (var value in s1) {
    if (value > 10) break;
    print(value);
  }
}
