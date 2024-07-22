import csv
from bs4 import BeautifulSoup

# https://www.jobpersonality.com/beroepenzoeker?riasoc_1=&riasoc_2=&jobZone=&submitted=1
data = '''<div class="row nopadding">
		<div class="column-40">
			<div class="label hide-on-mobile">BEROEP</div>
			<div class="label show-on-mobile">BEROEP EN OPLEIDINGSNIVEAU</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/ceo-directievoorzitter';"><a href="https://www.jobpersonality.com/ceo-directievoorzitter" class="bold-on-mobile">CEO <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/ceo-directievoorzitter">
							Vacatures: 0<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/manager-duurzaamheidsbeleid';"><a href="https://www.jobpersonality.com/manager-duurzaamheidsbeleid" class="bold-on-mobile">Projectleider duurzaamheid <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/manager-duurzaamheidsbeleid">
							Vacatures: 3<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bestuurder-basis-voortgezet-onderwijs';"><a href="https://www.jobpersonality.com/bestuurder-basis-voortgezet-onderwijs" class="bold-on-mobile">Onderwijsbestuurder <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bestuurder-basis-voortgezet-onderwijs">
							Vacatures: 1<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bestuurder-beroepsonderwijs-hogescholen-universiteiten';"><a href="https://www.jobpersonality.com/bestuurder-beroepsonderwijs-hogescholen-universiteiten" class="bold-on-mobile">Onderwijsbestuurder beroepsonderwijs <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bestuurder-beroepsonderwijs-hogescholen-universiteiten">
							Vacatures: 0<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bouwkundig-manager';"><a href="https://www.jobpersonality.com/bouwkundig-manager" class="bold-on-mobile">Bouwkundig manager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bouwkundig-manager">
							Vacatures: 8<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/manager-natuurwetenschappen';"><a href="https://www.jobpersonality.com/manager-natuurwetenschappen" class="bold-on-mobile">Manager natuurwetenschappen <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/manager-natuurwetenschappen">
							Vacatures: 2<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/coordinator-klinisch-onderzoek';"><a href="https://www.jobpersonality.com/coordinator-klinisch-onderzoek" class="bold-on-mobile">Coördinator klinisch onderzoek <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/coordinator-klinisch-onderzoek">
							Vacatures: 0<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/beleggingsfondsmanager';"><a href="https://www.jobpersonality.com/beleggingsfondsmanager" class="bold-on-mobile">Investment manager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/beleggingsfondsmanager">
							Vacatures: 1<br>
							Robotiserings%: 25%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/lijkschouwer';"><a href="https://www.jobpersonality.com/lijkschouwer" class="bold-on-mobile">Lijkschouwer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/lijkschouwer">
							Vacatures: 0<br>
							Robotiserings%: 8%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/marktonderzoeker';"><a href="https://www.jobpersonality.com/marktonderzoeker" class="bold-on-mobile">Marktonderzoeker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/marktonderzoeker">
							Vacatures: 0<br>
							Robotiserings%: 61%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/marketingexpert';"><a href="https://www.jobpersonality.com/marketingexpert" class="bold-on-mobile">Marketingexpert <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/marketingexpert">
							Vacatures: 3<br>
							Robotiserings%: 31%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/wetenschappelijk-onderzoeker-ict';"><a href="https://www.jobpersonality.com/wetenschappelijk-onderzoeker-ict" class="bold-on-mobile">Wetenschappelijk IT onderzoeker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/wetenschappelijk-onderzoeker-ict">
							Vacatures: 0<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/wiskundige';"><a href="https://www.jobpersonality.com/wiskundige" class="bold-on-mobile">Wiskundige <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/wiskundige">
							Vacatures: 50<br>
							Robotiserings%: 5%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/business-intelligence-analist';"><a href="https://www.jobpersonality.com/business-intelligence-analist" class="bold-on-mobile">BI analist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/business-intelligence-analist">
							Vacatures: 1<br>
							Robotiserings%: 22%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/statisticus';"><a href="https://www.jobpersonality.com/statisticus" class="bold-on-mobile">Statisticus <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/statisticus">
							Vacatures: 0<br>
							Robotiserings%: 22%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/biostatisticus';"><a href="https://www.jobpersonality.com/biostatisticus" class="bold-on-mobile">Biostatisticus <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/biostatisticus">
							Vacatures: 0<br>
							Robotiserings%: 22%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/milieukundig-ingenieur';"><a href="https://www.jobpersonality.com/milieukundig-ingenieur" class="bold-on-mobile">Milieukundig ingenieur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/milieukundig-ingenieur">
							Vacatures: 0<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/ergonoom';"><a href="https://www.jobpersonality.com/ergonoom" class="bold-on-mobile">Ergonoom <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/ergonoom">
							Vacatures: 2<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/brandstofcelingenieur';"><a href="https://www.jobpersonality.com/brandstofcelingenieur" class="bold-on-mobile">Brandstofcelingenieur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/brandstofcelingenieur">
							Vacatures: 0<br>
							Robotiserings%: 10%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/ingenieur-nanosystemen';"><a href="https://www.jobpersonality.com/ingenieur-nanosystemen" class="bold-on-mobile">Nanotechnoloog <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/ingenieur-nanosystemen">
							Vacatures: 0<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/wetenschapper-veeteelt';"><a href="https://www.jobpersonality.com/wetenschapper-veeteelt" class="bold-on-mobile">Wetenschapper veeteelt <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/wetenschapper-veeteelt">
							Vacatures: 0<br>
							Robotiserings%: 6%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/landbouwwetenschapper';"><a href="https://www.jobpersonality.com/landbouwwetenschapper" class="bold-on-mobile">Landbouwwetenschapper  <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/landbouwwetenschapper">
							Vacatures: 2<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bioloog';"><a href="https://www.jobpersonality.com/bioloog" class="bold-on-mobile">Bioloog <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bioloog">
							Vacatures: 0<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/biochemicus';"><a href="https://www.jobpersonality.com/biochemicus" class="bold-on-mobile">Biochemicus <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/biochemicus">
							Vacatures: 0<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/microbioloog';"><a href="https://www.jobpersonality.com/microbioloog" class="bold-on-mobile">Microbioloog <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/microbioloog">
							Vacatures: 0<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/zooloog';"><a href="https://www.jobpersonality.com/zooloog" class="bold-on-mobile">Zoöloog <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/zooloog">
							Vacatures: 0<br>
							Robotiserings%: 30%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bio-informaticus';"><a href="https://www.jobpersonality.com/bio-informaticus" class="bold-on-mobile">Bio-informaticus <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bio-informaticus">
							Vacatures: 0<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/moleculair-bioloog';"><a href="https://www.jobpersonality.com/moleculair-bioloog" class="bold-on-mobile">Moleculair bioloog <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/moleculair-bioloog">
							Vacatures: 0<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/geneticus';"><a href="https://www.jobpersonality.com/geneticus" class="bold-on-mobile">Geneticus <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/geneticus">
							Vacatures: 0<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/epidemioloog';"><a href="https://www.jobpersonality.com/epidemioloog" class="bold-on-mobile">Epidemioloog <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/epidemioloog">
							Vacatures: 1<br>
							Robotiserings%: 20%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medische-wetenschapper';"><a href="https://www.jobpersonality.com/medische-wetenschapper" class="bold-on-mobile">Arts-onderzoeker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medische-wetenschapper">
							Vacatures: 0<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/astronoom';"><a href="https://www.jobpersonality.com/astronoom" class="bold-on-mobile">Astronoom <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/astronoom">
							Vacatures: 0<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/natuurkundige';"><a href="https://www.jobpersonality.com/natuurkundige" class="bold-on-mobile">Natuurkundige <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/natuurkundige">
							Vacatures: 53<br>
							Robotiserings%: 10%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/scheikundige';"><a href="https://www.jobpersonality.com/scheikundige" class="bold-on-mobile">Chemicus <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/scheikundige">
							Vacatures: 0<br>
							Robotiserings%: 10%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/materiaalkundige';"><a href="https://www.jobpersonality.com/materiaalkundige" class="bold-on-mobile">Materiaalkundige <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/materiaalkundige">
							Vacatures: 4<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/analist-klimaatverandering';"><a href="https://www.jobpersonality.com/analist-klimaatverandering" class="bold-on-mobile">Klimatoloog <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/analist-klimaatverandering">
							Vacatures: 0<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/milieuvervuilingsspecialist';"><a href="https://www.jobpersonality.com/milieuvervuilingsspecialist" class="bold-on-mobile">Adviseur milieuvervuiling <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/milieuvervuilingsspecialist">
							Vacatures: 10<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/industrieel-ecoloog';"><a href="https://www.jobpersonality.com/industrieel-ecoloog" class="bold-on-mobile">Ecoloog <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/industrieel-ecoloog">
							Vacatures: 0<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/teledetectiespecialist';"><a href="https://www.jobpersonality.com/teledetectiespecialist" class="bold-on-mobile">Teledetectiespecialist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/teledetectiespecialist">
							Vacatures: 0<br>
							Robotiserings%: 43%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/econoom';"><a href="https://www.jobpersonality.com/econoom" class="bold-on-mobile">Econoom <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/econoom">
							Vacatures: 3<br>
							Robotiserings%: 43%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/milieu-econoom';"><a href="https://www.jobpersonality.com/milieu-econoom" class="bold-on-mobile">Milieueconoom <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/milieu-econoom">
							Vacatures: 7<br>
							Robotiserings%: 43%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/opiniepeiler';"><a href="https://www.jobpersonality.com/opiniepeiler" class="bold-on-mobile">Opiniepeiler <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/opiniepeiler">
							Vacatures: 0<br>
							Robotiserings%: 23%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/schoolpsycholoog';"><a href="https://www.jobpersonality.com/schoolpsycholoog" class="bold-on-mobile">Schoolpsycholoog <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/schoolpsycholoog">
							Vacatures: 0<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/klinisch-psycholoog';"><a href="https://www.jobpersonality.com/klinisch-psycholoog" class="bold-on-mobile">Klinisch psycholoog <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/klinisch-psycholoog">
							Vacatures: 20<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/psychotherapeut';"><a href="https://www.jobpersonality.com/psychotherapeut" class="bold-on-mobile">Psychotherapeut <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/psychotherapeut">
							Vacatures: 24<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/organisatiepsycholoog';"><a href="https://www.jobpersonality.com/organisatiepsycholoog" class="bold-on-mobile">A&amp;O psycholoog <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/organisatiepsycholoog">
							Vacatures: 0<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/neuropsycholoog';"><a href="https://www.jobpersonality.com/neuropsycholoog" class="bold-on-mobile">Neuropsycholoog <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/neuropsycholoog">
							Vacatures: 0<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/neuromarketeer';"><a href="https://www.jobpersonality.com/neuromarketeer" class="bold-on-mobile">Neuromarketeer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/neuromarketeer">
							Vacatures: 0<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/socioloog';"><a href="https://www.jobpersonality.com/socioloog" class="bold-on-mobile">Socioloog <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/socioloog">
							Vacatures: 0<br>
							Robotiserings%: 6%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/specialist-ruimtelijke-ordening';"><a href="https://www.jobpersonality.com/specialist-ruimtelijke-ordening" class="bold-on-mobile">Stedenbouwkundige <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/specialist-ruimtelijke-ordening">
							Vacatures: 8<br>
							Robotiserings%: 13%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/antropoloog';"><a href="https://www.jobpersonality.com/antropoloog" class="bold-on-mobile">Antropoloog <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/antropoloog">
							Vacatures: 0<br>
							Robotiserings%: 6%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/geograaf';"><a href="https://www.jobpersonality.com/geograaf" class="bold-on-mobile">Geograaf <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/geograaf">
							Vacatures: 0<br>
							Robotiserings%: 25%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/historicus';"><a href="https://www.jobpersonality.com/historicus" class="bold-on-mobile">Historicus <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/historicus">
							Vacatures: 0<br>
							Robotiserings%: 44%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/politicoloog';"><a href="https://www.jobpersonality.com/politicoloog" class="bold-on-mobile">Politicoloog  <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/politicoloog">
							Vacatures: 0<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/relatie-gezinstherapeut';"><a href="https://www.jobpersonality.com/relatie-gezinstherapeut" class="bold-on-mobile">Relatietherapeut <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/relatie-gezinstherapeut">
							Vacatures: 0<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/psychische-gezondheidsadviseur';"><a href="https://www.jobpersonality.com/psychische-gezondheidsadviseur" class="bold-on-mobile">GZ-Psycholoog <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/psychische-gezondheidsadviseur">
							Vacatures: 49<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/re-integratie-adviseur';"><a href="https://www.jobpersonality.com/re-integratie-adviseur" class="bold-on-mobile">Re-integratiecoach <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/re-integratie-adviseur">
							Vacatures: 0<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/geestelijk-leider-voorganger';"><a href="https://www.jobpersonality.com/geestelijk-leider-voorganger" class="bold-on-mobile">Voorganger <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/geestelijk-leider-voorganger">
							Vacatures: 9<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/advocaat';"><a href="https://www.jobpersonality.com/advocaat" class="bold-on-mobile">Advocaat <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/advocaat">
							Vacatures: 37<br>
							Robotiserings%: 40%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/griffier';"><a href="https://www.jobpersonality.com/griffier" class="bold-on-mobile">Griffier rechtbank <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/griffier">
							Vacatures: 3<br>
							Robotiserings%: 41%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bestuursrechter';"><a href="https://www.jobpersonality.com/bestuursrechter" class="bold-on-mobile">Bestuursrechter <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bestuursrechter">
							Vacatures: 0<br>
							Robotiserings%: 64%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/mediator';"><a href="https://www.jobpersonality.com/mediator" class="bold-on-mobile">Mediator <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/mediator">
							Vacatures: 3<br>
							Robotiserings%: 6%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/rechter';"><a href="https://www.jobpersonality.com/rechter" class="bold-on-mobile">Rechter <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/rechter">
							Vacatures: 3<br>
							Robotiserings%: 40%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/docent-architectuur';"><a href="https://www.jobpersonality.com/docent-architectuur" class="bold-on-mobile">Docent architectuur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/docent-architectuur">
							Vacatures: 0<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/docent-psychologie';"><a href="https://www.jobpersonality.com/docent-psychologie" class="bold-on-mobile">Docent psychologie <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/docent-psychologie">
							Vacatures: 0<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/docent-gespecialiseerde-gezondheidszorg';"><a href="https://www.jobpersonality.com/docent-gespecialiseerde-gezondheidszorg" class="bold-on-mobile">Medisch docent <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/docent-gespecialiseerde-gezondheidszorg">
							Vacatures: 1<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/docent-strafrecht';"><a href="https://www.jobpersonality.com/docent-strafrecht" class="bold-on-mobile">Docent strafrecht <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/docent-strafrecht">
							Vacatures: 1<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/docent-recht';"><a href="https://www.jobpersonality.com/docent-recht" class="bold-on-mobile">Docent recht <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/docent-recht">
							Vacatures: 1<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/student-assistent';"><a href="https://www.jobpersonality.com/student-assistent" class="bold-on-mobile">Student-assistent <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/student-assistent">
							Vacatures: 1<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/archivaris';"><a href="https://www.jobpersonality.com/archivaris" class="bold-on-mobile">Archivaris <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/archivaris">
							Vacatures: 0<br>
							Robotiserings%: 76%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/curator';"><a href="https://www.jobpersonality.com/curator" class="bold-on-mobile">Curator <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/curator">
							Vacatures: 6<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bibliothecaris';"><a href="https://www.jobpersonality.com/bibliothecaris" class="bold-on-mobile">Bibliothecaris <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bibliothecaris">
							Vacatures: 0<br>
							Robotiserings%: 65%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/landbouw-huishoudadviseur';"><a href="https://www.jobpersonality.com/landbouw-huishoudadviseur" class="bold-on-mobile">Adviseur landbouw <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/landbouw-huishoudadviseur">
							Vacatures: 1<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/ontwikkelaar-onderwijsmateriaal';"><a href="https://www.jobpersonality.com/ontwikkelaar-onderwijsmateriaal" class="bold-on-mobile">Onderwijsontwikkelaar <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/ontwikkelaar-onderwijsmateriaal">
							Vacatures: 0<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/ontwikkelaar-technologisch-onderwijsmateriaal';"><a href="https://www.jobpersonality.com/ontwikkelaar-technologisch-onderwijsmateriaal" class="bold-on-mobile">Technologisch onderwijsontwikkelaar <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/ontwikkelaar-technologisch-onderwijsmateriaal">
							Vacatures: 0<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/decorontwerper';"><a href="https://www.jobpersonality.com/decorontwerper" class="bold-on-mobile">Decorontwerper <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/decorontwerper">
							Vacatures: 0<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/technische-directeur';"><a href="https://www.jobpersonality.com/technische-directeur" class="bold-on-mobile">Technisch directeur of CTO <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/technische-directeur">
							Vacatures: 4<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/chiropractor';"><a href="https://www.jobpersonality.com/chiropractor" class="bold-on-mobile">Chiropractor <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/chiropractor">
							Vacatures: 0<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/tandarts';"><a href="https://www.jobpersonality.com/tandarts" class="bold-on-mobile">Tandarts <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/tandarts">
							Vacatures: 7<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/kaakchirurg';"><a href="https://www.jobpersonality.com/kaakchirurg" class="bold-on-mobile">Kaakchirurg <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/kaakchirurg">
							Vacatures: 0<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/orthodontist';"><a href="https://www.jobpersonality.com/orthodontist" class="bold-on-mobile">Orthodontist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/orthodontist">
							Vacatures: 0<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/tandprotheticus';"><a href="https://www.jobpersonality.com/tandprotheticus" class="bold-on-mobile">Tandprotheticus <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/tandprotheticus">
							Vacatures: 0<br>
							Robotiserings%: 6%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/apotheker';"><a href="https://www.jobpersonality.com/apotheker" class="bold-on-mobile">Apotheker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/apotheker">
							Vacatures: 3<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/anesthesist';"><a href="https://www.jobpersonality.com/anesthesist" class="bold-on-mobile">Anesthesist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/anesthesist">
							Vacatures: 0<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/huisarts';"><a href="https://www.jobpersonality.com/huisarts" class="bold-on-mobile">Huisarts <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/huisarts">
							Vacatures: 8<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/internist';"><a href="https://www.jobpersonality.com/internist" class="bold-on-mobile">Internist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/internist">
							Vacatures: 0<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/gynaecoloog';"><a href="https://www.jobpersonality.com/gynaecoloog" class="bold-on-mobile">Gynaecoloog <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/gynaecoloog">
							Vacatures: 0<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/kinderarts';"><a href="https://www.jobpersonality.com/kinderarts" class="bold-on-mobile">Kinderarts <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/kinderarts">
							Vacatures: 0<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/psychiater';"><a href="https://www.jobpersonality.com/psychiater" class="bold-on-mobile">Psychiater <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/psychiater">
							Vacatures: 33<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/chirurg';"><a href="https://www.jobpersonality.com/chirurg" class="bold-on-mobile">Chirurg <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/chirurg">
							Vacatures: 1<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/allergoloog';"><a href="https://www.jobpersonality.com/allergoloog" class="bold-on-mobile">Allergoloog <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/allergoloog">
							Vacatures: 0<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/dermatoloog';"><a href="https://www.jobpersonality.com/dermatoloog" class="bold-on-mobile">Dermatoloog <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/dermatoloog">
							Vacatures: 0<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/ziekenhuisarts';"><a href="https://www.jobpersonality.com/ziekenhuisarts" class="bold-on-mobile">Ziekenhuisarts <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/ziekenhuisarts">
							Vacatures: 0<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/neuroloog';"><a href="https://www.jobpersonality.com/neuroloog" class="bold-on-mobile">Neuroloog <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/neuroloog">
							Vacatures: 1<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/nucleair-geneeskundige';"><a href="https://www.jobpersonality.com/nucleair-geneeskundige" class="bold-on-mobile">Nucleair geneeskundige <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/nucleair-geneeskundige">
							Vacatures: 3<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/oogarts';"><a href="https://www.jobpersonality.com/oogarts" class="bold-on-mobile">Oogarts <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/oogarts">
							Vacatures: 0<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/patholoog';"><a href="https://www.jobpersonality.com/patholoog" class="bold-on-mobile">Patholoog <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/patholoog">
							Vacatures: 0<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/revalidatiearts';"><a href="https://www.jobpersonality.com/revalidatiearts" class="bold-on-mobile">Revalidatiearts <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/revalidatiearts">
							Vacatures: 0<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bedrijfsarts';"><a href="https://www.jobpersonality.com/bedrijfsarts" class="bold-on-mobile">Bedrijfsarts <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bedrijfsarts">
							Vacatures: 3<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/radioloog';"><a href="https://www.jobpersonality.com/radioloog" class="bold-on-mobile">Radioloog <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/radioloog">
							Vacatures: 0<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/sportarts';"><a href="https://www.jobpersonality.com/sportarts" class="bold-on-mobile">Sportarts <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/sportarts">
							Vacatures: 0<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/uroloog';"><a href="https://www.jobpersonality.com/uroloog" class="bold-on-mobile">Uroloog <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/uroloog">
							Vacatures: 0<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/visueel-therapeut';"><a href="https://www.jobpersonality.com/visueel-therapeut" class="bold-on-mobile">Visueel therapeut <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/visueel-therapeut">
							Vacatures: 0<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/inspanningsfysioloog';"><a href="https://www.jobpersonality.com/inspanningsfysioloog" class="bold-on-mobile">Inspanningsfysioloog <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/inspanningsfysioloog">
							Vacatures: 0<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/dierenarts';"><a href="https://www.jobpersonality.com/dierenarts" class="bold-on-mobile">Dierenarts <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/dierenarts">
							Vacatures: 1<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/audioloog';"><a href="https://www.jobpersonality.com/audioloog" class="bold-on-mobile">Audioloog <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/audioloog">
							Vacatures: 0<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/natuurgeneeskundig-arts';"><a href="https://www.jobpersonality.com/natuurgeneeskundig-arts" class="bold-on-mobile">Natuurgeneeskundige arts <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/natuurgeneeskundig-arts">
							Vacatures: 0<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/cardioloog';"><a href="https://www.jobpersonality.com/cardioloog" class="bold-on-mobile">Cardioloog <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/cardioloog">
							Vacatures: 0<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/radiotherapeut';"><a href="https://www.jobpersonality.com/radiotherapeut" class="bold-on-mobile">Radiotherapeut <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/radiotherapeut">
							Vacatures: 0<br>
							Robotiserings%: 13%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/orthopedisch-instrumentmaker';"><a href="https://www.jobpersonality.com/orthopedisch-instrumentmaker" class="bold-on-mobile">Orthopedisch instrumentenmaker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/orthopedisch-instrumentmaker">
							Vacatures: 0<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/sporttrainer';"><a href="https://www.jobpersonality.com/sporttrainer" class="bold-on-mobile">Sporttrainer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/sporttrainer">
							Vacatures: 0<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/klinisch-geneticus';"><a href="https://www.jobpersonality.com/klinisch-geneticus" class="bold-on-mobile">Klinisch geneticus <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/klinisch-geneticus">
							Vacatures: 0<br>
							Robotiserings%: 6%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/notaris';"><a href="https://www.jobpersonality.com/notaris" class="bold-on-mobile">Notaris <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/notaris">
							Vacatures: 13<br>
							Robotiserings%: 40%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/interim-manager';"><a href="https://www.jobpersonality.com/interim-manager" class="bold-on-mobile">Interim-manager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/interim-manager">
							Vacatures: 14<br>
							Robotiserings%: 13%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/consultant';"><a href="https://www.jobpersonality.com/consultant" class="bold-on-mobile">Consultant <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/consultant">
							Vacatures: 858<br>
							Robotiserings%: 13%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/jurist';"><a href="https://www.jobpersonality.com/jurist" class="bold-on-mobile">Jurist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/jurist">
							Vacatures: 85<br>
							Robotiserings%: 40%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/onderwijsinspecteur';"><a href="https://www.jobpersonality.com/onderwijsinspecteur" class="bold-on-mobile">Onderwijsinspecteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/onderwijsinspecteur">
							Vacatures: 0<br>
							Robotiserings%: 13%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/cfo-financieel-directeur';"><a href="https://www.jobpersonality.com/cfo-financieel-directeur" class="bold-on-mobile">Financieel directeur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/cfo-financieel-directeur">
							Vacatures: 3<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/coo-chief-operating-officer';"><a href="https://www.jobpersonality.com/coo-chief-operating-officer" class="bold-on-mobile">COO <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/coo-chief-operating-officer">
							Vacatures: 0<br>
							Robotiserings%: 16%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/kno-arts';"><a href="https://www.jobpersonality.com/kno-arts" class="bold-on-mobile">KNO-arts <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/kno-arts">
							Vacatures: 0<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/gemeentesecretaris';"><a href="https://www.jobpersonality.com/gemeentesecretaris" class="bold-on-mobile">Gemeentesecretaris <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/gemeentesecretaris">
							Vacatures: 4<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/psycholoog';"><a href="https://www.jobpersonality.com/psycholoog" class="bold-on-mobile">Psycholoog <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/psycholoog">
							Vacatures: 102<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/pedagoog';"><a href="https://www.jobpersonality.com/pedagoog" class="bold-on-mobile">Pedagoog <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/pedagoog">
							Vacatures: 3<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/orthopedagoog';"><a href="https://www.jobpersonality.com/orthopedagoog" class="bold-on-mobile">Orthopedagoog <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/orthopedagoog">
							Vacatures: 24<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bestuurskundige';"><a href="https://www.jobpersonality.com/bestuurskundige" class="bold-on-mobile">Bestuurskundige <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bestuurskundige">
							Vacatures: 14<br>
							Robotiserings%: 6%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/immunoloog';"><a href="https://www.jobpersonality.com/immunoloog" class="bold-on-mobile">Immunoloog <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/immunoloog">
							Vacatures: 0<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/iot-consultant';"><a href="https://www.jobpersonality.com/iot-consultant" class="bold-on-mobile">IoT consultant <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/iot-consultant">
							Vacatures: 0<br>
							Robotiserings%: 13%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/fiscalist';"><a href="https://www.jobpersonality.com/fiscalist" class="bold-on-mobile">Fiscalist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/fiscalist">
							Vacatures: 88<br>
							Robotiserings%: 99%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bestuurder-hoger-onderwijs';"><a href="https://www.jobpersonality.com/bestuurder-hoger-onderwijs" class="bold-on-mobile">Onderwijsbestuurder hoger onderwijs <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bestuurder-hoger-onderwijs">
							Vacatures: 1<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/ict-consultant';"><a href="https://www.jobpersonality.com/ict-consultant" class="bold-on-mobile">IT Consultant <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/ict-consultant">
							Vacatures: 58<br>
							Robotiserings%: 13%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bewindvoerder';"><a href="https://www.jobpersonality.com/bewindvoerder" class="bold-on-mobile">Bewindvoerder <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bewindvoerder">
							Vacatures: 4<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/planoloog';"><a href="https://www.jobpersonality.com/planoloog" class="bold-on-mobile">Planoloog <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/planoloog">
							Vacatures: 8<br>
							Robotiserings%: 25%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/jurist-handhaving';"><a href="https://www.jobpersonality.com/jurist-handhaving" class="bold-on-mobile">Jurist handhaving <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/jurist-handhaving">
							Vacatures: 7<br>
							Robotiserings%: 40%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/business-consultant';"><a href="https://www.jobpersonality.com/business-consultant" class="bold-on-mobile">Business consultant <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/business-consultant">
							Vacatures: 41<br>
							Robotiserings%: 13%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/specialist-ouderengeneeskunde';"><a href="https://www.jobpersonality.com/specialist-ouderengeneeskunde" class="bold-on-mobile">Specialist ouderengeneeskunde <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/specialist-ouderengeneeskunde">
							Vacatures: 6<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medisch-specialist';"><a href="https://www.jobpersonality.com/medisch-specialist" class="bold-on-mobile">Medisch specialist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medisch-specialist">
							Vacatures: 3<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/orthopeed';"><a href="https://www.jobpersonality.com/orthopeed" class="bold-on-mobile">Orthopeed <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/orthopeed">
							Vacatures: 0<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/verzekeringsarts';"><a href="https://www.jobpersonality.com/verzekeringsarts" class="bold-on-mobile">Verzekeringsarts <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/verzekeringsarts">
							Vacatures: 3<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/econometrist';"><a href="https://www.jobpersonality.com/econometrist" class="bold-on-mobile">Econometrist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/econometrist">
							Vacatures: 0<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/adviseur-public-affairs';"><a href="https://www.jobpersonality.com/adviseur-public-affairs" class="bold-on-mobile">Adviseur public affairs <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/adviseur-public-affairs">
							Vacatures: 2<br>
							Robotiserings%: 6%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/diplomaat';"><a href="https://www.jobpersonality.com/diplomaat" class="bold-on-mobile">Diplomaat <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/diplomaat">
							Vacatures: 0<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/burgemeester';"><a href="https://www.jobpersonality.com/burgemeester" class="bold-on-mobile">Burgemeester <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/burgemeester">
							Vacatures: 14<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/hoogleraar';"><a href="https://www.jobpersonality.com/hoogleraar" class="bold-on-mobile">Hoogleraar <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/hoogleraar">
							Vacatures: 0<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/schooldirecteur';"><a href="https://www.jobpersonality.com/schooldirecteur" class="bold-on-mobile">Schooldirecteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/schooldirecteur">
							Vacatures: 9<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/overheidsmanager';"><a href="https://www.jobpersonality.com/overheidsmanager" class="bold-on-mobile">Overheidsmanager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/overheidsmanager">
							Vacatures: 0<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bestuurder';"><a href="https://www.jobpersonality.com/bestuurder" class="bold-on-mobile">Bestuurder <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bestuurder">
							Vacatures: 86<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/organisatieadviseur';"><a href="https://www.jobpersonality.com/organisatieadviseur" class="bold-on-mobile">Organisatieadviseur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/organisatieadviseur">
							Vacatures: 1<br>
							Robotiserings%: 13%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/officier-van-justitie';"><a href="https://www.jobpersonality.com/officier-van-justitie" class="bold-on-mobile">Officier van justitie <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/officier-van-justitie">
							Vacatures: 2<br>
							Robotiserings%: 40%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bedrijfsjurist';"><a href="https://www.jobpersonality.com/bedrijfsjurist" class="bold-on-mobile">Bedrijfsjurist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bedrijfsjurist">
							Vacatures: 5<br>
							Robotiserings%: 40%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/afvalstoffenspecialist';"><a href="https://www.jobpersonality.com/afvalstoffenspecialist" class="bold-on-mobile">Afvalstoffenspecialist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/afvalstoffenspecialist">
							Vacatures: 0<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/filosoof';"><a href="https://www.jobpersonality.com/filosoof" class="bold-on-mobile">Filosoof <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/filosoof">
							Vacatures: 0<br>
							Robotiserings%: 6%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/testontwikkelaar';"><a href="https://www.jobpersonality.com/testontwikkelaar" class="bold-on-mobile">Testontwikkelaar <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/testontwikkelaar">
							Vacatures: 0<br>
							Robotiserings%: 23%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/basisarts';"><a href="https://www.jobpersonality.com/basisarts" class="bold-on-mobile">Basisarts <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/basisarts">
							Vacatures: 6<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/seksuoloog';"><a href="https://www.jobpersonality.com/seksuoloog" class="bold-on-mobile">Seksuoloog <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/seksuoloog">
							Vacatures: 0<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 5<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bestuurssecretaris';"><a href="https://www.jobpersonality.com/bestuurssecretaris" class="bold-on-mobile">Bestuurssecretaris <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bestuurssecretaris">
							Vacatures: 3<br>
							Robotiserings%: 44%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/algemeen-directeur';"><a href="https://www.jobpersonality.com/algemeen-directeur" class="bold-on-mobile">Algemeen directeur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/algemeen-directeur">
							Vacatures: 19<br>
							Robotiserings%: 16%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/politicus-volksvertegenwoordiger';"><a href="https://www.jobpersonality.com/politicus-volksvertegenwoordiger" class="bold-on-mobile">Politicus <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/politicus-volksvertegenwoordiger">
							Vacatures: 0<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/manager-reclame-promotiebeleid';"><a href="https://www.jobpersonality.com/manager-reclame-promotiebeleid" class="bold-on-mobile">Account executive <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/manager-reclame-promotiebeleid">
							Vacatures: 1<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/marketingmanager';"><a href="https://www.jobpersonality.com/marketingmanager" class="bold-on-mobile">Marketingmanager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/marketingmanager">
							Vacatures: 1<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/startend-ondernemer';"><a href="https://www.jobpersonality.com/startend-ondernemer" class="bold-on-mobile">Entrepreneur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/startend-ondernemer">
							Vacatures: 5<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/salesmanager';"><a href="https://www.jobpersonality.com/salesmanager" class="bold-on-mobile">Salesmanager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/salesmanager">
							Vacatures: 28<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/public-relations-manager';"><a href="https://www.jobpersonality.com/public-relations-manager" class="bold-on-mobile">PR manager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/public-relations-manager">
							Vacatures: 2<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/manager-ict';"><a href="https://www.jobpersonality.com/manager-ict" class="bold-on-mobile">IT manager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/manager-ict">
							Vacatures: 66<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/penningmeester';"><a href="https://www.jobpersonality.com/penningmeester" class="bold-on-mobile">Penningmeester <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/penningmeester">
							Vacatures: 0<br>
							Robotiserings%: 7%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/financiele-afdelingsmanager';"><a href="https://www.jobpersonality.com/financiele-afdelingsmanager" class="bold-on-mobile">Financieel manager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/financiele-afdelingsmanager">
							Vacatures: 17<br>
							Robotiserings%: 7%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/industriele-productmanager';"><a href="https://www.jobpersonality.com/industriele-productmanager" class="bold-on-mobile">Plant manager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/industriele-productmanager">
							Vacatures: 8<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/kwaliteitsmanager';"><a href="https://www.jobpersonality.com/kwaliteitsmanager" class="bold-on-mobile">Kwaliteitsmanager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/kwaliteitsmanager">
							Vacatures: 10<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/manager-productie-biobrandstof';"><a href="https://www.jobpersonality.com/manager-productie-biobrandstof" class="bold-on-mobile">Manager biobrandstof <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/manager-productie-biobrandstof">
							Vacatures: 0<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/manager-duurzame-energie';"><a href="https://www.jobpersonality.com/manager-duurzame-energie" class="bold-on-mobile">Manager duurzame energie <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/manager-duurzame-energie">
							Vacatures: 3<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/inkoopmanager';"><a href="https://www.jobpersonality.com/inkoopmanager" class="bold-on-mobile">Inkoopmanager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/inkoopmanager">
							Vacatures: 2<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/transportmanager';"><a href="https://www.jobpersonality.com/transportmanager" class="bold-on-mobile">Transportmanager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/transportmanager">
							Vacatures: 0<br>
							Robotiserings%: 59%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/manager-opslag-distributie';"><a href="https://www.jobpersonality.com/manager-opslag-distributie" class="bold-on-mobile">Warehousemanager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/manager-opslag-distributie">
							Vacatures: 1<br>
							Robotiserings%: 59%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/manager-salaris-beloningsbeleid';"><a href="https://www.jobpersonality.com/manager-salaris-beloningsbeleid" class="bold-on-mobile">Compensation &amp; benefits manager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/manager-salaris-beloningsbeleid">
							Vacatures: 0<br>
							Robotiserings%: 96%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/human-resources-manager';"><a href="https://www.jobpersonality.com/human-resources-manager" class="bold-on-mobile">HR manager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/human-resources-manager">
							Vacatures: 85<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/training-ontwikkelingsmanager';"><a href="https://www.jobpersonality.com/training-ontwikkelingsmanager" class="bold-on-mobile">Opleidingsmanager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/training-ontwikkelingsmanager">
							Vacatures: 3<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/agrarier';"><a href="https://www.jobpersonality.com/agrarier" class="bold-on-mobile">Agrariër <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/agrarier">
							Vacatures: 4<br>
							Robotiserings%: 5%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/aquacultuurmanager';"><a href="https://www.jobpersonality.com/aquacultuurmanager" class="bold-on-mobile">Aquacultuurmanager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/aquacultuurmanager">
							Vacatures: 0<br>
							Robotiserings%: 5%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bouwmanager';"><a href="https://www.jobpersonality.com/bouwmanager" class="bold-on-mobile">Bouwmanager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bouwmanager">
							Vacatures: 2<br>
							Robotiserings%: 7%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bestuurder-kinderdagverblijf-peuterschool';"><a href="https://www.jobpersonality.com/bestuurder-kinderdagverblijf-peuterschool" class="bold-on-mobile">Vestigingsmanager kinderdagverblijf <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bestuurder-kinderdagverblijf-peuterschool">
							Vacatures: 0<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/coordinator-leren-op-afstand';"><a href="https://www.jobpersonality.com/coordinator-leren-op-afstand" class="bold-on-mobile">Manager e-learning <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/coordinator-leren-op-afstand">
							Vacatures: 0<br>
							Robotiserings%: 59%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/ontwikkelingsmanager-biobrandstof';"><a href="https://www.jobpersonality.com/ontwikkelingsmanager-biobrandstof" class="bold-on-mobile">Ontwikkelingsmanager biobrandstof <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/ontwikkelingsmanager-biobrandstof">
							Vacatures: 0<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/gezondheidszorgmanager';"><a href="https://www.jobpersonality.com/gezondheidszorgmanager" class="bold-on-mobile">Zorgmanager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/gezondheidszorgmanager">
							Vacatures: 3<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/specialist-waterbeheer';"><a href="https://www.jobpersonality.com/specialist-waterbeheer" class="bold-on-mobile">Adviseur waterbeheer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/specialist-waterbeheer">
							Vacatures: 1<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/manager-vastgoed';"><a href="https://www.jobpersonality.com/manager-vastgoed" class="bold-on-mobile">Manager vastgoed <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/manager-vastgoed">
							Vacatures: 5<br>
							Robotiserings%: 81%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/klantmanager-inkomen';"><a href="https://www.jobpersonality.com/klantmanager-inkomen" class="bold-on-mobile">Klantmanager inkomen <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/klantmanager-inkomen">
							Vacatures: 5<br>
							Robotiserings%: 70%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/crisis-en-calamiteitenmanager';"><a href="https://www.jobpersonality.com/crisis-en-calamiteitenmanager" class="bold-on-mobile">Crisis- en calamiteitenmanager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/crisis-en-calamiteitenmanager">
							Vacatures: 0<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/manager-regelgeving';"><a href="https://www.jobpersonality.com/manager-regelgeving" class="bold-on-mobile">Regulatory affairs manager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/manager-regelgeving">
							Vacatures: 0<br>
							Robotiserings%: 25%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/compliance-manager';"><a href="https://www.jobpersonality.com/compliance-manager" class="bold-on-mobile">Compliance officer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/compliance-manager">
							Vacatures: 9<br>
							Robotiserings%: 25%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/supply-chain-manager';"><a href="https://www.jobpersonality.com/supply-chain-manager" class="bold-on-mobile">Supply chain manager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/supply-chain-manager">
							Vacatures: 14<br>
							Robotiserings%: 25%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/manager-schadebeheersing';"><a href="https://www.jobpersonality.com/manager-schadebeheersing" class="bold-on-mobile">Manager schadebeheersing <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/manager-schadebeheersing">
							Vacatures: 0<br>
							Robotiserings%: 25%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/projectleider-bodem';"><a href="https://www.jobpersonality.com/projectleider-bodem" class="bold-on-mobile">Projectleider bodem <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/projectleider-bodem">
							Vacatures: 1<br>
							Robotiserings%: 25%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/zaakwaarnemer-voor-artiesten-en-atleten';"><a href="https://www.jobpersonality.com/zaakwaarnemer-voor-artiesten-en-atleten" class="bold-on-mobile">Zaakwaarnemer voor artiesten en atleten <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/zaakwaarnemer-voor-artiesten-en-atleten">
							Vacatures: 3<br>
							Robotiserings%: 24%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/inkoper-landbouwproducten';"><a href="https://www.jobpersonality.com/inkoper-landbouwproducten" class="bold-on-mobile">Inkoper landbouwproducten <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/inkoper-landbouwproducten">
							Vacatures: 1<br>
							Robotiserings%: 87%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/schadebehandelaar-eigendom-ongevallenverzekering';"><a href="https://www.jobpersonality.com/schadebehandelaar-eigendom-ongevallenverzekering" class="bold-on-mobile">Schadebehandelaar <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/schadebehandelaar-eigendom-ongevallenverzekering">
							Vacatures: 12<br>
							Robotiserings%: 98%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/inspecteur-swz';"><a href="https://www.jobpersonality.com/inspecteur-swz" class="bold-on-mobile">Inspecteur SWZ <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/inspecteur-swz">
							Vacatures: 0<br>
							Robotiserings%: 8%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/interne-specialist-regelgeving';"><a href="https://www.jobpersonality.com/interne-specialist-regelgeving" class="bold-on-mobile">Interne specialist regelgeving <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/interne-specialist-regelgeving">
							Vacatures: 0<br>
							Robotiserings%: 8%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/kostprijs-analist';"><a href="https://www.jobpersonality.com/kostprijs-analist" class="bold-on-mobile">Kostprijsdeskundige <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/kostprijs-analist">
							Vacatures: 2<br>
							Robotiserings%: 57%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/hr-specialist';"><a href="https://www.jobpersonality.com/hr-specialist" class="bold-on-mobile">HR specialist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/hr-specialist">
							Vacatures: 52<br>
							Robotiserings%: 31%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/deskundige-arbeidsrelaties';"><a href="https://www.jobpersonality.com/deskundige-arbeidsrelaties" class="bold-on-mobile">Deskundige arbeidsrelaties <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/deskundige-arbeidsrelaties">
							Vacatures: 0<br>
							Robotiserings%: 31%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/logistiek-specialist';"><a href="https://www.jobpersonality.com/logistiek-specialist" class="bold-on-mobile">Logistiek specialist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/logistiek-specialist">
							Vacatures: 9<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/logistiek-ingenieur';"><a href="https://www.jobpersonality.com/logistiek-ingenieur" class="bold-on-mobile">Logistiek engineer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/logistiek-ingenieur">
							Vacatures: 9<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/logistiek-analist';"><a href="https://www.jobpersonality.com/logistiek-analist" class="bold-on-mobile">Logistiek analist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/logistiek-analist">
							Vacatures: 1<br>
							Robotiserings%: 13%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/management-consultant';"><a href="https://www.jobpersonality.com/management-consultant" class="bold-on-mobile">Management consultant <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/management-consultant">
							Vacatures: 10<br>
							Robotiserings%: 13%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/fondsenwerver';"><a href="https://www.jobpersonality.com/fondsenwerver" class="bold-on-mobile">Fondsenwerver <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/fondsenwerver">
							Vacatures: 4<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/salaris-arbeidsvoorwaardenspecialist';"><a href="https://www.jobpersonality.com/salaris-arbeidsvoorwaardenspecialist" class="bold-on-mobile">Consultant compensation &amp; benefits <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/salaris-arbeidsvoorwaardenspecialist">
							Vacatures: 2<br>
							Robotiserings%: 47%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/specialist-training-ontwikkeling';"><a href="https://www.jobpersonality.com/specialist-training-ontwikkeling" class="bold-on-mobile">Trainer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/specialist-training-ontwikkeling">
							Vacatures: 132<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/specialist-beveiligingsmanagement';"><a href="https://www.jobpersonality.com/specialist-beveiligingsmanagement" class="bold-on-mobile">Veiligheidsadviseur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/specialist-beveiligingsmanagement">
							Vacatures: 5<br>
							Robotiserings%: 23%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/manager-bedrijfscontinuiteit';"><a href="https://www.jobpersonality.com/manager-bedrijfscontinuiteit" class="bold-on-mobile">Riskmanager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/manager-bedrijfscontinuiteit">
							Vacatures: 4<br>
							Robotiserings%: 23%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/specialist-duurzaamheid';"><a href="https://www.jobpersonality.com/specialist-duurzaamheid" class="bold-on-mobile">Adviseur duurzaamheid <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/specialist-duurzaamheid">
							Vacatures: 9<br>
							Robotiserings%: 23%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/online-verkoper';"><a href="https://www.jobpersonality.com/online-verkoper" class="bold-on-mobile">Online verkoper <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/online-verkoper">
							Vacatures: 0<br>
							Robotiserings%: 23%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/accountant';"><a href="https://www.jobpersonality.com/accountant" class="bold-on-mobile">Accountant <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/accountant">
							Vacatures: 266<br>
							Robotiserings%: 94%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/auditor';"><a href="https://www.jobpersonality.com/auditor" class="bold-on-mobile">Auditor <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/auditor">
							Vacatures: 52<br>
							Robotiserings%: 94%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/vastgoedtaxateur';"><a href="https://www.jobpersonality.com/vastgoedtaxateur" class="bold-on-mobile">Vastgoedtaxateur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/vastgoedtaxateur">
							Vacatures: 6<br>
							Robotiserings%: 90%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/budgetanalist';"><a href="https://www.jobpersonality.com/budgetanalist" class="bold-on-mobile">Budgetanalist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/budgetanalist">
							Vacatures: 0<br>
							Robotiserings%: 94%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/kredietanalist';"><a href="https://www.jobpersonality.com/kredietanalist" class="bold-on-mobile">Kredietanalist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/kredietanalist">
							Vacatures: 1<br>
							Robotiserings%: 98%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/financieel-analist';"><a href="https://www.jobpersonality.com/financieel-analist" class="bold-on-mobile">Financieel analist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/financieel-analist">
							Vacatures: 2<br>
							Robotiserings%: 23%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/persoonlijk-financieel-adviseur';"><a href="https://www.jobpersonality.com/persoonlijk-financieel-adviseur" class="bold-on-mobile">Persoonlijk financieel adviseur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/persoonlijk-financieel-adviseur">
							Vacatures: 0<br>
							Robotiserings%: 58%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/verzekeringsmakelaar';"><a href="https://www.jobpersonality.com/verzekeringsmakelaar" class="bold-on-mobile">Verzekeringsmakelaar <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/verzekeringsmakelaar">
							Vacatures: 1<br>
							Robotiserings%: 99%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/financieel-toezichthouder';"><a href="https://www.jobpersonality.com/financieel-toezichthouder" class="bold-on-mobile">Financieel toezichthouder <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/financieel-toezichthouder">
							Vacatures: 0<br>
							Robotiserings%: 17%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/schuldadviseur';"><a href="https://www.jobpersonality.com/schuldadviseur" class="bold-on-mobile">Schuldhulpverlener <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/schuldadviseur">
							Vacatures: 6<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/budgetcoach';"><a href="https://www.jobpersonality.com/budgetcoach" class="bold-on-mobile">Budgetcoach <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/budgetcoach">
							Vacatures: 14<br>
							Robotiserings%: 5%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/hypotheekadviseur';"><a href="https://www.jobpersonality.com/hypotheekadviseur" class="bold-on-mobile">Hypotheekadviseur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/hypotheekadviseur">
							Vacatures: 295<br>
							Robotiserings%: 98%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/belastinginspecteur';"><a href="https://www.jobpersonality.com/belastinginspecteur" class="bold-on-mobile">Belastinginspecteur  <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/belastinginspecteur">
							Vacatures: 0<br>
							Robotiserings%: 93%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/belastingconsulent-belastingadviseur';"><a href="https://www.jobpersonality.com/belastingconsulent-belastingadviseur" class="bold-on-mobile">Belastingadviseur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/belastingconsulent-belastingadviseur">
							Vacatures: 88<br>
							Robotiserings%: 99%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/kwantitatief-financieel-analist';"><a href="https://www.jobpersonality.com/kwantitatief-financieel-analist" class="bold-on-mobile">Kwantitatief financieel analist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/kwantitatief-financieel-analist">
							Vacatures: 0<br>
							Robotiserings%: 33%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/specialist-risicomanagement';"><a href="https://www.jobpersonality.com/specialist-risicomanagement" class="bold-on-mobile">Adviseur risicomanagement <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/specialist-risicomanagement">
							Vacatures: 0<br>
							Robotiserings%: 23%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/investeringsmakelaar';"><a href="https://www.jobpersonality.com/investeringsmakelaar" class="bold-on-mobile">Adviseur corporate finance <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/investeringsmakelaar">
							Vacatures: 1<br>
							Robotiserings%: 23%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/fraudebestrijder-onderzoeker';"><a href="https://www.jobpersonality.com/fraudebestrijder-onderzoeker" class="bold-on-mobile">Fraudebestrijder <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/fraudebestrijder-onderzoeker">
							Vacatures: 0<br>
							Robotiserings%: 23%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/business-analist';"><a href="https://www.jobpersonality.com/business-analist" class="bold-on-mobile">Business analist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/business-analist">
							Vacatures: 43<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/informaticaspecialist-verpleegkunde';"><a href="https://www.jobpersonality.com/informaticaspecialist-verpleegkunde" class="bold-on-mobile">IT consultant zorg <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/informaticaspecialist-verpleegkunde">
							Vacatures: 0<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/analist-databeveiliging';"><a href="https://www.jobpersonality.com/analist-databeveiliging" class="bold-on-mobile">Security specialist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/analist-databeveiliging">
							Vacatures: 29<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/programmeur';"><a href="https://www.jobpersonality.com/programmeur" class="bold-on-mobile">Programmeur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/programmeur">
							Vacatures: 50<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/softwareontwikkelaar';"><a href="https://www.jobpersonality.com/softwareontwikkelaar" class="bold-on-mobile">Software developer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/softwareontwikkelaar">
							Vacatures: 62<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/systeemontwikkelaar';"><a href="https://www.jobpersonality.com/systeemontwikkelaar" class="bold-on-mobile">Systeemontwikkelaar <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/systeemontwikkelaar">
							Vacatures: 0<br>
							Robotiserings%: 13%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/databasebeheerder';"><a href="https://www.jobpersonality.com/databasebeheerder" class="bold-on-mobile">Big data engineer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/databasebeheerder">
							Vacatures: 0<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/it-specialist';"><a href="https://www.jobpersonality.com/it-specialist" class="bold-on-mobile">IT specialist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/it-specialist">
							Vacatures: 116<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/computernetwerkontwerper';"><a href="https://www.jobpersonality.com/computernetwerkontwerper" class="bold-on-mobile">Netwerkontwerper <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/computernetwerkontwerper">
							Vacatures: 0<br>
							Robotiserings%: 22%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/netwerk-engineer-ontwerper';"><a href="https://www.jobpersonality.com/netwerk-engineer-ontwerper" class="bold-on-mobile">Netwerk engineer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/netwerk-engineer-ontwerper">
							Vacatures: 9<br>
							Robotiserings%: 22%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/geografisch-informatiewetenschapper';"><a href="https://www.jobpersonality.com/geografisch-informatiewetenschapper" class="bold-on-mobile">Geografisch data analist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/geografisch-informatiewetenschapper">
							Vacatures: 0<br>
							Robotiserings%: 22%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/technicus-geografische-informatie-systemen';"><a href="https://www.jobpersonality.com/technicus-geografische-informatie-systemen" class="bold-on-mobile">GIS engineer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/technicus-geografische-informatie-systemen">
							Vacatures: 3<br>
							Robotiserings%: 22%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/databaseontwerper-database-architect';"><a href="https://www.jobpersonality.com/databaseontwerper-database-architect" class="bold-on-mobile">Database architect <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/databaseontwerper-database-architect">
							Vacatures: 19<br>
							Robotiserings%: 22%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/datawarehouse-specialist';"><a href="https://www.jobpersonality.com/datawarehouse-specialist" class="bold-on-mobile">Datawarehouse specialist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/datawarehouse-specialist">
							Vacatures: 0<br>
							Robotiserings%: 22%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/data-analist';"><a href="https://www.jobpersonality.com/data-analist" class="bold-on-mobile">Data analist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/data-analist">
							Vacatures: 40<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/it-projectmanager';"><a href="https://www.jobpersonality.com/it-projectmanager" class="bold-on-mobile">IT projectmanager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/it-projectmanager">
							Vacatures: 12<br>
							Robotiserings%: 22%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/seo-specialist';"><a href="https://www.jobpersonality.com/seo-specialist" class="bold-on-mobile">SEO Specialist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/seo-specialist">
							Vacatures: 6<br>
							Robotiserings%: 22%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/internet-marketeer';"><a href="https://www.jobpersonality.com/internet-marketeer" class="bold-on-mobile">Online marketeer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/internet-marketeer">
							Vacatures: 30<br>
							Robotiserings%: 10%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/game-ontwerper';"><a href="https://www.jobpersonality.com/game-ontwerper" class="bold-on-mobile">Game developer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/game-ontwerper">
							Vacatures: 1<br>
							Robotiserings%: 22%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/informatie-analist';"><a href="https://www.jobpersonality.com/informatie-analist" class="bold-on-mobile">Informatie analist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/informatie-analist">
							Vacatures: 6<br>
							Robotiserings%: 22%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/actuaris-of-verzekeringswiskundige';"><a href="https://www.jobpersonality.com/actuaris-of-verzekeringswiskundige" class="bold-on-mobile">Actuaris <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/actuaris-of-verzekeringswiskundige">
							Vacatures: 0<br>
							Robotiserings%: 21%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/klinisch-dataspecialist';"><a href="https://www.jobpersonality.com/klinisch-dataspecialist" class="bold-on-mobile">Klinische dataspecialist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/klinisch-dataspecialist">
							Vacatures: 0<br>
							Robotiserings%: 22%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/wiskundig-specialist';"><a href="https://www.jobpersonality.com/wiskundig-specialist" class="bold-on-mobile">Wiskundig specialist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/wiskundig-specialist">
							Vacatures: 50<br>
							Robotiserings%: 99%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/architect';"><a href="https://www.jobpersonality.com/architect" class="bold-on-mobile">Architect <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/architect">
							Vacatures: 299<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/landschapsarchitect';"><a href="https://www.jobpersonality.com/landschapsarchitect" class="bold-on-mobile">Landschapsarchitect <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/landschapsarchitect">
							Vacatures: 3<br>
							Robotiserings%: 5%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/cartograaf';"><a href="https://www.jobpersonality.com/cartograaf" class="bold-on-mobile">Cartograaf <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/cartograaf">
							Vacatures: 0<br>
							Robotiserings%: 88%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/landmeter';"><a href="https://www.jobpersonality.com/landmeter" class="bold-on-mobile">Landmeter <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/landmeter">
							Vacatures: 6<br>
							Robotiserings%: 38%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/geodetisch-specialist';"><a href="https://www.jobpersonality.com/geodetisch-specialist" class="bold-on-mobile">Geodetische specialist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/geodetisch-specialist">
							Vacatures: 0<br>
							Robotiserings%: 38%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/vliegtuigbouwkundige';"><a href="https://www.jobpersonality.com/vliegtuigbouwkundige" class="bold-on-mobile">Vliegtuigbouwkundige <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/vliegtuigbouwkundige">
							Vacatures: 20<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/landbouwingenieur';"><a href="https://www.jobpersonality.com/landbouwingenieur" class="bold-on-mobile">Landbouwingenieur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/landbouwingenieur">
							Vacatures: 0<br>
							Robotiserings%: 49%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/biomedisch-ingenieur';"><a href="https://www.jobpersonality.com/biomedisch-ingenieur" class="bold-on-mobile">Biomedische ingenieur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/biomedisch-ingenieur">
							Vacatures: 1<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/scheikundig-ingenieur';"><a href="https://www.jobpersonality.com/scheikundig-ingenieur" class="bold-on-mobile">Chemisch technoloog <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/scheikundig-ingenieur">
							Vacatures: 12<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/civiel-ingenieur';"><a href="https://www.jobpersonality.com/civiel-ingenieur" class="bold-on-mobile">Civiel ingenieur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/civiel-ingenieur">
							Vacatures: 25<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/wegenbouwkundige';"><a href="https://www.jobpersonality.com/wegenbouwkundige" class="bold-on-mobile">Wegenbouwkundige <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/wegenbouwkundige">
							Vacatures: 5<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/computer-hardware-engineer';"><a href="https://www.jobpersonality.com/computer-hardware-engineer" class="bold-on-mobile">Hardware engineer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/computer-hardware-engineer">
							Vacatures: 46<br>
							Robotiserings%: 22%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/elektrisch-ingenieur';"><a href="https://www.jobpersonality.com/elektrisch-ingenieur" class="bold-on-mobile">Electrical engineer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/elektrisch-ingenieur">
							Vacatures: 111<br>
							Robotiserings%: 10%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/elektronisch-ingenieur';"><a href="https://www.jobpersonality.com/elektronisch-ingenieur" class="bold-on-mobile">Elektro engineer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/elektronisch-ingenieur">
							Vacatures: 5<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/waterbouwkundige';"><a href="https://www.jobpersonality.com/waterbouwkundige" class="bold-on-mobile">Waterbouwkundige <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/waterbouwkundige">
							Vacatures: 18<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/ingenieur-veiligheid-gezondheid';"><a href="https://www.jobpersonality.com/ingenieur-veiligheid-gezondheid" class="bold-on-mobile">Ingenieur veiligheid en gezondheid <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/ingenieur-veiligheid-gezondheid">
							Vacatures: 3<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/ingenieur-brandveiligheid';"><a href="https://www.jobpersonality.com/ingenieur-brandveiligheid" class="bold-on-mobile">Adviseur brandveiligheid <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/ingenieur-brandveiligheid">
							Vacatures: 5<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/ingenieur-productveiligheid';"><a href="https://www.jobpersonality.com/ingenieur-productveiligheid" class="bold-on-mobile">Safety engineer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/ingenieur-productveiligheid">
							Vacatures: 21<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/industrieel-ingenieur';"><a href="https://www.jobpersonality.com/industrieel-ingenieur" class="bold-on-mobile">Industrieel ingenieur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/industrieel-ingenieur">
							Vacatures: 2<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/scheepbouwkundig-ingenieur';"><a href="https://www.jobpersonality.com/scheepbouwkundig-ingenieur" class="bold-on-mobile">Scheepbouwkundig ingenieur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/scheepbouwkundig-ingenieur">
							Vacatures: 7<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/scheepsbouwkundig-ontwerper';"><a href="https://www.jobpersonality.com/scheepsbouwkundig-ontwerper" class="bold-on-mobile">Scheepsbouwkundig ontwerper <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/scheepsbouwkundig-ontwerper">
							Vacatures: 2<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/materiaalkundig-ingenieur';"><a href="https://www.jobpersonality.com/materiaalkundig-ingenieur" class="bold-on-mobile">Material engineer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/materiaalkundig-ingenieur">
							Vacatures: 9<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/werktuigbouwkundige';"><a href="https://www.jobpersonality.com/werktuigbouwkundige" class="bold-on-mobile">Werktuigbouwkundige <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/werktuigbouwkundige">
							Vacatures: 3<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/automotive-ingenieur';"><a href="https://www.jobpersonality.com/automotive-ingenieur" class="bold-on-mobile">Engineer automotive <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/automotive-ingenieur">
							Vacatures: 10<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/mijnbouwkundige-ingenieur';"><a href="https://www.jobpersonality.com/mijnbouwkundige-ingenieur" class="bold-on-mobile">Mijnbouwkundige ingenieur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/mijnbouwkundige-ingenieur">
							Vacatures: 0<br>
							Robotiserings%: 14%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/nucleair-ingenieur';"><a href="https://www.jobpersonality.com/nucleair-ingenieur" class="bold-on-mobile">Nucleair ingenieur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/nucleair-ingenieur">
							Vacatures: 0<br>
							Robotiserings%: 7%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/ingenieur-olie-industrie';"><a href="https://www.jobpersonality.com/ingenieur-olie-industrie" class="bold-on-mobile">Ingenieur olie-industrie <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/ingenieur-olie-industrie">
							Vacatures: 0<br>
							Robotiserings%: 16%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/biochemische-ingenieur';"><a href="https://www.jobpersonality.com/biochemische-ingenieur" class="bold-on-mobile">Biochemische ingenieur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/biochemische-ingenieur">
							Vacatures: 0<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/ingenieur-procesbeheersing';"><a href="https://www.jobpersonality.com/ingenieur-procesbeheersing" class="bold-on-mobile">Quality engineer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/ingenieur-procesbeheersing">
							Vacatures: 45<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/energie-ingenieur';"><a href="https://www.jobpersonality.com/energie-ingenieur" class="bold-on-mobile">Energie-ingenieur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/energie-ingenieur">
							Vacatures: 25<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/productie-ingenieur';"><a href="https://www.jobpersonality.com/productie-ingenieur" class="bold-on-mobile">Productie ingenieur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/productie-ingenieur">
							Vacatures: 39<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/ingenieur-mechatronica';"><a href="https://www.jobpersonality.com/ingenieur-mechatronica" class="bold-on-mobile">Mechatronica engineer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/ingenieur-mechatronica">
							Vacatures: 15<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/ingenieur-fotonica';"><a href="https://www.jobpersonality.com/ingenieur-fotonica" class="bold-on-mobile">Ingenieur fotonica <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/ingenieur-fotonica">
							Vacatures: 0<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/ingenieur-robotica';"><a href="https://www.jobpersonality.com/ingenieur-robotica" class="bold-on-mobile">Robotics engineer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/ingenieur-robotica">
							Vacatures: 1<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/ingenieur-windenergie';"><a href="https://www.jobpersonality.com/ingenieur-windenergie" class="bold-on-mobile">Ingenieur windenergie <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/ingenieur-windenergie">
							Vacatures: 5<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/ingenieur-zonneergie';"><a href="https://www.jobpersonality.com/ingenieur-zonneergie" class="bold-on-mobile">Ingenieur zonne-energie <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/ingenieur-zonneergie">
							Vacatures: 2<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bouwkundig-tekenaar';"><a href="https://www.jobpersonality.com/bouwkundig-tekenaar" class="bold-on-mobile">Bouwkundig tekenaar <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bouwkundig-tekenaar">
							Vacatures: 27<br>
							Robotiserings%: 52%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/vliegtuigbouwkundig-technicus';"><a href="https://www.jobpersonality.com/vliegtuigbouwkundig-technicus" class="bold-on-mobile">Vliegtuigbouwkundig technicus <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/vliegtuigbouwkundig-technicus">
							Vacatures: 0<br>
							Robotiserings%: 48%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/milieutechnicus';"><a href="https://www.jobpersonality.com/milieutechnicus" class="bold-on-mobile">Milieutechnicus <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/milieutechnicus">
							Vacatures: 0<br>
							Robotiserings%: 25%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/procestechnoloog';"><a href="https://www.jobpersonality.com/procestechnoloog" class="bold-on-mobile">Procestechnoloog <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/procestechnoloog">
							Vacatures: 12<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/elektrotechnisch-technoloog';"><a href="https://www.jobpersonality.com/elektrotechnisch-technoloog" class="bold-on-mobile">Elektrotechnisch engineer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/elektrotechnisch-technoloog">
							Vacatures: 37<br>
							Robotiserings%: 24%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/elektromechanicus';"><a href="https://www.jobpersonality.com/elektromechanicus" class="bold-on-mobile">Coördinator elektromechanica <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/elektromechanicus">
							Vacatures: 0<br>
							Robotiserings%: 24%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/productieplanner';"><a href="https://www.jobpersonality.com/productieplanner" class="bold-on-mobile">Productieplanner <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/productieplanner">
							Vacatures: 30<br>
							Robotiserings%: 24%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/productietechnicus';"><a href="https://www.jobpersonality.com/productietechnicus" class="bold-on-mobile">Productietechnicus <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/productietechnicus">
							Vacatures: 0<br>
							Robotiserings%: 24%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/nanotechnologische-ingenieur';"><a href="https://www.jobpersonality.com/nanotechnologische-ingenieur" class="bold-on-mobile">Nanotechnologist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/nanotechnologische-ingenieur">
							Vacatures: 0<br>
							Robotiserings%: 24%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/voedingsmiddelentechnoloog';"><a href="https://www.jobpersonality.com/voedingsmiddelentechnoloog" class="bold-on-mobile">Levensmiddelentechnoloog <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/voedingsmiddelentechnoloog">
							Vacatures: 0<br>
							Robotiserings%: 8%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/specialist-water-bodembehoud';"><a href="https://www.jobpersonality.com/specialist-water-bodembehoud" class="bold-on-mobile">Specialist water- en bodembehoud <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/specialist-water-bodembehoud">
							Vacatures: 10<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/beheerder-buitengebied';"><a href="https://www.jobpersonality.com/beheerder-buitengebied" class="bold-on-mobile">Beheerder buitengebied <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/beheerder-buitengebied">
							Vacatures: 0<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/publieksvoorlichter';"><a href="https://www.jobpersonality.com/publieksvoorlichter" class="bold-on-mobile">Publieksvoorlichter <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/publieksvoorlichter">
							Vacatures: 0<br>
							Robotiserings%: 96%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/meteoroloog-ruimtewetenschapper';"><a href="https://www.jobpersonality.com/meteoroloog-ruimtewetenschapper" class="bold-on-mobile">Meteoroloog <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/meteoroloog-ruimtewetenschapper">
							Vacatures: 0<br>
							Robotiserings%: 67%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/milieu-en-gezondheidswetenschapper';"><a href="https://www.jobpersonality.com/milieu-en-gezondheidswetenschapper" class="bold-on-mobile">Gezondheidswetenschapper <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/milieu-en-gezondheidswetenschapper">
							Vacatures: 0<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/geowetenschapper';"><a href="https://www.jobpersonality.com/geowetenschapper" class="bold-on-mobile">Geoloog <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/geowetenschapper">
							Vacatures: 0<br>
							Robotiserings%: 63%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/hydroloog';"><a href="https://www.jobpersonality.com/hydroloog" class="bold-on-mobile">Hydroloog <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/hydroloog">
							Vacatures: 1<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/archeoloog';"><a href="https://www.jobpersonality.com/archeoloog" class="bold-on-mobile">Archeoloog <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/archeoloog">
							Vacatures: 0<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/transportdeskundige';"><a href="https://www.jobpersonality.com/transportdeskundige" class="bold-on-mobile">Transportdeskundige <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/transportdeskundige">
							Vacatures: 17<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/biologisch-laborant';"><a href="https://www.jobpersonality.com/biologisch-laborant" class="bold-on-mobile">Biologisch laborant <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/biologisch-laborant">
							Vacatures: 0<br>
							Robotiserings%: 30%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/geologisch-technicus';"><a href="https://www.jobpersonality.com/geologisch-technicus" class="bold-on-mobile">Geotechnical engineer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/geologisch-technicus">
							Vacatures: 0<br>
							Robotiserings%: 91%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/operationeel-technicus-kerncentrales';"><a href="https://www.jobpersonality.com/operationeel-technicus-kerncentrales" class="bold-on-mobile">Hoofdwerktuigkundige kerncentrale <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/operationeel-technicus-kerncentrales">
							Vacatures: 0<br>
							Robotiserings%: 85%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/onderzoeksassistent';"><a href="https://www.jobpersonality.com/onderzoeksassistent" class="bold-on-mobile">Onderzoeksassistent <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/onderzoeksassistent">
							Vacatures: 0<br>
							Robotiserings%: 65%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/beleidsmedewerker-ruimtelijke-ordening';"><a href="https://www.jobpersonality.com/beleidsmedewerker-ruimtelijke-ordening" class="bold-on-mobile">Beleidsmedewerker ruimtelijke ordening <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/beleidsmedewerker-ruimtelijke-ordening">
							Vacatures: 1<br>
							Robotiserings%: 65%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medewerker-milieu-en-gezondheidsdiensten';"><a href="https://www.jobpersonality.com/medewerker-milieu-en-gezondheidsdiensten" class="bold-on-mobile">Onderzoeker milieu- en gezondheidsdiensten <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medewerker-milieu-en-gezondheidsdiensten">
							Vacatures: 0<br>
							Robotiserings%: 77%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/forensisch-expert';"><a href="https://www.jobpersonality.com/forensisch-expert" class="bold-on-mobile">Forensisch rechercheur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/forensisch-expert">
							Vacatures: 0<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/specialist-precisielandbouw';"><a href="https://www.jobpersonality.com/specialist-precisielandbouw" class="bold-on-mobile">Specialist precisielandbouw <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/specialist-precisielandbouw">
							Vacatures: 1<br>
							Robotiserings%: 61%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/teledetectietechnicus';"><a href="https://www.jobpersonality.com/teledetectietechnicus" class="bold-on-mobile">Teledetectietechnicus <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/teledetectietechnicus">
							Vacatures: 0<br>
							Robotiserings%: 61%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/ambulant-begeleider';"><a href="https://www.jobpersonality.com/ambulant-begeleider" class="bold-on-mobile">Ambulant begeleider <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/ambulant-begeleider">
							Vacatures: 13<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/decaan';"><a href="https://www.jobpersonality.com/decaan" class="bold-on-mobile">Decaan <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/decaan">
							Vacatures: 1<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/maatschappelijk-werker-jeugd-gezin';"><a href="https://www.jobpersonality.com/maatschappelijk-werker-jeugd-gezin" class="bold-on-mobile">Jeugdconsulent <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/maatschappelijk-werker-jeugd-gezin">
							Vacatures: 18<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/maatschappelijk-werker-gezondheidszorg';"><a href="https://www.jobpersonality.com/maatschappelijk-werker-gezondheidszorg" class="bold-on-mobile">Maatschappelijk werker gezondheidszorg <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/maatschappelijk-werker-gezondheidszorg">
							Vacatures: 35<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/maatschappelijk-werker-psychiatrie';"><a href="https://www.jobpersonality.com/maatschappelijk-werker-psychiatrie" class="bold-on-mobile">Maatschappelijk werker psychiatrie <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/maatschappelijk-werker-psychiatrie">
							Vacatures: 35<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/maatschappelijk-werker-verslavingszorg';"><a href="https://www.jobpersonality.com/maatschappelijk-werker-verslavingszorg" class="bold-on-mobile">Maatschappelijk werker verslavingszorg <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/maatschappelijk-werker-verslavingszorg">
							Vacatures: 35<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/gezondheidsdeskundige';"><a href="https://www.jobpersonality.com/gezondheidsdeskundige" class="bold-on-mobile">Adviseur gezondheidsbevordering <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/gezondheidsdeskundige">
							Vacatures: 0<br>
							Robotiserings%: 5%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medewerker-re-integratie-reclassering';"><a href="https://www.jobpersonality.com/medewerker-re-integratie-reclassering" class="bold-on-mobile">Reclasseringswerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medewerker-re-integratie-reclassering">
							Vacatures: 0<br>
							Robotiserings%: 25%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/maatschappelijk-werker';"><a href="https://www.jobpersonality.com/maatschappelijk-werker" class="bold-on-mobile">Maatschappelijk werker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/maatschappelijk-werker">
							Vacatures: 35<br>
							Robotiserings%: 13%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/gezondheidswerker';"><a href="https://www.jobpersonality.com/gezondheidswerker" class="bold-on-mobile">Gezondheidswerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/gezondheidswerker">
							Vacatures: 0<br>
							Robotiserings%: 13%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/docent-bedrijfskunde';"><a href="https://www.jobpersonality.com/docent-bedrijfskunde" class="bold-on-mobile">Docent bedrijfskunde <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/docent-bedrijfskunde">
							Vacatures: 0<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/docent-informatica';"><a href="https://www.jobpersonality.com/docent-informatica" class="bold-on-mobile">Docent ICT <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/docent-informatica">
							Vacatures: 3<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/docent-rekenen';"><a href="https://www.jobpersonality.com/docent-rekenen" class="bold-on-mobile">Docent rekenen <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/docent-rekenen">
							Vacatures: 13<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/docent-bouwkunde';"><a href="https://www.jobpersonality.com/docent-bouwkunde" class="bold-on-mobile">Docent bouwkunde <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/docent-bouwkunde">
							Vacatures: 0<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/docent-landbouwwetenschap';"><a href="https://www.jobpersonality.com/docent-landbouwwetenschap" class="bold-on-mobile">Docent agrotechniek <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/docent-landbouwwetenschap">
							Vacatures: 0<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/docent-biologie-hoger-onderwijs';"><a href="https://www.jobpersonality.com/docent-biologie-hoger-onderwijs" class="bold-on-mobile">Docent biologie <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/docent-biologie-hoger-onderwijs">
							Vacatures: 6<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/docent-groen';"><a href="https://www.jobpersonality.com/docent-groen" class="bold-on-mobile">Docent groen <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/docent-groen">
							Vacatures: 0<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/docent-natuurwetenschappen';"><a href="https://www.jobpersonality.com/docent-natuurwetenschappen" class="bold-on-mobile">Docent natuurwetenschappen <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/docent-natuurwetenschappen">
							Vacatures: 35<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/docent-scheikunde';"><a href="https://www.jobpersonality.com/docent-scheikunde" class="bold-on-mobile">Docent scheikunde <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/docent-scheikunde">
							Vacatures: 11<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/docent-milieuwetenschap';"><a href="https://www.jobpersonality.com/docent-milieuwetenschap" class="bold-on-mobile">Docent milieuwetenschappen <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/docent-milieuwetenschap">
							Vacatures: 0<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/docent-natuurkunde';"><a href="https://www.jobpersonality.com/docent-natuurkunde" class="bold-on-mobile">Docent natuurkunde <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/docent-natuurkunde">
							Vacatures: 35<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/docent-antropologie';"><a href="https://www.jobpersonality.com/docent-antropologie" class="bold-on-mobile">Docent antropologie <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/docent-antropologie">
							Vacatures: 0<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/docent-minderhedenstudies';"><a href="https://www.jobpersonality.com/docent-minderhedenstudies" class="bold-on-mobile">Docent minderhedenstudies <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/docent-minderhedenstudies">
							Vacatures: 0<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/docent-economie';"><a href="https://www.jobpersonality.com/docent-economie" class="bold-on-mobile">Docent economie <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/docent-economie">
							Vacatures: 4<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/docent-geografie';"><a href="https://www.jobpersonality.com/docent-geografie" class="bold-on-mobile">Docent aardrijkskunde  <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/docent-geografie">
							Vacatures: 10<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/docent-politicologie';"><a href="https://www.jobpersonality.com/docent-politicologie" class="bold-on-mobile">Docent politicologie <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/docent-politicologie">
							Vacatures: 0<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/docent-maatschappijleer';"><a href="https://www.jobpersonality.com/docent-maatschappijleer" class="bold-on-mobile">Docent maatschappijleer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/docent-maatschappijleer">
							Vacatures: 2<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/docent-verpleegkunde';"><a href="https://www.jobpersonality.com/docent-verpleegkunde" class="bold-on-mobile">Docent verpleegkunde <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/docent-verpleegkunde">
							Vacatures: 1<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/docent-pedagogiek';"><a href="https://www.jobpersonality.com/docent-pedagogiek" class="bold-on-mobile">Docent pedagogiek <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/docent-pedagogiek">
							Vacatures: 0<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/docent-bibliotheekwetenschap';"><a href="https://www.jobpersonality.com/docent-bibliotheekwetenschap" class="bold-on-mobile">Docent bibliotheekwetenschap <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/docent-bibliotheekwetenschap">
							Vacatures: 0<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/docent-maatschappelijk-werk';"><a href="https://www.jobpersonality.com/docent-maatschappelijk-werk" class="bold-on-mobile">Docent maatschappelijk werk <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/docent-maatschappelijk-werk">
							Vacatures: 1<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/docent-beeldende-kunst-en-vormgeving';"><a href="https://www.jobpersonality.com/docent-beeldende-kunst-en-vormgeving" class="bold-on-mobile">Docent beeldende vorming <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/docent-beeldende-kunst-en-vormgeving">
							Vacatures: 0<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/docent-communicatie';"><a href="https://www.jobpersonality.com/docent-communicatie" class="bold-on-mobile">Docent communicatie <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/docent-communicatie">
							Vacatures: 0<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/docent-nederlands-literatuur';"><a href="https://www.jobpersonality.com/docent-nederlands-literatuur" class="bold-on-mobile">Docent Nederlands <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/docent-nederlands-literatuur">
							Vacatures: 52<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/docent-vreemde-talen-literatuur';"><a href="https://www.jobpersonality.com/docent-vreemde-talen-literatuur" class="bold-on-mobile">Docent vreemde talen <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/docent-vreemde-talen-literatuur">
							Vacatures: 33<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/docent-geschiedenis';"><a href="https://www.jobpersonality.com/docent-geschiedenis" class="bold-on-mobile">Docent geschiedenis <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/docent-geschiedenis">
							Vacatures: 3<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/docent-filosofie';"><a href="https://www.jobpersonality.com/docent-filosofie" class="bold-on-mobile">Docent filosofie <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/docent-filosofie">
							Vacatures: 0<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/docent-zorg-en-welzijn';"><a href="https://www.jobpersonality.com/docent-zorg-en-welzijn" class="bold-on-mobile">Docent zorg en welzijn <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/docent-zorg-en-welzijn">
							Vacatures: 9<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/docent-vrijetijdskunde-sportwetenschap';"><a href="https://www.jobpersonality.com/docent-vrijetijdskunde-sportwetenschap" class="bold-on-mobile">Docent sportacademie <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/docent-vrijetijdskunde-sportwetenschap">
							Vacatures: 0<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/docent-techniek';"><a href="https://www.jobpersonality.com/docent-techniek" class="bold-on-mobile">Docent techniek <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/docent-techniek">
							Vacatures: 8<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/leraar-basisonderwijs';"><a href="https://www.jobpersonality.com/leraar-basisonderwijs" class="bold-on-mobile">Leerkracht basisonderwijs <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/leraar-basisonderwijs">
							Vacatures: 7<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/leraar-voortgezet-onderwijs';"><a href="https://www.jobpersonality.com/leraar-voortgezet-onderwijs" class="bold-on-mobile">Docent voortgezet onderwijs <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/leraar-voortgezet-onderwijs">
							Vacatures: 2<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/wiskundeleraar';"><a href="https://www.jobpersonality.com/wiskundeleraar" class="bold-on-mobile">Docent wiskunde <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/wiskundeleraar">
							Vacatures: 22<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/docent-science';"><a href="https://www.jobpersonality.com/docent-science" class="bold-on-mobile">Docent science <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/docent-science">
							Vacatures: 0<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/leerkracht-so';"><a href="https://www.jobpersonality.com/leerkracht-so" class="bold-on-mobile">Leerkracht SO <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/leerkracht-so">
							Vacatures: 3<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/onderwijzer-speciaal-basisonderwijs';"><a href="https://www.jobpersonality.com/onderwijzer-speciaal-basisonderwijs" class="bold-on-mobile">Leerkracht speciaal basisonderwijs <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/onderwijzer-speciaal-basisonderwijs">
							Vacatures: 2<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/docent-speciaal-onderwijs';"><a href="https://www.jobpersonality.com/docent-speciaal-onderwijs" class="bold-on-mobile">Docent speciaal onderwijs <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/docent-speciaal-onderwijs">
							Vacatures: 6<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/gespecialiseerde-gymnastiekdocent';"><a href="https://www.jobpersonality.com/gespecialiseerde-gymnastiekdocent" class="bold-on-mobile">Gespecialiseerde gymdocent <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/gespecialiseerde-gymnastiekdocent">
							Vacatures: 0<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/gymleraar';"><a href="https://www.jobpersonality.com/gymleraar" class="bold-on-mobile">Gymdocent <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/gymleraar">
							Vacatures: 0<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/remedial-teacher';"><a href="https://www.jobpersonality.com/remedial-teacher" class="bold-on-mobile">Remedial teacher <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/remedial-teacher">
							Vacatures: 3<br>
							Robotiserings%: 19%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/coach';"><a href="https://www.jobpersonality.com/coach" class="bold-on-mobile">Coach <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/coach">
							Vacatures: 856<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/conservator';"><a href="https://www.jobpersonality.com/conservator" class="bold-on-mobile">Conservator <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/conservator">
							Vacatures: 0<br>
							Robotiserings%: 59%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bibliotheektechnicus';"><a href="https://www.jobpersonality.com/bibliotheektechnicus" class="bold-on-mobile">Bibliotheektechnicus <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bibliotheektechnicus">
							Vacatures: 0<br>
							Robotiserings%: 99%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/art-director';"><a href="https://www.jobpersonality.com/art-director" class="bold-on-mobile">Art director <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/art-director">
							Vacatures: 0<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/kunstenaar';"><a href="https://www.jobpersonality.com/kunstenaar" class="bold-on-mobile">Kunstenaar <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/kunstenaar">
							Vacatures: 55<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/special-effects-editor';"><a href="https://www.jobpersonality.com/special-effects-editor" class="bold-on-mobile">Special effects editor <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/special-effects-editor">
							Vacatures: 0<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/industrieel-ontwerper';"><a href="https://www.jobpersonality.com/industrieel-ontwerper" class="bold-on-mobile">Industrieel ontwerper <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/industrieel-ontwerper">
							Vacatures: 0<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/grafisch-vormgever';"><a href="https://www.jobpersonality.com/grafisch-vormgever" class="bold-on-mobile">Grafisch vormgever <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/grafisch-vormgever">
							Vacatures: 0<br>
							Robotiserings%: 8%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/interieurarchitect';"><a href="https://www.jobpersonality.com/interieurarchitect" class="bold-on-mobile">Interieurarchitect <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/interieurarchitect">
							Vacatures: 0<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/galeriehouder';"><a href="https://www.jobpersonality.com/galeriehouder" class="bold-on-mobile">Galeriehouder <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/galeriehouder">
							Vacatures: 0<br>
							Robotiserings%: 10%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/producer';"><a href="https://www.jobpersonality.com/producer" class="bold-on-mobile">Producer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/producer">
							Vacatures: 598<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/regisseur';"><a href="https://www.jobpersonality.com/regisseur" class="bold-on-mobile">Regisseur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/regisseur">
							Vacatures: 111<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/programmadirecteur';"><a href="https://www.jobpersonality.com/programmadirecteur" class="bold-on-mobile">Programmadirecteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/programmadirecteur">
							Vacatures: 1<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/talentenscout';"><a href="https://www.jobpersonality.com/talentenscout" class="bold-on-mobile">Talentenscout <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/talentenscout">
							Vacatures: 1<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/sportcoach';"><a href="https://www.jobpersonality.com/sportcoach" class="bold-on-mobile">Sportcoach <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/sportcoach">
							Vacatures: 0<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/choreograaf';"><a href="https://www.jobpersonality.com/choreograaf" class="bold-on-mobile">Choreograaf <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/choreograaf">
							Vacatures: 0<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/dirigent';"><a href="https://www.jobpersonality.com/dirigent" class="bold-on-mobile">Dirigent <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/dirigent">
							Vacatures: 22<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/nieuwsanalist';"><a href="https://www.jobpersonality.com/nieuwsanalist" class="bold-on-mobile">Nieuwsanalist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/nieuwsanalist">
							Vacatures: 0<br>
							Robotiserings%: 7%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/verslaggever';"><a href="https://www.jobpersonality.com/verslaggever" class="bold-on-mobile">Verslaggever <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/verslaggever">
							Vacatures: 0<br>
							Robotiserings%: 11%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/pr-specialist';"><a href="https://www.jobpersonality.com/pr-specialist" class="bold-on-mobile">PR specialist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/pr-specialist">
							Vacatures: 0<br>
							Robotiserings%: 18%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/redacteur';"><a href="https://www.jobpersonality.com/redacteur" class="bold-on-mobile">Redacteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/redacteur">
							Vacatures: 0<br>
							Robotiserings%: 6%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/technische-schrijver';"><a href="https://www.jobpersonality.com/technische-schrijver" class="bold-on-mobile">Technisch schrijver <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/technische-schrijver">
							Vacatures: 0<br>
							Robotiserings%: 89%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/copywriter';"><a href="https://www.jobpersonality.com/copywriter" class="bold-on-mobile">Copywriter <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/copywriter">
							Vacatures: 3<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/auteur';"><a href="https://www.jobpersonality.com/auteur" class="bold-on-mobile">Auteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/auteur">
							Vacatures: 3<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/script-scenarioschrijver';"><a href="https://www.jobpersonality.com/script-scenarioschrijver" class="bold-on-mobile">Scenarioschrijver <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/script-scenarioschrijver">
							Vacatures: 0<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/vertaler';"><a href="https://www.jobpersonality.com/vertaler" class="bold-on-mobile">Vertaler <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/vertaler">
							Vacatures: 4<br>
							Robotiserings%: 38%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/tolk';"><a href="https://www.jobpersonality.com/tolk" class="bold-on-mobile">Tolk <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/tolk">
							Vacatures: 0<br>
							Robotiserings%: 38%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/dietist';"><a href="https://www.jobpersonality.com/dietist" class="bold-on-mobile">Diëtist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/dietist">
							Vacatures: 2<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/optometrist';"><a href="https://www.jobpersonality.com/optometrist" class="bold-on-mobile">Optometrist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/optometrist">
							Vacatures: 0<br>
							Robotiserings%: 14%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/anesthesiemedewerker';"><a href="https://www.jobpersonality.com/anesthesiemedewerker" class="bold-on-mobile">Anesthesiemedewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/anesthesiemedewerker">
							Vacatures: 1<br>
							Robotiserings%: 14%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/podotherapeut';"><a href="https://www.jobpersonality.com/podotherapeut" class="bold-on-mobile">Podotherapeut <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/podotherapeut">
							Vacatures: 0<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/ergotherapeut';"><a href="https://www.jobpersonality.com/ergotherapeut" class="bold-on-mobile">Ergotherapeut <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/ergotherapeut">
							Vacatures: 4<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/fysiotherapeut';"><a href="https://www.jobpersonality.com/fysiotherapeut" class="bold-on-mobile">Fysiotherapeut <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/fysiotherapeut">
							Vacatures: 6<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/assistent-radioloog';"><a href="https://www.jobpersonality.com/assistent-radioloog" class="bold-on-mobile">Radiodiagnostisch laborant <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/assistent-radioloog">
							Vacatures: 0<br>
							Robotiserings%: 34%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/recreatietherapeut';"><a href="https://www.jobpersonality.com/recreatietherapeut" class="bold-on-mobile">Recreatietherapeut <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/recreatietherapeut">
							Vacatures: 0<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/creatief-therapeut';"><a href="https://www.jobpersonality.com/creatief-therapeut" class="bold-on-mobile">Creatief therapeut <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/creatief-therapeut">
							Vacatures: 0<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/muziektherapeut';"><a href="https://www.jobpersonality.com/muziektherapeut" class="bold-on-mobile">Muziektherapeut <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/muziektherapeut">
							Vacatures: 0<br>
							Robotiserings%: 7%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/ademhalingstherapeut';"><a href="https://www.jobpersonality.com/ademhalingstherapeut" class="bold-on-mobile">Ademhalingstherapeut <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/ademhalingstherapeut">
							Vacatures: 0<br>
							Robotiserings%: 7%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/logopedist';"><a href="https://www.jobpersonality.com/logopedist" class="bold-on-mobile">Logopedist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/logopedist">
							Vacatures: 5<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/wijkverpleegkundige';"><a href="https://www.jobpersonality.com/wijkverpleegkundige" class="bold-on-mobile">Wijkverpleegkundige <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/wijkverpleegkundige">
							Vacatures: 1<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/verpleegkundige-spoedeisende-hulp';"><a href="https://www.jobpersonality.com/verpleegkundige-spoedeisende-hulp" class="bold-on-mobile">Spoedeisende Hulp Verpleegkundige <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/verpleegkundige-spoedeisende-hulp">
							Vacatures: 0<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/verpleegkundige-psychiatrie';"><a href="https://www.jobpersonality.com/verpleegkundige-psychiatrie" class="bold-on-mobile">Verpleegkundige psychiatrie <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/verpleegkundige-psychiatrie">
							Vacatures: 0<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/verpleegkundige-intensive-care';"><a href="https://www.jobpersonality.com/verpleegkundige-intensive-care" class="bold-on-mobile">Verpleegkundige intensive care <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/verpleegkundige-intensive-care">
							Vacatures: 0<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/hoofdverpleegkundige';"><a href="https://www.jobpersonality.com/hoofdverpleegkundige" class="bold-on-mobile">hoofdverpleegkundige <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/hoofdverpleegkundige">
							Vacatures: 0<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/anesthesieverpleegkundige';"><a href="https://www.jobpersonality.com/anesthesieverpleegkundige" class="bold-on-mobile">Recovery verpleegkundige <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/anesthesieverpleegkundige">
							Vacatures: 0<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/verloskundig-verpleegkundige';"><a href="https://www.jobpersonality.com/verloskundig-verpleegkundige" class="bold-on-mobile">Verloskundig verpleegkundige <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/verloskundig-verpleegkundige">
							Vacatures: 0<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/hbo-verpleegkundige';"><a href="https://www.jobpersonality.com/hbo-verpleegkundige" class="bold-on-mobile">Hbo-verpleegkundige <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/hbo-verpleegkundige">
							Vacatures: 9<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/acupuncturist';"><a href="https://www.jobpersonality.com/acupuncturist" class="bold-on-mobile">Acupuncturist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/acupuncturist">
							Vacatures: 2<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/orthoptist';"><a href="https://www.jobpersonality.com/orthoptist" class="bold-on-mobile">Orthoptist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/orthoptist">
							Vacatures: 0<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medisch-klinisch-laboratoriumonderzoeker';"><a href="https://www.jobpersonality.com/medisch-klinisch-laboratoriumonderzoeker" class="bold-on-mobile">Medisch laboratoriumonderzoeker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medisch-klinisch-laboratoriumonderzoeker">
							Vacatures: 0<br>
							Robotiserings%: 90%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/cytogenetisch-onderzoeker';"><a href="https://www.jobpersonality.com/cytogenetisch-onderzoeker" class="bold-on-mobile">Cytogenetisch onderzoeker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/cytogenetisch-onderzoeker">
							Vacatures: 0<br>
							Robotiserings%: 90%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/mondhygienist';"><a href="https://www.jobpersonality.com/mondhygienist" class="bold-on-mobile">Mondhygiënist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/mondhygienist">
							Vacatures: 0<br>
							Robotiserings%: 68%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/echoscopist';"><a href="https://www.jobpersonality.com/echoscopist" class="bold-on-mobile">Echoscopist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/echoscopist">
							Vacatures: 0<br>
							Robotiserings%: 35%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/radiologische-technicus';"><a href="https://www.jobpersonality.com/radiologische-technicus" class="bold-on-mobile">Radiologische technicus <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/radiologische-technicus">
							Vacatures: 0<br>
							Robotiserings%: 23%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/hartfunctielaborant';"><a href="https://www.jobpersonality.com/hartfunctielaborant" class="bold-on-mobile">Hartfunctielaborant <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/hartfunctielaborant">
							Vacatures: 0<br>
							Robotiserings%: 47%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/operatieassistent';"><a href="https://www.jobpersonality.com/operatieassistent" class="bold-on-mobile">Operatieassistent <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/operatieassistent">
							Vacatures: 2<br>
							Robotiserings%: 35%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/adviseur-arbeidsomstandigheden';"><a href="https://www.jobpersonality.com/adviseur-arbeidsomstandigheden" class="bold-on-mobile">Arbo adviseur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/adviseur-arbeidsomstandigheden">
							Vacatures: 1<br>
							Robotiserings%: 17%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/verloskundige';"><a href="https://www.jobpersonality.com/verloskundige" class="bold-on-mobile">Verloskundige <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/verloskundige">
							Vacatures: 0<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/endoscopie-verpleegkundige';"><a href="https://www.jobpersonality.com/endoscopie-verpleegkundige" class="bold-on-mobile">Endoscopie verpleegkundige <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/endoscopie-verpleegkundige">
							Vacatures: 0<br>
							Robotiserings%: 34%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/deurwaarder';"><a href="https://www.jobpersonality.com/deurwaarder" class="bold-on-mobile">Deurwaarder <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/deurwaarder">
							Vacatures: 1<br>
							Robotiserings%: 36%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/rechercheur';"><a href="https://www.jobpersonality.com/rechercheur" class="bold-on-mobile">Rechercheur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/rechercheur">
							Vacatures: 1<br>
							Robotiserings%: 34%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/inlichtingenanalist';"><a href="https://www.jobpersonality.com/inlichtingenanalist" class="bold-on-mobile">Inlichtingenofficier <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/inlichtingenanalist">
							Vacatures: 0<br>
							Robotiserings%: 34%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/jachtopziener';"><a href="https://www.jobpersonality.com/jachtopziener" class="bold-on-mobile">Jachtopziener <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/jachtopziener">
							Vacatures: 0<br>
							Robotiserings%: 8%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/privedetective';"><a href="https://www.jobpersonality.com/privedetective" class="bold-on-mobile">Privédetective <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/privedetective">
							Vacatures: 7<br>
							Robotiserings%: 31%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/zelfstandig-hovenier';"><a href="https://www.jobpersonality.com/zelfstandig-hovenier" class="bold-on-mobile">Zelfstandig hovenier <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/zelfstandig-hovenier">
							Vacatures: 21<br>
							Robotiserings%: 35%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/verkoopmanager-groothandel';"><a href="https://www.jobpersonality.com/verkoopmanager-groothandel" class="bold-on-mobile">Verkoopmanager groothandel <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/verkoopmanager-groothandel">
							Vacatures: 0<br>
							Robotiserings%: 8%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/verzekeringsagent';"><a href="https://www.jobpersonality.com/verzekeringsagent" class="bold-on-mobile">Verzekeringsagent <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/verzekeringsagent">
							Vacatures: 0<br>
							Robotiserings%: 92%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/effectenhandelaar';"><a href="https://www.jobpersonality.com/effectenhandelaar" class="bold-on-mobile">Effectenhandelaar <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/effectenhandelaar">
							Vacatures: 0<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/energie-makelaar';"><a href="https://www.jobpersonality.com/energie-makelaar" class="bold-on-mobile">Energy broker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/energie-makelaar">
							Vacatures: 0<br>
							Robotiserings%: 97%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/makelaar';"><a href="https://www.jobpersonality.com/makelaar" class="bold-on-mobile">Makelaar <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/makelaar">
							Vacatures: 14<br>
							Robotiserings%: 97%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/vastgoedhandelaar';"><a href="https://www.jobpersonality.com/vastgoedhandelaar" class="bold-on-mobile">Vastgoedhandelaar <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/vastgoedhandelaar">
							Vacatures: 5<br>
							Robotiserings%: 86%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/sales-engineer';"><a href="https://www.jobpersonality.com/sales-engineer" class="bold-on-mobile">Sales engineer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/sales-engineer">
							Vacatures: 82<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/griffier-gemeenteraad-provinciale-staten';"><a href="https://www.jobpersonality.com/griffier-gemeenteraad-provinciale-staten" class="bold-on-mobile">Griffier volksvertegenwoordiging <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/griffier-gemeenteraad-provinciale-staten">
							Vacatures: 3<br>
							Robotiserings%: 46%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/patientvertegenwoordiger';"><a href="https://www.jobpersonality.com/patientvertegenwoordiger" class="bold-on-mobile">Casemanager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/patientvertegenwoordiger">
							Vacatures: 38<br>
							Robotiserings%: 25%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medewerker-etikettering';"><a href="https://www.jobpersonality.com/medewerker-etikettering" class="bold-on-mobile">Etiketteringsspecialist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medewerker-etikettering">
							Vacatures: 0<br>
							Robotiserings%: 40%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/proeflezer';"><a href="https://www.jobpersonality.com/proeflezer" class="bold-on-mobile">Proeflezer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/proeflezer">
							Vacatures: 0<br>
							Robotiserings%: 84%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/technisch-bio-informaticus';"><a href="https://www.jobpersonality.com/technisch-bio-informaticus" class="bold-on-mobile">Onderzoeksmedewerker bio-informatica <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/technisch-bio-informaticus">
							Vacatures: 0<br>
							Robotiserings%: 66%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/manager-viskwekerij';"><a href="https://www.jobpersonality.com/manager-viskwekerij" class="bold-on-mobile">Manager viskwekerij <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/manager-viskwekerij">
							Vacatures: 0<br>
							Robotiserings%: 57%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bouwinspecteur';"><a href="https://www.jobpersonality.com/bouwinspecteur" class="bold-on-mobile">Bouwkundig inspecteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bouwinspecteur">
							Vacatures: 1<br>
							Robotiserings%: 63%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/springmeester-explosievendeskundige';"><a href="https://www.jobpersonality.com/springmeester-explosievendeskundige" class="bold-on-mobile">Springmeester <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/springmeester-explosievendeskundige">
							Vacatures: 0<br>
							Robotiserings%: 48%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/coordinatoor-recycling';"><a href="https://www.jobpersonality.com/coordinatoor-recycling" class="bold-on-mobile">Coördinatoor recycling <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/coordinatoor-recycling">
							Vacatures: 0<br>
							Robotiserings%: 42%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/piloot';"><a href="https://www.jobpersonality.com/piloot" class="bold-on-mobile">Piloot <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/piloot">
							Vacatures: 0<br>
							Robotiserings%: 18%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/luchtverkeersleider';"><a href="https://www.jobpersonality.com/luchtverkeersleider" class="bold-on-mobile">Luchtverkeersleider <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/luchtverkeersleider">
							Vacatures: 1<br>
							Robotiserings%: 11%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/operationeel-manager';"><a href="https://www.jobpersonality.com/operationeel-manager" class="bold-on-mobile">Operationeel manager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/operationeel-manager">
							Vacatures: 55<br>
							Robotiserings%: 57%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/kapitein-zeevaart-of-scheepskapitein';"><a href="https://www.jobpersonality.com/kapitein-zeevaart-of-scheepskapitein" class="bold-on-mobile">Kapitein <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/kapitein-zeevaart-of-scheepskapitein">
							Vacatures: 52<br>
							Robotiserings%: 27%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/loods';"><a href="https://www.jobpersonality.com/loods" class="bold-on-mobile">Loods <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/loods">
							Vacatures: 65<br>
							Robotiserings%: 27%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/verkeerskundige';"><a href="https://www.jobpersonality.com/verkeerskundige" class="bold-on-mobile">Verkeerskundige <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/verkeerskundige">
							Vacatures: 19<br>
							Robotiserings%: 61%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/luchtvaartinspecteur';"><a href="https://www.jobpersonality.com/luchtvaartinspecteur" class="bold-on-mobile">Luchtvaartinspecteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/luchtvaartinspecteur">
							Vacatures: 0<br>
							Robotiserings%: 90%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/transportinspecteur';"><a href="https://www.jobpersonality.com/transportinspecteur" class="bold-on-mobile">Transportinspecteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/transportinspecteur">
							Vacatures: 11<br>
							Robotiserings%: 90%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/vrachtinspecteur';"><a href="https://www.jobpersonality.com/vrachtinspecteur" class="bold-on-mobile">Vrachtinspecteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/vrachtinspecteur">
							Vacatures: 0<br>
							Robotiserings%: 90%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/zorgcoordinator';"><a href="https://www.jobpersonality.com/zorgcoordinator" class="bold-on-mobile">Zorgcoördinator <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/zorgcoordinator">
							Vacatures: 2<br>
							Robotiserings%: 15%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/accountmanager';"><a href="https://www.jobpersonality.com/accountmanager" class="bold-on-mobile">Accountmanager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/accountmanager">
							Vacatures: 634<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/docent-duits';"><a href="https://www.jobpersonality.com/docent-duits" class="bold-on-mobile">Docent Duits <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/docent-duits">
							Vacatures: 40<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/futuroloog';"><a href="https://www.jobpersonality.com/futuroloog" class="bold-on-mobile">Trendwatcher <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/futuroloog">
							Vacatures: 0<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/illustrator';"><a href="https://www.jobpersonality.com/illustrator" class="bold-on-mobile">Illustrator <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/illustrator">
							Vacatures: 6<br>
							Robotiserings%: 8%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/arbeidsinspecteur';"><a href="https://www.jobpersonality.com/arbeidsinspecteur" class="bold-on-mobile">Arbeidsinspecteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/arbeidsinspecteur">
							Vacatures: 0<br>
							Robotiserings%: 10%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/motion-designer';"><a href="https://www.jobpersonality.com/motion-designer" class="bold-on-mobile">Motion designer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/motion-designer">
							Vacatures: 0<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/3d-printspecialist';"><a href="https://www.jobpersonality.com/3d-printspecialist" class="bold-on-mobile">3d printspecialist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/3d-printspecialist">
							Vacatures: 0<br>
							Robotiserings%: 8%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/crowdfunding-specialist';"><a href="https://www.jobpersonality.com/crowdfunding-specialist" class="bold-on-mobile">Crowdfunding specialist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/crowdfunding-specialist">
							Vacatures: 2<br>
							Robotiserings%: 10%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/aspergeteler';"><a href="https://www.jobpersonality.com/aspergeteler" class="bold-on-mobile">Aspergeteler <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/aspergeteler">
							Vacatures: 0<br>
							Robotiserings%: 5%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/cartoonist';"><a href="https://www.jobpersonality.com/cartoonist" class="bold-on-mobile">Cartoonist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/cartoonist">
							Vacatures: 0<br>
							Robotiserings%: 8%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/outplacementcoach';"><a href="https://www.jobpersonality.com/outplacementcoach" class="bold-on-mobile">Outplacementcoach <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/outplacementcoach">
							Vacatures: 0<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/loopbaanadviseur';"><a href="https://www.jobpersonality.com/loopbaanadviseur" class="bold-on-mobile">Loopbaanadviseur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/loopbaanadviseur">
							Vacatures: 0<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/tekstschrijver';"><a href="https://www.jobpersonality.com/tekstschrijver" class="bold-on-mobile">Tekstschrijver <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/tekstschrijver">
							Vacatures: 1<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/beleidsmedewerker';"><a href="https://www.jobpersonality.com/beleidsmedewerker" class="bold-on-mobile">Beleidsmedewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/beleidsmedewerker">
							Vacatures: 46<br>
							Robotiserings%: 13%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/wethouder';"><a href="https://www.jobpersonality.com/wethouder" class="bold-on-mobile">Wethouder <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/wethouder">
							Vacatures: 6<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/gemeenteraadslid';"><a href="https://www.jobpersonality.com/gemeenteraadslid" class="bold-on-mobile">Gemeenteraadslid <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/gemeenteraadslid">
							Vacatures: 0<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/creative-director';"><a href="https://www.jobpersonality.com/creative-director" class="bold-on-mobile">Creative Director <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/creative-director">
							Vacatures: 1<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/technisch-directeur-radio-tv';"><a href="https://www.jobpersonality.com/technisch-directeur-radio-tv" class="bold-on-mobile">Technisch directeur radio en tv <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/technisch-directeur-radio-tv">
							Vacatures: 0<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/physician-assistant';"><a href="https://www.jobpersonality.com/physician-assistant" class="bold-on-mobile">Physician Assistant <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/physician-assistant">
							Vacatures: 0<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/wmo-consulent';"><a href="https://www.jobpersonality.com/wmo-consulent" class="bold-on-mobile">WMO consulent <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/wmo-consulent">
							Vacatures: 36<br>
							Robotiserings%: 70%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/business-controller';"><a href="https://www.jobpersonality.com/business-controller" class="bold-on-mobile">Business controller <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/business-controller">
							Vacatures: 67<br>
							Robotiserings%: 13%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/controller';"><a href="https://www.jobpersonality.com/controller" class="bold-on-mobile">Controller <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/controller">
							Vacatures: 284<br>
							Robotiserings%: 7%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/financial-controller';"><a href="https://www.jobpersonality.com/financial-controller" class="bold-on-mobile">Financial controller <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/financial-controller">
							Vacatures: 104<br>
							Robotiserings%: 7%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/big-data-analist';"><a href="https://www.jobpersonality.com/big-data-analist" class="bold-on-mobile">Big data analist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/big-data-analist">
							Vacatures: 15<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/docent-engels';"><a href="https://www.jobpersonality.com/docent-engels" class="bold-on-mobile">Docent Engels <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/docent-engels">
							Vacatures: 27<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/docent';"><a href="https://www.jobpersonality.com/docent" class="bold-on-mobile">Docent <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/docent">
							Vacatures: 751<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/docent-archeologie';"><a href="https://www.jobpersonality.com/docent-archeologie" class="bold-on-mobile">Docent archeologie <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/docent-archeologie">
							Vacatures: 0<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/muziekdocent';"><a href="https://www.jobpersonality.com/muziekdocent" class="bold-on-mobile">Muziekdocent <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/muziekdocent">
							Vacatures: 0<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/test-engineer';"><a href="https://www.jobpersonality.com/test-engineer" class="bold-on-mobile">Test engineer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/test-engineer">
							Vacatures: 48<br>
							Robotiserings%: 22%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/recruiter';"><a href="https://www.jobpersonality.com/recruiter" class="bold-on-mobile">Recruiter <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/recruiter">
							Vacatures: 1963<br>
							Robotiserings%: 31%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/beeldend-therapeut';"><a href="https://www.jobpersonality.com/beeldend-therapeut" class="bold-on-mobile">Beeldend therapeut <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/beeldend-therapeut">
							Vacatures: 0<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/data-scientist';"><a href="https://www.jobpersonality.com/data-scientist" class="bold-on-mobile">Data scientist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/data-scientist">
							Vacatures: 8<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/operations-engineer';"><a href="https://www.jobpersonality.com/operations-engineer" class="bold-on-mobile">Operations Engineer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/operations-engineer">
							Vacatures: 10<br>
							Robotiserings%: 22%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/gis-specialist';"><a href="https://www.jobpersonality.com/gis-specialist" class="bold-on-mobile">GIS Specialist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/gis-specialist">
							Vacatures: 1<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/hoofdwerktuigkundige';"><a href="https://www.jobpersonality.com/hoofdwerktuigkundige" class="bold-on-mobile">Hoofdwerktuigkundige <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/hoofdwerktuigkundige">
							Vacatures: 0<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/visual-designer';"><a href="https://www.jobpersonality.com/visual-designer" class="bold-on-mobile">Visual designer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/visual-designer">
							Vacatures: 1<br>
							Robotiserings%: 8%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/hacker';"><a href="https://www.jobpersonality.com/hacker" class="bold-on-mobile">Ethical hacker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/hacker">
							Vacatures: 1<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/production-engineer';"><a href="https://www.jobpersonality.com/production-engineer" class="bold-on-mobile">Production engineer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/production-engineer">
							Vacatures: 24<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/product-engineer';"><a href="https://www.jobpersonality.com/product-engineer" class="bold-on-mobile">Product engineer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/product-engineer">
							Vacatures: 61<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/webshop-manager';"><a href="https://www.jobpersonality.com/webshop-manager" class="bold-on-mobile">Webshop manager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/webshop-manager">
							Vacatures: 0<br>
							Robotiserings%: 45%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/sea-specialist';"><a href="https://www.jobpersonality.com/sea-specialist" class="bold-on-mobile">SEA specialist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/sea-specialist">
							Vacatures: 1<br>
							Robotiserings%: 22%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/webredacteur';"><a href="https://www.jobpersonality.com/webredacteur" class="bold-on-mobile">Webredacteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/webredacteur">
							Vacatures: 0<br>
							Robotiserings%: 6%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/communicatiemedewerker';"><a href="https://www.jobpersonality.com/communicatiemedewerker" class="bold-on-mobile">Communicatiemedewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/communicatiemedewerker">
							Vacatures: 3<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/ios-developer';"><a href="https://www.jobpersonality.com/ios-developer" class="bold-on-mobile">iOS developer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/ios-developer">
							Vacatures: 0<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/cobol-programmeur';"><a href="https://www.jobpersonality.com/cobol-programmeur" class="bold-on-mobile">Cobol-programmeur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/cobol-programmeur">
							Vacatures: 1<br>
							Robotiserings%: 48%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/social-media-specialist';"><a href="https://www.jobpersonality.com/social-media-specialist" class="bold-on-mobile">Social media specialist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/social-media-specialist">
							Vacatures: 0<br>
							Robotiserings%: 10%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/php-developer';"><a href="https://www.jobpersonality.com/php-developer" class="bold-on-mobile">PHP developer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/php-developer">
							Vacatures: 22<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/net-developer';"><a href="https://www.jobpersonality.com/net-developer" class="bold-on-mobile">NET developer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/net-developer">
							Vacatures: 34<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/java-developer';"><a href="https://www.jobpersonality.com/java-developer" class="bold-on-mobile">Java developer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/java-developer">
							Vacatures: 37<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/journalist';"><a href="https://www.jobpersonality.com/journalist" class="bold-on-mobile">Journalist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/journalist">
							Vacatures: 0<br>
							Robotiserings%: 11%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/commercieel-directeur';"><a href="https://www.jobpersonality.com/commercieel-directeur" class="bold-on-mobile">Commercieel directeur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/commercieel-directeur">
							Vacatures: 13<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/category-manager';"><a href="https://www.jobpersonality.com/category-manager" class="bold-on-mobile">Category manager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/category-manager">
							Vacatures: 9<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/front-end-developer';"><a href="https://www.jobpersonality.com/front-end-developer" class="bold-on-mobile">Front-end developer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/front-end-developer">
							Vacatures: 13<br>
							Robotiserings%: 39%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/praktijkondersteuner';"><a href="https://www.jobpersonality.com/praktijkondersteuner" class="bold-on-mobile">Praktijkondersteuner <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/praktijkondersteuner">
							Vacatures: 3<br>
							Robotiserings%: 14%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/relatiemanager';"><a href="https://www.jobpersonality.com/relatiemanager" class="bold-on-mobile">Relatiemanager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/relatiemanager">
							Vacatures: 6<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/mensendiecktherapeut';"><a href="https://www.jobpersonality.com/mensendiecktherapeut" class="bold-on-mobile">Mensendiecktherapeut <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/mensendiecktherapeut">
							Vacatures: 0<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/manueel-therapeut';"><a href="https://www.jobpersonality.com/manueel-therapeut" class="bold-on-mobile">Manueel therapeut <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/manueel-therapeut">
							Vacatures: 0<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/back-end-developer';"><a href="https://www.jobpersonality.com/back-end-developer" class="bold-on-mobile">Back-end developer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/back-end-developer">
							Vacatures: 12<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/functioneel-beheerder';"><a href="https://www.jobpersonality.com/functioneel-beheerder" class="bold-on-mobile">Functioneel beheerder <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/functioneel-beheerder">
							Vacatures: 33<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/voedingsdeskundige';"><a href="https://www.jobpersonality.com/voedingsdeskundige" class="bold-on-mobile">Voedingsdeskundige <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/voedingsdeskundige">
							Vacatures: 0<br>
							Robotiserings%: 13%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/adviseur';"><a href="https://www.jobpersonality.com/adviseur" class="bold-on-mobile">Adviseur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/adviseur">
							Vacatures: 943<br>
							Robotiserings%: 13%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/handhavingsspecialist';"><a href="https://www.jobpersonality.com/handhavingsspecialist" class="bold-on-mobile">Medewerker handhaving <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/handhavingsspecialist">
							Vacatures: 8<br>
							Robotiserings%: 34%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/cdo';"><a href="https://www.jobpersonality.com/cdo" class="bold-on-mobile">CDO <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/cdo">
							Vacatures: 2<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bouwkundig-adviseur';"><a href="https://www.jobpersonality.com/bouwkundig-adviseur" class="bold-on-mobile">Bouwkundig adviseur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bouwkundig-adviseur">
							Vacatures: 4<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/implementatie-consultant';"><a href="https://www.jobpersonality.com/implementatie-consultant" class="bold-on-mobile">Implementatie consultant <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/implementatie-consultant">
							Vacatures: 10<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/marketing-consultant';"><a href="https://www.jobpersonality.com/marketing-consultant" class="bold-on-mobile">Marketing consultant <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/marketing-consultant">
							Vacatures: 1<br>
							Robotiserings%: 13%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/sap-consultant';"><a href="https://www.jobpersonality.com/sap-consultant" class="bold-on-mobile">SAP consultant <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/sap-consultant">
							Vacatures: 20<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/business-intelligence-consultant';"><a href="https://www.jobpersonality.com/business-intelligence-consultant" class="bold-on-mobile">Business intelligence consultant <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/business-intelligence-consultant">
							Vacatures: 14<br>
							Robotiserings%: 13%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/recruitment-consultant';"><a href="https://www.jobpersonality.com/recruitment-consultant" class="bold-on-mobile">Recruitment consultant <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/recruitment-consultant">
							Vacatures: 3012<br>
							Robotiserings%: 31%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/sales-consultant';"><a href="https://www.jobpersonality.com/sales-consultant" class="bold-on-mobile">Sales consultant <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/sales-consultant">
							Vacatures: 94<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/technisch-consultant';"><a href="https://www.jobpersonality.com/technisch-consultant" class="bold-on-mobile">Technisch consultant <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/technisch-consultant">
							Vacatures: 30<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/hr-adviseur';"><a href="https://www.jobpersonality.com/hr-adviseur" class="bold-on-mobile">HR consultant <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/hr-adviseur">
							Vacatures: 5<br>
							Robotiserings%: 31%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/security-consultant';"><a href="https://www.jobpersonality.com/security-consultant" class="bold-on-mobile">Security consultant <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/security-consultant">
							Vacatures: 13<br>
							Robotiserings%: 13%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/huiswerkbegeleider';"><a href="https://www.jobpersonality.com/huiswerkbegeleider" class="bold-on-mobile">Huiswerkbegeleider <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/huiswerkbegeleider">
							Vacatures: 3<br>
							Robotiserings%: 19%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/consulent-relatiebemiddeling';"><a href="https://www.jobpersonality.com/consulent-relatiebemiddeling" class="bold-on-mobile">Consulent relatiebemiddeling <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/consulent-relatiebemiddeling">
							Vacatures: 0<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/agile-coach';"><a href="https://www.jobpersonality.com/agile-coach" class="bold-on-mobile">Agile coach <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/agile-coach">
							Vacatures: 5<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/scrum-master';"><a href="https://www.jobpersonality.com/scrum-master" class="bold-on-mobile">Scrum Master <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/scrum-master">
							Vacatures: 48<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/content-marketeer';"><a href="https://www.jobpersonality.com/content-marketeer" class="bold-on-mobile">Content marketeer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/content-marketeer">
							Vacatures: 12<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/recruitment-manager';"><a href="https://www.jobpersonality.com/recruitment-manager" class="bold-on-mobile">Recruitment manager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/recruitment-manager">
							Vacatures: 22<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/business-developer';"><a href="https://www.jobpersonality.com/business-developer" class="bold-on-mobile">Business developer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/business-developer">
							Vacatures: 28<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/headhunter';"><a href="https://www.jobpersonality.com/headhunter" class="bold-on-mobile">Headhunter <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/headhunter">
							Vacatures: 30<br>
							Robotiserings%: 31%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bim-modelleur';"><a href="https://www.jobpersonality.com/bim-modelleur" class="bold-on-mobile">BIM Modelleur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bim-modelleur">
							Vacatures: 26<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/3d-ontwerper';"><a href="https://www.jobpersonality.com/3d-ontwerper" class="bold-on-mobile">3d ontwerper <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/3d-ontwerper">
							Vacatures: 1<br>
							Robotiserings%: 52%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/blockchain-developer';"><a href="https://www.jobpersonality.com/blockchain-developer" class="bold-on-mobile">Blockchain developer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/blockchain-developer">
							Vacatures: 0<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/contractmanager';"><a href="https://www.jobpersonality.com/contractmanager" class="bold-on-mobile">Contractmanager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/contractmanager">
							Vacatures: 47<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/functionaris-gegevensbescherming';"><a href="https://www.jobpersonality.com/functionaris-gegevensbescherming" class="bold-on-mobile">Functionaris gegevensbescherming <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/functionaris-gegevensbescherming">
							Vacatures: 11<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/communicatieadviseur';"><a href="https://www.jobpersonality.com/communicatieadviseur" class="bold-on-mobile">Communicatieadviseur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/communicatieadviseur">
							Vacatures: 15<br>
							Robotiserings%: 13%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/professional-organizer';"><a href="https://www.jobpersonality.com/professional-organizer" class="bold-on-mobile">Professional organizer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/professional-organizer">
							Vacatures: 0<br>
							Robotiserings%: 13%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/full-stack-developer';"><a href="https://www.jobpersonality.com/full-stack-developer" class="bold-on-mobile">Full stack developer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/full-stack-developer">
							Vacatures: 39<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/projectmanager';"><a href="https://www.jobpersonality.com/projectmanager" class="bold-on-mobile">Projectmanager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/projectmanager">
							Vacatures: 489<br>
							Robotiserings%: 22%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/belastingdeurwaarder';"><a href="https://www.jobpersonality.com/belastingdeurwaarder" class="bold-on-mobile">Belastingdeurwaarder <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/belastingdeurwaarder">
							Vacatures: 0<br>
							Robotiserings%: 36%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/procesmanager';"><a href="https://www.jobpersonality.com/procesmanager" class="bold-on-mobile">Procesmanager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/procesmanager">
							Vacatures: 27<br>
							Robotiserings%: 13%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/c-developer';"><a href="https://www.jobpersonality.com/c-developer" class="bold-on-mobile">C# developer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/c-developer">
							Vacatures: 71<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/knf-laborant';"><a href="https://www.jobpersonality.com/knf-laborant" class="bold-on-mobile">KNF-laborant <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/knf-laborant">
							Vacatures: 0<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/product-owner';"><a href="https://www.jobpersonality.com/product-owner" class="bold-on-mobile">Product owner <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/product-owner">
							Vacatures: 132<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/projectleider';"><a href="https://www.jobpersonality.com/projectleider" class="bold-on-mobile">Projectleider <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/projectleider">
							Vacatures: 1271<br>
							Robotiserings%: 7%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/software-engineer';"><a href="https://www.jobpersonality.com/software-engineer" class="bold-on-mobile">Software engineer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/software-engineer">
							Vacatures: 178<br>
							Robotiserings%: 13%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/mentor';"><a href="https://www.jobpersonality.com/mentor" class="bold-on-mobile">Mentor <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/mentor">
							Vacatures: 152<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/commissioning-engineer';"><a href="https://www.jobpersonality.com/commissioning-engineer" class="bold-on-mobile">Commissioning engineer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/commissioning-engineer">
							Vacatures: 19<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/javascript-developer';"><a href="https://www.jobpersonality.com/javascript-developer" class="bold-on-mobile">Javascript developer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/javascript-developer">
							Vacatures: 1<br>
							Robotiserings%: 21%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/application-engineer';"><a href="https://www.jobpersonality.com/application-engineer" class="bold-on-mobile">Application engineer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/application-engineer">
							Vacatures: 27<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/leerplichtambtenaar';"><a href="https://www.jobpersonality.com/leerplichtambtenaar" class="bold-on-mobile">Leerplichtambtenaar <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/leerplichtambtenaar">
							Vacatures: 4<br>
							Robotiserings%: 13%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/werkconsulent';"><a href="https://www.jobpersonality.com/werkconsulent" class="bold-on-mobile">Werkconsulent <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/werkconsulent">
							Vacatures: 0<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/kyc-analist';"><a href="https://www.jobpersonality.com/kyc-analist" class="bold-on-mobile">KYC analist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/kyc-analist">
							Vacatures: 3<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/cdd-analist';"><a href="https://www.jobpersonality.com/cdd-analist" class="bold-on-mobile">CDD analist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/cdd-analist">
							Vacatures: 8<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/horecaondernemer';"><a href="https://www.jobpersonality.com/horecaondernemer" class="bold-on-mobile">Horecaondernemer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/horecaondernemer">
							Vacatures: 4<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/docent-mbo';"><a href="https://www.jobpersonality.com/docent-mbo" class="bold-on-mobile">Docent mbo <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/docent-mbo">
							Vacatures: 8<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/wordpress-developer';"><a href="https://www.jobpersonality.com/wordpress-developer" class="bold-on-mobile">WordPress developer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/wordpress-developer">
							Vacatures: 0<br>
							Robotiserings%: 39%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/commissaris';"><a href="https://www.jobpersonality.com/commissaris" class="bold-on-mobile">Commissaris <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/commissaris">
							Vacatures: 64<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/python-developer';"><a href="https://www.jobpersonality.com/python-developer" class="bold-on-mobile">Python developer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/python-developer">
							Vacatures: 13<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/react-developer';"><a href="https://www.jobpersonality.com/react-developer" class="bold-on-mobile">React developer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/react-developer">
							Vacatures: 5<br>
							Robotiserings%: 39%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/osteopaat';"><a href="https://www.jobpersonality.com/osteopaat" class="bold-on-mobile">Osteopaat <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/osteopaat">
							Vacatures: 2<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/vve-manager';"><a href="https://www.jobpersonality.com/vve-manager" class="bold-on-mobile">Vve-beheerder <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/vve-manager">
							Vacatures: 2<br>
							Robotiserings%: 31%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/systeemanalist';"><a href="https://www.jobpersonality.com/systeemanalist" class="bold-on-mobile">Systeemanalist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/systeemanalist">
							Vacatures: 0<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/ingenieur';"><a href="https://www.jobpersonality.com/ingenieur" class="bold-on-mobile">Ingenieur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/ingenieur">
							Vacatures: 2705<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/it-recruiter';"><a href="https://www.jobpersonality.com/it-recruiter" class="bold-on-mobile">IT recruiter <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/it-recruiter">
							Vacatures: 29<br>
							Robotiserings%: 31%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/huidtherapeut';"><a href="https://www.jobpersonality.com/huidtherapeut" class="bold-on-mobile">Huidtherapeut <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/huidtherapeut">
							Vacatures: 0<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/informatiemanager';"><a href="https://www.jobpersonality.com/informatiemanager" class="bold-on-mobile">Informatiemanager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/informatiemanager">
							Vacatures: 7<br>
							Robotiserings%: 13%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/communicatiemanager';"><a href="https://www.jobpersonality.com/communicatiemanager" class="bold-on-mobile">Communicatiemanager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/communicatiemanager">
							Vacatures: 1<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/site-manager';"><a href="https://www.jobpersonality.com/site-manager" class="bold-on-mobile">Site manager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/site-manager">
							Vacatures: 18<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/prompter';"><a href="https://www.jobpersonality.com/prompter" class="bold-on-mobile">Prompter <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/prompter">
							Vacatures: 0<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medisch-tatoeeerder';"><a href="https://www.jobpersonality.com/medisch-tatoeeerder" class="bold-on-mobile">Medisch tatoeëerder <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medisch-tatoeeerder">
							Vacatures: 0<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/maintenance-engineer';"><a href="https://www.jobpersonality.com/maintenance-engineer" class="bold-on-mobile">Maintenance engineer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/maintenance-engineer">
							Vacatures: 128<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/regieverpleegkundige';"><a href="https://www.jobpersonality.com/regieverpleegkundige" class="bold-on-mobile">Regieverpleegkundige <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/regieverpleegkundige">
							Vacatures: 6<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/it-architect';"><a href="https://www.jobpersonality.com/it-architect" class="bold-on-mobile">IT-architect <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/it-architect">
							Vacatures: 19<br>
							Robotiserings%: 22%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/programmamanager';"><a href="https://www.jobpersonality.com/programmamanager" class="bold-on-mobile">Programmamanager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/programmamanager">
							Vacatures: 22<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/linkbuilding-specialist';"><a href="https://www.jobpersonality.com/linkbuilding-specialist" class="bold-on-mobile">Linkbuilding specialist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/linkbuilding-specialist">
							Vacatures: 0<br>
							Robotiserings%: 22%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/content-manager';"><a href="https://www.jobpersonality.com/content-manager" class="bold-on-mobile">Content manager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/content-manager">
							Vacatures: 1<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/online-marketing-adviseur';"><a href="https://www.jobpersonality.com/online-marketing-adviseur" class="bold-on-mobile">Online marketing adviseur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/online-marketing-adviseur">
							Vacatures: 0<br>
							Robotiserings%: 10%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/trusted-advisor';"><a href="https://www.jobpersonality.com/trusted-advisor" class="bold-on-mobile">Trusted advisor <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/trusted-advisor">
							Vacatures: 14<br>
							Robotiserings%: 13%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/digital-nomad';"><a href="https://www.jobpersonality.com/digital-nomad" class="bold-on-mobile">Digital nomad <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/digital-nomad">
							Vacatures: 2<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/affiliate-marketeer';"><a href="https://www.jobpersonality.com/affiliate-marketeer" class="bold-on-mobile">Affiliate marketeer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/affiliate-marketeer">
							Vacatures: 0<br>
							Robotiserings%: 10%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/klachtenfunctionaris';"><a href="https://www.jobpersonality.com/klachtenfunctionaris" class="bold-on-mobile">Klachtenfunctionaris <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/klachtenfunctionaris">
							Vacatures: 0<br>
							Robotiserings%: 44%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/data-steward';"><a href="https://www.jobpersonality.com/data-steward" class="bold-on-mobile">Data steward <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/data-steward">
							Vacatures: 3<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/technisch-manager';"><a href="https://www.jobpersonality.com/technisch-manager" class="bold-on-mobile">Technisch manager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/technisch-manager">
							Vacatures: 83<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/crisismanager';"><a href="https://www.jobpersonality.com/crisismanager" class="bold-on-mobile">Crisismanager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/crisismanager">
							Vacatures: 2<br>
							Robotiserings%: 13%<br>
							Opleidingsniveau: 4<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/hoofd-administratie';"><a href="https://www.jobpersonality.com/hoofd-administratie" class="bold-on-mobile">Hoofd administratie <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/hoofd-administratie">
							Vacatures: 6<br>
							Robotiserings%: 73%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/manager-geothermische-energieproductie';"><a href="https://www.jobpersonality.com/manager-geothermische-energieproductie" class="bold-on-mobile">Manager geothermische energieproductie <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/manager-geothermische-energieproductie">
							Vacatures: 0<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/logistiek-manager';"><a href="https://www.jobpersonality.com/logistiek-manager" class="bold-on-mobile">Logistiek manager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/logistiek-manager">
							Vacatures: 43<br>
							Robotiserings%: 59%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/kwekerij-tuinmanager';"><a href="https://www.jobpersonality.com/kwekerij-tuinmanager" class="bold-on-mobile">Teeltmanager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/kwekerij-tuinmanager">
							Vacatures: 2<br>
							Robotiserings%: 5%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/horecamanager';"><a href="https://www.jobpersonality.com/horecamanager" class="bold-on-mobile">Horecamanager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/horecamanager">
							Vacatures: 275<br>
							Robotiserings%: 8%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/uitvaartzorgmanager';"><a href="https://www.jobpersonality.com/uitvaartzorgmanager" class="bold-on-mobile">Manager uitvaartcentrum <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/uitvaartzorgmanager">
							Vacatures: 0<br>
							Robotiserings%: 8%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/casinomanager';"><a href="https://www.jobpersonality.com/casinomanager" class="bold-on-mobile">Casinomanager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/casinomanager">
							Vacatures: 74<br>
							Robotiserings%: 9%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/front-office-manager';"><a href="https://www.jobpersonality.com/front-office-manager" class="bold-on-mobile">Front office manager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/front-office-manager">
							Vacatures: 48<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/postkantoormanager';"><a href="https://www.jobpersonality.com/postkantoormanager" class="bold-on-mobile">Postkantoormanager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/postkantoormanager">
							Vacatures: 0<br>
							Robotiserings%: 75%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/beveiligingsmanager';"><a href="https://www.jobpersonality.com/beveiligingsmanager" class="bold-on-mobile">Beveiligingsmanager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/beveiligingsmanager">
							Vacatures: 0<br>
							Robotiserings%: 25%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/inkoper-groothandel-detailhandel';"><a href="https://www.jobpersonality.com/inkoper-groothandel-detailhandel" class="bold-on-mobile">Inkoper <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/inkoper-groothandel-detailhandel">
							Vacatures: 160<br>
							Robotiserings%: 29%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/inkoopagent';"><a href="https://www.jobpersonality.com/inkoopagent" class="bold-on-mobile">Technisch inkoper <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/inkoopagent">
							Vacatures: 10<br>
							Robotiserings%: 77%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/verzekeringsexpert-schaderegelaar';"><a href="https://www.jobpersonality.com/verzekeringsexpert-schaderegelaar" class="bold-on-mobile">Schade expert <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/verzekeringsexpert-schaderegelaar">
							Vacatures: 2<br>
							Robotiserings%: 98%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/schade-expert-autoverzekering';"><a href="https://www.jobpersonality.com/schade-expert-autoverzekering" class="bold-on-mobile">Autoschade expert <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/schade-expert-autoverzekering">
							Vacatures: 0<br>
							Robotiserings%: 98%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/milieu-inspecteur';"><a href="https://www.jobpersonality.com/milieu-inspecteur" class="bold-on-mobile">Milieu-inspecteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/milieu-inspecteur">
							Vacatures: 1<br>
							Robotiserings%: 8%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/examinator';"><a href="https://www.jobpersonality.com/examinator" class="bold-on-mobile">Examinator <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/examinator">
							Vacatures: 11<br>
							Robotiserings%: 8%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/inspecteur-en-onderzoeker-rijksvastgoed';"><a href="https://www.jobpersonality.com/inspecteur-en-onderzoeker-rijksvastgoed" class="bold-on-mobile">Inspecteur vastgoed <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/inspecteur-en-onderzoeker-rijksvastgoed">
							Vacatures: 0<br>
							Robotiserings%: 8%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/hr-specialist-landbouw';"><a href="https://www.jobpersonality.com/hr-specialist-landbouw" class="bold-on-mobile">Intercedent landbouw <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/hr-specialist-landbouw">
							Vacatures: 0<br>
							Robotiserings%: 97%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/evenement-conferentieplanner';"><a href="https://www.jobpersonality.com/evenement-conferentieplanner" class="bold-on-mobile">Event manager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/evenement-conferentieplanner">
							Vacatures: 8<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/energie-auditor';"><a href="https://www.jobpersonality.com/energie-auditor" class="bold-on-mobile">Energieadviseur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/energie-auditor">
							Vacatures: 4<br>
							Robotiserings%: 23%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/douane-declarant';"><a href="https://www.jobpersonality.com/douane-declarant" class="bold-on-mobile">Douane declarant <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/douane-declarant">
							Vacatures: 4<br>
							Robotiserings%: 23%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/taxateur';"><a href="https://www.jobpersonality.com/taxateur" class="bold-on-mobile">Taxateur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/taxateur">
							Vacatures: 6<br>
							Robotiserings%: 90%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/websitebouwer';"><a href="https://www.jobpersonality.com/websitebouwer" class="bold-on-mobile">Webdeveloper <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/websitebouwer">
							Vacatures: 1<br>
							Robotiserings%: 21%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/webdesigner';"><a href="https://www.jobpersonality.com/webdesigner" class="bold-on-mobile">Webdesigner <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/webdesigner">
							Vacatures: 2<br>
							Robotiserings%: 30%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/telecom-engineer';"><a href="https://www.jobpersonality.com/telecom-engineer" class="bold-on-mobile">Telecom engineer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/telecom-engineer">
							Vacatures: 3<br>
							Robotiserings%: 22%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/helpdeskmedewerker-ict';"><a href="https://www.jobpersonality.com/helpdeskmedewerker-ict" class="bold-on-mobile">Helpdeskmedewerker ICT <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/helpdeskmedewerker-ict">
							Vacatures: 0<br>
							Robotiserings%: 65%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/monteur-ict';"><a href="https://www.jobpersonality.com/monteur-ict" class="bold-on-mobile">ICT Monteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/monteur-ict">
							Vacatures: 9<br>
							Robotiserings%: 45%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/netwerkbeheerder';"><a href="https://www.jobpersonality.com/netwerkbeheerder" class="bold-on-mobile">Netwerkbeheerder <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/netwerkbeheerder">
							Vacatures: 14<br>
							Robotiserings%: 22%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/software-tester';"><a href="https://www.jobpersonality.com/software-tester" class="bold-on-mobile">Software tester <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/software-tester">
							Vacatures: 8<br>
							Robotiserings%: 22%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/web-administrator';"><a href="https://www.jobpersonality.com/web-administrator" class="bold-on-mobile">Webmaster <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/web-administrator">
							Vacatures: 0<br>
							Robotiserings%: 22%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/civieltechnisch-tekenaar';"><a href="https://www.jobpersonality.com/civieltechnisch-tekenaar" class="bold-on-mobile">Civieltechnisch tekenaar <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/civieltechnisch-tekenaar">
							Vacatures: 4<br>
							Robotiserings%: 52%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/elektronisch-tekenaar';"><a href="https://www.jobpersonality.com/elektronisch-tekenaar" class="bold-on-mobile">Tekenaar elektrotechniek <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/elektronisch-tekenaar">
							Vacatures: 7<br>
							Robotiserings%: 52%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/elektrisch-tekenaar';"><a href="https://www.jobpersonality.com/elektrisch-tekenaar" class="bold-on-mobile">Elektrisch tekenaar <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/elektrisch-tekenaar">
							Vacatures: 0<br>
							Robotiserings%: 81%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/mechanisch-tekenaar';"><a href="https://www.jobpersonality.com/mechanisch-tekenaar" class="bold-on-mobile">Tekenaar constructeur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/mechanisch-tekenaar">
							Vacatures: 14<br>
							Robotiserings%: 68%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/civiel-technicus';"><a href="https://www.jobpersonality.com/civiel-technicus" class="bold-on-mobile">Civiel technicus <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/civiel-technicus">
							Vacatures: 0<br>
							Robotiserings%: 75%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/elektronicatechnicus';"><a href="https://www.jobpersonality.com/elektronicatechnicus" class="bold-on-mobile">Elektronicatechnicus <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/elektronicatechnicus">
							Vacatures: 0<br>
							Robotiserings%: 84%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/elektrotechnicus';"><a href="https://www.jobpersonality.com/elektrotechnicus" class="bold-on-mobile">Elektrotechnicus <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/elektrotechnicus">
							Vacatures: 12<br>
							Robotiserings%: 84%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/elektromechanisch-technicus';"><a href="https://www.jobpersonality.com/elektromechanisch-technicus" class="bold-on-mobile">Elektromechanisch technicus <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/elektromechanisch-technicus">
							Vacatures: 4<br>
							Robotiserings%: 81%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/roboticatechnicus';"><a href="https://www.jobpersonality.com/roboticatechnicus" class="bold-on-mobile">Roboticatechnicus <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/roboticatechnicus">
							Vacatures: 0<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/instrumentenmaker';"><a href="https://www.jobpersonality.com/instrumentenmaker" class="bold-on-mobile">Instrumentenmaker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/instrumentenmaker">
							Vacatures: 0<br>
							Robotiserings%: 38%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/niet-destructief-onderzoeker';"><a href="https://www.jobpersonality.com/niet-destructief-onderzoeker" class="bold-on-mobile">Niet-destructief onderzoeker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/niet-destructief-onderzoeker">
							Vacatures: 0<br>
							Robotiserings%: 24%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medewerker-elektrotechniek';"><a href="https://www.jobpersonality.com/medewerker-elektrotechniek" class="bold-on-mobile">Medewerker elektrotechniek <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medewerker-elektrotechniek">
							Vacatures: 37<br>
							Robotiserings%: 84%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/monteur-werktuigbouw';"><a href="https://www.jobpersonality.com/monteur-werktuigbouw" class="bold-on-mobile">Monteur werktuigbouw <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/monteur-werktuigbouw">
							Vacatures: 10<br>
							Robotiserings%: 24%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/technicus-fotonica';"><a href="https://www.jobpersonality.com/technicus-fotonica" class="bold-on-mobile">Technicus fotonica <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/technicus-fotonica">
							Vacatures: 0<br>
							Robotiserings%: 24%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/technicus-industriele-productie';"><a href="https://www.jobpersonality.com/technicus-industriele-productie" class="bold-on-mobile">Technisch operator <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/technicus-industriele-productie">
							Vacatures: 90<br>
							Robotiserings%: 24%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/nanotechnologische-technicus';"><a href="https://www.jobpersonality.com/nanotechnologische-technicus" class="bold-on-mobile">Medewerker nanotechnologie <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/nanotechnologische-technicus">
							Vacatures: 0<br>
							Robotiserings%: 24%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/landmeetkundige-technicus';"><a href="https://www.jobpersonality.com/landmeetkundige-technicus" class="bold-on-mobile">Landmeetkundige technicus <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/landmeetkundige-technicus">
							Vacatures: 0<br>
							Robotiserings%: 96%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/cartografische-technicus';"><a href="https://www.jobpersonality.com/cartografische-technicus" class="bold-on-mobile">Cartografische technicus <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/cartografische-technicus">
							Vacatures: 0<br>
							Robotiserings%: 96%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/boswachter';"><a href="https://www.jobpersonality.com/boswachter" class="bold-on-mobile">Boswachter <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/boswachter">
							Vacatures: 2<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/landbouwlaborant';"><a href="https://www.jobpersonality.com/landbouwlaborant" class="bold-on-mobile">Landbouwlaborant <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/landbouwlaborant">
							Vacatures: 0<br>
							Robotiserings%: 97%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/chemisch-fysisch-laborant';"><a href="https://www.jobpersonality.com/chemisch-fysisch-laborant" class="bold-on-mobile">Chemisch-fysisch laborant <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/chemisch-fysisch-laborant">
							Vacatures: 4<br>
							Robotiserings%: 97%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/laborant';"><a href="https://www.jobpersonality.com/laborant" class="bold-on-mobile">Laborant <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/laborant">
							Vacatures: 37<br>
							Robotiserings%: 57%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/geologische-onderzoeker';"><a href="https://www.jobpersonality.com/geologische-onderzoeker" class="bold-on-mobile">Geologische onderzoeker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/geologische-onderzoeker">
							Vacatures: 0<br>
							Robotiserings%: 91%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/veiligheidstechnicus-kerncentrales';"><a href="https://www.jobpersonality.com/veiligheidstechnicus-kerncentrales" class="bold-on-mobile">Storingstechnicus kerncentrale <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/veiligheidstechnicus-kerncentrales">
							Vacatures: 0<br>
							Robotiserings%: 85%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medewerker-bosbeheer';"><a href="https://www.jobpersonality.com/medewerker-bosbeheer" class="bold-on-mobile">Medewerker bosbeheer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medewerker-bosbeheer">
							Vacatures: 0<br>
							Robotiserings%: 42%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/analist-kwaliteitscontrole';"><a href="https://www.jobpersonality.com/analist-kwaliteitscontrole" class="bold-on-mobile">Kwaliteitscontroleur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/analist-kwaliteitscontrole">
							Vacatures: 23<br>
							Robotiserings%: 61%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/juridisch-assistent';"><a href="https://www.jobpersonality.com/juridisch-assistent" class="bold-on-mobile">Paralegal <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/juridisch-assistent">
							Vacatures: 2<br>
							Robotiserings%: 94%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/notarieel-medewerker';"><a href="https://www.jobpersonality.com/notarieel-medewerker" class="bold-on-mobile">Notarieel medewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/notarieel-medewerker">
							Vacatures: 3<br>
							Robotiserings%: 99%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/pedagogisch-medewerker';"><a href="https://www.jobpersonality.com/pedagogisch-medewerker" class="bold-on-mobile">Pedagogisch medewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/pedagogisch-medewerker">
							Vacatures: 1423<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/gespecialiseerd-pedagogisch-medewerker';"><a href="https://www.jobpersonality.com/gespecialiseerd-pedagogisch-medewerker" class="bold-on-mobile">Gespecialiseerd pedagogisch medewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/gespecialiseerd-pedagogisch-medewerker">
							Vacatures: 0<br>
							Robotiserings%: 15%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/docent-cursussen-workshops';"><a href="https://www.jobpersonality.com/docent-cursussen-workshops" class="bold-on-mobile">Docent cursussen en workshops <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/docent-cursussen-workshops">
							Vacatures: 0<br>
							Robotiserings%: 13%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/museummedewerker';"><a href="https://www.jobpersonality.com/museummedewerker" class="bold-on-mobile">Museummedewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/museummedewerker">
							Vacatures: 0<br>
							Robotiserings%: 60%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/specialist-multimediale-lesmiddelen';"><a href="https://www.jobpersonality.com/specialist-multimediale-lesmiddelen" class="bold-on-mobile">AV specialist onderwijs <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/specialist-multimediale-lesmiddelen">
							Vacatures: 0<br>
							Robotiserings%: 39%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/onderwijsassistent';"><a href="https://www.jobpersonality.com/onderwijsassistent" class="bold-on-mobile">Onderwijsassistent <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/onderwijsassistent">
							Vacatures: 18<br>
							Robotiserings%: 56%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/ambachtelijk-kunstenaar';"><a href="https://www.jobpersonality.com/ambachtelijk-kunstenaar" class="bold-on-mobile">Ambachtelijk kunstenaar <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/ambachtelijk-kunstenaar">
							Vacatures: 0<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/modeontwerper';"><a href="https://www.jobpersonality.com/modeontwerper" class="bold-on-mobile">Modeontwerper <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/modeontwerper">
							Vacatures: 0<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bloemist-en-bloemschikker';"><a href="https://www.jobpersonality.com/bloemist-en-bloemschikker" class="bold-on-mobile">Bloemist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bloemist-en-bloemschikker">
							Vacatures: 12<br>
							Robotiserings%: 5%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/acteur';"><a href="https://www.jobpersonality.com/acteur" class="bold-on-mobile">Acteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/acteur">
							Vacatures: 0<br>
							Robotiserings%: 37%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/scheidsrechter-sportofficial';"><a href="https://www.jobpersonality.com/scheidsrechter-sportofficial" class="bold-on-mobile">Scheidsrechter <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/scheidsrechter-sportofficial">
							Vacatures: 0<br>
							Robotiserings%: 98%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/danser';"><a href="https://www.jobpersonality.com/danser" class="bold-on-mobile">Danser <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/danser">
							Vacatures: 0<br>
							Robotiserings%: 13%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/dansleraar';"><a href="https://www.jobpersonality.com/dansleraar" class="bold-on-mobile">Dansleraar <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/dansleraar">
							Vacatures: 0<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/componist-arrangeur';"><a href="https://www.jobpersonality.com/componist-arrangeur" class="bold-on-mobile">Componist en arrangeur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/componist-arrangeur">
							Vacatures: 0<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/zanger';"><a href="https://www.jobpersonality.com/zanger" class="bold-on-mobile">Zanger <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/zanger">
							Vacatures: 3<br>
							Robotiserings%: 13%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/musicus';"><a href="https://www.jobpersonality.com/musicus" class="bold-on-mobile">Muzikant <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/musicus">
							Vacatures: 1<br>
							Robotiserings%: 13%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/omroeper';"><a href="https://www.jobpersonality.com/omroeper" class="bold-on-mobile">Presentator <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/omroeper">
							Vacatures: 0<br>
							Robotiserings%: 10%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/speaker';"><a href="https://www.jobpersonality.com/speaker" class="bold-on-mobile">Speaker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/speaker">
							Vacatures: 10<br>
							Robotiserings%: 72%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/audio-videotechnicus';"><a href="https://www.jobpersonality.com/audio-videotechnicus" class="bold-on-mobile">Audio- en videotechnicus <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/audio-videotechnicus">
							Vacatures: 2<br>
							Robotiserings%: 55%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bediener-zend-apparatuur';"><a href="https://www.jobpersonality.com/bediener-zend-apparatuur" class="bold-on-mobile">Bediener zend-apparatuur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bediener-zend-apparatuur">
							Vacatures: 0<br>
							Robotiserings%: 74%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/radiotechnicus';"><a href="https://www.jobpersonality.com/radiotechnicus" class="bold-on-mobile">Radiotechnicus <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/radiotechnicus">
							Vacatures: 0<br>
							Robotiserings%: 98%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/geluidstechnicus';"><a href="https://www.jobpersonality.com/geluidstechnicus" class="bold-on-mobile">Geluidstechnicus <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/geluidstechnicus">
							Vacatures: 0<br>
							Robotiserings%: 13%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/fotograaf';"><a href="https://www.jobpersonality.com/fotograaf" class="bold-on-mobile">Fotograaf <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/fotograaf">
							Vacatures: 4<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/cameraman';"><a href="https://www.jobpersonality.com/cameraman" class="bold-on-mobile">Cameraman <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/cameraman">
							Vacatures: 0<br>
							Robotiserings%: 60%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/film-video-editor';"><a href="https://www.jobpersonality.com/film-video-editor" class="bold-on-mobile">Video editor <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/film-video-editor">
							Vacatures: 0<br>
							Robotiserings%: 31%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/doktersassistent';"><a href="https://www.jobpersonality.com/doktersassistent" class="bold-on-mobile">Doktersassistent <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/doktersassistent">
							Vacatures: 6<br>
							Robotiserings%: 14%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/mbo-verpleegkundige';"><a href="https://www.jobpersonality.com/mbo-verpleegkundige" class="bold-on-mobile">Mbo-verpleegkundige <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/mbo-verpleegkundige">
							Vacatures: 8<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/cytologisch-onderzoeker';"><a href="https://www.jobpersonality.com/cytologisch-onderzoeker" class="bold-on-mobile">Cytologisch onderzoeker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/cytologisch-onderzoeker">
							Vacatures: 0<br>
							Robotiserings%: 90%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/weefselonderzoeker';"><a href="https://www.jobpersonality.com/weefselonderzoeker" class="bold-on-mobile">Weefselonderzoeker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/weefselonderzoeker">
							Vacatures: 0<br>
							Robotiserings%: 90%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/biologisch-medisch-laborant';"><a href="https://www.jobpersonality.com/biologisch-medisch-laborant" class="bold-on-mobile">Biologisch medisch laborant <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/biologisch-medisch-laborant">
							Vacatures: 0<br>
							Robotiserings%: 47%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/mri-technicus';"><a href="https://www.jobpersonality.com/mri-technicus" class="bold-on-mobile">MRI-technicus <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/mri-technicus">
							Vacatures: 0<br>
							Robotiserings%: 23%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/ambulancebroeder';"><a href="https://www.jobpersonality.com/ambulancebroeder" class="bold-on-mobile">Ambulanceverpleegkundige <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/ambulancebroeder">
							Vacatures: 0<br>
							Robotiserings%: 5%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/gewichtsconsulent';"><a href="https://www.jobpersonality.com/gewichtsconsulent" class="bold-on-mobile">Gewichtsconsulent <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/gewichtsconsulent">
							Vacatures: 0<br>
							Robotiserings%: 13%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/laborant-apotheek';"><a href="https://www.jobpersonality.com/laborant-apotheek" class="bold-on-mobile">Laborant apotheek <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/laborant-apotheek">
							Vacatures: 36<br>
							Robotiserings%: 92%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/assistent-psychiatrie';"><a href="https://www.jobpersonality.com/assistent-psychiatrie" class="bold-on-mobile">Assistent psychiatrie <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/assistent-psychiatrie">
							Vacatures: 0<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/assistent-beademing';"><a href="https://www.jobpersonality.com/assistent-beademing" class="bold-on-mobile">Assistent beademing <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/assistent-beademing">
							Vacatures: 0<br>
							Robotiserings%: 10%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/chirurgisch-assistent';"><a href="https://www.jobpersonality.com/chirurgisch-assistent" class="bold-on-mobile">Verpleegkundige chirurgie <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/chirurgisch-assistent">
							Vacatures: 0<br>
							Robotiserings%: 34%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/diergeneeskundige';"><a href="https://www.jobpersonality.com/diergeneeskundige" class="bold-on-mobile">Diergeneeskundige <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/diergeneeskundige">
							Vacatures: 0<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/oogheelkundig-assistent';"><a href="https://www.jobpersonality.com/oogheelkundig-assistent" class="bold-on-mobile">Oogheelkundig assistent <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/oogheelkundig-assistent">
							Vacatures: 0<br>
							Robotiserings%: 34%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/assistent-dienstverlening-zorg';"><a href="https://www.jobpersonality.com/assistent-dienstverlening-zorg" class="bold-on-mobile">Assistent zorg  <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/assistent-dienstverlening-zorg">
							Vacatures: 192<br>
							Robotiserings%: 6%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medisch-gegevensbeheerder';"><a href="https://www.jobpersonality.com/medisch-gegevensbeheerder" class="bold-on-mobile">Medewerker zorgadministratie <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medisch-gegevensbeheerder">
							Vacatures: 1<br>
							Robotiserings%: 91%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/opticien';"><a href="https://www.jobpersonality.com/opticien" class="bold-on-mobile">Opticien <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/opticien">
							Vacatures: 0<br>
							Robotiserings%: 71%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/audicien';"><a href="https://www.jobpersonality.com/audicien" class="bold-on-mobile">Audicien <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/audicien">
							Vacatures: 0<br>
							Robotiserings%: 40%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/technisch-oogheelkundig-assistent';"><a href="https://www.jobpersonality.com/technisch-oogheelkundig-assistent" class="bold-on-mobile">Technisch oogheelkundig assistent <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/technisch-oogheelkundig-assistent">
							Vacatures: 0<br>
							Robotiserings%: 40%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/technicus-radiologische-apparatuur';"><a href="https://www.jobpersonality.com/technicus-radiologische-apparatuur" class="bold-on-mobile">Medisch instrumentatietechnicus radiologie <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/technicus-radiologische-apparatuur">
							Vacatures: 0<br>
							Robotiserings%: 30%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/coordinator-arbeidsomstandigheden';"><a href="https://www.jobpersonality.com/coordinator-arbeidsomstandigheden" class="bold-on-mobile">KAM-coördinator <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/coordinator-arbeidsomstandigheden">
							Vacatures: 14<br>
							Robotiserings%: 25%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/ondersteunend-medewerker-thuiszorg';"><a href="https://www.jobpersonality.com/ondersteunend-medewerker-thuiszorg" class="bold-on-mobile">Verzorgende thuiszorg <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/ondersteunend-medewerker-thuiszorg">
							Vacatures: 15<br>
							Robotiserings%: 39%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/verpleegkundig-assistent';"><a href="https://www.jobpersonality.com/verpleegkundig-assistent" class="bold-on-mobile">Helpende zorg en welzijn <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/verpleegkundig-assistent">
							Vacatures: 337<br>
							Robotiserings%: 47%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/verpleeghulp';"><a href="https://www.jobpersonality.com/verpleeghulp" class="bold-on-mobile">Verpleeghulp <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/verpleeghulp">
							Vacatures: 0<br>
							Robotiserings%: 47%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/assistent-ergotherapeut';"><a href="https://www.jobpersonality.com/assistent-ergotherapeut" class="bold-on-mobile">Assistent ergotherapeut <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/assistent-ergotherapeut">
							Vacatures: 0<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/assistent-fysiotherapeut';"><a href="https://www.jobpersonality.com/assistent-fysiotherapeut" class="bold-on-mobile">Assistent fysiotherapeut <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/assistent-fysiotherapeut">
							Vacatures: 0<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/masseur';"><a href="https://www.jobpersonality.com/masseur" class="bold-on-mobile">Masseur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/masseur">
							Vacatures: 4<br>
							Robotiserings%: 54%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/tandartsassistent';"><a href="https://www.jobpersonality.com/tandartsassistent" class="bold-on-mobile">Tandartsassistent <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/tandartsassistent">
							Vacatures: 2<br>
							Robotiserings%: 51%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medisch-assistent';"><a href="https://www.jobpersonality.com/medisch-assistent" class="bold-on-mobile">Medisch assistent <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medisch-assistent">
							Vacatures: 0<br>
							Robotiserings%: 30%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medewerker-sterilisatie';"><a href="https://www.jobpersonality.com/medewerker-sterilisatie" class="bold-on-mobile">Medewerker sterilisatie <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medewerker-sterilisatie">
							Vacatures: 0<br>
							Robotiserings%: 78%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medische-transcriptionist';"><a href="https://www.jobpersonality.com/medische-transcriptionist" class="bold-on-mobile">Medische transcriptionist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medische-transcriptionist">
							Vacatures: 0<br>
							Robotiserings%: 89%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/apothekersassistent';"><a href="https://www.jobpersonality.com/apothekersassistent" class="bold-on-mobile">Apothekersassistent <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/apothekersassistent">
							Vacatures: 2<br>
							Robotiserings%: 72%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/dierenartsassistent';"><a href="https://www.jobpersonality.com/dierenartsassistent" class="bold-on-mobile">Dierenartsassistent <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/dierenartsassistent">
							Vacatures: 0<br>
							Robotiserings%: 86%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medewerker-bloedafname';"><a href="https://www.jobpersonality.com/medewerker-bloedafname" class="bold-on-mobile">Medewerker bloedafname <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medewerker-bloedafname">
							Vacatures: 0<br>
							Robotiserings%: 63%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/logopedie-assistent';"><a href="https://www.jobpersonality.com/logopedie-assistent" class="bold-on-mobile">Logopedie assistent <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/logopedie-assistent">
							Vacatures: 0<br>
							Robotiserings%: 63%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/manager-gevangenbewaarders';"><a href="https://www.jobpersonality.com/manager-gevangenbewaarders" class="bold-on-mobile">Manager gevangenbewaarders <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/manager-gevangenbewaarders">
							Vacatures: 0<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/teamleider-politie';"><a href="https://www.jobpersonality.com/teamleider-politie" class="bold-on-mobile">Teamleider politie <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/teamleider-politie">
							Vacatures: 0<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/hoofd-brandbestrijding-brandpreventie';"><a href="https://www.jobpersonality.com/hoofd-brandbestrijding-brandpreventie" class="bold-on-mobile">Hoofdbrandmeester <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/hoofd-brandbestrijding-brandpreventie">
							Vacatures: 0<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/brandweerman';"><a href="https://www.jobpersonality.com/brandweerman" class="bold-on-mobile">Brandweerman <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/brandweerman">
							Vacatures: 0<br>
							Robotiserings%: 17%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/brandinspecteur';"><a href="https://www.jobpersonality.com/brandinspecteur" class="bold-on-mobile">Brandinspecteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/brandinspecteur">
							Vacatures: 0<br>
							Robotiserings%: 48%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/brandonderzoeker';"><a href="https://www.jobpersonality.com/brandonderzoeker" class="bold-on-mobile">Brandonderzoeker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/brandonderzoeker">
							Vacatures: 0<br>
							Robotiserings%: 48%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bosbrandinspecteur';"><a href="https://www.jobpersonality.com/bosbrandinspecteur" class="bold-on-mobile">Bosbrandinspecteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bosbrandinspecteur">
							Vacatures: 0<br>
							Robotiserings%: 5%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/gevangenbewaarder-cipier';"><a href="https://www.jobpersonality.com/gevangenbewaarder-cipier" class="bold-on-mobile">Cipier <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/gevangenbewaarder-cipier">
							Vacatures: 0<br>
							Robotiserings%: 60%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/forensisch-politie-onderzoeker';"><a href="https://www.jobpersonality.com/forensisch-politie-onderzoeker" class="bold-on-mobile">Forensisch politie onderzoeker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/forensisch-politie-onderzoeker">
							Vacatures: 0<br>
							Robotiserings%: 34%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/buitengewoon-opsporingsambtenaar';"><a href="https://www.jobpersonality.com/buitengewoon-opsporingsambtenaar" class="bold-on-mobile">Buitengewoon opsporingsambtenaar <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/buitengewoon-opsporingsambtenaar">
							Vacatures: 4<br>
							Robotiserings%: 75%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/immigratie-douane-inspecteur';"><a href="https://www.jobpersonality.com/immigratie-douane-inspecteur" class="bold-on-mobile">Douanier <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/immigratie-douane-inspecteur">
							Vacatures: 0<br>
							Robotiserings%: 34%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/beroepsmilitair';"><a href="https://www.jobpersonality.com/beroepsmilitair" class="bold-on-mobile">Militair <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/beroepsmilitair">
							Vacatures: 16<br>
							Robotiserings%: 10%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/politieagent';"><a href="https://www.jobpersonality.com/politieagent" class="bold-on-mobile">Politieagent <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/politieagent">
							Vacatures: 1<br>
							Robotiserings%: 10%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/spoorwegpolitie';"><a href="https://www.jobpersonality.com/spoorwegpolitie" class="bold-on-mobile">Spoorwegpolitie <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/spoorwegpolitie">
							Vacatures: 0<br>
							Robotiserings%: 57%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/toezichthouder-casino';"><a href="https://www.jobpersonality.com/toezichthouder-casino" class="bold-on-mobile">Toezichthouder casino <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/toezichthouder-casino">
							Vacatures: 0<br>
							Robotiserings%: 95%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/beveiliger';"><a href="https://www.jobpersonality.com/beveiliger" class="bold-on-mobile">Beveiliger <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/beveiliger">
							Vacatures: 23<br>
							Robotiserings%: 84%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/specialist-preventie-diefstal-detailhandel';"><a href="https://www.jobpersonality.com/specialist-preventie-diefstal-detailhandel" class="bold-on-mobile">Specialist diefstalpreventie detailhandel <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/specialist-preventie-diefstal-detailhandel">
							Vacatures: 0<br>
							Robotiserings%: 67%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/chef-kok';"><a href="https://www.jobpersonality.com/chef-kok" class="bold-on-mobile">Chef-kok <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/chef-kok">
							Vacatures: 135<br>
							Robotiserings%: 10%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/leidinggevende-voedselbereiding-bediening';"><a href="https://www.jobpersonality.com/leidinggevende-voedselbereiding-bediening" class="bold-on-mobile">Leidinggevende voedselbereiding en bediening <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/leidinggevende-voedselbereiding-bediening">
							Vacatures: 54<br>
							Robotiserings%: 63%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medewerker-fastfoodrestaurant';"><a href="https://www.jobpersonality.com/medewerker-fastfoodrestaurant" class="bold-on-mobile">Medewerker fastservice <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medewerker-fastfoodrestaurant">
							Vacatures: 0<br>
							Robotiserings%: 81%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/kok-bij-instellingen-cafetaria';"><a href="https://www.jobpersonality.com/kok-bij-instellingen-cafetaria" class="bold-on-mobile">Kok catering <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/kok-bij-instellingen-cafetaria">
							Vacatures: 34<br>
							Robotiserings%: 83%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/prive-kok';"><a href="https://www.jobpersonality.com/prive-kok" class="bold-on-mobile">Privé kok <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/prive-kok">
							Vacatures: 4<br>
							Robotiserings%: 30%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/kok';"><a href="https://www.jobpersonality.com/kok" class="bold-on-mobile">Kok <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/kok">
							Vacatures: 735<br>
							Robotiserings%: 96%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/gastheer-gastvrouw';"><a href="https://www.jobpersonality.com/gastheer-gastvrouw" class="bold-on-mobile">Gastvrouw of gastheer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/gastheer-gastvrouw">
							Vacatures: 364<br>
							Robotiserings%: 97%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/teamleider-schoonmaak';"><a href="https://www.jobpersonality.com/teamleider-schoonmaak" class="bold-on-mobile">Teamleider schoonmaak <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/teamleider-schoonmaak">
							Vacatures: 0<br>
							Robotiserings%: 94%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/toezichthouder-tuinaanleg-onderhoud';"><a href="https://www.jobpersonality.com/toezichthouder-tuinaanleg-onderhoud" class="bold-on-mobile">Uitvoerder groen onderhoud <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/toezichthouder-tuinaanleg-onderhoud">
							Vacatures: 28<br>
							Robotiserings%: 57%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/ongediertebestrijder';"><a href="https://www.jobpersonality.com/ongediertebestrijder" class="bold-on-mobile">Ongediertebestrijder <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/ongediertebestrijder">
							Vacatures: 2<br>
							Robotiserings%: 66%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/hovenier-tuinman';"><a href="https://www.jobpersonality.com/hovenier-tuinman" class="bold-on-mobile">Hovenier <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/hovenier-tuinman">
							Vacatures: 714<br>
							Robotiserings%: 95%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/aanbrenger-pesticiden';"><a href="https://www.jobpersonality.com/aanbrenger-pesticiden" class="bold-on-mobile">Pesticiden aanbrenger <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/aanbrenger-pesticiden">
							Vacatures: 0<br>
							Robotiserings%: 97%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/boomsnoeier-boomchirurg';"><a href="https://www.jobpersonality.com/boomsnoeier-boomchirurg" class="bold-on-mobile">Boomsnoeier <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/boomsnoeier-boomchirurg">
							Vacatures: 0<br>
							Robotiserings%: 77%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/supervisor-fruitautomaten';"><a href="https://www.jobpersonality.com/supervisor-fruitautomaten" class="bold-on-mobile">Supervisor speelautomaten <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/supervisor-fruitautomaten">
							Vacatures: 17<br>
							Robotiserings%: 54%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bedrijfsleider';"><a href="https://www.jobpersonality.com/bedrijfsleider" class="bold-on-mobile">Bedrijfsleider <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bedrijfsleider">
							Vacatures: 72<br>
							Robotiserings%: 8%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/wellnessmanager';"><a href="https://www.jobpersonality.com/wellnessmanager" class="bold-on-mobile">Wellnessmanager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/wellnessmanager">
							Vacatures: 0<br>
							Robotiserings%: 8%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/dierenverzorger';"><a href="https://www.jobpersonality.com/dierenverzorger" class="bold-on-mobile">Dierenverzorger <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/dierenverzorger">
							Vacatures: 3<br>
							Robotiserings%: 82%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/croupier';"><a href="https://www.jobpersonality.com/croupier" class="bold-on-mobile">Croupier <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/croupier">
							Vacatures: 0<br>
							Robotiserings%: 96%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medewerker-leisure-en-hospitality';"><a href="https://www.jobpersonality.com/medewerker-leisure-en-hospitality" class="bold-on-mobile">Recreatiemedewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medewerker-leisure-en-hospitality">
							Vacatures: 0<br>
							Robotiserings%: 72%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/balsemer';"><a href="https://www.jobpersonality.com/balsemer" class="bold-on-mobile">Balsemer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/balsemer">
							Vacatures: 0<br>
							Robotiserings%: 54%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/begrafenisondernemer-uitvaartondernemer';"><a href="https://www.jobpersonality.com/begrafenisondernemer-uitvaartondernemer" class="bold-on-mobile">Uitvaartverzorger <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/begrafenisondernemer-uitvaartondernemer">
							Vacatures: 1<br>
							Robotiserings%: 20%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/kapper-haarstylist';"><a href="https://www.jobpersonality.com/kapper-haarstylist" class="bold-on-mobile">Kapper <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/kapper-haarstylist">
							Vacatures: 7<br>
							Robotiserings%: 11%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/grimeur-make-up-artist';"><a href="https://www.jobpersonality.com/grimeur-make-up-artist" class="bold-on-mobile">Grimeur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/grimeur-make-up-artist">
							Vacatures: 0<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/pedicure';"><a href="https://www.jobpersonality.com/pedicure" class="bold-on-mobile">Pedicure <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/pedicure">
							Vacatures: 0<br>
							Robotiserings%: 95%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/schoonheidsspecialist';"><a href="https://www.jobpersonality.com/schoonheidsspecialist" class="bold-on-mobile">Schoonheidsspecialist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/schoonheidsspecialist">
							Vacatures: 5<br>
							Robotiserings%: 29%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/concierge';"><a href="https://www.jobpersonality.com/concierge" class="bold-on-mobile">Conciërge <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/concierge">
							Vacatures: 17<br>
							Robotiserings%: 21%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/gids-begeleider';"><a href="https://www.jobpersonality.com/gids-begeleider" class="bold-on-mobile">Gids <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/gids-begeleider">
							Vacatures: 10<br>
							Robotiserings%: 91%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/reisgids';"><a href="https://www.jobpersonality.com/reisgids" class="bold-on-mobile">Reisleider <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/reisgids">
							Vacatures: 2<br>
							Robotiserings%: 6%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/kindermeisje';"><a href="https://www.jobpersonality.com/kindermeisje" class="bold-on-mobile">Nanny <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/kindermeisje">
							Vacatures: 4<br>
							Robotiserings%: 8%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/persoonlijke-hulp-thuishulp';"><a href="https://www.jobpersonality.com/persoonlijke-hulp-thuishulp" class="bold-on-mobile">Thuishulp <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/persoonlijke-hulp-thuishulp">
							Vacatures: 480<br>
							Robotiserings%: 74%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/sportinstructeur';"><a href="https://www.jobpersonality.com/sportinstructeur" class="bold-on-mobile">Sportinstructeur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/sportinstructeur">
							Vacatures: 0<br>
							Robotiserings%: 9%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/groepslesinstructeur';"><a href="https://www.jobpersonality.com/groepslesinstructeur" class="bold-on-mobile">Groepslesinstructeur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/groepslesinstructeur">
							Vacatures: 3<br>
							Robotiserings%: 9%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/complexbeheerder';"><a href="https://www.jobpersonality.com/complexbeheerder" class="bold-on-mobile">Huismeester <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/complexbeheerder">
							Vacatures: 17<br>
							Robotiserings%: 6%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/verkoopmanager-eerste-verkoper';"><a href="https://www.jobpersonality.com/verkoopmanager-eerste-verkoper" class="bold-on-mobile">Verkoopmanager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/verkoopmanager-eerste-verkoper">
							Vacatures: 1<br>
							Robotiserings%: 28%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/balie-verhuurmedewerker';"><a href="https://www.jobpersonality.com/balie-verhuurmedewerker" class="bold-on-mobile">Baliemedewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/balie-verhuurmedewerker">
							Vacatures: 191<br>
							Robotiserings%: 97%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/onderdelenverkoper';"><a href="https://www.jobpersonality.com/onderdelenverkoper" class="bold-on-mobile">Onderdelenverkoper <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/onderdelenverkoper">
							Vacatures: 0<br>
							Robotiserings%: 98%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/verkoopspecialist';"><a href="https://www.jobpersonality.com/verkoopspecialist" class="bold-on-mobile">Verkoopspecialist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/verkoopspecialist">
							Vacatures: 1<br>
							Robotiserings%: 92%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/commercieel-medewerker';"><a href="https://www.jobpersonality.com/commercieel-medewerker" class="bold-on-mobile">Commercieel medewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/commercieel-medewerker">
							Vacatures: 263<br>
							Robotiserings%: 54%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/financieel-adviseur';"><a href="https://www.jobpersonality.com/financieel-adviseur" class="bold-on-mobile">Financieel adviseur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/financieel-adviseur">
							Vacatures: 33<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/reisagent-reisbureaumedewerker';"><a href="https://www.jobpersonality.com/reisagent-reisbureaumedewerker" class="bold-on-mobile">Reisagent <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/reisagent-reisbureaumedewerker">
							Vacatures: 1<br>
							Robotiserings%: 10%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/vertegenwoordiger-technische-producten';"><a href="https://www.jobpersonality.com/vertegenwoordiger-technische-producten" class="bold-on-mobile">Vertegenwoordiger technische producten <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/vertegenwoordiger-technische-producten">
							Vacatures: 0<br>
							Robotiserings%: 25%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/handelsvertegenwoordiger-zonnesystemen';"><a href="https://www.jobpersonality.com/handelsvertegenwoordiger-zonnesystemen" class="bold-on-mobile">Verkoper zonnesystemen <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/handelsvertegenwoordiger-zonnesystemen">
							Vacatures: 0<br>
							Robotiserings%: 25%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/vertegenwoordiger';"><a href="https://www.jobpersonality.com/vertegenwoordiger" class="bold-on-mobile">Vertegenwoordiger <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/vertegenwoordiger">
							Vacatures: 62<br>
							Robotiserings%: 25%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/telemarketeer';"><a href="https://www.jobpersonality.com/telemarketeer" class="bold-on-mobile">Telemarketeer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/telemarketeer">
							Vacatures: 2<br>
							Robotiserings%: 99%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/callcenter-medewerker';"><a href="https://www.jobpersonality.com/callcenter-medewerker" class="bold-on-mobile">Callcenter medewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/callcenter-medewerker">
							Vacatures: 29<br>
							Robotiserings%: 97%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/huis-aan-huis-verkoper-straatverkoper';"><a href="https://www.jobpersonality.com/huis-aan-huis-verkoper-straatverkoper" class="bold-on-mobile">Straatverkoper <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/huis-aan-huis-verkoper-straatverkoper">
							Vacatures: 0<br>
							Robotiserings%: 94%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/leidinggevende';"><a href="https://www.jobpersonality.com/leidinggevende" class="bold-on-mobile">Leidinggevende <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/leidinggevende">
							Vacatures: 1574<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/incassomedewerker';"><a href="https://www.jobpersonality.com/incassomedewerker" class="bold-on-mobile">Incassomedewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/incassomedewerker">
							Vacatures: 8<br>
							Robotiserings%: 95%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medewerker-facturering';"><a href="https://www.jobpersonality.com/medewerker-facturering" class="bold-on-mobile">Medewerker facturatie <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medewerker-facturering">
							Vacatures: 3<br>
							Robotiserings%: 96%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/financieel-administratief-medewerker';"><a href="https://www.jobpersonality.com/financieel-administratief-medewerker" class="bold-on-mobile">Financieel administratief medewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/financieel-administratief-medewerker">
							Vacatures: 74<br>
							Robotiserings%: 98%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/boekhouder';"><a href="https://www.jobpersonality.com/boekhouder" class="bold-on-mobile">Boekhouder <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/boekhouder">
							Vacatures: 40<br>
							Robotiserings%: 90%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medewerker-salarisadministratie-en-tijdregistratie';"><a href="https://www.jobpersonality.com/medewerker-salarisadministratie-en-tijdregistratie" class="bold-on-mobile">Salarisadministrateur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medewerker-salarisadministratie-en-tijdregistratie">
							Vacatures: 83<br>
							Robotiserings%: 97%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/inkoopadministratief-medewerker';"><a href="https://www.jobpersonality.com/inkoopadministratief-medewerker" class="bold-on-mobile">Inkoopadministratief medewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/inkoopadministratief-medewerker">
							Vacatures: 0<br>
							Robotiserings%: 98%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/correspondentiemedewerker';"><a href="https://www.jobpersonality.com/correspondentiemedewerker" class="bold-on-mobile">Medewerker klantcontact <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/correspondentiemedewerker">
							Vacatures: 46<br>
							Robotiserings%: 86%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/licentieverlener';"><a href="https://www.jobpersonality.com/licentieverlener" class="bold-on-mobile">Vergunningverlener <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/licentieverlener">
							Vacatures: 27<br>
							Robotiserings%: 46%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/kredietacceptant';"><a href="https://www.jobpersonality.com/kredietacceptant" class="bold-on-mobile">Kredietacceptant <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/kredietacceptant">
							Vacatures: 1<br>
							Robotiserings%: 97%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/kredietcontroleur';"><a href="https://www.jobpersonality.com/kredietcontroleur" class="bold-on-mobile">Compliance medewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/kredietcontroleur">
							Vacatures: 5<br>
							Robotiserings%: 97%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/klantenservicemedewerker';"><a href="https://www.jobpersonality.com/klantenservicemedewerker" class="bold-on-mobile">Klantenservicemedewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/klantenservicemedewerker">
							Vacatures: 190<br>
							Robotiserings%: 55%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medewerker-sociale-dienst';"><a href="https://www.jobpersonality.com/medewerker-sociale-dienst" class="bold-on-mobile">Medewerker sociale dienst <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medewerker-sociale-dienst">
							Vacatures: 5<br>
							Robotiserings%: 70%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/div-medewerker';"><a href="https://www.jobpersonality.com/div-medewerker" class="bold-on-mobile">DIV medewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/div-medewerker">
							Vacatures: 1<br>
							Robotiserings%: 97%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/enqueteur';"><a href="https://www.jobpersonality.com/enqueteur" class="bold-on-mobile">Enquêteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/enqueteur">
							Vacatures: 0<br>
							Robotiserings%: 94%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medewerker-bibliotheek';"><a href="https://www.jobpersonality.com/medewerker-bibliotheek" class="bold-on-mobile">Bibliotheekmedewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medewerker-bibliotheek">
							Vacatures: 0<br>
							Robotiserings%: 95%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/administratief-medewerker-leningen-hypotheken';"><a href="https://www.jobpersonality.com/administratief-medewerker-leningen-hypotheken" class="bold-on-mobile">Medewerker hypotheken <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/administratief-medewerker-leningen-hypotheken">
							Vacatures: 2<br>
							Robotiserings%: 92%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/assistent-personeelsbeleid';"><a href="https://www.jobpersonality.com/assistent-personeelsbeleid" class="bold-on-mobile">HR medewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/assistent-personeelsbeleid">
							Vacatures: 76<br>
							Robotiserings%: 90%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/receptionist';"><a href="https://www.jobpersonality.com/receptionist" class="bold-on-mobile">Receptionist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/receptionist">
							Vacatures: 191<br>
							Robotiserings%: 96%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medewerker-havenlogistiek';"><a href="https://www.jobpersonality.com/medewerker-havenlogistiek" class="bold-on-mobile">Medewerker havenlogistiek <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medewerker-havenlogistiek">
							Vacatures: 0<br>
							Robotiserings%: 99%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/expediteur';"><a href="https://www.jobpersonality.com/expediteur" class="bold-on-mobile">Expediteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/expediteur">
							Vacatures: 18<br>
							Robotiserings%: 99%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/alarmcentrale-centralist';"><a href="https://www.jobpersonality.com/alarmcentrale-centralist" class="bold-on-mobile">Centralist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/alarmcentrale-centralist">
							Vacatures: 14<br>
							Robotiserings%: 49%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/centralist-planner';"><a href="https://www.jobpersonality.com/centralist-planner" class="bold-on-mobile">Planner <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/centralist-planner">
							Vacatures: 548<br>
							Robotiserings%: 96%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/werkvoorbereider';"><a href="https://www.jobpersonality.com/werkvoorbereider" class="bold-on-mobile">Werkvoorbereider <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/werkvoorbereider">
							Vacatures: 1556<br>
							Robotiserings%: 88%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medewerker-voorraadbeheer';"><a href="https://www.jobpersonality.com/medewerker-voorraadbeheer" class="bold-on-mobile">Medewerker voorraadbeheer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medewerker-voorraadbeheer">
							Vacatures: 2<br>
							Robotiserings%: 95%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/office-manager';"><a href="https://www.jobpersonality.com/office-manager" class="bold-on-mobile">Office Manager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/office-manager">
							Vacatures: 69<br>
							Robotiserings%: 86%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/juridisch-administratief-dienstverlener';"><a href="https://www.jobpersonality.com/juridisch-administratief-dienstverlener" class="bold-on-mobile">Juridisch administratief medewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/juridisch-administratief-dienstverlener">
							Vacatures: 5<br>
							Robotiserings%: 98%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medische-secretaresse';"><a href="https://www.jobpersonality.com/medische-secretaresse" class="bold-on-mobile">Medisch secretaresse <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medische-secretaresse">
							Vacatures: 0<br>
							Robotiserings%: 81%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/secretaresse';"><a href="https://www.jobpersonality.com/secretaresse" class="bold-on-mobile">Secretaresse <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/secretaresse">
							Vacatures: 23<br>
							Robotiserings%: 96%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/systeembeheerder';"><a href="https://www.jobpersonality.com/systeembeheerder" class="bold-on-mobile">Systeembeheerder <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/systeembeheerder">
							Vacatures: 41<br>
							Robotiserings%: 22%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/datatypiste';"><a href="https://www.jobpersonality.com/datatypiste" class="bold-on-mobile">Data entry medewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/datatypiste">
							Vacatures: 0<br>
							Robotiserings%: 99%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/desktop-publisher';"><a href="https://www.jobpersonality.com/desktop-publisher" class="bold-on-mobile">Desktop publisher <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/desktop-publisher">
							Vacatures: 3<br>
							Robotiserings%: 16%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medewerker-verzekeringsclaims';"><a href="https://www.jobpersonality.com/medewerker-verzekeringsclaims" class="bold-on-mobile">Medewerker verzekeringsclaims <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medewerker-verzekeringsclaims">
							Vacatures: 8<br>
							Robotiserings%: 98%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medewerker-verzekeringen';"><a href="https://www.jobpersonality.com/medewerker-verzekeringen" class="bold-on-mobile">Medewerker verzekeringen <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medewerker-verzekeringen">
							Vacatures: 16<br>
							Robotiserings%: 98%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/facilitair-medewerker';"><a href="https://www.jobpersonality.com/facilitair-medewerker" class="bold-on-mobile">Facilitair medewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/facilitair-medewerker">
							Vacatures: 30<br>
							Robotiserings%: 96%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/statistisch-medewerker';"><a href="https://www.jobpersonality.com/statistisch-medewerker" class="bold-on-mobile">Statistisch medewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/statistisch-medewerker">
							Vacatures: 0<br>
							Robotiserings%: 66%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/manager-bosbouw';"><a href="https://www.jobpersonality.com/manager-bosbouw" class="bold-on-mobile">Manager bosbouw <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/manager-bosbouw">
							Vacatures: 0<br>
							Robotiserings%: 57%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/manager-land-tuinbouw';"><a href="https://www.jobpersonality.com/manager-land-tuinbouw" class="bold-on-mobile">Manager land- en tuinbouw <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/manager-land-tuinbouw">
							Vacatures: 3<br>
							Robotiserings%: 57%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/manager-dierverzorging';"><a href="https://www.jobpersonality.com/manager-dierverzorging" class="bold-on-mobile">Manager dierverzorging <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/manager-dierverzorging">
							Vacatures: 0<br>
							Robotiserings%: 8%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/voedselinspecteur';"><a href="https://www.jobpersonality.com/voedselinspecteur" class="bold-on-mobile">Voedselinspecteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/voedselinspecteur">
							Vacatures: 0<br>
							Robotiserings%: 94%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/dierenfokker';"><a href="https://www.jobpersonality.com/dierenfokker" class="bold-on-mobile">Dierenfokker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/dierenfokker">
							Vacatures: 0<br>
							Robotiserings%: 95%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/agrarisch-loonwerker';"><a href="https://www.jobpersonality.com/agrarisch-loonwerker" class="bold-on-mobile">Agrarisch loonwerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/agrarisch-loonwerker">
							Vacatures: 11<br>
							Robotiserings%: 87%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medewerker-veehouderij';"><a href="https://www.jobpersonality.com/medewerker-veehouderij" class="bold-on-mobile">Medewerker veehouderij  <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medewerker-veehouderij">
							Vacatures: 9<br>
							Robotiserings%: 75%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medewerker-bosbouw-natuurbehoud';"><a href="https://www.jobpersonality.com/medewerker-bosbouw-natuurbehoud" class="bold-on-mobile">Medewerker bosbouw en natuurbehoud <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medewerker-bosbouw-natuurbehoud">
							Vacatures: 0<br>
							Robotiserings%: 87%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/boominspecteur';"><a href="https://www.jobpersonality.com/boominspecteur" class="bold-on-mobile">Boominspecteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/boominspecteur">
							Vacatures: 0<br>
							Robotiserings%: 97%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/manager-bouwhandel';"><a href="https://www.jobpersonality.com/manager-bouwhandel" class="bold-on-mobile">Manager bouwmarkt <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/manager-bouwhandel">
							Vacatures: 0<br>
							Robotiserings%: 17%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/manager-installatiebedrijf-zonnepanelen';"><a href="https://www.jobpersonality.com/manager-installatiebedrijf-zonnepanelen" class="bold-on-mobile">Manager installatiebedrijf zonnepanelen <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/manager-installatiebedrijf-zonnepanelen">
							Vacatures: 0<br>
							Robotiserings%: 17%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/ketelmaker';"><a href="https://www.jobpersonality.com/ketelmaker" class="bold-on-mobile">Monteur stoomtechniek <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/ketelmaker">
							Vacatures: 1<br>
							Robotiserings%: 68%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/metselaar';"><a href="https://www.jobpersonality.com/metselaar" class="bold-on-mobile">Metselaar <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/metselaar">
							Vacatures: 7<br>
							Robotiserings%: 82%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/stenenlegger';"><a href="https://www.jobpersonality.com/stenenlegger" class="bold-on-mobile">Stenenlegger <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/stenenlegger">
							Vacatures: 0<br>
							Robotiserings%: 89%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/timmerman';"><a href="https://www.jobpersonality.com/timmerman" class="bold-on-mobile">Timmerman <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/timmerman">
							Vacatures: 288<br>
							Robotiserings%: 72%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/timmerman-grof-werk';"><a href="https://www.jobpersonality.com/timmerman-grof-werk" class="bold-on-mobile">Betontimmerman <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/timmerman-grof-werk">
							Vacatures: 9<br>
							Robotiserings%: 82%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/dekvloerenlegger';"><a href="https://www.jobpersonality.com/dekvloerenlegger" class="bold-on-mobile">Dekvloerenlegger <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/dekvloerenlegger">
							Vacatures: 4<br>
							Robotiserings%: 79%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/specialist-vloeronderhoud';"><a href="https://www.jobpersonality.com/specialist-vloeronderhoud" class="bold-on-mobile">Specialist vloeronderhoud  <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/specialist-vloeronderhoud">
							Vacatures: 2<br>
							Robotiserings%: 87%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/tegelzetter';"><a href="https://www.jobpersonality.com/tegelzetter" class="bold-on-mobile">Tegelzetter <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/tegelzetter">
							Vacatures: 22<br>
							Robotiserings%: 75%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/afwerker-cement-en-beton';"><a href="https://www.jobpersonality.com/afwerker-cement-en-beton" class="bold-on-mobile">Betonboorder <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/afwerker-cement-en-beton">
							Vacatures: 7<br>
							Robotiserings%: 94%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/terrazzowerker';"><a href="https://www.jobpersonality.com/terrazzowerker" class="bold-on-mobile">Terrazzowerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/terrazzowerker">
							Vacatures: 0<br>
							Robotiserings%: 88%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/machinist-wegenbouw';"><a href="https://www.jobpersonality.com/machinist-wegenbouw" class="bold-on-mobile">Machinist wegenbouw <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/machinist-wegenbouw">
							Vacatures: 13<br>
							Robotiserings%: 83%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/plafond-en-gipsplateninstallateur';"><a href="https://www.jobpersonality.com/plafond-en-gipsplateninstallateur" class="bold-on-mobile">Plafond- en wandmonteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/plafond-en-gipsplateninstallateur">
							Vacatures: 0<br>
							Robotiserings%: 79%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/elektricien';"><a href="https://www.jobpersonality.com/elektricien" class="bold-on-mobile">Elektricien <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/elektricien">
							Vacatures: 41<br>
							Robotiserings%: 15%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/glaszetter';"><a href="https://www.jobpersonality.com/glaszetter" class="bold-on-mobile">Glaszetter <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/glaszetter">
							Vacatures: 59<br>
							Robotiserings%: 73%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/isolator-mechanische-systemen';"><a href="https://www.jobpersonality.com/isolator-mechanische-systemen" class="bold-on-mobile">Technisch isolatie monteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/isolator-mechanische-systemen">
							Vacatures: 1<br>
							Robotiserings%: 64%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/schilder';"><a href="https://www.jobpersonality.com/schilder" class="bold-on-mobile">Schilder <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/schilder">
							Vacatures: 707<br>
							Robotiserings%: 75%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/pijpfitter';"><a href="https://www.jobpersonality.com/pijpfitter" class="bold-on-mobile">Pijpfitter <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/pijpfitter">
							Vacatures: 10<br>
							Robotiserings%: 40%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/loodgieter';"><a href="https://www.jobpersonality.com/loodgieter" class="bold-on-mobile">Loodgieter <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/loodgieter">
							Vacatures: 119<br>
							Robotiserings%: 35%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/stukadoor';"><a href="https://www.jobpersonality.com/stukadoor" class="bold-on-mobile">Stukadoor <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/stukadoor">
							Vacatures: 16<br>
							Robotiserings%: 84%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/betonstaalvlechter';"><a href="https://www.jobpersonality.com/betonstaalvlechter" class="bold-on-mobile">IJzervlechter <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/betonstaalvlechter">
							Vacatures: 0<br>
							Robotiserings%: 90%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/dakdekker';"><a href="https://www.jobpersonality.com/dakdekker" class="bold-on-mobile">Dakdekker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/dakdekker">
							Vacatures: 35<br>
							Robotiserings%: 90%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/plaatmetaalbewerker';"><a href="https://www.jobpersonality.com/plaatmetaalbewerker" class="bold-on-mobile">Plaatwerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/plaatmetaalbewerker">
							Vacatures: 28<br>
							Robotiserings%: 82%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/constructiewerker';"><a href="https://www.jobpersonality.com/constructiewerker" class="bold-on-mobile">Constructiewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/constructiewerker">
							Vacatures: 226<br>
							Robotiserings%: 83%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/liftmonteur';"><a href="https://www.jobpersonality.com/liftmonteur" class="bold-on-mobile">Liftmonteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/liftmonteur">
							Vacatures: 10<br>
							Robotiserings%: 39%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/schoonmaker-gevaarlijke-stoffen';"><a href="https://www.jobpersonality.com/schoonmaker-gevaarlijke-stoffen" class="bold-on-mobile">Schoonmaker gevaarlijke stoffen <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/schoonmaker-gevaarlijke-stoffen">
							Vacatures: 3<br>
							Robotiserings%: 53%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/spoorwegmonteur';"><a href="https://www.jobpersonality.com/spoorwegmonteur" class="bold-on-mobile">Spoorwegmonteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/spoorwegmonteur">
							Vacatures: 0<br>
							Robotiserings%: 89%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/stratenmaker';"><a href="https://www.jobpersonality.com/stratenmaker" class="bold-on-mobile">Stratenmaker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/stratenmaker">
							Vacatures: 51<br>
							Robotiserings%: 83%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/installateur-zonnesystemen';"><a href="https://www.jobpersonality.com/installateur-zonnesystemen" class="bold-on-mobile">Monteur zonnepanelen <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/installateur-zonnesystemen">
							Vacatures: 22<br>
							Robotiserings%: 71%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/isolatiemonteur';"><a href="https://www.jobpersonality.com/isolatiemonteur" class="bold-on-mobile">Isolatiemonteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/isolatiemonteur">
							Vacatures: 1<br>
							Robotiserings%: 71%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/manager-installatie-en-reparatie';"><a href="https://www.jobpersonality.com/manager-installatie-en-reparatie" class="bold-on-mobile">Technisch leidinggevende <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/manager-installatie-en-reparatie">
							Vacatures: 42<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/onderhoudsmonteur-kantoorapparatuur';"><a href="https://www.jobpersonality.com/onderhoudsmonteur-kantoorapparatuur" class="bold-on-mobile">Onderhoudsmonteur kantoorapparatuur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/onderhoudsmonteur-kantoorapparatuur">
							Vacatures: 0<br>
							Robotiserings%: 74%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/monteur-zendmasten';"><a href="https://www.jobpersonality.com/monteur-zendmasten" class="bold-on-mobile">Antennebouwer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/monteur-zendmasten">
							Vacatures: 0<br>
							Robotiserings%: 15%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/radiomonteur';"><a href="https://www.jobpersonality.com/radiomonteur" class="bold-on-mobile">Radiomonteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/radiomonteur">
							Vacatures: 0<br>
							Robotiserings%: 76%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/installatiemonteur-telecommunicatieapparatuur';"><a href="https://www.jobpersonality.com/installatiemonteur-telecommunicatieapparatuur" class="bold-on-mobile">Telecom monteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/installatiemonteur-telecommunicatieapparatuur">
							Vacatures: 6<br>
							Robotiserings%: 36%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/luchtvaarttechnicus';"><a href="https://www.jobpersonality.com/luchtvaarttechnicus" class="bold-on-mobile">Luchtvaarttechnicus <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/luchtvaarttechnicus">
							Vacatures: 0<br>
							Robotiserings%: 70%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/monteur-elektrische-motoren';"><a href="https://www.jobpersonality.com/monteur-elektrische-motoren" class="bold-on-mobile">Monteur elektrische voertuigen <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/monteur-elektrische-motoren">
							Vacatures: 2<br>
							Robotiserings%: 76%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/elektromonteur-transportapparatuur';"><a href="https://www.jobpersonality.com/elektromonteur-transportapparatuur" class="bold-on-mobile">Elektromonteur transportapparatuur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/elektromonteur-transportapparatuur">
							Vacatures: 3<br>
							Robotiserings%: 91%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/elektromonteur-industriele-apparatuur';"><a href="https://www.jobpersonality.com/elektromonteur-industriele-apparatuur" class="bold-on-mobile">Monteur mechatronica <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/elektromonteur-industriele-apparatuur">
							Vacatures: 55<br>
							Robotiserings%: 41%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/elektromonteur-motorvoertuigen';"><a href="https://www.jobpersonality.com/elektromonteur-motorvoertuigen" class="bold-on-mobile">Elektromonteur automotive <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/elektromonteur-motorvoertuigen">
							Vacatures: 0<br>
							Robotiserings%: 61%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/elektromonteur-home-entertainmentapparatuur';"><a href="https://www.jobpersonality.com/elektromonteur-home-entertainmentapparatuur" class="bold-on-mobile">Monteur consumentenelektronica <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/elektromonteur-home-entertainmentapparatuur">
							Vacatures: 1<br>
							Robotiserings%: 65%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/beveiliging-en-alarminstallateur';"><a href="https://www.jobpersonality.com/beveiliging-en-alarminstallateur" class="bold-on-mobile">Beveiliging- en alarminstallateur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/beveiliging-en-alarminstallateur">
							Vacatures: 5<br>
							Robotiserings%: 82%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/luchtvaartmonteur';"><a href="https://www.jobpersonality.com/luchtvaartmonteur" class="bold-on-mobile">Luchtvaartmonteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/luchtvaartmonteur">
							Vacatures: 219<br>
							Robotiserings%: 71%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/autoschadehersteller';"><a href="https://www.jobpersonality.com/autoschadehersteller" class="bold-on-mobile">Autoschadehersteller <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/autoschadehersteller">
							Vacatures: 11<br>
							Robotiserings%: 91%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/servicemonteur-autoruitschade';"><a href="https://www.jobpersonality.com/servicemonteur-autoruitschade" class="bold-on-mobile">Servicemonteur autoruitschade <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/servicemonteur-autoruitschade">
							Vacatures: 0<br>
							Robotiserings%: 55%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/automonteur-of-autotechnicus';"><a href="https://www.jobpersonality.com/automonteur-of-autotechnicus" class="bold-on-mobile">Automonteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/automonteur-of-autotechnicus">
							Vacatures: 126<br>
							Robotiserings%: 59%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/gespecialiseerde-motor-of-automonteur';"><a href="https://www.jobpersonality.com/gespecialiseerde-motor-of-automonteur" class="bold-on-mobile">Gespecialiseerde motor- of automonteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/gespecialiseerde-motor-of-automonteur">
							Vacatures: 0<br>
							Robotiserings%: 59%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/vrachtwagenmonteur';"><a href="https://www.jobpersonality.com/vrachtwagenmonteur" class="bold-on-mobile">Vrachtwagenmonteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/vrachtwagenmonteur">
							Vacatures: 22<br>
							Robotiserings%: 73%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/monteur-boerderijapparatuur';"><a href="https://www.jobpersonality.com/monteur-boerderijapparatuur" class="bold-on-mobile">Monteur landbouw <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/monteur-boerderijapparatuur">
							Vacatures: 3<br>
							Robotiserings%: 75%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/monteur-industriele-voertuigen';"><a href="https://www.jobpersonality.com/monteur-industriele-voertuigen" class="bold-on-mobile">Monteur industriële voertuigen <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/monteur-industriele-voertuigen">
							Vacatures: 0<br>
							Robotiserings%: 40%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/monteur-spoorvoertuigen';"><a href="https://www.jobpersonality.com/monteur-spoorvoertuigen" class="bold-on-mobile">Monteur spoorvoertuigen <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/monteur-spoorvoertuigen">
							Vacatures: 0<br>
							Robotiserings%: 88%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/scheepsbouwer';"><a href="https://www.jobpersonality.com/scheepsbouwer" class="bold-on-mobile">Scheepsbouwer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/scheepsbouwer">
							Vacatures: 1<br>
							Robotiserings%: 66%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/monteur-motorfietsen';"><a href="https://www.jobpersonality.com/monteur-motorfietsen" class="bold-on-mobile">Motorfietstechnicus <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/monteur-motorfietsen">
							Vacatures: 1<br>
							Robotiserings%: 79%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/monteur-tuinmachines';"><a href="https://www.jobpersonality.com/monteur-tuinmachines" class="bold-on-mobile">Monteur tuinmachines <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/monteur-tuinmachines">
							Vacatures: 2<br>
							Robotiserings%: 93%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/fietsmonteur';"><a href="https://www.jobpersonality.com/fietsmonteur" class="bold-on-mobile">Fietsmonteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/fietsmonteur">
							Vacatures: 2<br>
							Robotiserings%: 94%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/caravan-monteur';"><a href="https://www.jobpersonality.com/caravan-monteur" class="bold-on-mobile">Caravan en camper monteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/caravan-monteur">
							Vacatures: 0<br>
							Robotiserings%: 59%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bandenmonteur';"><a href="https://www.jobpersonality.com/bandenmonteur" class="bold-on-mobile">Bandenmonteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bandenmonteur">
							Vacatures: 4<br>
							Robotiserings%: 70%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/monteur-mechanische-deuren';"><a href="https://www.jobpersonality.com/monteur-mechanische-deuren" class="bold-on-mobile">Monteur bedrijfsdeuren <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/monteur-mechanische-deuren">
							Vacatures: 0<br>
							Robotiserings%: 91%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/monteur-mechanische-regelaars';"><a href="https://www.jobpersonality.com/monteur-mechanische-regelaars" class="bold-on-mobile">Monteur mechanisch <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/monteur-mechanische-regelaars">
							Vacatures: 73<br>
							Robotiserings%: 63%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/verwarmingsmonteur';"><a href="https://www.jobpersonality.com/verwarmingsmonteur" class="bold-on-mobile">Verwarmingsmonteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/verwarmingsmonteur">
							Vacatures: 0<br>
							Robotiserings%: 65%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/installatiemonteur';"><a href="https://www.jobpersonality.com/installatiemonteur" class="bold-on-mobile">Installatiemonteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/installatiemonteur">
							Vacatures: 117<br>
							Robotiserings%: 40%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/monteur-koelingen';"><a href="https://www.jobpersonality.com/monteur-koelingen" class="bold-on-mobile">Koelmonteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/monteur-koelingen">
							Vacatures: 18<br>
							Robotiserings%: 65%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/monteur-huishoudelijke-apparatuur';"><a href="https://www.jobpersonality.com/monteur-huishoudelijke-apparatuur" class="bold-on-mobile">Monteur huishoudelijke apparatuur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/monteur-huishoudelijke-apparatuur">
							Vacatures: 0<br>
							Robotiserings%: 72%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/monteur-industriele-machines';"><a href="https://www.jobpersonality.com/monteur-industriele-machines" class="bold-on-mobile">Monteur industrie <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/monteur-industriele-machines">
							Vacatures: 26<br>
							Robotiserings%: 67%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/machinebouwer';"><a href="https://www.jobpersonality.com/machinebouwer" class="bold-on-mobile">Machinebouwer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/machinebouwer">
							Vacatures: 49<br>
							Robotiserings%: 59%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/reparateur-vuurvast-materialen';"><a href="https://www.jobpersonality.com/reparateur-vuurvast-materialen" class="bold-on-mobile">Monteur vuurvast materialen <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/reparateur-vuurvast-materialen">
							Vacatures: 0<br>
							Robotiserings%: 82%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/monteur-elektriciteitsleidingen';"><a href="https://www.jobpersonality.com/monteur-elektriciteitsleidingen" class="bold-on-mobile">Monteur data <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/monteur-elektriciteitsleidingen">
							Vacatures: 12<br>
							Robotiserings%: 10%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/monteur-telecommunicatieleidingen';"><a href="https://www.jobpersonality.com/monteur-telecommunicatieleidingen" class="bold-on-mobile">Kabelmonteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/monteur-telecommunicatieleidingen">
							Vacatures: 0<br>
							Robotiserings%: 49%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/monteur-camera-en-fotoapparatuur';"><a href="https://www.jobpersonality.com/monteur-camera-en-fotoapparatuur" class="bold-on-mobile">Monteur camera- en fotoapparatuur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/monteur-camera-en-fotoapparatuur">
							Vacatures: 0<br>
							Robotiserings%: 97%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/monteur-medische-apparatuur';"><a href="https://www.jobpersonality.com/monteur-medische-apparatuur" class="bold-on-mobile">Medisch instrumentatietechnicus <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/monteur-medische-apparatuur">
							Vacatures: 0<br>
							Robotiserings%: 27%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/muziekinstrumentenmaker';"><a href="https://www.jobpersonality.com/muziekinstrumentenmaker" class="bold-on-mobile">Muziekinstrumentenmaker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/muziekinstrumentenmaker">
							Vacatures: 0<br>
							Robotiserings%: 91%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/horlogereparateur';"><a href="https://www.jobpersonality.com/horlogereparateur" class="bold-on-mobile">Horlogereparateur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/horlogereparateur">
							Vacatures: 0<br>
							Robotiserings%: 99%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medewerker-onderhoud-en-reparatie';"><a href="https://www.jobpersonality.com/medewerker-onderhoud-en-reparatie" class="bold-on-mobile">Onderhoudsmonteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medewerker-onderhoud-en-reparatie">
							Vacatures: 405<br>
							Robotiserings%: 64%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/servicemonteur-windturbines';"><a href="https://www.jobpersonality.com/servicemonteur-windturbines" class="bold-on-mobile">Servicemonteur windturbines <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/servicemonteur-windturbines">
							Vacatures: 7<br>
							Robotiserings%: 64%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/monteur-wissel-snoep-speelautomaten';"><a href="https://www.jobpersonality.com/monteur-wissel-snoep-speelautomaten" class="bold-on-mobile">Monteur automaten <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/monteur-wissel-snoep-speelautomaten">
							Vacatures: 1<br>
							Robotiserings%: 94%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/beroepsduiker';"><a href="https://www.jobpersonality.com/beroepsduiker" class="bold-on-mobile">Beroepsduiker  <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/beroepsduiker">
							Vacatures: 0<br>
							Robotiserings%: 18%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/monteur-seinen-wissels';"><a href="https://www.jobpersonality.com/monteur-seinen-wissels" class="bold-on-mobile">Monteur seinwezen <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/monteur-seinen-wissels">
							Vacatures: 1<br>
							Robotiserings%: 90%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/monteur-geothermische-energie';"><a href="https://www.jobpersonality.com/monteur-geothermische-energie" class="bold-on-mobile">Monteur geothermische energie <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/monteur-geothermische-energie">
							Vacatures: 18<br>
							Robotiserings%: 50%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/productiemanager';"><a href="https://www.jobpersonality.com/productiemanager" class="bold-on-mobile">Productiemanager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/productiemanager">
							Vacatures: 25<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/assemblage-monteur-luchtvaart';"><a href="https://www.jobpersonality.com/assemblage-monteur-luchtvaart" class="bold-on-mobile">Assemblagemonteur luchtvaart <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/assemblage-monteur-luchtvaart">
							Vacatures: 0<br>
							Robotiserings%: 79%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/assemblagemedewerker-elektronische-apparatuur';"><a href="https://www.jobpersonality.com/assemblagemedewerker-elektronische-apparatuur" class="bold-on-mobile">Elektronisch assemblagemedewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/assemblagemedewerker-elektronische-apparatuur">
							Vacatures: 0<br>
							Robotiserings%: 95%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/assemblagemedewerker-elektromechanische-apparatuur';"><a href="https://www.jobpersonality.com/assemblagemedewerker-elektromechanische-apparatuur" class="bold-on-mobile">Elektromechanisch assemblagemedewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/assemblagemedewerker-elektromechanische-apparatuur">
							Vacatures: 0<br>
							Robotiserings%: 97%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/assemblagemedewerker-machines';"><a href="https://www.jobpersonality.com/assemblagemedewerker-machines" class="bold-on-mobile">Assemblagemedewerker machines <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/assemblagemedewerker-machines">
							Vacatures: 3<br>
							Robotiserings%: 82%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/metaalbewerker';"><a href="https://www.jobpersonality.com/metaalbewerker" class="bold-on-mobile">Metaalbewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/metaalbewerker">
							Vacatures: 49<br>
							Robotiserings%: 93%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/carrosseriebouwer';"><a href="https://www.jobpersonality.com/carrosseriebouwer" class="bold-on-mobile">Carrosseriebouwer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/carrosseriebouwer">
							Vacatures: 10<br>
							Robotiserings%: 97%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/glasvezelmonteur';"><a href="https://www.jobpersonality.com/glasvezelmonteur" class="bold-on-mobile">Glasvezelmonteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/glasvezelmonteur">
							Vacatures: 8<br>
							Robotiserings%: 49%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/assembleur-tijdmetingsapparatuur';"><a href="https://www.jobpersonality.com/assembleur-tijdmetingsapparatuur" class="bold-on-mobile">Assembleur tijdmetingsapparatuur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/assembleur-tijdmetingsapparatuur">
							Vacatures: 0<br>
							Robotiserings%: 98%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bakker';"><a href="https://www.jobpersonality.com/bakker" class="bold-on-mobile">Bakker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bakker">
							Vacatures: 9<br>
							Robotiserings%: 89%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/slager';"><a href="https://www.jobpersonality.com/slager" class="bold-on-mobile">Slager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/slager">
							Vacatures: 19<br>
							Robotiserings%: 93%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/productiemedewerker-vlees';"><a href="https://www.jobpersonality.com/productiemedewerker-vlees" class="bold-on-mobile">Productiemedewerker slagerij <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/productiemedewerker-vlees">
							Vacatures: 0<br>
							Robotiserings%: 60%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/operator-voedingsmiddelen';"><a href="https://www.jobpersonality.com/operator-voedingsmiddelen" class="bold-on-mobile">Operator voeding <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/operator-voedingsmiddelen">
							Vacatures: 5<br>
							Robotiserings%: 70%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/robotoperator';"><a href="https://www.jobpersonality.com/robotoperator" class="bold-on-mobile">Robot operator <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/robotoperator">
							Vacatures: 0<br>
							Robotiserings%: 86%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/robot-programmeur';"><a href="https://www.jobpersonality.com/robot-programmeur" class="bold-on-mobile">Robot programmeur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/robot-programmeur">
							Vacatures: 1<br>
							Robotiserings%: 36%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/operator-draaibank';"><a href="https://www.jobpersonality.com/operator-draaibank" class="bold-on-mobile">Draaier <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/operator-draaibank">
							Vacatures: 26<br>
							Robotiserings%: 84%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/operator-schaafmachines';"><a href="https://www.jobpersonality.com/operator-schaafmachines" class="bold-on-mobile">Schaver <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/operator-schaafmachines">
							Vacatures: 3<br>
							Robotiserings%: 98%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/onderhoudsmachinist';"><a href="https://www.jobpersonality.com/onderhoudsmachinist" class="bold-on-mobile">Onderhoudsmonteur machines <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/onderhoudsmachinist">
							Vacatures: 195<br>
							Robotiserings%: 65%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/metaalgieter';"><a href="https://www.jobpersonality.com/metaalgieter" class="bold-on-mobile">Metaalgieter <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/metaalgieter">
							Vacatures: 1<br>
							Robotiserings%: 87%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/modelmaker-industrie';"><a href="https://www.jobpersonality.com/modelmaker-industrie" class="bold-on-mobile">Mallenmaker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/modelmaker-industrie">
							Vacatures: 2<br>
							Robotiserings%: 93%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/cnc-operator';"><a href="https://www.jobpersonality.com/cnc-operator" class="bold-on-mobile">CNC operator <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/cnc-operator">
							Vacatures: 43<br>
							Robotiserings%: 90%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/gereedschapmaker';"><a href="https://www.jobpersonality.com/gereedschapmaker" class="bold-on-mobile">Gereedschapmaker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/gereedschapmaker">
							Vacatures: 0<br>
							Robotiserings%: 84%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/lasser';"><a href="https://www.jobpersonality.com/lasser" class="bold-on-mobile">Lasser <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/lasser">
							Vacatures: 226<br>
							Robotiserings%: 94%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/frezer';"><a href="https://www.jobpersonality.com/frezer" class="bold-on-mobile">Frezer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/frezer">
							Vacatures: 35<br>
							Robotiserings%: 94%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/operator-las-en-soldeermachine';"><a href="https://www.jobpersonality.com/operator-las-en-soldeermachine" class="bold-on-mobile">Operator lasrobot <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/operator-las-en-soldeermachine">
							Vacatures: 4<br>
							Robotiserings%: 61%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/operator-coating';"><a href="https://www.jobpersonality.com/operator-coating" class="bold-on-mobile">Operator coating <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/operator-coating">
							Vacatures: 1<br>
							Robotiserings%: 92%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/drukvoorbereider';"><a href="https://www.jobpersonality.com/drukvoorbereider" class="bold-on-mobile">Medewerker printmedia <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/drukvoorbereider">
							Vacatures: 0<br>
							Robotiserings%: 97%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/drukker-print-operator';"><a href="https://www.jobpersonality.com/drukker-print-operator" class="bold-on-mobile">Print operator <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/drukker-print-operator">
							Vacatures: 0<br>
							Robotiserings%: 83%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/inbinder-nabewerker';"><a href="https://www.jobpersonality.com/inbinder-nabewerker" class="bold-on-mobile">Nabewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/inbinder-nabewerker">
							Vacatures: 1<br>
							Robotiserings%: 95%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/schoenmaker';"><a href="https://www.jobpersonality.com/schoenmaker" class="bold-on-mobile">Schoenmaker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/schoenmaker">
							Vacatures: 3<br>
							Robotiserings%: 52%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/kleermaker';"><a href="https://www.jobpersonality.com/kleermaker" class="bold-on-mobile">Coupeuse of Kleermaker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/kleermaker">
							Vacatures: 0<br>
							Robotiserings%: 84%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/patroonmaker-kledingproductie';"><a href="https://www.jobpersonality.com/patroonmaker-kledingproductie" class="bold-on-mobile">Patroonmaker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/patroonmaker-kledingproductie">
							Vacatures: 0<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/stoffeerder';"><a href="https://www.jobpersonality.com/stoffeerder" class="bold-on-mobile">Stoffeerder <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/stoffeerder">
							Vacatures: 8<br>
							Robotiserings%: 39%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/houtbewerker';"><a href="https://www.jobpersonality.com/houtbewerker" class="bold-on-mobile">Houtbewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/houtbewerker">
							Vacatures: 31<br>
							Robotiserings%: 92%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/meubelrestaurateur';"><a href="https://www.jobpersonality.com/meubelrestaurateur" class="bold-on-mobile">Meubelrestaurateur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/meubelrestaurateur">
							Vacatures: 0<br>
							Robotiserings%: 87%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/meubelmaker';"><a href="https://www.jobpersonality.com/meubelmaker" class="bold-on-mobile">Meubelmaker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/meubelmaker">
							Vacatures: 18<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/modelmaker-hout';"><a href="https://www.jobpersonality.com/modelmaker-hout" class="bold-on-mobile">Modelmaker hout <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/modelmaker-hout">
							Vacatures: 0<br>
							Robotiserings%: 96%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/parketlegger';"><a href="https://www.jobpersonality.com/parketlegger" class="bold-on-mobile">Parketlegger <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/parketlegger">
							Vacatures: 0<br>
							Robotiserings%: 91%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/operator-kerncentrale';"><a href="https://www.jobpersonality.com/operator-kerncentrale" class="bold-on-mobile">Operator kerncentrale <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/operator-kerncentrale">
							Vacatures: 0<br>
							Robotiserings%: 95%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/operator-energiecentrale';"><a href="https://www.jobpersonality.com/operator-energiecentrale" class="bold-on-mobile">Operator energiecentrale <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/operator-energiecentrale">
							Vacatures: 0<br>
							Robotiserings%: 64%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/technicus-energiecentrale';"><a href="https://www.jobpersonality.com/technicus-energiecentrale" class="bold-on-mobile">Technicus energiecentrale <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/technicus-energiecentrale">
							Vacatures: 1<br>
							Robotiserings%: 85%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/monteur-gasturbines';"><a href="https://www.jobpersonality.com/monteur-gasturbines" class="bold-on-mobile">Monteur gasturbines <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/monteur-gasturbines">
							Vacatures: 3<br>
							Robotiserings%: 89%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/operator-waterzuiveringsinstallatie';"><a href="https://www.jobpersonality.com/operator-waterzuiveringsinstallatie" class="bold-on-mobile">Operator waterzuivering <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/operator-waterzuiveringsinstallatie">
							Vacatures: 0<br>
							Robotiserings%: 61%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/operator-chemische-fabriek';"><a href="https://www.jobpersonality.com/operator-chemische-fabriek" class="bold-on-mobile">Procesoperator chemie <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/operator-chemische-fabriek">
							Vacatures: 10<br>
							Robotiserings%: 85%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/operator-gascentrale';"><a href="https://www.jobpersonality.com/operator-gascentrale" class="bold-on-mobile">Operator gascentrale <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/operator-gascentrale">
							Vacatures: 0<br>
							Robotiserings%: 78%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/operator-raffinaderij';"><a href="https://www.jobpersonality.com/operator-raffinaderij" class="bold-on-mobile">Operator raffinaderij <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/operator-raffinaderij">
							Vacatures: 0<br>
							Robotiserings%: 71%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/technicus-biomassacentrale';"><a href="https://www.jobpersonality.com/technicus-biomassacentrale" class="bold-on-mobile">Operator biogascentrale <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/technicus-biomassacentrale">
							Vacatures: 0<br>
							Robotiserings%: 86%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/operator-raffinage-apparatuur';"><a href="https://www.jobpersonality.com/operator-raffinage-apparatuur" class="bold-on-mobile">Operator raffinage <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/operator-raffinage-apparatuur">
							Vacatures: 0<br>
							Robotiserings%: 88%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/qc-medewerker';"><a href="https://www.jobpersonality.com/qc-medewerker" class="bold-on-mobile">QC medewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/qc-medewerker">
							Vacatures: 3<br>
							Robotiserings%: 98%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/juwelier';"><a href="https://www.jobpersonality.com/juwelier" class="bold-on-mobile">Juwelier <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/juwelier">
							Vacatures: 0<br>
							Robotiserings%: 92%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/edelsteen-diamantbewerker';"><a href="https://www.jobpersonality.com/edelsteen-diamantbewerker" class="bold-on-mobile">Edelsteen- en diamantbewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/edelsteen-diamantbewerker">
							Vacatures: 0<br>
							Robotiserings%: 95%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/goudsmid';"><a href="https://www.jobpersonality.com/goudsmid" class="bold-on-mobile">Goudsmid <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/goudsmid">
							Vacatures: 0<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/tandheelkundig-laborant';"><a href="https://www.jobpersonality.com/tandheelkundig-laborant" class="bold-on-mobile">Tandheelkundig laborant <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/tandheelkundig-laborant">
							Vacatures: 0<br>
							Robotiserings%: 97%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medisch-technicus';"><a href="https://www.jobpersonality.com/medisch-technicus" class="bold-on-mobile">Medisch technicus <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medisch-technicus">
							Vacatures: 0<br>
							Robotiserings%: 45%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/autospuiter';"><a href="https://www.jobpersonality.com/autospuiter" class="bold-on-mobile">Autospuiter <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/autospuiter">
							Vacatures: 10<br>
							Robotiserings%: 69%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/decorateur';"><a href="https://www.jobpersonality.com/decorateur" class="bold-on-mobile">Decorateur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/decorateur">
							Vacatures: 0<br>
							Robotiserings%: 92%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/halfgeleiderverwerker';"><a href="https://www.jobpersonality.com/halfgeleiderverwerker" class="bold-on-mobile">Semiconductor operator <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/halfgeleiderverwerker">
							Vacatures: 15<br>
							Robotiserings%: 88%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/foto-ontwikkelaar';"><a href="https://www.jobpersonality.com/foto-ontwikkelaar" class="bold-on-mobile">Foto-ontwikkelaar <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/foto-ontwikkelaar">
							Vacatures: 0<br>
							Robotiserings%: 99%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/graffiti-verwijderaar';"><a href="https://www.jobpersonality.com/graffiti-verwijderaar" class="bold-on-mobile">Graffiti verwijderaar <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/graffiti-verwijderaar">
							Vacatures: 5<br>
							Robotiserings%: 66%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/grafisch-medewerker';"><a href="https://www.jobpersonality.com/grafisch-medewerker" class="bold-on-mobile">Grafisch medewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/grafisch-medewerker">
							Vacatures: 0<br>
							Robotiserings%: 98%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/glasblazer';"><a href="https://www.jobpersonality.com/glasblazer" class="bold-on-mobile">Glasblazer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/glasblazer">
							Vacatures: 2<br>
							Robotiserings%: 90%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/pottenbakker';"><a href="https://www.jobpersonality.com/pottenbakker" class="bold-on-mobile">Keramist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/pottenbakker">
							Vacatures: 0<br>
							Robotiserings%: 90%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/luchtvrachtmanager';"><a href="https://www.jobpersonality.com/luchtvrachtmanager" class="bold-on-mobile">Luchtvrachtmanager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/luchtvrachtmanager">
							Vacatures: 0<br>
							Robotiserings%: 7%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/helikopterpiloot';"><a href="https://www.jobpersonality.com/helikopterpiloot" class="bold-on-mobile">Helikopterpiloot <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/helikopterpiloot">
							Vacatures: 0<br>
							Robotiserings%: 55%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/aviation-operations-officer';"><a href="https://www.jobpersonality.com/aviation-operations-officer" class="bold-on-mobile">Aviation operations officer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/aviation-operations-officer">
							Vacatures: 0<br>
							Robotiserings%: 71%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/steward-stewardess';"><a href="https://www.jobpersonality.com/steward-stewardess" class="bold-on-mobile">Stewardess <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/steward-stewardess">
							Vacatures: 1<br>
							Robotiserings%: 35%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/ambulancechauffeur-verzorger';"><a href="https://www.jobpersonality.com/ambulancechauffeur-verzorger" class="bold-on-mobile">Ambulancechauffeur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/ambulancechauffeur-verzorger">
							Vacatures: 0<br>
							Robotiserings%: 25%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/buschauffeur';"><a href="https://www.jobpersonality.com/buschauffeur" class="bold-on-mobile">Buschauffeur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/buschauffeur">
							Vacatures: 186<br>
							Robotiserings%: 67%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/leerlingenvervoerder';"><a href="https://www.jobpersonality.com/leerlingenvervoerder" class="bold-on-mobile">Leerlingenvervoerder <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/leerlingenvervoerder">
							Vacatures: 0<br>
							Robotiserings%: 89%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/vrachtwagenchauffeur';"><a href="https://www.jobpersonality.com/vrachtwagenchauffeur" class="bold-on-mobile">Vrachtwagenchauffeur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/vrachtwagenchauffeur">
							Vacatures: 1306<br>
							Robotiserings%: 79%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/taxichauffeur';"><a href="https://www.jobpersonality.com/taxichauffeur" class="bold-on-mobile">Taxichauffeur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/taxichauffeur">
							Vacatures: 9<br>
							Robotiserings%: 89%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/machinist';"><a href="https://www.jobpersonality.com/machinist" class="bold-on-mobile">Machinist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/machinist">
							Vacatures: 0<br>
							Robotiserings%: 96%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/werfmachinist';"><a href="https://www.jobpersonality.com/werfmachinist" class="bold-on-mobile">Werfmachinist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/werfmachinist">
							Vacatures: 0<br>
							Robotiserings%: 91%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/metro-trammachinist';"><a href="https://www.jobpersonality.com/metro-trammachinist" class="bold-on-mobile">Metro- of Trammachinist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/metro-trammachinist">
							Vacatures: 6<br>
							Robotiserings%: 86%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/matroos';"><a href="https://www.jobpersonality.com/matroos" class="bold-on-mobile">Matroos <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/matroos">
							Vacatures: 4<br>
							Robotiserings%: 83%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/kapitein-binnenvaart';"><a href="https://www.jobpersonality.com/kapitein-binnenvaart" class="bold-on-mobile">Schipper <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/kapitein-binnenvaart">
							Vacatures: 1<br>
							Robotiserings%: 27%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/stuurman';"><a href="https://www.jobpersonality.com/stuurman" class="bold-on-mobile">Stuurman <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/stuurman">
							Vacatures: 7<br>
							Robotiserings%: 27%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/schipper';"><a href="https://www.jobpersonality.com/schipper" class="bold-on-mobile">Schipper kleine boten <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/schipper">
							Vacatures: 1<br>
							Robotiserings%: 62%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/scheepswerktuigkundige';"><a href="https://www.jobpersonality.com/scheepswerktuigkundige" class="bold-on-mobile">Scheepswerktuigkundige <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/scheepswerktuigkundige">
							Vacatures: 7<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/brugwachter';"><a href="https://www.jobpersonality.com/brugwachter" class="bold-on-mobile">Brugwachter <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/brugwachter">
							Vacatures: 0<br>
							Robotiserings%: 97%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/verkeerstechnicus';"><a href="https://www.jobpersonality.com/verkeerstechnicus" class="bold-on-mobile">Verkeerstechnicus <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/verkeerstechnicus">
							Vacatures: 0<br>
							Robotiserings%: 90%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/hijskraanmachinist';"><a href="https://www.jobpersonality.com/hijskraanmachinist" class="bold-on-mobile">Hijskraanmachinist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/hijskraanmachinist">
							Vacatures: 78<br>
							Robotiserings%: 90%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/baggeraar';"><a href="https://www.jobpersonality.com/baggeraar" class="bold-on-mobile">Baggeraar <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/baggeraar">
							Vacatures: 0<br>
							Robotiserings%: 92%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/graafmachinist';"><a href="https://www.jobpersonality.com/graafmachinist" class="bold-on-mobile">Graafmachinist  <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/graafmachinist">
							Vacatures: 78<br>
							Robotiserings%: 94%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/compressor-technicus';"><a href="https://www.jobpersonality.com/compressor-technicus" class="bold-on-mobile">Compressor technicus <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/compressor-technicus">
							Vacatures: 18<br>
							Robotiserings%: 91%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/veilingmeester';"><a href="https://www.jobpersonality.com/veilingmeester" class="bold-on-mobile">Veilingmeester <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/veilingmeester">
							Vacatures: 0<br>
							Robotiserings%: 90%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/banketbakker';"><a href="https://www.jobpersonality.com/banketbakker" class="bold-on-mobile">Banketbakker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/banketbakker">
							Vacatures: 163<br>
							Robotiserings%: 8%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/etaleur';"><a href="https://www.jobpersonality.com/etaleur" class="bold-on-mobile">Visual merchandiser <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/etaleur">
							Vacatures: 2<br>
							Robotiserings%: 48%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/tandtechnicus-medewerker';"><a href="https://www.jobpersonality.com/tandtechnicus-medewerker" class="bold-on-mobile">Tandtechnicus medewerker  <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/tandtechnicus-medewerker">
							Vacatures: 0<br>
							Robotiserings%: 97%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/waardetransporteur';"><a href="https://www.jobpersonality.com/waardetransporteur" class="bold-on-mobile">Waardetransporteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/waardetransporteur">
							Vacatures: 0<br>
							Robotiserings%: 69%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/standbouwer';"><a href="https://www.jobpersonality.com/standbouwer" class="bold-on-mobile">Standbouwer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/standbouwer">
							Vacatures: 4<br>
							Robotiserings%: 18%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/montagemedewerker';"><a href="https://www.jobpersonality.com/montagemedewerker" class="bold-on-mobile">Montagemedewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/montagemedewerker">
							Vacatures: 109<br>
							Robotiserings%: 98%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/drone-piloot';"><a href="https://www.jobpersonality.com/drone-piloot" class="bold-on-mobile">Drone piloot <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/drone-piloot">
							Vacatures: 0<br>
							Robotiserings%: 5%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/commercieel-piloot';"><a href="https://www.jobpersonality.com/commercieel-piloot" class="bold-on-mobile">Commercieel piloot <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/commercieel-piloot">
							Vacatures: 0<br>
							Robotiserings%: 55%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/domotica-adviseur';"><a href="https://www.jobpersonality.com/domotica-adviseur" class="bold-on-mobile">Domotica adviseur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/domotica-adviseur">
							Vacatures: 0<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/vlogger';"><a href="https://www.jobpersonality.com/vlogger" class="bold-on-mobile">Vlogger <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/vlogger">
							Vacatures: 0<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/strandtenthouder';"><a href="https://www.jobpersonality.com/strandtenthouder" class="bold-on-mobile">Strandtenthouder <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/strandtenthouder">
							Vacatures: 0<br>
							Robotiserings%: 8%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/zwemleraar';"><a href="https://www.jobpersonality.com/zwemleraar" class="bold-on-mobile">Zweminstructeur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/zwemleraar">
							Vacatures: 2<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/junior-accountmanager';"><a href="https://www.jobpersonality.com/junior-accountmanager" class="bold-on-mobile">Junior accountmanager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/junior-accountmanager">
							Vacatures: 56<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/adviseur-schadeverzekeringen';"><a href="https://www.jobpersonality.com/adviseur-schadeverzekeringen" class="bold-on-mobile">Adviseur schadeverzekeringen <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/adviseur-schadeverzekeringen">
							Vacatures: 0<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/aftersales-manager';"><a href="https://www.jobpersonality.com/aftersales-manager" class="bold-on-mobile">Aftersales manager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/aftersales-manager">
							Vacatures: 7<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/verkoopadviseur-automotive';"><a href="https://www.jobpersonality.com/verkoopadviseur-automotive" class="bold-on-mobile">Autoverkoper <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/verkoopadviseur-automotive">
							Vacatures: 3<br>
							Robotiserings%: 85%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/verkoopadviseur';"><a href="https://www.jobpersonality.com/verkoopadviseur" class="bold-on-mobile">Verkoopadviseur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/verkoopadviseur">
							Vacatures: 57<br>
							Robotiserings%: 85%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medewerker-afvalbeheer';"><a href="https://www.jobpersonality.com/medewerker-afvalbeheer" class="bold-on-mobile">Medewerker afvalbeheer  <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medewerker-afvalbeheer">
							Vacatures: 9<br>
							Robotiserings%: 98%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/agogisch-medewerker';"><a href="https://www.jobpersonality.com/agogisch-medewerker" class="bold-on-mobile">Agogisch medewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/agogisch-medewerker">
							Vacatures: 0<br>
							Robotiserings%: 13%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/monteur-koudetechniek';"><a href="https://www.jobpersonality.com/monteur-koudetechniek" class="bold-on-mobile">Monteur koudetechniek <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/monteur-koudetechniek">
							Vacatures: 1<br>
							Robotiserings%: 40%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/monteur-airconditioning';"><a href="https://www.jobpersonality.com/monteur-airconditioning" class="bold-on-mobile">Monteur airconditioning <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/monteur-airconditioning">
							Vacatures: 2<br>
							Robotiserings%: 40%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/applicatieontwikkelaar';"><a href="https://www.jobpersonality.com/applicatieontwikkelaar" class="bold-on-mobile">App developer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/applicatieontwikkelaar">
							Vacatures: 3<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/asfaltwerker';"><a href="https://www.jobpersonality.com/asfaltwerker" class="bold-on-mobile">Asfaltafwerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/asfaltwerker">
							Vacatures: 1<br>
							Robotiserings%: 96%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/assemblagetechnicus-mobiliteitsbranche';"><a href="https://www.jobpersonality.com/assemblagetechnicus-mobiliteitsbranche" class="bold-on-mobile">Assemblagetechnicus mobiliteit <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/assemblagetechnicus-mobiliteitsbranche">
							Vacatures: 0<br>
							Robotiserings%: 79%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/zelfstandig-bakker';"><a href="https://www.jobpersonality.com/zelfstandig-bakker" class="bold-on-mobile">Zelfstandig bakker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/zelfstandig-bakker">
							Vacatures: 3<br>
							Robotiserings%: 8%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/balkman';"><a href="https://www.jobpersonality.com/balkman" class="bold-on-mobile">Balkman <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/balkman">
							Vacatures: 1<br>
							Robotiserings%: 80%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/zelfstandig-bloemist';"><a href="https://www.jobpersonality.com/zelfstandig-bloemist" class="bold-on-mobile">Zelfstandig bloemist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/zelfstandig-bloemist">
							Vacatures: 0<br>
							Robotiserings%: 5%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/begeleider-gehandicaptenzorg';"><a href="https://www.jobpersonality.com/begeleider-gehandicaptenzorg" class="bold-on-mobile">Begeleider gehandicaptenzorg <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/begeleider-gehandicaptenzorg">
							Vacatures: 105<br>
							Robotiserings%: 39%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/sociaal-cultureel-werker';"><a href="https://www.jobpersonality.com/sociaal-cultureel-werker" class="bold-on-mobile">Sociaal-cultureel werker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/sociaal-cultureel-werker">
							Vacatures: 0<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/zorgbegeleider';"><a href="https://www.jobpersonality.com/zorgbegeleider" class="bold-on-mobile">Zorgbegeleider <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/zorgbegeleider">
							Vacatures: 0<br>
							Robotiserings%: 39%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/beheerder-milieustraat';"><a href="https://www.jobpersonality.com/beheerder-milieustraat" class="bold-on-mobile">Beheerder milieustraat <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/beheerder-milieustraat">
							Vacatures: 9<br>
							Robotiserings%: 60%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/betonstaalverwerker';"><a href="https://www.jobpersonality.com/betonstaalverwerker" class="bold-on-mobile">Betonstaalverwerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/betonstaalverwerker">
							Vacatures: 0<br>
							Robotiserings%: 90%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/betonreparateur';"><a href="https://www.jobpersonality.com/betonreparateur" class="bold-on-mobile">Betonreparateur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/betonreparateur">
							Vacatures: 20<br>
							Robotiserings%: 82%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/behoudsmedewerker';"><a href="https://www.jobpersonality.com/behoudsmedewerker" class="bold-on-mobile">Behoudsmedewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/behoudsmedewerker">
							Vacatures: 0<br>
							Robotiserings%: 80%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bootman';"><a href="https://www.jobpersonality.com/bootman" class="bold-on-mobile">Bootman <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bootman">
							Vacatures: 0<br>
							Robotiserings%: 72%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/ondernemer-retail';"><a href="https://www.jobpersonality.com/ondernemer-retail" class="bold-on-mobile">Ondernemer retail of detailhandel <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/ondernemer-retail">
							Vacatures: 0<br>
							Robotiserings%: 8%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medewerker-logistiek';"><a href="https://www.jobpersonality.com/medewerker-logistiek" class="bold-on-mobile">Logistiek medewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medewerker-logistiek">
							Vacatures: 548<br>
							Robotiserings%: 95%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/revalidatieverpleegkundige';"><a href="https://www.jobpersonality.com/revalidatieverpleegkundige" class="bold-on-mobile">Revalidatieverpleegkundige <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/revalidatieverpleegkundige">
							Vacatures: 0<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/zelfstandig-werkend-kok';"><a href="https://www.jobpersonality.com/zelfstandig-werkend-kok" class="bold-on-mobile">Zelfstandig werkend kok <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/zelfstandig-werkend-kok">
							Vacatures: 196<br>
							Robotiserings%: 63%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/sommelier';"><a href="https://www.jobpersonality.com/sommelier" class="bold-on-mobile">Sommelier <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/sommelier">
							Vacatures: 9<br>
							Robotiserings%: 97%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/voeger-of-gevelbehandelaar';"><a href="https://www.jobpersonality.com/voeger-of-gevelbehandelaar" class="bold-on-mobile">Voeger <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/voeger-of-gevelbehandelaar">
							Vacatures: 4<br>
							Robotiserings%: 85%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/glazenier';"><a href="https://www.jobpersonality.com/glazenier" class="bold-on-mobile">Glazenier <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/glazenier">
							Vacatures: 0<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/glazenwasser';"><a href="https://www.jobpersonality.com/glazenwasser" class="bold-on-mobile">Glazenwasser <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/glazenwasser">
							Vacatures: 22<br>
							Robotiserings%: 66%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/objectleider';"><a href="https://www.jobpersonality.com/objectleider" class="bold-on-mobile">Objectleider <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/objectleider">
							Vacatures: 0<br>
							Robotiserings%: 94%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/action/jobs/job/1041/medewerker-teelt/';"><a href="https://www.jobpersonality.com/action/jobs/job/1041/medewerker-teelt/" class="bold-on-mobile">Medewerker teelt <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/action/jobs/job/1041/medewerker-teelt/">
							Vacatures: 7<br>
							Robotiserings%: 75%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/instructeur-paardrijlessen';"><a href="https://www.jobpersonality.com/instructeur-paardrijlessen" class="bold-on-mobile">Instructeur paardensport <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/instructeur-paardrijlessen">
							Vacatures: 0<br>
							Robotiserings%: 9%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/intercedent';"><a href="https://www.jobpersonality.com/intercedent" class="bold-on-mobile">Intercedent <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/intercedent">
							Vacatures: 1960<br>
							Robotiserings%: 31%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/interieuradviseur';"><a href="https://www.jobpersonality.com/interieuradviseur" class="bold-on-mobile">Interieuradviseur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/interieuradviseur">
							Vacatures: 0<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/hoefsmid';"><a href="https://www.jobpersonality.com/hoefsmid" class="bold-on-mobile">Hoefsmid <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/hoefsmid">
							Vacatures: 0<br>
							Robotiserings%: 82%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/kunststofbewerker';"><a href="https://www.jobpersonality.com/kunststofbewerker" class="bold-on-mobile">Kunststofbewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/kunststofbewerker">
							Vacatures: 4<br>
							Robotiserings%: 97%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/orthopedisch-schoenmaker';"><a href="https://www.jobpersonality.com/orthopedisch-schoenmaker" class="bold-on-mobile">Orthopedisch schoentechnicus  <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/orthopedisch-schoenmaker">
							Vacatures: 0<br>
							Robotiserings%: 52%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/manager-recreatiemedewerkers';"><a href="https://www.jobpersonality.com/manager-recreatiemedewerkers" class="bold-on-mobile">Hospitality manager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/manager-recreatiemedewerkers">
							Vacatures: 6<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/recherche-assistent';"><a href="https://www.jobpersonality.com/recherche-assistent" class="bold-on-mobile">Recherche assistent  <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/recherche-assistent">
							Vacatures: 5<br>
							Robotiserings%: 34%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medewerker-burgerzaken';"><a href="https://www.jobpersonality.com/medewerker-burgerzaken" class="bold-on-mobile">Medewerker Burgerzaken <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medewerker-burgerzaken">
							Vacatures: 4<br>
							Robotiserings%: 13%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/rijinstructeur';"><a href="https://www.jobpersonality.com/rijinstructeur" class="bold-on-mobile">Rijinstructeur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/rijinstructeur">
							Vacatures: 6<br>
							Robotiserings%: 13%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/persoonlijk-begeleider';"><a href="https://www.jobpersonality.com/persoonlijk-begeleider" class="bold-on-mobile">Persoonlijk begeleider <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/persoonlijk-begeleider">
							Vacatures: 73<br>
							Robotiserings%: 39%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/maritiem-officier';"><a href="https://www.jobpersonality.com/maritiem-officier" class="bold-on-mobile">Maritiem Officier <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/maritiem-officier">
							Vacatures: 3<br>
							Robotiserings%: 19%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/dieselmonteur';"><a href="https://www.jobpersonality.com/dieselmonteur" class="bold-on-mobile">Dieselmonteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/dieselmonteur">
							Vacatures: 3<br>
							Robotiserings%: 73%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/machine-operator';"><a href="https://www.jobpersonality.com/machine-operator" class="bold-on-mobile">Operator <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/machine-operator">
							Vacatures: 1983<br>
							Robotiserings%: 91%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/redactiemedewerker';"><a href="https://www.jobpersonality.com/redactiemedewerker" class="bold-on-mobile">Redactiemedewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/redactiemedewerker">
							Vacatures: 0<br>
							Robotiserings%: 6%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/monteur-gas-water-warmte';"><a href="https://www.jobpersonality.com/monteur-gas-water-warmte" class="bold-on-mobile">Monteur gas, water of warmte <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/monteur-gas-water-warmte">
							Vacatures: 2<br>
							Robotiserings%: 40%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/steigerbouwer';"><a href="https://www.jobpersonality.com/steigerbouwer" class="bold-on-mobile">Steigerbouwer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/steigerbouwer">
							Vacatures: 24<br>
							Robotiserings%: 88%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/musicalperformer-of-musicalartiest';"><a href="https://www.jobpersonality.com/musicalperformer-of-musicalartiest" class="bold-on-mobile">Musicalperformer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/musicalperformer-of-musicalartiest">
							Vacatures: 0<br>
							Robotiserings%: 13%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/planner-wegtransport';"><a href="https://www.jobpersonality.com/planner-wegtransport" class="bold-on-mobile">Logistiek planner <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/planner-wegtransport">
							Vacatures: 16<br>
							Robotiserings%: 99%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/ruimtelijk-vormgever';"><a href="https://www.jobpersonality.com/ruimtelijk-vormgever" class="bold-on-mobile">Ruimtelijk vormgever <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/ruimtelijk-vormgever">
							Vacatures: 0<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/serviceadviseur-automotive';"><a href="https://www.jobpersonality.com/serviceadviseur-automotive" class="bold-on-mobile">Serviceadviseur automotive <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/serviceadviseur-automotive">
							Vacatures: 2<br>
							Robotiserings%: 96%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/signmaker-signontwerper';"><a href="https://www.jobpersonality.com/signmaker-signontwerper" class="bold-on-mobile">Signmaker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/signmaker-signontwerper">
							Vacatures: 1<br>
							Robotiserings%: 8%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/traiteur-of-cateraar';"><a href="https://www.jobpersonality.com/traiteur-of-cateraar" class="bold-on-mobile">Traiteur of Cateraar <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/traiteur-of-cateraar">
							Vacatures: 2<br>
							Robotiserings%: 8%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/sloper';"><a href="https://www.jobpersonality.com/sloper" class="bold-on-mobile">Sloper <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/sloper">
							Vacatures: 6<br>
							Robotiserings%: 53%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/technicus-human-technology';"><a href="https://www.jobpersonality.com/technicus-human-technology" class="bold-on-mobile">Technicus human technology <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/technicus-human-technology">
							Vacatures: 0<br>
							Robotiserings%: 75%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/verbrandingsmotortechnicus';"><a href="https://www.jobpersonality.com/verbrandingsmotortechnicus" class="bold-on-mobile">Verbrandingsmotortechnicus  <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/verbrandingsmotortechnicus">
							Vacatures: 3<br>
							Robotiserings%: 79%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/tekenaar-werktuigbouw';"><a href="https://www.jobpersonality.com/tekenaar-werktuigbouw" class="bold-on-mobile">Tekenaar werktuigbouw <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/tekenaar-werktuigbouw">
							Vacatures: 2<br>
							Robotiserings%: 52%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/uitvoerder';"><a href="https://www.jobpersonality.com/uitvoerder" class="bold-on-mobile">Uitvoerder <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/uitvoerder">
							Vacatures: 1322<br>
							Robotiserings%: 7%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/projectleider-gww';"><a href="https://www.jobpersonality.com/projectleider-gww" class="bold-on-mobile">Projectleider GWW <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/projectleider-gww">
							Vacatures: 6<br>
							Robotiserings%: 7%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medewerker-tuincentrum';"><a href="https://www.jobpersonality.com/medewerker-tuincentrum" class="bold-on-mobile">Medewerker tuincentrum <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medewerker-tuincentrum">
							Vacatures: 0<br>
							Robotiserings%: 92%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/verzorgende-ig';"><a href="https://www.jobpersonality.com/verzorgende-ig" class="bold-on-mobile">Verzorgende IG <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/verzorgende-ig">
							Vacatures: 1272<br>
							Robotiserings%: 47%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/verpleegkundige';"><a href="https://www.jobpersonality.com/verpleegkundige" class="bold-on-mobile">Verpleegkundige <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/verpleegkundige">
							Vacatures: 116<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/manager';"><a href="https://www.jobpersonality.com/manager" class="bold-on-mobile">Manager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/manager">
							Vacatures: 2637<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/procesoperator';"><a href="https://www.jobpersonality.com/procesoperator" class="bold-on-mobile">Procesoperator <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/procesoperator">
							Vacatures: 430<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/boomverzorger';"><a href="https://www.jobpersonality.com/boomverzorger" class="bold-on-mobile">Boomverzorger <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/boomverzorger">
							Vacatures: 131<br>
							Robotiserings%: 77%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/hondentrimmer';"><a href="https://www.jobpersonality.com/hondentrimmer" class="bold-on-mobile">Hondentrimmer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/hondentrimmer">
							Vacatures: 0<br>
							Robotiserings%: 82%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/drone-technicus';"><a href="https://www.jobpersonality.com/drone-technicus" class="bold-on-mobile">Drone technicus <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/drone-technicus">
							Vacatures: 0<br>
							Robotiserings%: 15%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/assemblage-monteur';"><a href="https://www.jobpersonality.com/assemblage-monteur" class="bold-on-mobile">Assemblagemonteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/assemblage-monteur">
							Vacatures: 215<br>
							Robotiserings%: 93%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/promotiemedewerker';"><a href="https://www.jobpersonality.com/promotiemedewerker" class="bold-on-mobile">Promotiemedewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/promotiemedewerker">
							Vacatures: 35<br>
							Robotiserings%: 94%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bagagemedewerker';"><a href="https://www.jobpersonality.com/bagagemedewerker" class="bold-on-mobile">Bagagemedewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bagagemedewerker">
							Vacatures: 3<br>
							Robotiserings%: 0%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/toezichthouder';"><a href="https://www.jobpersonality.com/toezichthouder" class="bold-on-mobile">Toezichthouder <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/toezichthouder">
							Vacatures: 74<br>
							Robotiserings%: 8%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/asbestsaneerder';"><a href="https://www.jobpersonality.com/asbestsaneerder" class="bold-on-mobile">Asbestsaneerder <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/asbestsaneerder">
							Vacatures: 3<br>
							Robotiserings%: 53%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/cv-monteur';"><a href="https://www.jobpersonality.com/cv-monteur" class="bold-on-mobile">CV monteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/cv-monteur">
							Vacatures: 34<br>
							Robotiserings%: 65%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/kipper-chauffeur';"><a href="https://www.jobpersonality.com/kipper-chauffeur" class="bold-on-mobile">Kipper chauffeur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/kipper-chauffeur">
							Vacatures: 20<br>
							Robotiserings%: 79%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/kraamverzorgende';"><a href="https://www.jobpersonality.com/kraamverzorgende" class="bold-on-mobile">Kraamverzorgende <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/kraamverzorgende">
							Vacatures: 1<br>
							Robotiserings%: 47%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/service-engineer';"><a href="https://www.jobpersonality.com/service-engineer" class="bold-on-mobile">Service engineer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/service-engineer">
							Vacatures: 192<br>
							Robotiserings%: 52%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/administratief-medewerker';"><a href="https://www.jobpersonality.com/administratief-medewerker" class="bold-on-mobile">Administratief medewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/administratief-medewerker">
							Vacatures: 300<br>
							Robotiserings%: 98%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/visagist';"><a href="https://www.jobpersonality.com/visagist" class="bold-on-mobile">Visagist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/visagist">
							Vacatures: 0<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/android-developer';"><a href="https://www.jobpersonality.com/android-developer" class="bold-on-mobile">Android developer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/android-developer">
							Vacatures: 0<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/gastouder';"><a href="https://www.jobpersonality.com/gastouder" class="bold-on-mobile">Gastouder <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/gastouder">
							Vacatures: 2<br>
							Robotiserings%: 8%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/machinemonteur';"><a href="https://www.jobpersonality.com/machinemonteur" class="bold-on-mobile">Machinemonteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/machinemonteur">
							Vacatures: 5<br>
							Robotiserings%: 64%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/woonbegeleider';"><a href="https://www.jobpersonality.com/woonbegeleider" class="bold-on-mobile">Woonbegeleider <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/woonbegeleider">
							Vacatures: 6<br>
							Robotiserings%: 13%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/middenkaderfunctionaris';"><a href="https://www.jobpersonality.com/middenkaderfunctionaris" class="bold-on-mobile">Middenkaderfunctionaris <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/middenkaderfunctionaris">
							Vacatures: 4<br>
							Robotiserings%: 88%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/management-assistent';"><a href="https://www.jobpersonality.com/management-assistent" class="bold-on-mobile">Management assistent <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/management-assistent">
							Vacatures: 24<br>
							Robotiserings%: 86%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/ux-designer';"><a href="https://www.jobpersonality.com/ux-designer" class="bold-on-mobile">UX Designer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/ux-designer">
							Vacatures: 8<br>
							Robotiserings%: 48%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/ui-designer';"><a href="https://www.jobpersonality.com/ui-designer" class="bold-on-mobile">UI Designer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/ui-designer">
							Vacatures: 2<br>
							Robotiserings%: 30%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/industrieel-schoonmaker';"><a href="https://www.jobpersonality.com/industrieel-schoonmaker" class="bold-on-mobile">Industrieel schoonmaker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/industrieel-schoonmaker">
							Vacatures: 14<br>
							Robotiserings%: 66%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/cad-tekenaar';"><a href="https://www.jobpersonality.com/cad-tekenaar" class="bold-on-mobile">CAD tekenaar <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/cad-tekenaar">
							Vacatures: 20<br>
							Robotiserings%: 68%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/sous-chef';"><a href="https://www.jobpersonality.com/sous-chef" class="bold-on-mobile">Sous-chef <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/sous-chef">
							Vacatures: 84<br>
							Robotiserings%: 10%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/transportmedewerker';"><a href="https://www.jobpersonality.com/transportmedewerker" class="bold-on-mobile">Transportmedewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/transportmedewerker">
							Vacatures: 0<br>
							Robotiserings%: 95%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/molenaar';"><a href="https://www.jobpersonality.com/molenaar" class="bold-on-mobile">Molenaar <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/molenaar">
							Vacatures: 4<br>
							Robotiserings%: 97%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/kwaliteitsmedewerker';"><a href="https://www.jobpersonality.com/kwaliteitsmedewerker" class="bold-on-mobile">Kwaliteitsmedewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/kwaliteitsmedewerker">
							Vacatures: 39<br>
							Robotiserings%: 98%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/assemblagemedewerker';"><a href="https://www.jobpersonality.com/assemblagemedewerker" class="bold-on-mobile">Assemblagemedewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/assemblagemedewerker">
							Vacatures: 243<br>
							Robotiserings%: 93%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/shopmanager';"><a href="https://www.jobpersonality.com/shopmanager" class="bold-on-mobile">Shopmanager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/shopmanager">
							Vacatures: 4<br>
							Robotiserings%: 28%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/marktplaatsverkoper';"><a href="https://www.jobpersonality.com/marktplaatsverkoper" class="bold-on-mobile">Marktplaatsverkoper <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/marktplaatsverkoper">
							Vacatures: 0<br>
							Robotiserings%: 23%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/blogger';"><a href="https://www.jobpersonality.com/blogger" class="bold-on-mobile">Blogger <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/blogger">
							Vacatures: 0<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/monteur-elektrotechniek';"><a href="https://www.jobpersonality.com/monteur-elektrotechniek" class="bold-on-mobile">Monteur elektrotechniek <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/monteur-elektrotechniek">
							Vacatures: 290<br>
							Robotiserings%: 15%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/autocad-tekenaar';"><a href="https://www.jobpersonality.com/autocad-tekenaar" class="bold-on-mobile">AutoCAD tekenaar <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/autocad-tekenaar">
							Vacatures: 9<br>
							Robotiserings%: 68%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/host-hostess';"><a href="https://www.jobpersonality.com/host-hostess" class="bold-on-mobile">Hostess of host <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/host-hostess">
							Vacatures: 513<br>
							Robotiserings%: 97%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/servicemonteur';"><a href="https://www.jobpersonality.com/servicemonteur" class="bold-on-mobile">Servicemonteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/servicemonteur">
							Vacatures: 476<br>
							Robotiserings%: 45%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/chemisch-fysisch-analist';"><a href="https://www.jobpersonality.com/chemisch-fysisch-analist" class="bold-on-mobile">Chemisch fysisch analist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/chemisch-fysisch-analist">
							Vacatures: 0<br>
							Robotiserings%: 98%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/spuitgiet-operator';"><a href="https://www.jobpersonality.com/spuitgiet-operator" class="bold-on-mobile">Spuitgiet operator <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/spuitgiet-operator">
							Vacatures: 1<br>
							Robotiserings%: 91%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/stemacteur';"><a href="https://www.jobpersonality.com/stemacteur" class="bold-on-mobile">Stemacteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/stemacteur">
							Vacatures: 0<br>
							Robotiserings%: 37%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/juridisch-medewerker';"><a href="https://www.jobpersonality.com/juridisch-medewerker" class="bold-on-mobile">Juridisch medewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/juridisch-medewerker">
							Vacatures: 16<br>
							Robotiserings%: 94%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/monteur-hoogspanning';"><a href="https://www.jobpersonality.com/monteur-hoogspanning" class="bold-on-mobile">Monteur hoogspanning <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/monteur-hoogspanning">
							Vacatures: 17<br>
							Robotiserings%: 15%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/av-specialist';"><a href="https://www.jobpersonality.com/av-specialist" class="bold-on-mobile">AV-specialist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/av-specialist">
							Vacatures: 0<br>
							Robotiserings%: 55%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/lichttechnicus';"><a href="https://www.jobpersonality.com/lichttechnicus" class="bold-on-mobile">Lichttechnicus <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/lichttechnicus">
							Vacatures: 0<br>
							Robotiserings%: 13%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/preparateur';"><a href="https://www.jobpersonality.com/preparateur" class="bold-on-mobile">Preparateur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/preparateur">
							Vacatures: 0<br>
							Robotiserings%: 4%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/zelfstandig-ondernemer';"><a href="https://www.jobpersonality.com/zelfstandig-ondernemer" class="bold-on-mobile">Zelfstandig ondernemer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/zelfstandig-ondernemer">
							Vacatures: 11<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/monteur-buitendienst';"><a href="https://www.jobpersonality.com/monteur-buitendienst" class="bold-on-mobile">Monteur buitendienst <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/monteur-buitendienst">
							Vacatures: 84<br>
							Robotiserings%: 40%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/activiteitenbegeleider';"><a href="https://www.jobpersonality.com/activiteitenbegeleider" class="bold-on-mobile">Activiteitenbegeleider <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/activiteitenbegeleider">
							Vacatures: 0<br>
							Robotiserings%: 13%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/personal-assistant';"><a href="https://www.jobpersonality.com/personal-assistant" class="bold-on-mobile">Personal assistant <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/personal-assistant">
							Vacatures: 8<br>
							Robotiserings%: 35%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/keukenmonteur';"><a href="https://www.jobpersonality.com/keukenmonteur" class="bold-on-mobile">Keukenmonteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/keukenmonteur">
							Vacatures: 17<br>
							Robotiserings%: 40%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/werkvoorbereider-bouw';"><a href="https://www.jobpersonality.com/werkvoorbereider-bouw" class="bold-on-mobile">Werkvoorbereider bouw <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/werkvoorbereider-bouw">
							Vacatures: 100<br>
							Robotiserings%: 88%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/technisch-werkvoorbereider';"><a href="https://www.jobpersonality.com/technisch-werkvoorbereider" class="bold-on-mobile">Technisch werkvoorbereider <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/technisch-werkvoorbereider">
							Vacatures: 148<br>
							Robotiserings%: 88%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/assistent-accountant';"><a href="https://www.jobpersonality.com/assistent-accountant" class="bold-on-mobile">Assistent accountant <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/assistent-accountant">
							Vacatures: 136<br>
							Robotiserings%: 94%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/roostermaker';"><a href="https://www.jobpersonality.com/roostermaker" class="bold-on-mobile">Roostermaker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/roostermaker">
							Vacatures: 0<br>
							Robotiserings%: 88%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/drogist';"><a href="https://www.jobpersonality.com/drogist" class="bold-on-mobile">Drogist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/drogist">
							Vacatures: 1<br>
							Robotiserings%: 92%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/virtueel-assistent';"><a href="https://www.jobpersonality.com/virtueel-assistent" class="bold-on-mobile">Virtueel assistent <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/virtueel-assistent">
							Vacatures: 0<br>
							Robotiserings%: 86%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/calculator';"><a href="https://www.jobpersonality.com/calculator" class="bold-on-mobile">Calculator <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/calculator">
							Vacatures: 437<br>
							Robotiserings%: 88%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/storingsmonteur';"><a href="https://www.jobpersonality.com/storingsmonteur" class="bold-on-mobile">Storingsmonteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/storingsmonteur">
							Vacatures: 98<br>
							Robotiserings%: 40%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/teeltspecialist';"><a href="https://www.jobpersonality.com/teeltspecialist" class="bold-on-mobile">Teeltspecialist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/teeltspecialist">
							Vacatures: 7<br>
							Robotiserings%: 25%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/groom';"><a href="https://www.jobpersonality.com/groom" class="bold-on-mobile">Groom <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/groom">
							Vacatures: 0<br>
							Robotiserings%: 82%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/vaccinatiemedewerker';"><a href="https://www.jobpersonality.com/vaccinatiemedewerker" class="bold-on-mobile">Vaccinatiemedewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/vaccinatiemedewerker">
							Vacatures: 0<br>
							Robotiserings%: 47%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medewerker-verhuur';"><a href="https://www.jobpersonality.com/medewerker-verhuur" class="bold-on-mobile">Medewerker verhuur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medewerker-verhuur">
							Vacatures: 2<br>
							Robotiserings%: 97%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/triagist';"><a href="https://www.jobpersonality.com/triagist" class="bold-on-mobile">Triagist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/triagist">
							Vacatures: 1<br>
							Robotiserings%: 14%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/praktijkopleider';"><a href="https://www.jobpersonality.com/praktijkopleider" class="bold-on-mobile">Praktijkopleider <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/praktijkopleider">
							Vacatures: 15<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/treinverkeersleider';"><a href="https://www.jobpersonality.com/treinverkeersleider" class="bold-on-mobile">Treinverkeersleider <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/treinverkeersleider">
							Vacatures: 0<br>
							Robotiserings%: 11%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/tap-monteur';"><a href="https://www.jobpersonality.com/tap-monteur" class="bold-on-mobile">Tapmonteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/tap-monteur">
							Vacatures: 0<br>
							Robotiserings%: 64%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/hotelmanager';"><a href="https://www.jobpersonality.com/hotelmanager" class="bold-on-mobile">Hotelmanager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/hotelmanager">
							Vacatures: 4<br>
							Robotiserings%: 8%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/technisch-tekenaar';"><a href="https://www.jobpersonality.com/technisch-tekenaar" class="bold-on-mobile">Technisch tekenaar <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/technisch-tekenaar">
							Vacatures: 38<br>
							Robotiserings%: 52%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/laboratorium-assistent';"><a href="https://www.jobpersonality.com/laboratorium-assistent" class="bold-on-mobile">Laboratorium assistent <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/laboratorium-assistent">
							Vacatures: 0<br>
							Robotiserings%: 98%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/ploegbaas';"><a href="https://www.jobpersonality.com/ploegbaas" class="bold-on-mobile">Ploegleider <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/ploegbaas">
							Vacatures: 68<br>
							Robotiserings%: 7%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/winkeleigenaar';"><a href="https://www.jobpersonality.com/winkeleigenaar" class="bold-on-mobile">Winkeleigenaar <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/winkeleigenaar">
							Vacatures: 6<br>
							Robotiserings%: 8%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/campingeigenaar';"><a href="https://www.jobpersonality.com/campingeigenaar" class="bold-on-mobile">campingeigenaar <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/campingeigenaar">
							Vacatures: 0<br>
							Robotiserings%: 8%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/reinigingsmedewerker';"><a href="https://www.jobpersonality.com/reinigingsmedewerker" class="bold-on-mobile">Reinigingsmedewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/reinigingsmedewerker">
							Vacatures: 4<br>
							Robotiserings%: 66%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medewerker-housekeeping';"><a href="https://www.jobpersonality.com/medewerker-housekeeping" class="bold-on-mobile">Medewerker housekeeping <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medewerker-housekeeping">
							Vacatures: 51<br>
							Robotiserings%: 69%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/interieurbouwer';"><a href="https://www.jobpersonality.com/interieurbouwer" class="bold-on-mobile">Interieurbouwer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/interieurbouwer">
							Vacatures: 23<br>
							Robotiserings%: 40%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/teamleider';"><a href="https://www.jobpersonality.com/teamleider" class="bold-on-mobile">Teamleider <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/teamleider">
							Vacatures: 788<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/verzekeringsadviseur';"><a href="https://www.jobpersonality.com/verzekeringsadviseur" class="bold-on-mobile">Verzekeringsadviseur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/verzekeringsadviseur">
							Vacatures: 10<br>
							Robotiserings%: 92%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/portier';"><a href="https://www.jobpersonality.com/portier" class="bold-on-mobile">Portier <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/portier">
							Vacatures: 8<br>
							Robotiserings%: 84%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/dj-discjockey';"><a href="https://www.jobpersonality.com/dj-discjockey" class="bold-on-mobile">DJ <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/dj-discjockey">
							Vacatures: 11<br>
							Robotiserings%: 10%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/keurmeester-agf';"><a href="https://www.jobpersonality.com/keurmeester-agf" class="bold-on-mobile">Keurmeester AGF <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/keurmeester-agf">
							Vacatures: 3<br>
							Robotiserings%: 94%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/verspaner';"><a href="https://www.jobpersonality.com/verspaner" class="bold-on-mobile">Verspaner <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/verspaner">
							Vacatures: 11<br>
							Robotiserings%: 90%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/monteur-laagspanning';"><a href="https://www.jobpersonality.com/monteur-laagspanning" class="bold-on-mobile">Monteur laagspanning <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/monteur-laagspanning">
							Vacatures: 1<br>
							Robotiserings%: 15%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/franchisenemer';"><a href="https://www.jobpersonality.com/franchisenemer" class="bold-on-mobile">Franchisenemer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/franchisenemer">
							Vacatures: 11<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/transportplanner';"><a href="https://www.jobpersonality.com/transportplanner" class="bold-on-mobile">Transportplanner <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/transportplanner">
							Vacatures: 62<br>
							Robotiserings%: 99%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/vertrouwenspersoon';"><a href="https://www.jobpersonality.com/vertrouwenspersoon" class="bold-on-mobile">Vertrouwenspersoon <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/vertrouwenspersoon">
							Vacatures: 11<br>
							Robotiserings%: 6%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/moderator';"><a href="https://www.jobpersonality.com/moderator" class="bold-on-mobile">Moderator <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/moderator">
							Vacatures: 0<br>
							Robotiserings%: 55%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/monteur-warmtepompen';"><a href="https://www.jobpersonality.com/monteur-warmtepompen" class="bold-on-mobile">Monteur warmtepompen <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/monteur-warmtepompen">
							Vacatures: 5<br>
							Robotiserings%: 15%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/stylist';"><a href="https://www.jobpersonality.com/stylist" class="bold-on-mobile">Stylist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/stylist">
							Vacatures: 3<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/facility-manager';"><a href="https://www.jobpersonality.com/facility-manager" class="bold-on-mobile">Facilitair manager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/facility-manager">
							Vacatures: 9<br>
							Robotiserings%: 57%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/marketingmedewerker';"><a href="https://www.jobpersonality.com/marketingmedewerker" class="bold-on-mobile">Marketingmedewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/marketingmedewerker">
							Vacatures: 6<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/elektro-monteur';"><a href="https://www.jobpersonality.com/elektro-monteur" class="bold-on-mobile">Elektromonteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/elektro-monteur">
							Vacatures: 498<br>
							Robotiserings%: 15%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/vestigingsmanager';"><a href="https://www.jobpersonality.com/vestigingsmanager" class="bold-on-mobile">Vestigingsmanager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/vestigingsmanager">
							Vacatures: 121<br>
							Robotiserings%: 8%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/store-manager';"><a href="https://www.jobpersonality.com/store-manager" class="bold-on-mobile">Store manager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/store-manager">
							Vacatures: 3<br>
							Robotiserings%: 8%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/zzper';"><a href="https://www.jobpersonality.com/zzper" class="bold-on-mobile">Zzp’er <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/zzper">
							Vacatures: 426<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/monteur-laadpalen';"><a href="https://www.jobpersonality.com/monteur-laadpalen" class="bold-on-mobile">Monteur laadpalen <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/monteur-laadpalen">
							Vacatures: 3<br>
							Robotiserings%: 15%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/stalmedewerker';"><a href="https://www.jobpersonality.com/stalmedewerker" class="bold-on-mobile">Stalmedewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/stalmedewerker">
							Vacatures: 0<br>
							Robotiserings%: 82%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medewerker-technische-dienst';"><a href="https://www.jobpersonality.com/medewerker-technische-dienst" class="bold-on-mobile">Medewerker technische dienst <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medewerker-technische-dienst">
							Vacatures: 138<br>
							Robotiserings%: 64%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/monteur-meet-en-regeltechniek';"><a href="https://www.jobpersonality.com/monteur-meet-en-regeltechniek" class="bold-on-mobile">Monteur meet- en regeltechniek <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/monteur-meet-en-regeltechniek">
							Vacatures: 4<br>
							Robotiserings%: 15%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/spuiter';"><a href="https://www.jobpersonality.com/spuiter" class="bold-on-mobile">Spuiter <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/spuiter">
							Vacatures: 34<br>
							Robotiserings%: 69%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/personeelsplanner';"><a href="https://www.jobpersonality.com/personeelsplanner" class="bold-on-mobile">Personeelsplanner <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/personeelsplanner">
							Vacatures: 6<br>
							Robotiserings%: 96%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bankwerker';"><a href="https://www.jobpersonality.com/bankwerker" class="bold-on-mobile">Bankwerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bankwerker">
							Vacatures: 27<br>
							Robotiserings%: 64%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/battery-swapper';"><a href="https://www.jobpersonality.com/battery-swapper" class="bold-on-mobile">Battery Swapper <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/battery-swapper">
							Vacatures: 0<br>
							Robotiserings%: 69%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/ervaringsdeskundige';"><a href="https://www.jobpersonality.com/ervaringsdeskundige" class="bold-on-mobile">Ervaringsdeskundige <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/ervaringsdeskundige">
							Vacatures: 18<br>
							Robotiserings%: 25%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/dropshipper';"><a href="https://www.jobpersonality.com/dropshipper" class="bold-on-mobile">Dropshipper <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/dropshipper">
							Vacatures: 0<br>
							Robotiserings%: 23%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/internetondernemer';"><a href="https://www.jobpersonality.com/internetondernemer" class="bold-on-mobile">Internetondernemer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/internetondernemer">
							Vacatures: 0<br>
							Robotiserings%: 2%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/penitentiair-inrichtingswerker';"><a href="https://www.jobpersonality.com/penitentiair-inrichtingswerker" class="bold-on-mobile">Penitentiair inrichtingswerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/penitentiair-inrichtingswerker">
							Vacatures: 0<br>
							Robotiserings%: 25%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/influencer';"><a href="https://www.jobpersonality.com/influencer" class="bold-on-mobile">Influencer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/influencer">
							Vacatures: 5<br>
							Robotiserings%: 1%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/filiaalmanager';"><a href="https://www.jobpersonality.com/filiaalmanager" class="bold-on-mobile">Filiaalmanager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/filiaalmanager">
							Vacatures: 28<br>
							Robotiserings%: 8%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/fitnessinstructeur';"><a href="https://www.jobpersonality.com/fitnessinstructeur" class="bold-on-mobile">Fitnessinstructeur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/fitnessinstructeur">
							Vacatures: 0<br>
							Robotiserings%: 9%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/verkoper-buitendienst';"><a href="https://www.jobpersonality.com/verkoper-buitendienst" class="bold-on-mobile">Verkoper buitendienst <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/verkoper-buitendienst">
							Vacatures: 3<br>
							Robotiserings%: 25%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/verkoper-binnendienst';"><a href="https://www.jobpersonality.com/verkoper-binnendienst" class="bold-on-mobile">Verkoper binnendienst <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/verkoper-binnendienst">
							Vacatures: 20<br>
							Robotiserings%: 54%<br>
							Opleidingsniveau: 3<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/marktkoopman';"><a href="https://www.jobpersonality.com/marktkoopman" class="bold-on-mobile">Marktkoopman <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/marktkoopman">
							Vacatures: 0<br>
							Robotiserings%: 29%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/topsporter';"><a href="https://www.jobpersonality.com/topsporter" class="bold-on-mobile">Topsporter <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/topsporter">
							Vacatures: 7<br>
							Robotiserings%: 28%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/ondersteunend-medewerker-psychiatrie';"><a href="https://www.jobpersonality.com/ondersteunend-medewerker-psychiatrie" class="bold-on-mobile">Ondersteunend medewerker psychiatrie <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/ondersteunend-medewerker-psychiatrie">
							Vacatures: 0<br>
							Robotiserings%: 47%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/ondersteunend-medewerker-ergotherapie';"><a href="https://www.jobpersonality.com/ondersteunend-medewerker-ergotherapie" class="bold-on-mobile">Ondersteunend medewerker ergotherapie <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/ondersteunend-medewerker-ergotherapie">
							Vacatures: 0<br>
							Robotiserings%: 27%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/ondersteunend-medewerker-fysiotherapie';"><a href="https://www.jobpersonality.com/ondersteunend-medewerker-fysiotherapie" class="bold-on-mobile">Ondersteunend medewerker fysiotherapie <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/ondersteunend-medewerker-fysiotherapie">
							Vacatures: 0<br>
							Robotiserings%: 61%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/parkeercontroleur';"><a href="https://www.jobpersonality.com/parkeercontroleur" class="bold-on-mobile">Parkeercontroleur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/parkeercontroleur">
							Vacatures: 0<br>
							Robotiserings%: 84%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/dierenpolitie';"><a href="https://www.jobpersonality.com/dierenpolitie" class="bold-on-mobile">Dierenpolitie <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/dierenpolitie">
							Vacatures: 0<br>
							Robotiserings%: 21%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/badmeester-toezichthouder-in-recreatiegebieden';"><a href="https://www.jobpersonality.com/badmeester-toezichthouder-in-recreatiegebieden" class="bold-on-mobile">Lifeguard <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/badmeester-toezichthouder-in-recreatiegebieden">
							Vacatures: 0<br>
							Robotiserings%: 67%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/vervoersbeveiliger';"><a href="https://www.jobpersonality.com/vervoersbeveiliger" class="bold-on-mobile">Vervoersbeveiliger <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/vervoersbeveiliger">
							Vacatures: 0<br>
							Robotiserings%: 67%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/barista';"><a href="https://www.jobpersonality.com/barista" class="bold-on-mobile">Barista <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/barista">
							Vacatures: 140<br>
							Robotiserings%: 96%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/speltoezichthouder';"><a href="https://www.jobpersonality.com/speltoezichthouder" class="bold-on-mobile">Speltoezichthouder <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/speltoezichthouder">
							Vacatures: 0<br>
							Robotiserings%: 28%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/dierentrainer';"><a href="https://www.jobpersonality.com/dierentrainer" class="bold-on-mobile">Dierentrainer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/dierentrainer">
							Vacatures: 0<br>
							Robotiserings%: 10%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/filmoperateur';"><a href="https://www.jobpersonality.com/filmoperateur" class="bold-on-mobile">Filmoperateur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/filmoperateur">
							Vacatures: 0<br>
							Robotiserings%: 97%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/kostuumbediende';"><a href="https://www.jobpersonality.com/kostuumbediende" class="bold-on-mobile">Kleedster <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/kostuumbediende">
							Vacatures: 0<br>
							Robotiserings%: 61%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/kleedkamer-garderobebediende';"><a href="https://www.jobpersonality.com/kleedkamer-garderobebediende" class="bold-on-mobile">Kleedkamerhulp <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/kleedkamer-garderobebediende">
							Vacatures: 0<br>
							Robotiserings%: 43%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/uitvaartmedewerker';"><a href="https://www.jobpersonality.com/uitvaartmedewerker" class="bold-on-mobile">Medewerker uitvaartcentrum <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/uitvaartmedewerker">
							Vacatures: 0<br>
							Robotiserings%: 37%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/barbier';"><a href="https://www.jobpersonality.com/barbier" class="bold-on-mobile">Barbier <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/barbier">
							Vacatures: 0<br>
							Robotiserings%: 80%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/harenwasser';"><a href="https://www.jobpersonality.com/harenwasser" class="bold-on-mobile">Salonassistent <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/harenwasser">
							Vacatures: 0<br>
							Robotiserings%: 79%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bagagedrager-piccolo';"><a href="https://www.jobpersonality.com/bagagedrager-piccolo" class="bold-on-mobile">Piccolo <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bagagedrager-piccolo">
							Vacatures: 0<br>
							Robotiserings%: 83%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/kinderverzorger';"><a href="https://www.jobpersonality.com/kinderverzorger" class="bold-on-mobile">Kinderverzorger <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/kinderverzorger">
							Vacatures: 0<br>
							Robotiserings%: 8%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/geldwisselaar';"><a href="https://www.jobpersonality.com/geldwisselaar" class="bold-on-mobile">Geldwisselaar <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/geldwisselaar">
							Vacatures: 45<br>
							Robotiserings%: 83%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/promotor';"><a href="https://www.jobpersonality.com/promotor" class="bold-on-mobile">Promotor <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/promotor">
							Vacatures: 28<br>
							Robotiserings%: 51%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/telefoniste';"><a href="https://www.jobpersonality.com/telefoniste" class="bold-on-mobile">Telefoniste <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/telefoniste">
							Vacatures: 10<br>
							Robotiserings%: 96%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/spelloketbediende';"><a href="https://www.jobpersonality.com/spelloketbediende" class="bold-on-mobile">Spelloketbediende <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/spelloketbediende">
							Vacatures: 45<br>
							Robotiserings%: 39%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/baliemedewerker-hotel';"><a href="https://www.jobpersonality.com/baliemedewerker-hotel" class="bold-on-mobile">Baliemedewerker hotel <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/baliemedewerker-hotel">
							Vacatures: 191<br>
							Robotiserings%: 94%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/administratief-medewerker-rekeningen';"><a href="https://www.jobpersonality.com/administratief-medewerker-rekeningen" class="bold-on-mobile">Administratief medewerker rekeningen <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/administratief-medewerker-rekeningen">
							Vacatures: 1<br>
							Robotiserings%: 99%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/administratief-medewerker-bestellingen';"><a href="https://www.jobpersonality.com/administratief-medewerker-bestellingen" class="bold-on-mobile">Administratief medewerker bestellingen <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/administratief-medewerker-bestellingen">
							Vacatures: 0<br>
							Robotiserings%: 98%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medewerker-tickets-en-reserveringen';"><a href="https://www.jobpersonality.com/medewerker-tickets-en-reserveringen" class="bold-on-mobile">Medewerker reserveringen <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medewerker-tickets-en-reserveringen">
							Vacatures: 8<br>
							Robotiserings%: 61%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bedrijfskoerier';"><a href="https://www.jobpersonality.com/bedrijfskoerier" class="bold-on-mobile">Bedrijfskoerier <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bedrijfskoerier">
							Vacatures: 0<br>
							Robotiserings%: 94%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/meteropnemer-nutsbedrijven';"><a href="https://www.jobpersonality.com/meteropnemer-nutsbedrijven" class="bold-on-mobile">Meteropnemer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/meteropnemer-nutsbedrijven">
							Vacatures: 0<br>
							Robotiserings%: 85%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/servicemedewerker-postkantoor';"><a href="https://www.jobpersonality.com/servicemedewerker-postkantoor" class="bold-on-mobile">Medewerker postkantoor <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/servicemedewerker-postkantoor">
							Vacatures: 0<br>
							Robotiserings%: 95%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/postbode';"><a href="https://www.jobpersonality.com/postbode" class="bold-on-mobile">Postbode <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/postbode">
							Vacatures: 42<br>
							Robotiserings%: 68%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/postsorteerder-of-postvoorbereider';"><a href="https://www.jobpersonality.com/postsorteerder-of-postvoorbereider" class="bold-on-mobile">Postsorteerder <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/postsorteerder-of-postvoorbereider">
							Vacatures: 2<br>
							Robotiserings%: 79%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medewerker-transport-en-ontvangst';"><a href="https://www.jobpersonality.com/medewerker-transport-en-ontvangst" class="bold-on-mobile">Medewerker transport <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medewerker-transport-en-ontvangst">
							Vacatures: 24<br>
							Robotiserings%: 98%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/orderpicker';"><a href="https://www.jobpersonality.com/orderpicker" class="bold-on-mobile">Orderpicker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/orderpicker">
							Vacatures: 627<br>
							Robotiserings%: 95%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/tekstverwerker-typist';"><a href="https://www.jobpersonality.com/tekstverwerker-typist" class="bold-on-mobile">Typist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/tekstverwerker-typist">
							Vacatures: 0<br>
							Robotiserings%: 81%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/postkamermedewerker';"><a href="https://www.jobpersonality.com/postkamermedewerker" class="bold-on-mobile">Postkamer medewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/postkamermedewerker">
							Vacatures: 1<br>
							Robotiserings%: 94%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/repro-medewerker';"><a href="https://www.jobpersonality.com/repro-medewerker" class="bold-on-mobile">Repro medewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/repro-medewerker">
							Vacatures: 0<br>
							Robotiserings%: 92%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/tapijtlegger';"><a href="https://www.jobpersonality.com/tapijtlegger" class="bold-on-mobile">Tapijtlegger <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/tapijtlegger">
							Vacatures: 8<br>
							Robotiserings%: 87%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bouwvakker';"><a href="https://www.jobpersonality.com/bouwvakker" class="bold-on-mobile">Bouwvakker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bouwvakker">
							Vacatures: 3<br>
							Robotiserings%: 88%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/operator-heihamers';"><a href="https://www.jobpersonality.com/operator-heihamers" class="bold-on-mobile">Operator heihamers <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/operator-heihamers">
							Vacatures: 0<br>
							Robotiserings%: 82%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bulldozermachinist';"><a href="https://www.jobpersonality.com/bulldozermachinist" class="bold-on-mobile">Bulldozermachinist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bulldozermachinist">
							Vacatures: 0<br>
							Robotiserings%: 95%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/isoleerder';"><a href="https://www.jobpersonality.com/isoleerder" class="bold-on-mobile">Isoleerder <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/isoleerder">
							Vacatures: 3<br>
							Robotiserings%: 83%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/behanger';"><a href="https://www.jobpersonality.com/behanger" class="bold-on-mobile">Behanger <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/behanger">
							Vacatures: 1<br>
							Robotiserings%: 87%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/buizenlegger';"><a href="https://www.jobpersonality.com/buizenlegger" class="bold-on-mobile">Buizenlegger <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/buizenlegger">
							Vacatures: 1<br>
							Robotiserings%: 62%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/installateur-van-zonnepanelen';"><a href="https://www.jobpersonality.com/installateur-van-zonnepanelen" class="bold-on-mobile">Installateur zonnepanelen <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/installateur-van-zonnepanelen">
							Vacatures: 0<br>
							Robotiserings%: 75%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/assistent-bouwvakker';"><a href="https://www.jobpersonality.com/assistent-bouwvakker" class="bold-on-mobile">Assistent bouwvakker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/assistent-bouwvakker">
							Vacatures: 1<br>
							Robotiserings%: 83%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/assistent-timmerman';"><a href="https://www.jobpersonality.com/assistent-timmerman" class="bold-on-mobile">Assistent timmerman <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/assistent-timmerman">
							Vacatures: 6<br>
							Robotiserings%: 92%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/assistent-elektricien';"><a href="https://www.jobpersonality.com/assistent-elektricien" class="bold-on-mobile">Junior elektromonteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/assistent-elektricien">
							Vacatures: 3<br>
							Robotiserings%: 74%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/assistent-loodgieter';"><a href="https://www.jobpersonality.com/assistent-loodgieter" class="bold-on-mobile">Assistent loodgieter <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/assistent-loodgieter">
							Vacatures: 2<br>
							Robotiserings%: 57%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/assistent-dakdekker';"><a href="https://www.jobpersonality.com/assistent-dakdekker" class="bold-on-mobile">Assistent dakdekker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/assistent-dakdekker">
							Vacatures: 1<br>
							Robotiserings%: 92%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/hekkenbouwer';"><a href="https://www.jobpersonality.com/hekkenbouwer" class="bold-on-mobile">Hekwerkmonteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/hekkenbouwer">
							Vacatures: 3<br>
							Robotiserings%: 92%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/wegwerker';"><a href="https://www.jobpersonality.com/wegwerker" class="bold-on-mobile">Wegwerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/wegwerker">
							Vacatures: 5<br>
							Robotiserings%: 87%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/servicemonteur-rioleringen';"><a href="https://www.jobpersonality.com/servicemonteur-rioleringen" class="bold-on-mobile">Rioleur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/servicemonteur-rioleringen">
							Vacatures: 26<br>
							Robotiserings%: 83%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/boormachinist-olie-gas';"><a href="https://www.jobpersonality.com/boormachinist-olie-gas" class="bold-on-mobile">Boormachinist olie en gas <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/boormachinist-olie-gas">
							Vacatures: 2<br>
							Robotiserings%: 53%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/servicemonteur-mijnbouw';"><a href="https://www.jobpersonality.com/servicemonteur-mijnbouw" class="bold-on-mobile">Servicemonteur mijnbouw <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/servicemonteur-mijnbouw">
							Vacatures: 0<br>
							Robotiserings%: 93%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/boormachinist';"><a href="https://www.jobpersonality.com/boormachinist" class="bold-on-mobile">Boormachinist <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/boormachinist">
							Vacatures: 0<br>
							Robotiserings%: 85%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/machineoperator-mijnbouw';"><a href="https://www.jobpersonality.com/machineoperator-mijnbouw" class="bold-on-mobile">Machineoperator mijnbouw <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/machineoperator-mijnbouw">
							Vacatures: 0<br>
							Robotiserings%: 59%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medewerker-mijnbouw';"><a href="https://www.jobpersonality.com/medewerker-mijnbouw" class="bold-on-mobile">Medewerker mijnbouw <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medewerker-mijnbouw">
							Vacatures: 0<br>
							Robotiserings%: 37%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/onderhoudsmedewerker-machines';"><a href="https://www.jobpersonality.com/onderhoudsmedewerker-machines" class="bold-on-mobile">Onderhoudsmedewerker machines <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/onderhoudsmedewerker-machines">
							Vacatures: 0<br>
							Robotiserings%: 86%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/slotenmaker';"><a href="https://www.jobpersonality.com/slotenmaker" class="bold-on-mobile">Slotenmaker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/slotenmaker">
							Vacatures: 0<br>
							Robotiserings%: 77%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/installateur-prefab-woningen-gebouwen';"><a href="https://www.jobpersonality.com/installateur-prefab-woningen-gebouwen" class="bold-on-mobile">Monteur prefab montage <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/installateur-prefab-woningen-gebouwen">
							Vacatures: 0<br>
							Robotiserings%: 18%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/assistent-monteur';"><a href="https://www.jobpersonality.com/assistent-monteur" class="bold-on-mobile">Assistent monteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/assistent-monteur">
							Vacatures: 19<br>
							Robotiserings%: 79%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medewerker-assemblage-ploeg';"><a href="https://www.jobpersonality.com/medewerker-assemblage-ploeg" class="bold-on-mobile">Team medewerker assemblage <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medewerker-assemblage-ploeg">
							Vacatures: 1<br>
							Robotiserings%: 98%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/operator-voedselmachines';"><a href="https://www.jobpersonality.com/operator-voedselmachines" class="bold-on-mobile">Operator voedselmachine <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/operator-voedselmachines">
							Vacatures: 0<br>
							Robotiserings%: 91%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/operator-voedsel-en-kookapparatuur';"><a href="https://www.jobpersonality.com/operator-voedsel-en-kookapparatuur" class="bold-on-mobile">Koker-Menger <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/operator-voedsel-en-kookapparatuur">
							Vacatures: 0<br>
							Robotiserings%: 61%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/operator-extruder';"><a href="https://www.jobpersonality.com/operator-extruder" class="bold-on-mobile">Operator extruder <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/operator-extruder">
							Vacatures: 8<br>
							Robotiserings%: 91%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/operator-smeedmachine';"><a href="https://www.jobpersonality.com/operator-smeedmachine" class="bold-on-mobile">Operator smeedmachine <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/operator-smeedmachine">
							Vacatures: 0<br>
							Robotiserings%: 93%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/operator-rolmachine';"><a href="https://www.jobpersonality.com/operator-rolmachine" class="bold-on-mobile">Operator rolmachine <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/operator-rolmachine">
							Vacatures: 0<br>
							Robotiserings%: 83%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/operator-snij-drukmachine';"><a href="https://www.jobpersonality.com/operator-snij-drukmachine" class="bold-on-mobile">Operator van snij- of drukmachine <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/operator-snij-drukmachine">
							Vacatures: 0<br>
							Robotiserings%: 78%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/operator-boormachine';"><a href="https://www.jobpersonality.com/operator-boormachine" class="bold-on-mobile">Operator boormachine <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/operator-boormachine">
							Vacatures: 0<br>
							Robotiserings%: 94%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/operator-slijp-polijstmachine';"><a href="https://www.jobpersonality.com/operator-slijp-polijstmachine" class="bold-on-mobile">Operator van slijp- en polijstmachine <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/operator-slijp-polijstmachine">
							Vacatures: 4<br>
							Robotiserings%: 95%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/operator-metaalproductie';"><a href="https://www.jobpersonality.com/operator-metaalproductie" class="bold-on-mobile">Operator metaalproductie <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/operator-metaalproductie">
							Vacatures: 0<br>
							Robotiserings%: 88%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/mal-patroonmaker';"><a href="https://www.jobpersonality.com/mal-patroonmaker" class="bold-on-mobile">Mal- en patroonmaker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/mal-patroonmaker">
							Vacatures: 0<br>
							Robotiserings%: 67%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/operator-malmachine';"><a href="https://www.jobpersonality.com/operator-malmachine" class="bold-on-mobile">Operator malmachine <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/operator-malmachine">
							Vacatures: 0<br>
							Robotiserings%: 95%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/soldeerder';"><a href="https://www.jobpersonality.com/soldeerder" class="bold-on-mobile">Soldeerder <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/soldeerder">
							Vacatures: 2<br>
							Robotiserings%: 94%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/operator-apparatuur-warmtebehandeling';"><a href="https://www.jobpersonality.com/operator-apparatuur-warmtebehandeling" class="bold-on-mobile">Operator warmtebehandeling <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/operator-apparatuur-warmtebehandeling">
							Vacatures: 0<br>
							Robotiserings%: 91%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/layout-tekenaar-industrie';"><a href="https://www.jobpersonality.com/layout-tekenaar-industrie" class="bold-on-mobile">Layout tekenaar industrie <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/layout-tekenaar-industrie">
							Vacatures: 0<br>
							Robotiserings%: 84%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/gereedschapsvijler';"><a href="https://www.jobpersonality.com/gereedschapsvijler" class="bold-on-mobile">Slijper <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/gereedschapsvijler">
							Vacatures: 4<br>
							Robotiserings%: 88%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bediener-schoenmachines';"><a href="https://www.jobpersonality.com/bediener-schoenmachines" class="bold-on-mobile">Bediener schoenmachines <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bediener-schoenmachines">
							Vacatures: 0<br>
							Robotiserings%: 97%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/naaier-naaister';"><a href="https://www.jobpersonality.com/naaier-naaister" class="bold-on-mobile">Naaier of Naaister <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/naaier-naaister">
							Vacatures: 1<br>
							Robotiserings%: 99%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/operator-verfmachine';"><a href="https://www.jobpersonality.com/operator-verfmachine" class="bold-on-mobile">Operator verfmachine <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/operator-verfmachine">
							Vacatures: 0<br>
							Robotiserings%: 97%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bediener-knipmachine-textiel';"><a href="https://www.jobpersonality.com/bediener-knipmachine-textiel" class="bold-on-mobile">Bediener knipmachine textiel <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bediener-knipmachine-textiel">
							Vacatures: 0<br>
							Robotiserings%: 95%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bediener-weefmachine';"><a href="https://www.jobpersonality.com/bediener-weefmachine" class="bold-on-mobile">Bediener weefmachine <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bediener-weefmachine">
							Vacatures: 0<br>
							Robotiserings%: 73%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bediener-spinmachines';"><a href="https://www.jobpersonality.com/bediener-spinmachines" class="bold-on-mobile">Bediener spinmachines <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bediener-spinmachines">
							Vacatures: 0<br>
							Robotiserings%: 96%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/operator-extruder-machine-voor-kabels-en-draden';"><a href="https://www.jobpersonality.com/operator-extruder-machine-voor-kabels-en-draden" class="bold-on-mobile">Operator kabelmachine <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/operator-extruder-machine-voor-kabels-en-draden">
							Vacatures: 8<br>
							Robotiserings%: 88%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bediener-houtzaagmachine';"><a href="https://www.jobpersonality.com/bediener-houtzaagmachine" class="bold-on-mobile">Machinaal houtbewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bediener-houtzaagmachine">
							Vacatures: 25<br>
							Robotiserings%: 86%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bediener-houtbewerkingsmachine';"><a href="https://www.jobpersonality.com/bediener-houtbewerkingsmachine" class="bold-on-mobile">Assistent machinaal houtbewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bediener-houtbewerkingsmachine">
							Vacatures: 0<br>
							Robotiserings%: 97%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/operator-chemische-apparatuur';"><a href="https://www.jobpersonality.com/operator-chemische-apparatuur" class="bold-on-mobile">Chemisch operator <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/operator-chemische-apparatuur">
							Vacatures: 22<br>
							Robotiserings%: 76%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/operator-plet-slijp-polijstmachine';"><a href="https://www.jobpersonality.com/operator-plet-slijp-polijstmachine" class="bold-on-mobile">Operator plet-, slijp- en polijstmachine <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/operator-plet-slijp-polijstmachine">
							Vacatures: 7<br>
							Robotiserings%: 97%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/operator-mengmachine';"><a href="https://www.jobpersonality.com/operator-mengmachine" class="bold-on-mobile">Menger <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/operator-mengmachine">
							Vacatures: 21<br>
							Robotiserings%: 83%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/handsnijder';"><a href="https://www.jobpersonality.com/handsnijder" class="bold-on-mobile">Glassnijder <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/handsnijder">
							Vacatures: 0<br>
							Robotiserings%: 64%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/operator-snijmachine';"><a href="https://www.jobpersonality.com/operator-snijmachine" class="bold-on-mobile">Operator snijmachine <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/operator-snijmachine">
							Vacatures: 0<br>
							Robotiserings%: 86%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/operator-extrusie-vorm-persmachine';"><a href="https://www.jobpersonality.com/operator-extrusie-vorm-persmachine" class="bold-on-mobile">Extrusie operator <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/operator-extrusie-vorm-persmachine">
							Vacatures: 8<br>
							Robotiserings%: 93%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/operator-verwarmingsapparatuur';"><a href="https://www.jobpersonality.com/operator-verwarmingsapparatuur" class="bold-on-mobile">Operator verwarmingsapparatuur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/operator-verwarmingsapparatuur">
							Vacatures: 0<br>
							Robotiserings%: 37%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/oogheelkundig-laborant';"><a href="https://www.jobpersonality.com/oogheelkundig-laborant" class="bold-on-mobile">Oogheelkundig laborant <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/oogheelkundig-laborant">
							Vacatures: 0<br>
							Robotiserings%: 97%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/operator-verpak-vulmachines';"><a href="https://www.jobpersonality.com/operator-verpak-vulmachines" class="bold-on-mobile">Operator verpakking <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/operator-verpak-vulmachines">
							Vacatures: 7<br>
							Robotiserings%: 98%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/poedercoater';"><a href="https://www.jobpersonality.com/poedercoater" class="bold-on-mobile">Poedercoater <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/poedercoater">
							Vacatures: 16<br>
							Robotiserings%: 91%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/operator-lijmmachine';"><a href="https://www.jobpersonality.com/operator-lijmmachine" class="bold-on-mobile">Operator lijmmachine <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/operator-lijmmachine">
							Vacatures: 0<br>
							Robotiserings%: 95%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/operator-industriele-schoonmaakapparatuur';"><a href="https://www.jobpersonality.com/operator-industriele-schoonmaakapparatuur" class="bold-on-mobile">Operator industriële schoonmaakapparatuur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/operator-industriele-schoonmaakapparatuur">
							Vacatures: 0<br>
							Robotiserings%: 81%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/operator-industriele-koel-en-vriesapparatuur';"><a href="https://www.jobpersonality.com/operator-industriele-koel-en-vriesapparatuur" class="bold-on-mobile">Operator industriële vriesapparatuur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/operator-industriele-koel-en-vriesapparatuur">
							Vacatures: 0<br>
							Robotiserings%: 93%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/natuursteenbewerker';"><a href="https://www.jobpersonality.com/natuursteenbewerker" class="bold-on-mobile">Natuursteenbewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/natuursteenbewerker">
							Vacatures: 1<br>
							Robotiserings%: 90%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/malmaker-gieter';"><a href="https://www.jobpersonality.com/malmaker-gieter" class="bold-on-mobile">Malmaker en gieter <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/malmaker-gieter">
							Vacatures: 0<br>
							Robotiserings%: 90%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/operator-papiermachine';"><a href="https://www.jobpersonality.com/operator-papiermachine" class="bold-on-mobile">Operator papiermachine <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/operator-papiermachine">
							Vacatures: 0<br>
							Robotiserings%: 67%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bandenwisselaar';"><a href="https://www.jobpersonality.com/bandenwisselaar" class="bold-on-mobile">Bandenwisselaar <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bandenwisselaar">
							Vacatures: 0<br>
							Robotiserings%: 94%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/recyclingmedewerker';"><a href="https://www.jobpersonality.com/recyclingmedewerker" class="bold-on-mobile">Medewerker recycling <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/recyclingmedewerker">
							Vacatures: 5<br>
							Robotiserings%: 92%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/verhuismanager';"><a href="https://www.jobpersonality.com/verhuismanager" class="bold-on-mobile">Verhuismanager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/verhuismanager">
							Vacatures: 4<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/chauffeur-bestelwagen';"><a href="https://www.jobpersonality.com/chauffeur-bestelwagen" class="bold-on-mobile">Chauffeur bestelwagen <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/chauffeur-bestelwagen">
							Vacatures: 0<br>
							Robotiserings%: 98%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/koerier';"><a href="https://www.jobpersonality.com/koerier" class="bold-on-mobile">Koerier <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/koerier">
							Vacatures: 182<br>
							Robotiserings%: 69%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/locomotiefstoker';"><a href="https://www.jobpersonality.com/locomotiefstoker" class="bold-on-mobile">Locomotief engineer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/locomotiefstoker">
							Vacatures: 0<br>
							Robotiserings%: 93%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/rangeerder';"><a href="https://www.jobpersonality.com/rangeerder" class="bold-on-mobile">Rangeerder <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/rangeerder">
							Vacatures: 27<br>
							Robotiserings%: 83%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/steward-vervoer';"><a href="https://www.jobpersonality.com/steward-vervoer" class="bold-on-mobile">Steward vervoer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/steward-vervoer">
							Vacatures: 0<br>
							Robotiserings%: 75%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/operator-transportband';"><a href="https://www.jobpersonality.com/operator-transportband" class="bold-on-mobile">Operator transportband <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/operator-transportband">
							Vacatures: 0<br>
							Robotiserings%: 93%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/takel-of-lieroperator';"><a href="https://www.jobpersonality.com/takel-of-lieroperator" class="bold-on-mobile">Takel- of Lieroperator <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/takel-of-lieroperator">
							Vacatures: 0<br>
							Robotiserings%: 65%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/heftruckchauffeur';"><a href="https://www.jobpersonality.com/heftruckchauffeur" class="bold-on-mobile">Heftruckchauffeur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/heftruckchauffeur">
							Vacatures: 278<br>
							Robotiserings%: 93%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/autowasser-schoonmaker-voertuigen';"><a href="https://www.jobpersonality.com/autowasser-schoonmaker-voertuigen" class="bold-on-mobile">Autowasser <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/autowasser-schoonmaker-voertuigen">
							Vacatures: 0<br>
							Robotiserings%: 37%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bediener-transportpomp';"><a href="https://www.jobpersonality.com/bediener-transportpomp" class="bold-on-mobile">Bediener transportpomp <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bediener-transportpomp">
							Vacatures: 0<br>
							Robotiserings%: 90%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/vuilnisman';"><a href="https://www.jobpersonality.com/vuilnisman" class="bold-on-mobile">Belader <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/vuilnisman">
							Vacatures: 143<br>
							Robotiserings%: 93%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/machinaal-lader-losser';"><a href="https://www.jobpersonality.com/machinaal-lader-losser" class="bold-on-mobile">Lader en Losser <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/machinaal-lader-losser">
							Vacatures: 11<br>
							Robotiserings%: 72%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/conducteur-conductrice';"><a href="https://www.jobpersonality.com/conducteur-conductrice" class="bold-on-mobile">Conducteur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/conducteur-conductrice">
							Vacatures: 58<br>
							Robotiserings%: 75%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/festivalopbouwer';"><a href="https://www.jobpersonality.com/festivalopbouwer" class="bold-on-mobile">Festivalopbouwer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/festivalopbouwer">
							Vacatures: 4<br>
							Robotiserings%: 18%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/tractor-chauffeur';"><a href="https://www.jobpersonality.com/tractor-chauffeur" class="bold-on-mobile">Tractor chauffeur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/tractor-chauffeur">
							Vacatures: 1<br>
							Robotiserings%: 87%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/manicure';"><a href="https://www.jobpersonality.com/manicure" class="bold-on-mobile">Manicure <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/manicure">
							Vacatures: 0<br>
							Robotiserings%: 95%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/grondwerker';"><a href="https://www.jobpersonality.com/grondwerker" class="bold-on-mobile">Grondwerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/grondwerker">
							Vacatures: 71<br>
							Robotiserings%: 87%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/machinist-shovel';"><a href="https://www.jobpersonality.com/machinist-shovel" class="bold-on-mobile">Machinist shovel <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/machinist-shovel">
							Vacatures: 4<br>
							Robotiserings%: 95%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/servicemedewerker';"><a href="https://www.jobpersonality.com/servicemedewerker" class="bold-on-mobile">Servicemedewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/servicemedewerker">
							Vacatures: 23<br>
							Robotiserings%: 75%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/animatiemedewerker';"><a href="https://www.jobpersonality.com/animatiemedewerker" class="bold-on-mobile">Animatiemedewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/animatiemedewerker">
							Vacatures: 0<br>
							Robotiserings%: 3%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/propper';"><a href="https://www.jobpersonality.com/propper" class="bold-on-mobile">Propper <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/propper">
							Vacatures: 0<br>
							Robotiserings%: 51%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/reachtruckchauffeur';"><a href="https://www.jobpersonality.com/reachtruckchauffeur" class="bold-on-mobile">Reachtruckchauffeur <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/reachtruckchauffeur">
							Vacatures: 163<br>
							Robotiserings%: 93%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/theesommelier';"><a href="https://www.jobpersonality.com/theesommelier" class="bold-on-mobile">Theesommelier <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/theesommelier">
							Vacatures: 0<br>
							Robotiserings%: 97%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/cateringmedewerker';"><a href="https://www.jobpersonality.com/cateringmedewerker" class="bold-on-mobile">Cateringmedewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/cateringmedewerker">
							Vacatures: 142<br>
							Robotiserings%: 87%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/pakketbezorger';"><a href="https://www.jobpersonality.com/pakketbezorger" class="bold-on-mobile">Pakketbezorger <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/pakketbezorger">
							Vacatures: 14<br>
							Robotiserings%: 69%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/tatoeeerder';"><a href="https://www.jobpersonality.com/tatoeeerder" class="bold-on-mobile">Tatoeëerder <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/tatoeeerder">
							Vacatures: 0<br>
							Robotiserings%: 11%<br>
							Opleidingsniveau: 2<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/verkeersbrigadier';"><a href="https://www.jobpersonality.com/verkeersbrigadier" class="bold-on-mobile">Verkeersregelaar <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/verkeersbrigadier">
							Vacatures: 7<br>
							Robotiserings%: 49%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/kok-bistro-eetcafe';"><a href="https://www.jobpersonality.com/kok-bistro-eetcafe" class="bold-on-mobile">Kok eetcafé <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/kok-bistro-eetcafe">
							Vacatures: 0<br>
							Robotiserings%: 94%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medewerker-voedselbereiding';"><a href="https://www.jobpersonality.com/medewerker-voedselbereiding" class="bold-on-mobile">Keukenhulp <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medewerker-voedselbereiding">
							Vacatures: 32<br>
							Robotiserings%: 87%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/barman';"><a href="https://www.jobpersonality.com/barman" class="bold-on-mobile">Barkeeper <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/barman">
							Vacatures: 71<br>
							Robotiserings%: 77%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medewerker-voedselbereiding-en-bediening';"><a href="https://www.jobpersonality.com/medewerker-voedselbereiding-en-bediening" class="bold-on-mobile">Medewerker restaurant <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medewerker-voedselbereiding-en-bediening">
							Vacatures: 26<br>
							Robotiserings%: 92%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/kassamedewerker-cafetaria-kiosken-koffiebars';"><a href="https://www.jobpersonality.com/kassamedewerker-cafetaria-kiosken-koffiebars" class="bold-on-mobile">Kassamedewerker horeca <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/kassamedewerker-cafetaria-kiosken-koffiebars">
							Vacatures: 0<br>
							Robotiserings%: 96%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/ober-serveerster';"><a href="https://www.jobpersonality.com/ober-serveerster" class="bold-on-mobile">Ober of serveerster <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/ober-serveerster">
							Vacatures: 4<br>
							Robotiserings%: 94%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/maaltijd-serveerder';"><a href="https://www.jobpersonality.com/maaltijd-serveerder" class="bold-on-mobile">Maaltijd serveerder <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/maaltijd-serveerder">
							Vacatures: 0<br>
							Robotiserings%: 86%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/eetzaal-cafetariabediende-barhulp';"><a href="https://www.jobpersonality.com/eetzaal-cafetariabediende-barhulp" class="bold-on-mobile">Bar medewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/eetzaal-cafetariabediende-barhulp">
							Vacatures: 71<br>
							Robotiserings%: 91%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/afwasser';"><a href="https://www.jobpersonality.com/afwasser" class="bold-on-mobile">Afwasser <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/afwasser">
							Vacatures: 42<br>
							Robotiserings%: 77%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/schoonmaker';"><a href="https://www.jobpersonality.com/schoonmaker" class="bold-on-mobile">Schoonmaker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/schoonmaker">
							Vacatures: 1476<br>
							Robotiserings%: 66%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/dienstmeisje-huishoudster';"><a href="https://www.jobpersonality.com/dienstmeisje-huishoudster" class="bold-on-mobile">Huishoudster <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/dienstmeisje-huishoudster">
							Vacatures: 5<br>
							Robotiserings%: 69%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/hondenuitlater';"><a href="https://www.jobpersonality.com/hondenuitlater" class="bold-on-mobile">Hondenuitlater <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/hondenuitlater">
							Vacatures: 0<br>
							Robotiserings%: 82%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/servicemedewerker-lobbymedewerker-kaartjescontroleur';"><a href="https://www.jobpersonality.com/servicemedewerker-lobbymedewerker-kaartjescontroleur" class="bold-on-mobile">Medewerker evenementen <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/servicemedewerker-lobbymedewerker-kaartjescontroleur">
							Vacatures: 2<br>
							Robotiserings%: 96%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/kassiere-kassamedewerker';"><a href="https://www.jobpersonality.com/kassiere-kassamedewerker" class="bold-on-mobile">Kassamedewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/kassiere-kassamedewerker">
							Vacatures: 6<br>
							Robotiserings%: 97%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/fotomodel-of-mannequin';"><a href="https://www.jobpersonality.com/fotomodel-of-mannequin" class="bold-on-mobile">Fotomodel <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/fotomodel-of-mannequin">
							Vacatures: 0<br>
							Robotiserings%: 98%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/vakkenvuller';"><a href="https://www.jobpersonality.com/vakkenvuller" class="bold-on-mobile">Vakkenvuller <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/vakkenvuller">
							Vacatures: 29<br>
							Robotiserings%: 64%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/magazijnmedewerker';"><a href="https://www.jobpersonality.com/magazijnmedewerker" class="bold-on-mobile">Magazijnmedewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/magazijnmedewerker">
							Vacatures: 627<br>
							Robotiserings%: 95%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/controleur-sorteerder-landbouwproducten';"><a href="https://www.jobpersonality.com/controleur-sorteerder-landbouwproducten" class="bold-on-mobile">Sorteerder landbouwproducten <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/controleur-sorteerder-landbouwproducten">
							Vacatures: 9<br>
							Robotiserings%: 41%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/kwekerijmedewerker';"><a href="https://www.jobpersonality.com/kwekerijmedewerker" class="bold-on-mobile">Kwekerijmedewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/kwekerijmedewerker">
							Vacatures: 3<br>
							Robotiserings%: 75%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medewerker-akkerbouwbedrijf';"><a href="https://www.jobpersonality.com/medewerker-akkerbouwbedrijf" class="bold-on-mobile">Agrarisch medewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medewerker-akkerbouwbedrijf">
							Vacatures: 15<br>
							Robotiserings%: 75%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medewerker-viskwekerij-of-aquacultuur';"><a href="https://www.jobpersonality.com/medewerker-viskwekerij-of-aquacultuur" class="bold-on-mobile">Medewerker viskwekerij <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medewerker-viskwekerij-of-aquacultuur">
							Vacatures: 0<br>
							Robotiserings%: 75%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medewerker-insectenkwekerij';"><a href="https://www.jobpersonality.com/medewerker-insectenkwekerij" class="bold-on-mobile">Insectenkweker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medewerker-insectenkwekerij">
							Vacatures: 1<br>
							Robotiserings%: 75%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/visser';"><a href="https://www.jobpersonality.com/visser" class="bold-on-mobile">Visser <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/visser">
							Vacatures: 0<br>
							Robotiserings%: 83%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/jager-vallenzetter';"><a href="https://www.jobpersonality.com/jager-vallenzetter" class="bold-on-mobile">Jager <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/jager-vallenzetter">
							Vacatures: 6<br>
							Robotiserings%: 77%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/houthakker';"><a href="https://www.jobpersonality.com/houthakker" class="bold-on-mobile">Houthakker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/houthakker">
							Vacatures: 0<br>
							Robotiserings%: 76%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bestuurder-bosbouwmachines';"><a href="https://www.jobpersonality.com/bestuurder-bosbouwmachines" class="bold-on-mobile">Bestuurder bosbouwmachines <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bestuurder-bosbouwmachines">
							Vacatures: 1<br>
							Robotiserings%: 79%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/assistent-stuc-en-schilderwerk';"><a href="https://www.jobpersonality.com/assistent-stuc-en-schilderwerk" class="bold-on-mobile">Assistent schilder <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/assistent-stuc-en-schilderwerk">
							Vacatures: 0<br>
							Robotiserings%: 94%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/derrickman-of-derrickhand';"><a href="https://www.jobpersonality.com/derrickman-of-derrickhand" class="bold-on-mobile">Derrickman <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/derrickman-of-derrickhand">
							Vacatures: 0<br>
							Robotiserings%: 80%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/machineoperator-transport-mijnbouw';"><a href="https://www.jobpersonality.com/machineoperator-transport-mijnbouw" class="bold-on-mobile">Machineoperator transport mijnbouw <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/machineoperator-transport-mijnbouw">
							Vacatures: 0<br>
							Robotiserings%: 54%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/steenhouwer-steengroeve';"><a href="https://www.jobpersonality.com/steenhouwer-steengroeve" class="bold-on-mobile">Steenhouwer steengroeve <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/steenhouwer-steengroeve">
							Vacatures: 0<br>
							Robotiserings%: 96%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medewerker-offshore';"><a href="https://www.jobpersonality.com/medewerker-offshore" class="bold-on-mobile">Medewerker offshore <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medewerker-offshore">
							Vacatures: 3<br>
							Robotiserings%: 68%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/stoffenversteller';"><a href="https://www.jobpersonality.com/stoffenversteller" class="bold-on-mobile">Stoffenversteller <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/stoffenversteller">
							Vacatures: 1<br>
							Robotiserings%: 96%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/visfileerder';"><a href="https://www.jobpersonality.com/visfileerder" class="bold-on-mobile">Visfileerder <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/visfileerder">
							Vacatures: 0<br>
							Robotiserings%: 94%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/stomerijmedewerker';"><a href="https://www.jobpersonality.com/stomerijmedewerker" class="bold-on-mobile">Wasserijmedewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/stomerijmedewerker">
							Vacatures: 1<br>
							Robotiserings%: 71%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/textielperser';"><a href="https://www.jobpersonality.com/textielperser" class="bold-on-mobile">Textielperser <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/textielperser">
							Vacatures: 2<br>
							Robotiserings%: 81%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bediener-naaimachines';"><a href="https://www.jobpersonality.com/bediener-naaimachines" class="bold-on-mobile">Bediener naaimachines <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bediener-naaimachines">
							Vacatures: 1<br>
							Robotiserings%: 89%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/handslijper-polijster';"><a href="https://www.jobpersonality.com/handslijper-polijster" class="bold-on-mobile">Polijster <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/handslijper-polijster">
							Vacatures: 1<br>
							Robotiserings%: 97%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/assistentpproductiemedewerker';"><a href="https://www.jobpersonality.com/assistentpproductiemedewerker" class="bold-on-mobile">Assistent-operator <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/assistentpproductiemedewerker">
							Vacatures: 14<br>
							Robotiserings%: 66%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/verhuizer';"><a href="https://www.jobpersonality.com/verhuizer" class="bold-on-mobile">Verhuizer <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/verhuizer">
							Vacatures: 14<br>
							Robotiserings%: 50%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/parkeerwacht';"><a href="https://www.jobpersonality.com/parkeerwacht" class="bold-on-mobile">Parkeer medewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/parkeerwacht">
							Vacatures: 1<br>
							Robotiserings%: 87%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/pompbediende';"><a href="https://www.jobpersonality.com/pompbediende" class="bold-on-mobile">Pompbediende <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/pompbediende">
							Vacatures: 0<br>
							Robotiserings%: 83%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/klusjesman';"><a href="https://www.jobpersonality.com/klusjesman" class="bold-on-mobile">Klusjesman <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/klusjesman">
							Vacatures: 6<br>
							Robotiserings%: 85%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/productiemedewerker';"><a href="https://www.jobpersonality.com/productiemedewerker" class="bold-on-mobile">Productiemedewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/productiemedewerker">
							Vacatures: 803<br>
							Robotiserings%: 93%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/inpakker';"><a href="https://www.jobpersonality.com/inpakker" class="bold-on-mobile">Inpakker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/inpakker">
							Vacatures: 193<br>
							Robotiserings%: 38%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/vuilsorteerder';"><a href="https://www.jobpersonality.com/vuilsorteerder" class="bold-on-mobile">Vuilsorteerder <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/vuilsorteerder">
							Vacatures: 0<br>
							Robotiserings%: 71%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/interieurverzorger';"><a href="https://www.jobpersonality.com/interieurverzorger" class="bold-on-mobile">Schoonmaakmedewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/interieurverzorger">
							Vacatures: 1465<br>
							Robotiserings%: 69%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/demontage-medewerker';"><a href="https://www.jobpersonality.com/demontage-medewerker" class="bold-on-mobile">Demontage Medewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/demontage-medewerker">
							Vacatures: 0<br>
							Robotiserings%: 98%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/huishoudelijke-hulp';"><a href="https://www.jobpersonality.com/huishoudelijke-hulp" class="bold-on-mobile">Huishoudelijke hulp <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/huishoudelijke-hulp">
							Vacatures: 253<br>
							Robotiserings%: 74%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/koffiedame';"><a href="https://www.jobpersonality.com/koffiedame" class="bold-on-mobile">Koffiedame <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/koffiedame">
							Vacatures: 0<br>
							Robotiserings%: 97%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/verkoopmedewerker';"><a href="https://www.jobpersonality.com/verkoopmedewerker" class="bold-on-mobile">Verkoopmedewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/verkoopmedewerker">
							Vacatures: 1744<br>
							Robotiserings%: 92%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bouwhulp';"><a href="https://www.jobpersonality.com/bouwhulp" class="bold-on-mobile">Bouwhulp <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bouwhulp">
							Vacatures: 8<br>
							Robotiserings%: 88%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medewerker-groenvoorziening';"><a href="https://www.jobpersonality.com/medewerker-groenvoorziening" class="bold-on-mobile">Medewerker groenvoorziening <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medewerker-groenvoorziening">
							Vacatures: 278<br>
							Robotiserings%: 75%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medewerker-dierenverzorging';"><a href="https://www.jobpersonality.com/medewerker-dierenverzorging" class="bold-on-mobile">Medewerker dierenverzorging <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medewerker-dierenverzorging">
							Vacatures: 3<br>
							Robotiserings%: 75%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bijrijder';"><a href="https://www.jobpersonality.com/bijrijder" class="bold-on-mobile">Bijrijder <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bijrijder">
							Vacatures: 105<br>
							Robotiserings%: 50%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/fietskoerier';"><a href="https://www.jobpersonality.com/fietskoerier" class="bold-on-mobile">Fietskoerier <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/fietskoerier">
							Vacatures: 0<br>
							Robotiserings%: 69%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/bezorger-kranten-folders';"><a href="https://www.jobpersonality.com/bezorger-kranten-folders" class="bold-on-mobile">Bezorger <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/bezorger-kranten-folders">
							Vacatures: 273<br>
							Robotiserings%: 68%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/medewerker-bediening';"><a href="https://www.jobpersonality.com/medewerker-bediening" class="bold-on-mobile">Medewerker bediening <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/medewerker-bediening">
							Vacatures: 493<br>
							Robotiserings%: 94%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/campingmedewerker';"><a href="https://www.jobpersonality.com/campingmedewerker" class="bold-on-mobile">Campingmedewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/campingmedewerker">
							Vacatures: 0<br>
							Robotiserings%: 72%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/expeditiemedewerker';"><a href="https://www.jobpersonality.com/expeditiemedewerker" class="bold-on-mobile">Expeditiemedewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/expeditiemedewerker">
							Vacatures: 37<br>
							Robotiserings%: 95%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/horecamedewerker';"><a href="https://www.jobpersonality.com/horecamedewerker" class="bold-on-mobile">Horecamedewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/horecamedewerker">
							Vacatures: 493<br>
							Robotiserings%: 94%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/keukenmedewerker';"><a href="https://www.jobpersonality.com/keukenmedewerker" class="bold-on-mobile">Keukenmedewerker <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/keukenmedewerker">
							Vacatures: 32<br>
							Robotiserings%: 81%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/straatartiest';"><a href="https://www.jobpersonality.com/straatartiest" class="bold-on-mobile">Straatartiest <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/straatartiest">
							Vacatures: 0<br>
							Robotiserings%: 37%<br>
							Opleidingsniveau: 1<br>
						</a>
					</div>
				</div>
							<div class="result" onclick="window.location = 'https://www.jobpersonality.com/complexbeveiliger';"><a href="https://www.jobpersonality.com/complexbeveiliger" class="bold-on-mobile">Complexbeveiliger <span>&gt;</span></a>
					<div class="show-on-mobile" style="padding-left: 20px;">
						<a href="https://www.jobpersonality.com/complexbeveiliger">
							Vacatures: 0<br>
							Robotiserings%: 60%<br>
							Opleidingsniveau: 0<br>
						</a>
					</div>
				</div>
					</div>
		<div class="column-20-filter hide-on-mobile">
			<div class="label">VACATURES</div>
			<div class="label show-on-mobile"></div>
							<div class="result">0</div>
							<div class="result">3</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">8</div>
							<div class="result">2</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">3</div>
							<div class="result">0</div>
							<div class="result">50</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">2</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">2</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">53</div>
							<div class="result">0</div>
							<div class="result">4</div>
							<div class="result">0</div>
							<div class="result">10</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">3</div>
							<div class="result">7</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">20</div>
							<div class="result">24</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">8</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">49</div>
							<div class="result">0</div>
							<div class="result">9</div>
							<div class="result">37</div>
							<div class="result">3</div>
							<div class="result">0</div>
							<div class="result">3</div>
							<div class="result">3</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">1</div>
							<div class="result">1</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">6</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">4</div>
							<div class="result">0</div>
							<div class="result">7</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">3</div>
							<div class="result">0</div>
							<div class="result">8</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">33</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">3</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">3</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">13</div>
							<div class="result">14</div>
							<div class="result">858</div>
							<div class="result">85</div>
							<div class="result">0</div>
							<div class="result">3</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">4</div>
							<div class="result">102</div>
							<div class="result">3</div>
							<div class="result">24</div>
							<div class="result">14</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">88</div>
							<div class="result">1</div>
							<div class="result">58</div>
							<div class="result">4</div>
							<div class="result">8</div>
							<div class="result">7</div>
							<div class="result">41</div>
							<div class="result">6</div>
							<div class="result">3</div>
							<div class="result">0</div>
							<div class="result">3</div>
							<div class="result">0</div>
							<div class="result">2</div>
							<div class="result">0</div>
							<div class="result">14</div>
							<div class="result">0</div>
							<div class="result">9</div>
							<div class="result">0</div>
							<div class="result">86</div>
							<div class="result">1</div>
							<div class="result">2</div>
							<div class="result">5</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">6</div>
							<div class="result">0</div>
							<div class="result">3</div>
							<div class="result">19</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">1</div>
							<div class="result">5</div>
							<div class="result">28</div>
							<div class="result">2</div>
							<div class="result">66</div>
							<div class="result">0</div>
							<div class="result">17</div>
							<div class="result">8</div>
							<div class="result">10</div>
							<div class="result">0</div>
							<div class="result">3</div>
							<div class="result">2</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">85</div>
							<div class="result">3</div>
							<div class="result">4</div>
							<div class="result">0</div>
							<div class="result">2</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">3</div>
							<div class="result">1</div>
							<div class="result">5</div>
							<div class="result">5</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">9</div>
							<div class="result">14</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">3</div>
							<div class="result">1</div>
							<div class="result">12</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">2</div>
							<div class="result">52</div>
							<div class="result">0</div>
							<div class="result">9</div>
							<div class="result">9</div>
							<div class="result">1</div>
							<div class="result">10</div>
							<div class="result">4</div>
							<div class="result">2</div>
							<div class="result">132</div>
							<div class="result">5</div>
							<div class="result">4</div>
							<div class="result">9</div>
							<div class="result">0</div>
							<div class="result">266</div>
							<div class="result">52</div>
							<div class="result">6</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">2</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">6</div>
							<div class="result">14</div>
							<div class="result">295</div>
							<div class="result">0</div>
							<div class="result">88</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">43</div>
							<div class="result">0</div>
							<div class="result">29</div>
							<div class="result">50</div>
							<div class="result">62</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">116</div>
							<div class="result">0</div>
							<div class="result">9</div>
							<div class="result">0</div>
							<div class="result">3</div>
							<div class="result">19</div>
							<div class="result">0</div>
							<div class="result">40</div>
							<div class="result">12</div>
							<div class="result">6</div>
							<div class="result">30</div>
							<div class="result">1</div>
							<div class="result">6</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">50</div>
							<div class="result">299</div>
							<div class="result">3</div>
							<div class="result">0</div>
							<div class="result">6</div>
							<div class="result">0</div>
							<div class="result">20</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">12</div>
							<div class="result">25</div>
							<div class="result">5</div>
							<div class="result">46</div>
							<div class="result">111</div>
							<div class="result">5</div>
							<div class="result">18</div>
							<div class="result">3</div>
							<div class="result">5</div>
							<div class="result">21</div>
							<div class="result">2</div>
							<div class="result">7</div>
							<div class="result">2</div>
							<div class="result">9</div>
							<div class="result">3</div>
							<div class="result">10</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">45</div>
							<div class="result">25</div>
							<div class="result">39</div>
							<div class="result">15</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">5</div>
							<div class="result">2</div>
							<div class="result">27</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">12</div>
							<div class="result">37</div>
							<div class="result">0</div>
							<div class="result">30</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">10</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">17</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">13</div>
							<div class="result">1</div>
							<div class="result">18</div>
							<div class="result">35</div>
							<div class="result">35</div>
							<div class="result">35</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">35</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">3</div>
							<div class="result">13</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">6</div>
							<div class="result">0</div>
							<div class="result">35</div>
							<div class="result">11</div>
							<div class="result">0</div>
							<div class="result">35</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">4</div>
							<div class="result">10</div>
							<div class="result">0</div>
							<div class="result">2</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">52</div>
							<div class="result">33</div>
							<div class="result">3</div>
							<div class="result">0</div>
							<div class="result">9</div>
							<div class="result">0</div>
							<div class="result">8</div>
							<div class="result">7</div>
							<div class="result">2</div>
							<div class="result">22</div>
							<div class="result">0</div>
							<div class="result">3</div>
							<div class="result">2</div>
							<div class="result">6</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">3</div>
							<div class="result">856</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">55</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">598</div>
							<div class="result">111</div>
							<div class="result">1</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">22</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">3</div>
							<div class="result">3</div>
							<div class="result">0</div>
							<div class="result">4</div>
							<div class="result">0</div>
							<div class="result">2</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">4</div>
							<div class="result">6</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">5</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">9</div>
							<div class="result">2</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">2</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">7</div>
							<div class="result">21</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">14</div>
							<div class="result">5</div>
							<div class="result">82</div>
							<div class="result">3</div>
							<div class="result">38</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">55</div>
							<div class="result">52</div>
							<div class="result">65</div>
							<div class="result">19</div>
							<div class="result">0</div>
							<div class="result">11</div>
							<div class="result">0</div>
							<div class="result">2</div>
							<div class="result">634</div>
							<div class="result">40</div>
							<div class="result">0</div>
							<div class="result">6</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">2</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">46</div>
							<div class="result">6</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">36</div>
							<div class="result">67</div>
							<div class="result">284</div>
							<div class="result">104</div>
							<div class="result">15</div>
							<div class="result">27</div>
							<div class="result">751</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">48</div>
							<div class="result">1963</div>
							<div class="result">0</div>
							<div class="result">8</div>
							<div class="result">10</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">1</div>
							<div class="result">24</div>
							<div class="result">61</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">3</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">22</div>
							<div class="result">34</div>
							<div class="result">37</div>
							<div class="result">0</div>
							<div class="result">13</div>
							<div class="result">9</div>
							<div class="result">13</div>
							<div class="result">3</div>
							<div class="result">6</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">12</div>
							<div class="result">33</div>
							<div class="result">0</div>
							<div class="result">943</div>
							<div class="result">8</div>
							<div class="result">2</div>
							<div class="result">4</div>
							<div class="result">10</div>
							<div class="result">1</div>
							<div class="result">20</div>
							<div class="result">14</div>
							<div class="result">3012</div>
							<div class="result">94</div>
							<div class="result">30</div>
							<div class="result">5</div>
							<div class="result">13</div>
							<div class="result">3</div>
							<div class="result">0</div>
							<div class="result">5</div>
							<div class="result">48</div>
							<div class="result">12</div>
							<div class="result">22</div>
							<div class="result">28</div>
							<div class="result">30</div>
							<div class="result">26</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">47</div>
							<div class="result">11</div>
							<div class="result">15</div>
							<div class="result">0</div>
							<div class="result">39</div>
							<div class="result">489</div>
							<div class="result">0</div>
							<div class="result">27</div>
							<div class="result">71</div>
							<div class="result">0</div>
							<div class="result">132</div>
							<div class="result">1271</div>
							<div class="result">178</div>
							<div class="result">152</div>
							<div class="result">19</div>
							<div class="result">1</div>
							<div class="result">27</div>
							<div class="result">4</div>
							<div class="result">0</div>
							<div class="result">3</div>
							<div class="result">8</div>
							<div class="result">4</div>
							<div class="result">8</div>
							<div class="result">0</div>
							<div class="result">64</div>
							<div class="result">13</div>
							<div class="result">5</div>
							<div class="result">2</div>
							<div class="result">2</div>
							<div class="result">0</div>
							<div class="result">2705</div>
							<div class="result">29</div>
							<div class="result">0</div>
							<div class="result">7</div>
							<div class="result">1</div>
							<div class="result">18</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">128</div>
							<div class="result">6</div>
							<div class="result">19</div>
							<div class="result">22</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">14</div>
							<div class="result">2</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">3</div>
							<div class="result">83</div>
							<div class="result">2</div>
							<div class="result">6</div>
							<div class="result">0</div>
							<div class="result">43</div>
							<div class="result">2</div>
							<div class="result">275</div>
							<div class="result">0</div>
							<div class="result">74</div>
							<div class="result">48</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">160</div>
							<div class="result">10</div>
							<div class="result">2</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">11</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">8</div>
							<div class="result">4</div>
							<div class="result">4</div>
							<div class="result">6</div>
							<div class="result">1</div>
							<div class="result">2</div>
							<div class="result">3</div>
							<div class="result">0</div>
							<div class="result">9</div>
							<div class="result">14</div>
							<div class="result">8</div>
							<div class="result">0</div>
							<div class="result">4</div>
							<div class="result">7</div>
							<div class="result">0</div>
							<div class="result">14</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">12</div>
							<div class="result">4</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">37</div>
							<div class="result">10</div>
							<div class="result">0</div>
							<div class="result">90</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">2</div>
							<div class="result">0</div>
							<div class="result">4</div>
							<div class="result">37</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">23</div>
							<div class="result">2</div>
							<div class="result">3</div>
							<div class="result">1423</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">18</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">12</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">3</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">10</div>
							<div class="result">2</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">4</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">6</div>
							<div class="result">8</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">36</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">192</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">14</div>
							<div class="result">15</div>
							<div class="result">337</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">4</div>
							<div class="result">2</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">2</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">4</div>
							<div class="result">0</div>
							<div class="result">16</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">23</div>
							<div class="result">0</div>
							<div class="result">135</div>
							<div class="result">54</div>
							<div class="result">0</div>
							<div class="result">34</div>
							<div class="result">4</div>
							<div class="result">735</div>
							<div class="result">364</div>
							<div class="result">0</div>
							<div class="result">28</div>
							<div class="result">2</div>
							<div class="result">714</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">17</div>
							<div class="result">72</div>
							<div class="result">0</div>
							<div class="result">3</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">7</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">5</div>
							<div class="result">17</div>
							<div class="result">10</div>
							<div class="result">2</div>
							<div class="result">4</div>
							<div class="result">480</div>
							<div class="result">0</div>
							<div class="result">3</div>
							<div class="result">17</div>
							<div class="result">1</div>
							<div class="result">191</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">263</div>
							<div class="result">33</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">62</div>
							<div class="result">2</div>
							<div class="result">29</div>
							<div class="result">0</div>
							<div class="result">1574</div>
							<div class="result">8</div>
							<div class="result">3</div>
							<div class="result">74</div>
							<div class="result">40</div>
							<div class="result">83</div>
							<div class="result">0</div>
							<div class="result">46</div>
							<div class="result">27</div>
							<div class="result">1</div>
							<div class="result">5</div>
							<div class="result">190</div>
							<div class="result">5</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">2</div>
							<div class="result">76</div>
							<div class="result">191</div>
							<div class="result">0</div>
							<div class="result">18</div>
							<div class="result">14</div>
							<div class="result">548</div>
							<div class="result">1556</div>
							<div class="result">2</div>
							<div class="result">69</div>
							<div class="result">5</div>
							<div class="result">0</div>
							<div class="result">23</div>
							<div class="result">41</div>
							<div class="result">0</div>
							<div class="result">3</div>
							<div class="result">8</div>
							<div class="result">16</div>
							<div class="result">30</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">3</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">11</div>
							<div class="result">9</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">7</div>
							<div class="result">0</div>
							<div class="result">288</div>
							<div class="result">9</div>
							<div class="result">4</div>
							<div class="result">2</div>
							<div class="result">22</div>
							<div class="result">7</div>
							<div class="result">0</div>
							<div class="result">13</div>
							<div class="result">0</div>
							<div class="result">41</div>
							<div class="result">59</div>
							<div class="result">1</div>
							<div class="result">707</div>
							<div class="result">10</div>
							<div class="result">119</div>
							<div class="result">16</div>
							<div class="result">0</div>
							<div class="result">35</div>
							<div class="result">28</div>
							<div class="result">226</div>
							<div class="result">10</div>
							<div class="result">3</div>
							<div class="result">0</div>
							<div class="result">51</div>
							<div class="result">22</div>
							<div class="result">1</div>
							<div class="result">42</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">6</div>
							<div class="result">0</div>
							<div class="result">2</div>
							<div class="result">3</div>
							<div class="result">55</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">5</div>
							<div class="result">219</div>
							<div class="result">11</div>
							<div class="result">0</div>
							<div class="result">126</div>
							<div class="result">0</div>
							<div class="result">22</div>
							<div class="result">3</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">1</div>
							<div class="result">2</div>
							<div class="result">2</div>
							<div class="result">0</div>
							<div class="result">4</div>
							<div class="result">0</div>
							<div class="result">73</div>
							<div class="result">0</div>
							<div class="result">117</div>
							<div class="result">18</div>
							<div class="result">0</div>
							<div class="result">26</div>
							<div class="result">49</div>
							<div class="result">0</div>
							<div class="result">12</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">405</div>
							<div class="result">7</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">18</div>
							<div class="result">25</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">3</div>
							<div class="result">49</div>
							<div class="result">10</div>
							<div class="result">8</div>
							<div class="result">0</div>
							<div class="result">9</div>
							<div class="result">19</div>
							<div class="result">0</div>
							<div class="result">5</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">26</div>
							<div class="result">3</div>
							<div class="result">195</div>
							<div class="result">1</div>
							<div class="result">2</div>
							<div class="result">43</div>
							<div class="result">0</div>
							<div class="result">226</div>
							<div class="result">35</div>
							<div class="result">4</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">3</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">8</div>
							<div class="result">31</div>
							<div class="result">0</div>
							<div class="result">18</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">3</div>
							<div class="result">0</div>
							<div class="result">10</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">3</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">10</div>
							<div class="result">0</div>
							<div class="result">15</div>
							<div class="result">0</div>
							<div class="result">5</div>
							<div class="result">0</div>
							<div class="result">2</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">186</div>
							<div class="result">0</div>
							<div class="result">1306</div>
							<div class="result">9</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">6</div>
							<div class="result">4</div>
							<div class="result">1</div>
							<div class="result">7</div>
							<div class="result">1</div>
							<div class="result">7</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">78</div>
							<div class="result">0</div>
							<div class="result">78</div>
							<div class="result">18</div>
							<div class="result">0</div>
							<div class="result">163</div>
							<div class="result">2</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">4</div>
							<div class="result">109</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">2</div>
							<div class="result">56</div>
							<div class="result">0</div>
							<div class="result">7</div>
							<div class="result">3</div>
							<div class="result">57</div>
							<div class="result">9</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">2</div>
							<div class="result">3</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">3</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">105</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">9</div>
							<div class="result">0</div>
							<div class="result">20</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">548</div>
							<div class="result">0</div>
							<div class="result">196</div>
							<div class="result">9</div>
							<div class="result">4</div>
							<div class="result">0</div>
							<div class="result">22</div>
							<div class="result">0</div>
							<div class="result">7</div>
							<div class="result">0</div>
							<div class="result">1960</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">4</div>
							<div class="result">0</div>
							<div class="result">6</div>
							<div class="result">5</div>
							<div class="result">4</div>
							<div class="result">6</div>
							<div class="result">73</div>
							<div class="result">3</div>
							<div class="result">3</div>
							<div class="result">1983</div>
							<div class="result">0</div>
							<div class="result">2</div>
							<div class="result">24</div>
							<div class="result">0</div>
							<div class="result">16</div>
							<div class="result">0</div>
							<div class="result">2</div>
							<div class="result">1</div>
							<div class="result">2</div>
							<div class="result">6</div>
							<div class="result">0</div>
							<div class="result">3</div>
							<div class="result">2</div>
							<div class="result">1322</div>
							<div class="result">6</div>
							<div class="result">0</div>
							<div class="result">1272</div>
							<div class="result">116</div>
							<div class="result">2637</div>
							<div class="result">430</div>
							<div class="result">131</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">215</div>
							<div class="result">35</div>
							<div class="result">3</div>
							<div class="result">74</div>
							<div class="result">3</div>
							<div class="result">34</div>
							<div class="result">20</div>
							<div class="result">1</div>
							<div class="result">192</div>
							<div class="result">300</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">2</div>
							<div class="result">5</div>
							<div class="result">6</div>
							<div class="result">4</div>
							<div class="result">24</div>
							<div class="result">8</div>
							<div class="result">2</div>
							<div class="result">14</div>
							<div class="result">20</div>
							<div class="result">84</div>
							<div class="result">0</div>
							<div class="result">4</div>
							<div class="result">39</div>
							<div class="result">243</div>
							<div class="result">4</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">290</div>
							<div class="result">9</div>
							<div class="result">513</div>
							<div class="result">476</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">16</div>
							<div class="result">17</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">11</div>
							<div class="result">84</div>
							<div class="result">0</div>
							<div class="result">8</div>
							<div class="result">17</div>
							<div class="result">100</div>
							<div class="result">148</div>
							<div class="result">136</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">437</div>
							<div class="result">98</div>
							<div class="result">7</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">2</div>
							<div class="result">1</div>
							<div class="result">15</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">4</div>
							<div class="result">38</div>
							<div class="result">0</div>
							<div class="result">68</div>
							<div class="result">6</div>
							<div class="result">0</div>
							<div class="result">4</div>
							<div class="result">51</div>
							<div class="result">23</div>
							<div class="result">788</div>
							<div class="result">10</div>
							<div class="result">8</div>
							<div class="result">11</div>
							<div class="result">3</div>
							<div class="result">11</div>
							<div class="result">1</div>
							<div class="result">11</div>
							<div class="result">62</div>
							<div class="result">11</div>
							<div class="result">0</div>
							<div class="result">5</div>
							<div class="result">3</div>
							<div class="result">9</div>
							<div class="result">6</div>
							<div class="result">498</div>
							<div class="result">121</div>
							<div class="result">3</div>
							<div class="result">426</div>
							<div class="result">3</div>
							<div class="result">0</div>
							<div class="result">138</div>
							<div class="result">4</div>
							<div class="result">34</div>
							<div class="result">6</div>
							<div class="result">27</div>
							<div class="result">0</div>
							<div class="result">18</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">5</div>
							<div class="result">28</div>
							<div class="result">0</div>
							<div class="result">3</div>
							<div class="result">20</div>
							<div class="result">0</div>
							<div class="result">7</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">140</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">45</div>
							<div class="result">28</div>
							<div class="result">10</div>
							<div class="result">45</div>
							<div class="result">191</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">8</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">42</div>
							<div class="result">2</div>
							<div class="result">24</div>
							<div class="result">627</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">8</div>
							<div class="result">3</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">3</div>
							<div class="result">1</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">6</div>
							<div class="result">3</div>
							<div class="result">2</div>
							<div class="result">1</div>
							<div class="result">3</div>
							<div class="result">5</div>
							<div class="result">26</div>
							<div class="result">2</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">19</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">8</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">4</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">2</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">4</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">8</div>
							<div class="result">25</div>
							<div class="result">0</div>
							<div class="result">22</div>
							<div class="result">7</div>
							<div class="result">21</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">8</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">7</div>
							<div class="result">16</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">5</div>
							<div class="result">4</div>
							<div class="result">0</div>
							<div class="result">182</div>
							<div class="result">0</div>
							<div class="result">27</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">278</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">143</div>
							<div class="result">11</div>
							<div class="result">58</div>
							<div class="result">4</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">71</div>
							<div class="result">4</div>
							<div class="result">23</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">163</div>
							<div class="result">0</div>
							<div class="result">142</div>
							<div class="result">14</div>
							<div class="result">0</div>
							<div class="result">7</div>
							<div class="result">0</div>
							<div class="result">32</div>
							<div class="result">71</div>
							<div class="result">26</div>
							<div class="result">0</div>
							<div class="result">4</div>
							<div class="result">0</div>
							<div class="result">71</div>
							<div class="result">42</div>
							<div class="result">1476</div>
							<div class="result">5</div>
							<div class="result">0</div>
							<div class="result">2</div>
							<div class="result">6</div>
							<div class="result">0</div>
							<div class="result">29</div>
							<div class="result">627</div>
							<div class="result">9</div>
							<div class="result">3</div>
							<div class="result">15</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">6</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">0</div>
							<div class="result">3</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">1</div>
							<div class="result">2</div>
							<div class="result">1</div>
							<div class="result">1</div>
							<div class="result">14</div>
							<div class="result">14</div>
							<div class="result">1</div>
							<div class="result">0</div>
							<div class="result">6</div>
							<div class="result">803</div>
							<div class="result">193</div>
							<div class="result">0</div>
							<div class="result">1465</div>
							<div class="result">0</div>
							<div class="result">253</div>
							<div class="result">0</div>
							<div class="result">1744</div>
							<div class="result">8</div>
							<div class="result">278</div>
							<div class="result">3</div>
							<div class="result">105</div>
							<div class="result">0</div>
							<div class="result">273</div>
							<div class="result">493</div>
							<div class="result">0</div>
							<div class="result">37</div>
							<div class="result">493</div>
							<div class="result">32</div>
							<div class="result">0</div>
							<div class="result">0</div>
					</div>
		<div class="column-20-filter hide-on-mobile">
			<div class="label" title="Kans dat werkzaamheden bij dit beroep binnen 10 tot 20 jaar worden overgenomen door robots">ROBOTISERINGS%</div>
			<div class="label show-on-mobile"></div>
            				<div class="result">2%</div>
            				<div class="result">4%</div>
            				<div class="result">0%</div>
            				<div class="result">1%</div>
            				<div class="result">2%</div>
            				<div class="result">2%</div>
            				<div class="result">2%</div>
            				<div class="result">25%</div>
            				<div class="result">8%</div>
            				<div class="result">61%</div>
            				<div class="result">31%</div>
            				<div class="result">2%</div>
            				<div class="result">5%</div>
            				<div class="result">22%</div>
            				<div class="result">22%</div>
            				<div class="result">22%</div>
            				<div class="result">2%</div>
            				<div class="result">3%</div>
            				<div class="result">10%</div>
            				<div class="result">1%</div>
            				<div class="result">6%</div>
            				<div class="result">2%</div>
            				<div class="result">2%</div>
            				<div class="result">3%</div>
            				<div class="result">1%</div>
            				<div class="result">30%</div>
            				<div class="result">2%</div>
            				<div class="result">2%</div>
            				<div class="result">2%</div>
            				<div class="result">20%</div>
            				<div class="result">0%</div>
            				<div class="result">4%</div>
            				<div class="result">10%</div>
            				<div class="result">10%</div>
            				<div class="result">2%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">43%</div>
            				<div class="result">43%</div>
            				<div class="result">43%</div>
            				<div class="result">23%</div>
            				<div class="result">0%</div>
            				<div class="result">0%</div>
            				<div class="result">0%</div>
            				<div class="result">1%</div>
            				<div class="result">0%</div>
            				<div class="result">0%</div>
            				<div class="result">6%</div>
            				<div class="result">13%</div>
            				<div class="result">6%</div>
            				<div class="result">25%</div>
            				<div class="result">44%</div>
            				<div class="result">4%</div>
            				<div class="result">1%</div>
            				<div class="result">0%</div>
            				<div class="result">1%</div>
            				<div class="result">1%</div>
            				<div class="result">40%</div>
            				<div class="result">41%</div>
            				<div class="result">64%</div>
            				<div class="result">6%</div>
            				<div class="result">40%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">76%</div>
            				<div class="result">1%</div>
            				<div class="result">65%</div>
            				<div class="result">1%</div>
            				<div class="result">0%</div>
            				<div class="result">0%</div>
            				<div class="result">1%</div>
            				<div class="result">2%</div>
            				<div class="result">3%</div>
            				<div class="result">0%</div>
            				<div class="result">0%</div>
            				<div class="result">2%</div>
            				<div class="result">6%</div>
            				<div class="result">1%</div>
            				<div class="result">0%</div>
            				<div class="result">0%</div>
            				<div class="result">0%</div>
            				<div class="result">0%</div>
            				<div class="result">0%</div>
            				<div class="result">0%</div>
            				<div class="result">0%</div>
            				<div class="result">0%</div>
            				<div class="result">0%</div>
            				<div class="result">0%</div>
            				<div class="result">0%</div>
            				<div class="result">0%</div>
            				<div class="result">0%</div>
            				<div class="result">0%</div>
            				<div class="result">0%</div>
            				<div class="result">0%</div>
            				<div class="result">0%</div>
            				<div class="result">0%</div>
            				<div class="result">0%</div>
            				<div class="result">0%</div>
            				<div class="result">1%</div>
            				<div class="result">4%</div>
            				<div class="result">0%</div>
            				<div class="result">2%</div>
            				<div class="result">0%</div>
            				<div class="result">13%</div>
            				<div class="result">0%</div>
            				<div class="result">1%</div>
            				<div class="result">6%</div>
            				<div class="result">40%</div>
            				<div class="result">13%</div>
            				<div class="result">13%</div>
            				<div class="result">40%</div>
            				<div class="result">13%</div>
            				<div class="result">2%</div>
            				<div class="result">16%</div>
            				<div class="result">0%</div>
            				<div class="result">2%</div>
            				<div class="result">0%</div>
            				<div class="result">1%</div>
            				<div class="result">3%</div>
            				<div class="result">6%</div>
            				<div class="result">0%</div>
            				<div class="result">13%</div>
            				<div class="result">99%</div>
            				<div class="result">1%</div>
            				<div class="result">13%</div>
            				<div class="result">1%</div>
            				<div class="result">25%</div>
            				<div class="result">40%</div>
            				<div class="result">13%</div>
            				<div class="result">0%</div>
            				<div class="result">0%</div>
            				<div class="result">0%</div>
            				<div class="result">0%</div>
            				<div class="result">2%</div>
            				<div class="result">6%</div>
            				<div class="result">2%</div>
            				<div class="result">2%</div>
            				<div class="result">2%</div>
            				<div class="result">0%</div>
            				<div class="result">0%</div>
            				<div class="result">0%</div>
            				<div class="result">13%</div>
            				<div class="result">40%</div>
            				<div class="result">40%</div>
            				<div class="result">2%</div>
            				<div class="result">6%</div>
            				<div class="result">23%</div>
            				<div class="result">0%</div>
            				<div class="result">0%</div>
            				<div class="result">44%</div>
            				<div class="result">16%</div>
            				<div class="result">1%</div>
            				<div class="result">4%</div>
            				<div class="result">1%</div>
            				<div class="result">1%</div>
            				<div class="result">1%</div>
            				<div class="result">2%</div>
            				<div class="result">4%</div>
            				<div class="result">7%</div>
            				<div class="result">7%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">59%</div>
            				<div class="result">59%</div>
            				<div class="result">96%</div>
            				<div class="result">1%</div>
            				<div class="result">1%</div>
            				<div class="result">5%</div>
            				<div class="result">5%</div>
            				<div class="result">7%</div>
            				<div class="result">2%</div>
            				<div class="result">59%</div>
            				<div class="result">2%</div>
            				<div class="result">1%</div>
            				<div class="result">2%</div>
            				<div class="result">81%</div>
            				<div class="result">70%</div>
            				<div class="result">0%</div>
            				<div class="result">25%</div>
            				<div class="result">25%</div>
            				<div class="result">25%</div>
            				<div class="result">25%</div>
            				<div class="result">25%</div>
            				<div class="result">24%</div>
            				<div class="result">87%</div>
            				<div class="result">98%</div>
            				<div class="result">8%</div>
            				<div class="result">8%</div>
            				<div class="result">57%</div>
            				<div class="result">31%</div>
            				<div class="result">31%</div>
            				<div class="result">1%</div>
            				<div class="result">1%</div>
            				<div class="result">13%</div>
            				<div class="result">13%</div>
            				<div class="result">2%</div>
            				<div class="result">47%</div>
            				<div class="result">1%</div>
            				<div class="result">23%</div>
            				<div class="result">23%</div>
            				<div class="result">23%</div>
            				<div class="result">23%</div>
            				<div class="result">94%</div>
            				<div class="result">94%</div>
            				<div class="result">90%</div>
            				<div class="result">94%</div>
            				<div class="result">98%</div>
            				<div class="result">23%</div>
            				<div class="result">58%</div>
            				<div class="result">99%</div>
            				<div class="result">17%</div>
            				<div class="result">4%</div>
            				<div class="result">5%</div>
            				<div class="result">98%</div>
            				<div class="result">93%</div>
            				<div class="result">99%</div>
            				<div class="result">33%</div>
            				<div class="result">23%</div>
            				<div class="result">23%</div>
            				<div class="result">23%</div>
            				<div class="result">1%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">4%</div>
            				<div class="result">4%</div>
            				<div class="result">13%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">22%</div>
            				<div class="result">22%</div>
            				<div class="result">22%</div>
            				<div class="result">22%</div>
            				<div class="result">22%</div>
            				<div class="result">22%</div>
            				<div class="result">4%</div>
            				<div class="result">22%</div>
            				<div class="result">22%</div>
            				<div class="result">10%</div>
            				<div class="result">22%</div>
            				<div class="result">22%</div>
            				<div class="result">21%</div>
            				<div class="result">22%</div>
            				<div class="result">99%</div>
            				<div class="result">2%</div>
            				<div class="result">5%</div>
            				<div class="result">88%</div>
            				<div class="result">38%</div>
            				<div class="result">38%</div>
            				<div class="result">2%</div>
            				<div class="result">49%</div>
            				<div class="result">4%</div>
            				<div class="result">2%</div>
            				<div class="result">2%</div>
            				<div class="result">1%</div>
            				<div class="result">22%</div>
            				<div class="result">10%</div>
            				<div class="result">3%</div>
            				<div class="result">2%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">1%</div>
            				<div class="result">1%</div>
            				<div class="result">2%</div>
            				<div class="result">1%</div>
            				<div class="result">1%</div>
            				<div class="result">14%</div>
            				<div class="result">7%</div>
            				<div class="result">16%</div>
            				<div class="result">1%</div>
            				<div class="result">1%</div>
            				<div class="result">1%</div>
            				<div class="result">1%</div>
            				<div class="result">1%</div>
            				<div class="result">1%</div>
            				<div class="result">1%</div>
            				<div class="result">1%</div>
            				<div class="result">1%</div>
            				<div class="result">52%</div>
            				<div class="result">48%</div>
            				<div class="result">25%</div>
            				<div class="result">3%</div>
            				<div class="result">24%</div>
            				<div class="result">24%</div>
            				<div class="result">24%</div>
            				<div class="result">24%</div>
            				<div class="result">24%</div>
            				<div class="result">8%</div>
            				<div class="result">2%</div>
            				<div class="result">2%</div>
            				<div class="result">96%</div>
            				<div class="result">67%</div>
            				<div class="result">3%</div>
            				<div class="result">63%</div>
            				<div class="result">1%</div>
            				<div class="result">1%</div>
            				<div class="result">4%</div>
            				<div class="result">30%</div>
            				<div class="result">91%</div>
            				<div class="result">85%</div>
            				<div class="result">65%</div>
            				<div class="result">65%</div>
            				<div class="result">77%</div>
            				<div class="result">1%</div>
            				<div class="result">61%</div>
            				<div class="result">61%</div>
            				<div class="result">3%</div>
            				<div class="result">1%</div>
            				<div class="result">3%</div>
            				<div class="result">0%</div>
            				<div class="result">0%</div>
            				<div class="result">0%</div>
            				<div class="result">5%</div>
            				<div class="result">25%</div>
            				<div class="result">13%</div>
            				<div class="result">13%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">0%</div>
            				<div class="result">1%</div>
            				<div class="result">3%</div>
            				<div class="result">1%</div>
            				<div class="result">1%</div>
            				<div class="result">2%</div>
            				<div class="result">1%</div>
            				<div class="result">1%</div>
            				<div class="result">1%</div>
            				<div class="result">19%</div>
            				<div class="result">1%</div>
            				<div class="result">59%</div>
            				<div class="result">99%</div>
            				<div class="result">2%</div>
            				<div class="result">4%</div>
            				<div class="result">2%</div>
            				<div class="result">4%</div>
            				<div class="result">8%</div>
            				<div class="result">2%</div>
            				<div class="result">10%</div>
            				<div class="result">2%</div>
            				<div class="result">2%</div>
            				<div class="result">2%</div>
            				<div class="result">2%</div>
            				<div class="result">1%</div>
            				<div class="result">0%</div>
            				<div class="result">2%</div>
            				<div class="result">7%</div>
            				<div class="result">11%</div>
            				<div class="result">18%</div>
            				<div class="result">6%</div>
            				<div class="result">89%</div>
            				<div class="result">4%</div>
            				<div class="result">4%</div>
            				<div class="result">4%</div>
            				<div class="result">38%</div>
            				<div class="result">38%</div>
            				<div class="result">0%</div>
            				<div class="result">14%</div>
            				<div class="result">14%</div>
            				<div class="result">0%</div>
            				<div class="result">0%</div>
            				<div class="result">2%</div>
            				<div class="result">34%</div>
            				<div class="result">0%</div>
            				<div class="result">0%</div>
            				<div class="result">7%</div>
            				<div class="result">7%</div>
            				<div class="result">1%</div>
            				<div class="result">1%</div>
            				<div class="result">1%</div>
            				<div class="result">1%</div>
            				<div class="result">1%</div>
            				<div class="result">1%</div>
            				<div class="result">1%</div>
            				<div class="result">1%</div>
            				<div class="result">1%</div>
            				<div class="result">2%</div>
            				<div class="result">2%</div>
            				<div class="result">90%</div>
            				<div class="result">90%</div>
            				<div class="result">68%</div>
            				<div class="result">35%</div>
            				<div class="result">23%</div>
            				<div class="result">47%</div>
            				<div class="result">35%</div>
            				<div class="result">17%</div>
            				<div class="result">1%</div>
            				<div class="result">34%</div>
            				<div class="result">36%</div>
            				<div class="result">34%</div>
            				<div class="result">34%</div>
            				<div class="result">8%</div>
            				<div class="result">31%</div>
            				<div class="result">35%</div>
            				<div class="result">8%</div>
            				<div class="result">92%</div>
            				<div class="result">2%</div>
            				<div class="result">97%</div>
            				<div class="result">97%</div>
            				<div class="result">86%</div>
            				<div class="result">0%</div>
            				<div class="result">46%</div>
            				<div class="result">25%</div>
            				<div class="result">40%</div>
            				<div class="result">84%</div>
            				<div class="result">66%</div>
            				<div class="result">57%</div>
            				<div class="result">63%</div>
            				<div class="result">48%</div>
            				<div class="result">42%</div>
            				<div class="result">18%</div>
            				<div class="result">11%</div>
            				<div class="result">57%</div>
            				<div class="result">27%</div>
            				<div class="result">27%</div>
            				<div class="result">61%</div>
            				<div class="result">90%</div>
            				<div class="result">90%</div>
            				<div class="result">90%</div>
            				<div class="result">15%</div>
            				<div class="result">2%</div>
            				<div class="result">1%</div>
            				<div class="result">1%</div>
            				<div class="result">8%</div>
            				<div class="result">10%</div>
            				<div class="result">2%</div>
            				<div class="result">8%</div>
            				<div class="result">10%</div>
            				<div class="result">5%</div>
            				<div class="result">8%</div>
            				<div class="result">1%</div>
            				<div class="result">1%</div>
            				<div class="result">4%</div>
            				<div class="result">13%</div>
            				<div class="result">1%</div>
            				<div class="result">4%</div>
            				<div class="result">2%</div>
            				<div class="result">2%</div>
            				<div class="result">1%</div>
            				<div class="result">70%</div>
            				<div class="result">13%</div>
            				<div class="result">7%</div>
            				<div class="result">7%</div>
            				<div class="result">2%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">22%</div>
            				<div class="result">31%</div>
            				<div class="result">0%</div>
            				<div class="result">2%</div>
            				<div class="result">22%</div>
            				<div class="result">0%</div>
            				<div class="result">3%</div>
            				<div class="result">8%</div>
            				<div class="result">3%</div>
            				<div class="result">3%</div>
            				<div class="result">1%</div>
            				<div class="result">45%</div>
            				<div class="result">22%</div>
            				<div class="result">6%</div>
            				<div class="result">2%</div>
            				<div class="result">4%</div>
            				<div class="result">48%</div>
            				<div class="result">10%</div>
            				<div class="result">4%</div>
            				<div class="result">4%</div>
            				<div class="result">4%</div>
            				<div class="result">11%</div>
            				<div class="result">1%</div>
            				<div class="result">1%</div>
            				<div class="result">39%</div>
            				<div class="result">14%</div>
            				<div class="result">2%</div>
            				<div class="result">2%</div>
            				<div class="result">2%</div>
            				<div class="result">4%</div>
            				<div class="result">4%</div>
            				<div class="result">13%</div>
            				<div class="result">13%</div>
            				<div class="result">34%</div>
            				<div class="result">2%</div>
            				<div class="result">2%</div>
            				<div class="result">4%</div>
            				<div class="result">13%</div>
            				<div class="result">4%</div>
            				<div class="result">13%</div>
            				<div class="result">31%</div>
            				<div class="result">1%</div>
            				<div class="result">4%</div>
            				<div class="result">31%</div>
            				<div class="result">13%</div>
            				<div class="result">19%</div>
            				<div class="result">1%</div>
            				<div class="result">1%</div>
            				<div class="result">1%</div>
            				<div class="result">4%</div>
            				<div class="result">1%</div>
            				<div class="result">1%</div>
            				<div class="result">31%</div>
            				<div class="result">4%</div>
            				<div class="result">52%</div>
            				<div class="result">4%</div>
            				<div class="result">3%</div>
            				<div class="result">4%</div>
            				<div class="result">13%</div>
            				<div class="result">13%</div>
            				<div class="result">4%</div>
            				<div class="result">22%</div>
            				<div class="result">36%</div>
            				<div class="result">13%</div>
            				<div class="result">4%</div>
            				<div class="result">1%</div>
            				<div class="result">1%</div>
            				<div class="result">7%</div>
            				<div class="result">13%</div>
            				<div class="result">1%</div>
            				<div class="result">1%</div>
            				<div class="result">21%</div>
            				<div class="result">1%</div>
            				<div class="result">13%</div>
            				<div class="result">1%</div>
            				<div class="result">4%</div>
            				<div class="result">4%</div>
            				<div class="result">1%</div>
            				<div class="result">1%</div>
            				<div class="result">39%</div>
            				<div class="result">2%</div>
            				<div class="result">4%</div>
            				<div class="result">39%</div>
            				<div class="result">2%</div>
            				<div class="result">31%</div>
            				<div class="result">2%</div>
            				<div class="result">2%</div>
            				<div class="result">31%</div>
            				<div class="result">1%</div>
            				<div class="result">13%</div>
            				<div class="result">2%</div>
            				<div class="result">3%</div>
            				<div class="result">4%</div>
            				<div class="result">1%</div>
            				<div class="result">3%</div>
            				<div class="result">1%</div>
            				<div class="result">22%</div>
            				<div class="result">4%</div>
            				<div class="result">22%</div>
            				<div class="result">2%</div>
            				<div class="result">10%</div>
            				<div class="result">13%</div>
            				<div class="result">2%</div>
            				<div class="result">10%</div>
            				<div class="result">44%</div>
            				<div class="result">4%</div>
            				<div class="result">0%</div>
            				<div class="result">13%</div>
            				<div class="result">73%</div>
            				<div class="result">3%</div>
            				<div class="result">59%</div>
            				<div class="result">5%</div>
            				<div class="result">8%</div>
            				<div class="result">8%</div>
            				<div class="result">9%</div>
            				<div class="result">0%</div>
            				<div class="result">75%</div>
            				<div class="result">25%</div>
            				<div class="result">29%</div>
            				<div class="result">77%</div>
            				<div class="result">98%</div>
            				<div class="result">98%</div>
            				<div class="result">8%</div>
            				<div class="result">8%</div>
            				<div class="result">8%</div>
            				<div class="result">97%</div>
            				<div class="result">4%</div>
            				<div class="result">23%</div>
            				<div class="result">23%</div>
            				<div class="result">90%</div>
            				<div class="result">21%</div>
            				<div class="result">30%</div>
            				<div class="result">22%</div>
            				<div class="result">65%</div>
            				<div class="result">45%</div>
            				<div class="result">22%</div>
            				<div class="result">22%</div>
            				<div class="result">22%</div>
            				<div class="result">52%</div>
            				<div class="result">52%</div>
            				<div class="result">81%</div>
            				<div class="result">68%</div>
            				<div class="result">75%</div>
            				<div class="result">84%</div>
            				<div class="result">84%</div>
            				<div class="result">81%</div>
            				<div class="result">1%</div>
            				<div class="result">38%</div>
            				<div class="result">24%</div>
            				<div class="result">84%</div>
            				<div class="result">24%</div>
            				<div class="result">24%</div>
            				<div class="result">24%</div>
            				<div class="result">24%</div>
            				<div class="result">96%</div>
            				<div class="result">96%</div>
            				<div class="result">1%</div>
            				<div class="result">97%</div>
            				<div class="result">97%</div>
            				<div class="result">57%</div>
            				<div class="result">91%</div>
            				<div class="result">85%</div>
            				<div class="result">42%</div>
            				<div class="result">61%</div>
            				<div class="result">94%</div>
            				<div class="result">99%</div>
            				<div class="result">1%</div>
            				<div class="result">15%</div>
            				<div class="result">13%</div>
            				<div class="result">60%</div>
            				<div class="result">39%</div>
            				<div class="result">56%</div>
            				<div class="result">4%</div>
            				<div class="result">2%</div>
            				<div class="result">5%</div>
            				<div class="result">37%</div>
            				<div class="result">98%</div>
            				<div class="result">13%</div>
            				<div class="result">3%</div>
            				<div class="result">2%</div>
            				<div class="result">13%</div>
            				<div class="result">13%</div>
            				<div class="result">10%</div>
            				<div class="result">72%</div>
            				<div class="result">55%</div>
            				<div class="result">74%</div>
            				<div class="result">98%</div>
            				<div class="result">13%</div>
            				<div class="result">2%</div>
            				<div class="result">60%</div>
            				<div class="result">31%</div>
            				<div class="result">14%</div>
            				<div class="result">1%</div>
            				<div class="result">90%</div>
            				<div class="result">90%</div>
            				<div class="result">47%</div>
            				<div class="result">23%</div>
            				<div class="result">5%</div>
            				<div class="result">13%</div>
            				<div class="result">92%</div>
            				<div class="result">4%</div>
            				<div class="result">10%</div>
            				<div class="result">34%</div>
            				<div class="result">3%</div>
            				<div class="result">34%</div>
            				<div class="result">6%</div>
            				<div class="result">91%</div>
            				<div class="result">71%</div>
            				<div class="result">40%</div>
            				<div class="result">40%</div>
            				<div class="result">30%</div>
            				<div class="result">25%</div>
            				<div class="result">39%</div>
            				<div class="result">47%</div>
            				<div class="result">47%</div>
            				<div class="result">3%</div>
            				<div class="result">2%</div>
            				<div class="result">54%</div>
            				<div class="result">51%</div>
            				<div class="result">30%</div>
            				<div class="result">78%</div>
            				<div class="result">89%</div>
            				<div class="result">72%</div>
            				<div class="result">86%</div>
            				<div class="result">63%</div>
            				<div class="result">63%</div>
            				<div class="result">3%</div>
            				<div class="result">0%</div>
            				<div class="result">0%</div>
            				<div class="result">17%</div>
            				<div class="result">48%</div>
            				<div class="result">48%</div>
            				<div class="result">5%</div>
            				<div class="result">60%</div>
            				<div class="result">34%</div>
            				<div class="result">75%</div>
            				<div class="result">34%</div>
            				<div class="result">10%</div>
            				<div class="result">10%</div>
            				<div class="result">57%</div>
            				<div class="result">95%</div>
            				<div class="result">84%</div>
            				<div class="result">67%</div>
            				<div class="result">10%</div>
            				<div class="result">63%</div>
            				<div class="result">81%</div>
            				<div class="result">83%</div>
            				<div class="result">30%</div>
            				<div class="result">96%</div>
            				<div class="result">97%</div>
            				<div class="result">94%</div>
            				<div class="result">57%</div>
            				<div class="result">66%</div>
            				<div class="result">95%</div>
            				<div class="result">97%</div>
            				<div class="result">77%</div>
            				<div class="result">54%</div>
            				<div class="result">8%</div>
            				<div class="result">8%</div>
            				<div class="result">82%</div>
            				<div class="result">96%</div>
            				<div class="result">72%</div>
            				<div class="result">54%</div>
            				<div class="result">20%</div>
            				<div class="result">11%</div>
            				<div class="result">1%</div>
            				<div class="result">95%</div>
            				<div class="result">29%</div>
            				<div class="result">21%</div>
            				<div class="result">91%</div>
            				<div class="result">6%</div>
            				<div class="result">8%</div>
            				<div class="result">74%</div>
            				<div class="result">9%</div>
            				<div class="result">9%</div>
            				<div class="result">6%</div>
            				<div class="result">28%</div>
            				<div class="result">97%</div>
            				<div class="result">98%</div>
            				<div class="result">92%</div>
            				<div class="result">54%</div>
            				<div class="result">2%</div>
            				<div class="result">10%</div>
            				<div class="result">25%</div>
            				<div class="result">25%</div>
            				<div class="result">25%</div>
            				<div class="result">99%</div>
            				<div class="result">97%</div>
            				<div class="result">94%</div>
            				<div class="result">1%</div>
            				<div class="result">95%</div>
            				<div class="result">96%</div>
            				<div class="result">98%</div>
            				<div class="result">90%</div>
            				<div class="result">97%</div>
            				<div class="result">98%</div>
            				<div class="result">86%</div>
            				<div class="result">46%</div>
            				<div class="result">97%</div>
            				<div class="result">97%</div>
            				<div class="result">55%</div>
            				<div class="result">70%</div>
            				<div class="result">97%</div>
            				<div class="result">94%</div>
            				<div class="result">95%</div>
            				<div class="result">92%</div>
            				<div class="result">90%</div>
            				<div class="result">96%</div>
            				<div class="result">99%</div>
            				<div class="result">99%</div>
            				<div class="result">49%</div>
            				<div class="result">96%</div>
            				<div class="result">88%</div>
            				<div class="result">95%</div>
            				<div class="result">86%</div>
            				<div class="result">98%</div>
            				<div class="result">81%</div>
            				<div class="result">96%</div>
            				<div class="result">22%</div>
            				<div class="result">99%</div>
            				<div class="result">16%</div>
            				<div class="result">98%</div>
            				<div class="result">98%</div>
            				<div class="result">96%</div>
            				<div class="result">66%</div>
            				<div class="result">57%</div>
            				<div class="result">57%</div>
            				<div class="result">8%</div>
            				<div class="result">94%</div>
            				<div class="result">95%</div>
            				<div class="result">87%</div>
            				<div class="result">75%</div>
            				<div class="result">87%</div>
            				<div class="result">97%</div>
            				<div class="result">17%</div>
            				<div class="result">17%</div>
            				<div class="result">68%</div>
            				<div class="result">82%</div>
            				<div class="result">89%</div>
            				<div class="result">72%</div>
            				<div class="result">82%</div>
            				<div class="result">79%</div>
            				<div class="result">87%</div>
            				<div class="result">75%</div>
            				<div class="result">94%</div>
            				<div class="result">88%</div>
            				<div class="result">83%</div>
            				<div class="result">79%</div>
            				<div class="result">15%</div>
            				<div class="result">73%</div>
            				<div class="result">64%</div>
            				<div class="result">75%</div>
            				<div class="result">40%</div>
            				<div class="result">35%</div>
            				<div class="result">84%</div>
            				<div class="result">90%</div>
            				<div class="result">90%</div>
            				<div class="result">82%</div>
            				<div class="result">83%</div>
            				<div class="result">39%</div>
            				<div class="result">53%</div>
            				<div class="result">89%</div>
            				<div class="result">83%</div>
            				<div class="result">71%</div>
            				<div class="result">71%</div>
            				<div class="result">0%</div>
            				<div class="result">74%</div>
            				<div class="result">15%</div>
            				<div class="result">76%</div>
            				<div class="result">36%</div>
            				<div class="result">70%</div>
            				<div class="result">76%</div>
            				<div class="result">91%</div>
            				<div class="result">41%</div>
            				<div class="result">61%</div>
            				<div class="result">65%</div>
            				<div class="result">82%</div>
            				<div class="result">71%</div>
            				<div class="result">91%</div>
            				<div class="result">55%</div>
            				<div class="result">59%</div>
            				<div class="result">59%</div>
            				<div class="result">73%</div>
            				<div class="result">75%</div>
            				<div class="result">40%</div>
            				<div class="result">88%</div>
            				<div class="result">66%</div>
            				<div class="result">79%</div>
            				<div class="result">93%</div>
            				<div class="result">94%</div>
            				<div class="result">59%</div>
            				<div class="result">70%</div>
            				<div class="result">91%</div>
            				<div class="result">63%</div>
            				<div class="result">65%</div>
            				<div class="result">40%</div>
            				<div class="result">65%</div>
            				<div class="result">72%</div>
            				<div class="result">67%</div>
            				<div class="result">59%</div>
            				<div class="result">82%</div>
            				<div class="result">10%</div>
            				<div class="result">49%</div>
            				<div class="result">97%</div>
            				<div class="result">27%</div>
            				<div class="result">91%</div>
            				<div class="result">99%</div>
            				<div class="result">64%</div>
            				<div class="result">64%</div>
            				<div class="result">94%</div>
            				<div class="result">18%</div>
            				<div class="result">90%</div>
            				<div class="result">50%</div>
            				<div class="result">2%</div>
            				<div class="result">79%</div>
            				<div class="result">95%</div>
            				<div class="result">97%</div>
            				<div class="result">82%</div>
            				<div class="result">93%</div>
            				<div class="result">97%</div>
            				<div class="result">49%</div>
            				<div class="result">98%</div>
            				<div class="result">89%</div>
            				<div class="result">93%</div>
            				<div class="result">60%</div>
            				<div class="result">70%</div>
            				<div class="result">86%</div>
            				<div class="result">36%</div>
            				<div class="result">84%</div>
            				<div class="result">98%</div>
            				<div class="result">65%</div>
            				<div class="result">87%</div>
            				<div class="result">93%</div>
            				<div class="result">90%</div>
            				<div class="result">84%</div>
            				<div class="result">94%</div>
            				<div class="result">94%</div>
            				<div class="result">61%</div>
            				<div class="result">92%</div>
            				<div class="result">97%</div>
            				<div class="result">83%</div>
            				<div class="result">95%</div>
            				<div class="result">52%</div>
            				<div class="result">84%</div>
            				<div class="result">0%</div>
            				<div class="result">39%</div>
            				<div class="result">92%</div>
            				<div class="result">87%</div>
            				<div class="result">4%</div>
            				<div class="result">96%</div>
            				<div class="result">91%</div>
            				<div class="result">95%</div>
            				<div class="result">64%</div>
            				<div class="result">85%</div>
            				<div class="result">89%</div>
            				<div class="result">61%</div>
            				<div class="result">85%</div>
            				<div class="result">78%</div>
            				<div class="result">71%</div>
            				<div class="result">86%</div>
            				<div class="result">88%</div>
            				<div class="result">98%</div>
            				<div class="result">92%</div>
            				<div class="result">95%</div>
            				<div class="result">1%</div>
            				<div class="result">97%</div>
            				<div class="result">45%</div>
            				<div class="result">69%</div>
            				<div class="result">92%</div>
            				<div class="result">88%</div>
            				<div class="result">99%</div>
            				<div class="result">66%</div>
            				<div class="result">98%</div>
            				<div class="result">90%</div>
            				<div class="result">90%</div>
            				<div class="result">7%</div>
            				<div class="result">55%</div>
            				<div class="result">71%</div>
            				<div class="result">35%</div>
            				<div class="result">25%</div>
            				<div class="result">67%</div>
            				<div class="result">89%</div>
            				<div class="result">79%</div>
            				<div class="result">89%</div>
            				<div class="result">96%</div>
            				<div class="result">91%</div>
            				<div class="result">86%</div>
            				<div class="result">83%</div>
            				<div class="result">27%</div>
            				<div class="result">27%</div>
            				<div class="result">62%</div>
            				<div class="result">4%</div>
            				<div class="result">97%</div>
            				<div class="result">90%</div>
            				<div class="result">90%</div>
            				<div class="result">92%</div>
            				<div class="result">94%</div>
            				<div class="result">91%</div>
            				<div class="result">90%</div>
            				<div class="result">8%</div>
            				<div class="result">48%</div>
            				<div class="result">97%</div>
            				<div class="result">69%</div>
            				<div class="result">18%</div>
            				<div class="result">98%</div>
            				<div class="result">5%</div>
            				<div class="result">55%</div>
            				<div class="result">1%</div>
            				<div class="result">1%</div>
            				<div class="result">8%</div>
            				<div class="result">1%</div>
            				<div class="result">2%</div>
            				<div class="result">2%</div>
            				<div class="result">2%</div>
            				<div class="result">85%</div>
            				<div class="result">85%</div>
            				<div class="result">98%</div>
            				<div class="result">13%</div>
            				<div class="result">40%</div>
            				<div class="result">40%</div>
            				<div class="result">4%</div>
            				<div class="result">96%</div>
            				<div class="result">79%</div>
            				<div class="result">8%</div>
            				<div class="result">80%</div>
            				<div class="result">5%</div>
            				<div class="result">39%</div>
            				<div class="result">1%</div>
            				<div class="result">39%</div>
            				<div class="result">60%</div>
            				<div class="result">90%</div>
            				<div class="result">82%</div>
            				<div class="result">80%</div>
            				<div class="result">72%</div>
            				<div class="result">8%</div>
            				<div class="result">95%</div>
            				<div class="result">0%</div>
            				<div class="result">63%</div>
            				<div class="result">97%</div>
            				<div class="result">85%</div>
            				<div class="result">4%</div>
            				<div class="result">66%</div>
            				<div class="result">94%</div>
            				<div class="result">75%</div>
            				<div class="result">9%</div>
            				<div class="result">31%</div>
            				<div class="result">2%</div>
            				<div class="result">82%</div>
            				<div class="result">97%</div>
            				<div class="result">52%</div>
            				<div class="result">0%</div>
            				<div class="result">34%</div>
            				<div class="result">13%</div>
            				<div class="result">13%</div>
            				<div class="result">39%</div>
            				<div class="result">19%</div>
            				<div class="result">73%</div>
            				<div class="result">91%</div>
            				<div class="result">6%</div>
            				<div class="result">40%</div>
            				<div class="result">88%</div>
            				<div class="result">13%</div>
            				<div class="result">99%</div>
            				<div class="result">2%</div>
            				<div class="result">96%</div>
            				<div class="result">8%</div>
            				<div class="result">8%</div>
            				<div class="result">53%</div>
            				<div class="result">75%</div>
            				<div class="result">79%</div>
            				<div class="result">52%</div>
            				<div class="result">7%</div>
            				<div class="result">7%</div>
            				<div class="result">92%</div>
            				<div class="result">47%</div>
            				<div class="result">1%</div>
            				<div class="result">1%</div>
            				<div class="result">2%</div>
            				<div class="result">77%</div>
            				<div class="result">82%</div>
            				<div class="result">15%</div>
            				<div class="result">93%</div>
            				<div class="result">94%</div>
            				<div class="result">0%</div>
            				<div class="result">8%</div>
            				<div class="result">53%</div>
            				<div class="result">65%</div>
            				<div class="result">79%</div>
            				<div class="result">47%</div>
            				<div class="result">52%</div>
            				<div class="result">98%</div>
            				<div class="result">1%</div>
            				<div class="result">4%</div>
            				<div class="result">8%</div>
            				<div class="result">64%</div>
            				<div class="result">13%</div>
            				<div class="result">88%</div>
            				<div class="result">86%</div>
            				<div class="result">48%</div>
            				<div class="result">30%</div>
            				<div class="result">66%</div>
            				<div class="result">68%</div>
            				<div class="result">10%</div>
            				<div class="result">95%</div>
            				<div class="result">97%</div>
            				<div class="result">98%</div>
            				<div class="result">93%</div>
            				<div class="result">28%</div>
            				<div class="result">23%</div>
            				<div class="result">1%</div>
            				<div class="result">15%</div>
            				<div class="result">68%</div>
            				<div class="result">97%</div>
            				<div class="result">45%</div>
            				<div class="result">98%</div>
            				<div class="result">91%</div>
            				<div class="result">37%</div>
            				<div class="result">94%</div>
            				<div class="result">15%</div>
            				<div class="result">55%</div>
            				<div class="result">13%</div>
            				<div class="result">4%</div>
            				<div class="result">2%</div>
            				<div class="result">40%</div>
            				<div class="result">13%</div>
            				<div class="result">35%</div>
            				<div class="result">40%</div>
            				<div class="result">88%</div>
            				<div class="result">88%</div>
            				<div class="result">94%</div>
            				<div class="result">88%</div>
            				<div class="result">92%</div>
            				<div class="result">86%</div>
            				<div class="result">88%</div>
            				<div class="result">40%</div>
            				<div class="result">25%</div>
            				<div class="result">82%</div>
            				<div class="result">47%</div>
            				<div class="result">97%</div>
            				<div class="result">14%</div>
            				<div class="result">1%</div>
            				<div class="result">11%</div>
            				<div class="result">64%</div>
            				<div class="result">8%</div>
            				<div class="result">52%</div>
            				<div class="result">98%</div>
            				<div class="result">7%</div>
            				<div class="result">8%</div>
            				<div class="result">8%</div>
            				<div class="result">66%</div>
            				<div class="result">69%</div>
            				<div class="result">40%</div>
            				<div class="result">1%</div>
            				<div class="result">92%</div>
            				<div class="result">84%</div>
            				<div class="result">10%</div>
            				<div class="result">94%</div>
            				<div class="result">90%</div>
            				<div class="result">15%</div>
            				<div class="result">2%</div>
            				<div class="result">99%</div>
            				<div class="result">6%</div>
            				<div class="result">55%</div>
            				<div class="result">15%</div>
            				<div class="result">2%</div>
            				<div class="result">57%</div>
            				<div class="result">2%</div>
            				<div class="result">15%</div>
            				<div class="result">8%</div>
            				<div class="result">8%</div>
            				<div class="result">2%</div>
            				<div class="result">15%</div>
            				<div class="result">82%</div>
            				<div class="result">64%</div>
            				<div class="result">15%</div>
            				<div class="result">69%</div>
            				<div class="result">96%</div>
            				<div class="result">64%</div>
            				<div class="result">69%</div>
            				<div class="result">25%</div>
            				<div class="result">23%</div>
            				<div class="result">2%</div>
            				<div class="result">25%</div>
            				<div class="result">1%</div>
            				<div class="result">8%</div>
            				<div class="result">9%</div>
            				<div class="result">25%</div>
            				<div class="result">54%</div>
            				<div class="result">29%</div>
            				<div class="result">28%</div>
            				<div class="result">47%</div>
            				<div class="result">27%</div>
            				<div class="result">61%</div>
            				<div class="result">84%</div>
            				<div class="result">21%</div>
            				<div class="result">67%</div>
            				<div class="result">67%</div>
            				<div class="result">96%</div>
            				<div class="result">28%</div>
            				<div class="result">10%</div>
            				<div class="result">97%</div>
            				<div class="result">61%</div>
            				<div class="result">43%</div>
            				<div class="result">37%</div>
            				<div class="result">80%</div>
            				<div class="result">79%</div>
            				<div class="result">83%</div>
            				<div class="result">8%</div>
            				<div class="result">83%</div>
            				<div class="result">51%</div>
            				<div class="result">96%</div>
            				<div class="result">39%</div>
            				<div class="result">94%</div>
            				<div class="result">99%</div>
            				<div class="result">98%</div>
            				<div class="result">61%</div>
            				<div class="result">94%</div>
            				<div class="result">85%</div>
            				<div class="result">95%</div>
            				<div class="result">68%</div>
            				<div class="result">79%</div>
            				<div class="result">98%</div>
            				<div class="result">95%</div>
            				<div class="result">81%</div>
            				<div class="result">94%</div>
            				<div class="result">92%</div>
            				<div class="result">87%</div>
            				<div class="result">88%</div>
            				<div class="result">82%</div>
            				<div class="result">95%</div>
            				<div class="result">83%</div>
            				<div class="result">87%</div>
            				<div class="result">62%</div>
            				<div class="result">75%</div>
            				<div class="result">83%</div>
            				<div class="result">92%</div>
            				<div class="result">74%</div>
            				<div class="result">57%</div>
            				<div class="result">92%</div>
            				<div class="result">92%</div>
            				<div class="result">87%</div>
            				<div class="result">83%</div>
            				<div class="result">53%</div>
            				<div class="result">93%</div>
            				<div class="result">85%</div>
            				<div class="result">59%</div>
            				<div class="result">37%</div>
            				<div class="result">86%</div>
            				<div class="result">77%</div>
            				<div class="result">18%</div>
            				<div class="result">79%</div>
            				<div class="result">98%</div>
            				<div class="result">91%</div>
            				<div class="result">61%</div>
            				<div class="result">91%</div>
            				<div class="result">93%</div>
            				<div class="result">83%</div>
            				<div class="result">78%</div>
            				<div class="result">94%</div>
            				<div class="result">95%</div>
            				<div class="result">88%</div>
            				<div class="result">67%</div>
            				<div class="result">95%</div>
            				<div class="result">94%</div>
            				<div class="result">91%</div>
            				<div class="result">84%</div>
            				<div class="result">88%</div>
            				<div class="result">97%</div>
            				<div class="result">99%</div>
            				<div class="result">97%</div>
            				<div class="result">95%</div>
            				<div class="result">73%</div>
            				<div class="result">96%</div>
            				<div class="result">88%</div>
            				<div class="result">86%</div>
            				<div class="result">97%</div>
            				<div class="result">76%</div>
            				<div class="result">97%</div>
            				<div class="result">83%</div>
            				<div class="result">64%</div>
            				<div class="result">86%</div>
            				<div class="result">93%</div>
            				<div class="result">37%</div>
            				<div class="result">97%</div>
            				<div class="result">98%</div>
            				<div class="result">91%</div>
            				<div class="result">95%</div>
            				<div class="result">81%</div>
            				<div class="result">93%</div>
            				<div class="result">90%</div>
            				<div class="result">90%</div>
            				<div class="result">67%</div>
            				<div class="result">94%</div>
            				<div class="result">92%</div>
            				<div class="result">3%</div>
            				<div class="result">98%</div>
            				<div class="result">69%</div>
            				<div class="result">93%</div>
            				<div class="result">83%</div>
            				<div class="result">75%</div>
            				<div class="result">93%</div>
            				<div class="result">65%</div>
            				<div class="result">93%</div>
            				<div class="result">37%</div>
            				<div class="result">90%</div>
            				<div class="result">93%</div>
            				<div class="result">72%</div>
            				<div class="result">75%</div>
            				<div class="result">18%</div>
            				<div class="result">87%</div>
            				<div class="result">95%</div>
            				<div class="result">87%</div>
            				<div class="result">95%</div>
            				<div class="result">75%</div>
            				<div class="result">3%</div>
            				<div class="result">51%</div>
            				<div class="result">93%</div>
            				<div class="result">97%</div>
            				<div class="result">87%</div>
            				<div class="result">69%</div>
            				<div class="result">11%</div>
            				<div class="result">49%</div>
            				<div class="result">94%</div>
            				<div class="result">87%</div>
            				<div class="result">77%</div>
            				<div class="result">92%</div>
            				<div class="result">96%</div>
            				<div class="result">94%</div>
            				<div class="result">86%</div>
            				<div class="result">91%</div>
            				<div class="result">77%</div>
            				<div class="result">66%</div>
            				<div class="result">69%</div>
            				<div class="result">82%</div>
            				<div class="result">96%</div>
            				<div class="result">97%</div>
            				<div class="result">98%</div>
            				<div class="result">64%</div>
            				<div class="result">95%</div>
            				<div class="result">41%</div>
            				<div class="result">75%</div>
            				<div class="result">75%</div>
            				<div class="result">75%</div>
            				<div class="result">75%</div>
            				<div class="result">83%</div>
            				<div class="result">77%</div>
            				<div class="result">76%</div>
            				<div class="result">79%</div>
            				<div class="result">94%</div>
            				<div class="result">80%</div>
            				<div class="result">54%</div>
            				<div class="result">96%</div>
            				<div class="result">68%</div>
            				<div class="result">96%</div>
            				<div class="result">94%</div>
            				<div class="result">71%</div>
            				<div class="result">81%</div>
            				<div class="result">89%</div>
            				<div class="result">97%</div>
            				<div class="result">66%</div>
            				<div class="result">50%</div>
            				<div class="result">87%</div>
            				<div class="result">83%</div>
            				<div class="result">85%</div>
            				<div class="result">93%</div>
            				<div class="result">38%</div>
            				<div class="result">71%</div>
            				<div class="result">69%</div>
            				<div class="result">98%</div>
            				<div class="result">74%</div>
            				<div class="result">97%</div>
            				<div class="result">92%</div>
            				<div class="result">88%</div>
            				<div class="result">75%</div>
            				<div class="result">75%</div>
            				<div class="result">50%</div>
            				<div class="result">69%</div>
            				<div class="result">68%</div>
            				<div class="result">94%</div>
            				<div class="result">72%</div>
            				<div class="result">95%</div>
            				<div class="result">94%</div>
            				<div class="result">81%</div>
            				<div class="result">37%</div>
            				<div class="result">60%</div>
            		</div>
		<div class="column-20-filter hide-on-mobile">
			<div class="label">OPLEIDINGSNIVEAU</div>
			<div class="label show-on-mobile"></div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">5</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">4</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">3</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">2</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">1</div>
            				<div class="result">0</div>
            		</div>
	</div>'''


soup = BeautifulSoup(data, 'html.parser')
results = []

for result in soup.find_all('div', class_='result'):
    a_tag = result.find('a', class_='bold-on-mobile')
    if a_tag:
        profession = a_tag.text.strip()
        url = a_tag['href']
        details_div = result.find('div', class_='show-on-mobile')
        if details_div:
            details = details_div.text.strip().split('\n')
            vacatures = int(details[0].split(': ')[1])
            robotiserings = int(details[1].split(': ')[1][:-1])
            opleidingsniveau = int(details[2].split(': ')[1])
            
            results.append({
                'profession': profession,
                'url': url,
                'vacatures': vacatures,
                'robotiserings': robotiserings,
                'opleidingsniveau': opleidingsniveau
            })

# Write data to CSV
with open('jobs.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Profession', 'URL', 'Vacatures', 'Robotiserings', 'Opleidingsniveau']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for result in results:
        writer.writerow({
            'Profession': result['profession'],
            'URL': result['url'],
            'Vacatures': result['vacatures'],
            'Robotiserings': result['robotiserings'],
            'Opleidingsniveau': result['opleidingsniveau']
        })

print('Data has been written to jobs.csv')