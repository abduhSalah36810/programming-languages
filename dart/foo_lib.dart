import 'dart:mirrors';

class foo {
  foo() {
    print("foo");
  }
}

bool checkIf_classAvailableInlibrary(Symbol lib_name, Symbol class_name) {
  MirrorSystem mirrorSystem = currentMirrorSystem();
  LibraryMirror libMirror = mirrorSystem.findLibrary(lib_name);
  if (libMirror != null) {
    print("library found \n cheching class details .....");
    libMirror.declarations.forEach((s, d) => print(s));
    if (libMirror.declarations.containsKey(class_name)) {
      return true;
    }
  }
  return false;
}
