#include <stdio.h>

int main() {
  /*
  C strings are just arrays of characters
  it is required to use double quotes
  */
  char *will_never_hear_again =
      "Hey TJ, when is the memory course in C gonna be done?";

  // don't touch below this line
  printf("%s\n", will_never_hear_again);
  return 0;
}
