from lines import main, count_lines

def test_arguments():
   assert count_lines("text.py") == 2
   assert count_lines("text1.py") == 0
