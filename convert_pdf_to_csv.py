import tabula
import argparse
import os

parser = argparse.ArgumentParser(description='Convert pdf-table to csv')

parser.add_argument('--input-file', metavar='PATH', type=str, help='input .pdf file with the table to convert')
parser.add_argument('--output-file', metavar='PATH', type=str, help='optional output filename. '
																	'Default name is same as pdf filename, '
																	'created in the same directory as the input file')


if __name__ == '__main__':

	args = parser.parse_args()
	if args.input_file is None or not os.path.exists(args.input_file) or args.input_file[-4:] != ".pdf":
		print ("Please provide a valid pdf input file!")
		exit(1)

	if args.output_file is None:
		output_file = args.input_file[:-4] + ".csv"
	else:
		output_file = args.output_file

	tabula.convert_into(args.input_file, output_file, output_format="csv",
					   options="--pages all")

	# tabula.convert_pdf("/Users/Muks/Downloads/cse16.pdf", "/Users/Muks/Downloads/cse16.csv", output_format="csv",
	# 				   options="--pages all")
	print("Done! Output file can be found at: %s" % (output_file))