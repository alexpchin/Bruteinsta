def txt_to_lst(txt_file, lst_file):
    with open(txt_file, 'r') as txt:
        lines = txt.readlines()

    # Remove newline characters from each line
    lines = [line.strip() for line in lines]

    with open(lst_file, 'w') as lst:
        for item in lines:
            lst.write(item + '\n')

    print(f"{len(lines)} items have been converted and saved to '{lst_file}'.")

# Replace 'input.txt' with the path to your input TXT file
input_txt_file = '10-million-password-list-top-1000000.txt'

# Replace 'output.lst' with the path where you want to save the output LST file
output_lst_file = 'passwords2.lst'

txt_to_lst(input_txt_file, output_lst_file)