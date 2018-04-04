import os

ORCAD_PROJECTS_FOLDER = r'C:\Users\josemi\Dropbox'

def find_all_dats(path):
	files_found = []
	for root, dirs, files in os.walk(path):
		for name in files:
			files_found.append(os.path.join(root, name))
	dats = []
	for a in files_found:
		if a.endswith('.dat'):
			dats.append(a);
	return dats

files_found = find_all_dats(ORCAD_PROJECTS_FOLDER)

if files_found == []:
	input('\n - There isn\'t any file to delete. Press enter to continue.')
else:
	print( '\n - Files to delete: ' + str(files_found.__len__()) + ' files.\n' )
	total_size = 0;
	for a in files_found:
		print('File: ' + a)
		print('Size: ' + str(int(os.path.getsize(a)/1000)) + 'KB')
		total_size += int(os.path.getsize(a)/1000)
	print( 'Total file size: ' + str(total_size) + ' KB' )
	cont = input("\n Proceed? (Y/N): ")

	if (cont == 'y' or cont == 'Y'):
		for a in files_found:
			os.remove(a)
