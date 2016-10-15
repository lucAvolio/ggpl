from larlib import *

def buildStructure(pDistances, bDistances, pSection, bSection):
	
	(px,py) = pSection
	(bx,bz) = bSection

	#Build up pillars of given dimension
	pillarBasesList = []
	tmp = PROD([Q(px),Q(py)])
	for i in range(0, len(pDistances)):
		pillarBasesList.extend([tmp,T(2)(pDistances[i] + py)])
	pillarBasesList.extend([tmp])
	pillarBases = STRUCT(pillarBasesList)

	pillars = []
	for j in range(0, len(bDistances)):
		tmp = PROD([pillarBases, Q(bDistances[j])])
		pillars.extend([tmp,T(3)(bDistances[j] + bz)])
	pillars = STRUCT(pillars)

	

	#Build up beams of given dimension
	tmp = PROD([Q(bx),Q(bz)])
	beamBasesList = []
	prev = 0
	for i in range(0, len(bDistances)):
		beamBasesList.extend([T(2)(bDistances[i]+prev),tmp])
		prev = bz
	beamBases = STRUCT(beamBasesList)

	beams = []
	prev = py + py/2.0
	for j in range(0, len(pDistances)):
		tmp = PROD([beamBases,Q(-pDistances[j]-prev)])
		beams.extend([tmp,T(3)(-pDistances[j]-prev)])
		if(j == len(pDistances)-2):
			print(j, len(pDistances))
			prev = py+py/2.0
		else:
			prev = py


	beams = STRUCT(beams)
	beams = R([2,3])(PI/2.0)(beams)

	building = STRUCT([pillars,beams])

	return building


#Data
pillarDistances = [1, 2, 4, 3, 5, 2, 5]
beamDistances = [1, 1, 2, 6, 10, 5]
pillarSection = (0.5,1)
beamSection = (0.5,1)


s = buildStructure(pillarDistances, beamDistances, pillarSection, beamSection)
VIEW(s)