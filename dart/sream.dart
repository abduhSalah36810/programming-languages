void main() {
  final s1 = Stream.periodic(Duration(milliseconds: 500), (count) => count);
  final s2 = s1.where((event) => event % 2 == 0);
  s2.listen((event) {
    print(event);
  });
}
