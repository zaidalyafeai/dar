import os
import pandas as pd 
import datasets
from glob import glob
import zipfile

class ANETAC(datasets.GeneratorBasedBuilder):
	def _info(self):
		return datasets.DatasetInfo(features=datasets.Features({'Arabic':datasets.Value('string'),'Transliteration':datasets.Value('string')}))

	def extract_all(self, dir):
		zip_files = glob(dir+'/**/**.zip', recursive=True)
		for file in zip_files:
			with zipfile.ZipFile(file) as item:
				item.extractall('/'.join(file.split('/')[:-1])) 


	def get_all_files(self, dir):
		files = []
		valid_file_ext = ['txt', 'csv', 'tsv', 'xlsx', 'xls', 'xml', 'json', 'jsonl', 'html', 'wav', 'mp3', 'jpg', 'png']
		for ext in valid_file_ext:
			files += glob(f"{dir}/**/**.{ext}", recursive = True)
		return files

	def _split_generators(self, dl_manager):
		url = ['https://github.com/MohamedHadjAmeur/ANETAC/archive/master.zip']
		downloaded_files = dl_manager.download_and_extract(url)
		return [datasets.SplitGenerator(name=datasets.Split.VALIDATION, gen_kwargs={'filepaths':{'inputs':[os.path.join(downloaded_files[0],'ANETAC-master/EN-AR Translit/dev.ar'),],'targets1':[os.path.join(downloaded_files[0],'ANETAC-master/EN-AR Translit/dev.en'),]} }),datasets.SplitGenerator(name=datasets.Split.TEST, gen_kwargs={'filepaths':{'inputs':[os.path.join(downloaded_files[0],'ANETAC-master/EN-AR Translit/test.ar'),],'targets1':[os.path.join(downloaded_files[0],'ANETAC-master/EN-AR Translit/test.en'),]} }),datasets.SplitGenerator(name=datasets.Split.TRAIN, gen_kwargs={'filepaths':{'inputs':[os.path.join(downloaded_files[0],'ANETAC-master/EN-AR Translit/train.ar'),],'targets1':[os.path.join(downloaded_files[0],'ANETAC-master/EN-AR Translit/train.en'),]} })]


	def read_txt(self, filepath, skiprows = 0, lines = True):
		if lines:
			return pd.DataFrame(open(filepath, 'r').read().splitlines()[skiprows:])
		else:
			return pd.DataFrame([open(filepath, 'r').read()])

	def _generate_examples(self, filepaths):
		_id = 0
		for i,filepath in enumerate(filepaths['inputs']):
			df = self.read_txt(filepath, skiprows = 0, lines = True)
			dfs = [df] 
			dfs.append(self.read_txt(filepaths['targets1'][i], skiprows = 0, lines = True))
			df = pd.concat(dfs, axis = 1)
			if len(df.columns) != 2:
				continue
			df.columns = ['Arabic', 'Transliteration']
			for _, record in df.iterrows():
				yield str(_id), {'Arabic':record['Arabic'],'Transliteration':record['Transliteration']}
				_id += 1 

