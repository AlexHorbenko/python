import codecs
import re

# result_file = open(r'D:\Hillel_Python_Basic\pythonProject\DZ_12\cleaned.txt','w')
# result_file.write("Start")
# result_file.close()

#****************************** Варіант 1 *********************************

def delete_html_tags(html_file, result_file='cleaned.txt'):
      with codecs.open(html_file, 'r', 'utf-8') as file:
          html = file.read()
      for elem in html:
          if elem == '<':
              start = html.find('<')
          if elem == '>':
              end = html.find('>')
              result = html[start:end + 1]
              html = html.replace(result, '')

      with codecs.open(result_file, 'w', 'utf-8') as output_file:
          output_file.write(html)

      print(f"{result_file}")

delete_html_tags(r'D:\Hillel_Python_Basic\pythonProject\DZ_12\draft.html', r'D:\Hillel_Python_Basic\pythonProject\DZ_12\cleaned.txt')

#****************************************** Варіант 2 *****************************************
# def delete_html_tags(html_file, result_file='cleaned.txt'):
#     with codecs.open(html_file, 'r', 'utf-8') as file:
#         html = file.read()
#
#     while '<' in html and '>' in html:
#         start = html.find('<')
#         end = html.find('>', start)
#         if start != -1 and end != -1:
#             html = html[:start] + html[end + 1:]
#
#     with codecs.open(result_file, 'w', 'utf-8') as output_file:
#         output_file.write(html)
#
#     print(f"{result_file}")
#
# delete_html_tags(r'D:\Hillel_Python_Basic\pythonProject\DZ_12\draft.html', r'D:\Hillel_Python_Basic\pythonProject\DZ_12\cleaned.txt')

# ******************************************** Варіант 3 ********************************
# def delete_html_tags(html_file, result_file='cleaned.txt'):
#     with codecs.open(html_file, 'r', 'utf-8') as file:
#         html = file.read()
#         delete_html = re.sub(r'<[^>]*>', '', html)
#
#     with codecs.open(result_file, 'w', 'utf-8') as output_file:
#         output_file.write(delete_html)
#
#     print(f"{result_file}")
#
# delete_html_tags(r'D:\Hillel_Python_Basic\pythonProject\DZ_12\draft.html', r'D:\Hillel_Python_Basic\pythonProject\DZ_12\cleaned.txt')
