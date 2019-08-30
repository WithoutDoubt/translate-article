import librosa
 
for i in range(286,301):
	filename = str(i) + '.wav'
	newFilename = str(i) + '.wav'
	 
	y, sr = librosa.load(filename, sr=8000)
	y_16 = librosa.resample(y,sr,16000)
	 
	librosa.output.write_wav(newFilename, y_16, 16000)
