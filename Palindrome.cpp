#include <iostream>


std::string is_palindrome(std::string text){

std::string rev_str;

for (int i=text.size()-1 ; i>=0 ; i--){     // len() - 1, cuz index is 1 less than len, i>=0 cuz 0 is the min index of strings
  rev_str += text[i];
}


if( rev_str == text){
  return "text is palindrome";
}

else{
  return "text is not a palindrome";
}

}

int main() {
  
  std::cout << is_palindrome("madam") << "\n";
  std::cout << is_palindrome("ada") << "\n";
  std::cout << is_palindrome("lovelace") << "\n";
  
}
