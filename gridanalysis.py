#! /usr/bin/env python3
# set ts=4

import os

class GridAnalysis:
	'''Grid Analysis: Memilih berdasarkan berbagai faktor'''

	def __init__(self):
		self.topik   = ''
		self.pilihan = []
		self.faktor  = []
		self.bobot   = []
		self.skor    = []
		self.total   = []

	def formTopik(self):
		'''Update Topik'''

		print()
		print('Topik adalah judul yang akan diputuskan, ', end='')
		print('misal: Memilih Jenis Kendaraan')
		t = input("Input Topik: ")
		if t:
			self.topik = t

	def formPilihan(self):
		'''Update Pilihan'''

		print()
		print('Pilihan adalah hal-hal yang dipertimbangkan untuk dipilih.')
		print('Misal untuk topik Memilih Jenis Kendaraan, maka ')
		print('pilihannya mungkin: Minibus, Sedan, SUV, Truk, dll\n')

		if len(self.pilihan):
			print('Pilihan default: ', end='')
			print(','.join(self.pilihan))

		print('Masukan pilihan: (minimal 2 dan dipisahkan dengan koma)')
		p = input('Input: ')
		ap = p.split(',')
		lenp = len(ap)
		if lenp > 1:
			self.pilihan = ap
			self.total   = [0]*lenp;
			lens = len(self.skor)
			lenm = lenp * len(self.faktor)
			if lens < lenm:
				self.skor.extend([0]*(lenm-lens))


	def formFaktor(self):
		'''Update Faktor'''

		print()
		print('Faktor adalah aspek /kriteria untuk menentukan pemilihan,')
		print('misalnya Harga, Suku Cadang, Teknologi, Daya Angkut dll\n') 

		if len(self.faktor):
			print('Faktor-faktor default: ', end='')
			print(','.join(self.faktor))

		print('Masukkan faktor-faktor: (minimal 2 dan pisahkan dengan koma)')
		p = input('Input: ')
		ap = p.split(',')
		lenf = len(ap)
		if lenf > 1:
			self.faktor = ap
			lenb = len(self.bobot)
			if lenb < lenf:
				self.bobot.extend([1]*(lenf-lenb))
		
			lens = len(self.skor)
			lenm = lenf * len(self.pilihan)
			if lens < lenm:
				self.skor.extend([0]*(lenm-lens))

		
	def formBobot(self):
		'''Update Bobot'''

		print()
		print('Bobot adalah nilai /tingkat kepentingan dari setiap ')
		print('faktor pemilihan. Makin besar bobotnya semakin penting') 

		if len(self.faktor) <= 1:
			print('**ERROR** > Input faktor terlebih dahulu')
			input('Press Enter')
			return

		print('Input bobot masing-masing dari faktor berikut:')
		print('(minimal 2 dan pisahkan dengan koma)')
		print(','.join(self.faktor))
		print('Default:',','.join(map(str,self.bobot)))

		p = input('Input: ')
		ap = p.split(',')
		if len(ap) > 1:
			try:
				self.bobot = list(map(int, ap))
			except:
				self.bobot = [1]*len(ap);


	def formSkor(self):
		'''Update skor'''
	
		print()
		print('Skor adalah persepsi suatu Faktor dengan menbandingkan ')
		print('dari Pilihan-pilihan yang tersedia.')
		print('Pemberian skor biasanya menggunakan skala 1-5.')
		print('Semakin besar skor, semakin bagus/diminati pilihan tersebut.') 

		if len(self.faktor) <= 1 or len(self.pilihan) <= 1:
			print('**ERROR** > Input faktor/Pilihan terlebih dahulu')
			input('Press Enter')
			return

		for i,f in enumerate(self.faktor):
			print()
			print('Input Skor Faktor:', f)
			lenp = len(self.pilihan)
			for j,p in enumerate(self.pilihan):
				pc = p[0:15]
				print('%-15s (%d)' % (pc.lstrip(), self.skor[i*lenp+j]), end="")
				try:
					s = input(": ")
					if s != '':
						self.skor[i*lenp+j] = int(s)
				except:
					self.skor[i*lenp+j] = 0


	def reCalc(self):

		lenp = len(self.pilihan)
		self.total = [0]*lenp

		for i,f in enumerate(self.faktor):
			for j,p in enumerate(self.pilihan):
				self.total[j] += (self.skor[i*lenp +j] * self.bobot[i])


	def showGrid(self):
		'''Tampilkan grid analyis'''
		
		print("DECISION MAKING > GRID ANALYSIS\n")
		print("TOPIK:", self.topik)

		nf = len(self.faktor)
		w  = max(5, 60//(nf+1)) if nf > 1 else 10
		line1 = line2 = line3 = ''
		linesk = ['']*len(self.pilihan)

		if nf > 1:
			for i,f in enumerate(self.faktor):
				fc = f[0:w-1]
				li = "-"*(w-1)
				bc = str(self.bobot[i])
				line1 += (li.center(w-1)+"+")
				line2 += (fc.center(w-1)+"|")
				line3 += (bc.center(w-1)+"|")
				lenp = len(self.pilihan)

				for j,p in enumerate(self.pilihan):
					try:
						sk = str(self.skor[i*lenp+j])
					except:
						sk = "-"

					linesk[j] += (sk.center(w-1)+"|")

			#Total
			fc = "TOTAL"
			li = "-"*(w-1)
			bc = ''
			line1 += (li.center(w-1)+"+")
			line2 += (fc.center(w-1)+"|")
			line3 += (bc.center(w-1)+"|")
			lenp = len(self.pilihan)

			for j,p in enumerate(self.pilihan):
				try:
					sk = str(self.total[j])
				except:
					sk = "-"

				linesk[j] += (sk.center(w-1)+"|")
				
		else: 
			li = "-"*30
			bb = ''
			line1 += (li.center(30)+"+")
			line2 += ('FAKTOR-FAKTOR'.center(30)+'|')
			line3 += (bb.center(30)+"|")

			for j,p in enumerate(self.pilihan):
				linesk[j] += ("-".center(30)+"|")
				
		print('+----------------+'+line1)
		print('|         FAKTOR |'+line2)
		print('| PILIHAN        |'+line3)
		print('+----------------+'+line1)

		for j,p in enumerate(self.pilihan):
			pc = p[0:15]
			print('| %-15s|' % pc.lstrip(), sep="", end="")
			print(linesk[j])
		
		print('+----------------+'+line1)
		print('')


	def formKesimpulan(self):
		maxval = max(self.total)
		if maxval > 0:
			j = self.total.index(maxval)

			print()
			print("## KESIMPULAN")
			print('Pilihan: %s, mendapatkan skor tertinggi %d' % (self.pilihan[j], self.total[j]))
			print('')
			input('Press Enter')


	def showMainMenu(self):
		'''Show main menu'''

		while True:

			os.system("clear");
			#print(chr(27)+"[3J"+chr(27)+"[1;1H")
	
			self.showGrid()
			print('Menu Utama')
			print('T. Topik', end='')
			print('\tP. Pilihan', end='' )
			print('\tF. Faktor')
			print('B. Bobot Faktor', end='')
			print('\tS. Skor', end='')
			print('\t\tK. Kesimpulan')
			print('X. Exit')

			try:
				cho = input('Pilih: ').lower()

				if cho == 't':
					self.formTopik()
				elif cho == 'p':
					self.formPilihan()
					self.reCalc()
				elif cho == 'f':
					self.formFaktor()
					self.reCalc()
				elif cho == 'b':
					self.formBobot()
					self.reCalc()
				elif cho == "s":
					self.formSkor()
					self.reCalc()

				elif cho == "k":
					self.formKesimpulan()

				elif cho == "x":
					break
				else:
					pass

			except:
				pass



if __name__ == "__main__":

	grid = GridAnalysis()
	grid.showMainMenu()
