def is_armstrong_number(number):
  number_text = str(number)
  count, size = 0, len(number_text)
  for i in number_text:
    count += int(i) ** size
  return count == number
