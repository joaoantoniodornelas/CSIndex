# -*- coding: utf-8 -*-
import pandas as pd
from flask import Flask, make_response, request
from constants import confsHeader, scoresHeader, teachersHeader, papersHeader

#Salvar um arquivo CSV
def saveCSV(df, fileName):
	response = make_response(df.to_csv(sep=',',encoding='utf-8',index=False,header=False))
	response.headers["Content-Disposition"] = "attachment; filename = " + fileName + ".csv"
	response.headers["Content-Type"] = "text/csv"
	return response

#Abrir um arquivo CSV
def openCSV(fileName, headers):
	df = pd.read_csv(fileName, names=headers)
	return df

##############- Publications section - ###################
#Número de publicações em uma determinada conferência de uma área
def num_publications_by_conference_in_area(areaName,conferenceName):
	try:
		df = openCSV('../data/'+ areaName +'-out-confs.csv', confsHeader)
		result = df.loc[df['ConferenceName']==conferenceName]
		result = result['NumPublications']
		return saveCSV(result, areaName +'-out-confs'), 200

	except IOError:
		return format("Atenção: O arquivo solicitado não existe"), 404

	except IndexError:
		return format("Atenção: Não foram encontrados resultados que atendem a seus parâmetros"), 422

#Número de publicações no conjunto de conferências de uma área
def num_publications_by_area(areaName):
	try:
		df = openCSV('../data/'+ areaName +'-out-confs.csv', confsHeader)
		result = pd.DataFrame([df['NumPublications'].sum()], columns=['sum'])
		return saveCSV(result, areaName +'-out-confs'), 200

	except IOError:
		return format("Atenção: O arquivo solicitado não existe"), 404

	except IndexError:
		return format("Atenção: Não foram encontrados resultados que atendem a seus parâmetros"), 422

##############- Score section - ###################
# #Scores de todos os departamentos em uma área
def department_scores(areaName):
	try:
		df = openCSV('../data/'+ areaName +'-out-scores.csv', scoresHeader)
		return saveCSV(df, areaName +'-out-scores'), 200

	except IOError:
		return format("Atenção: O arquivo solicitado não existe"), 404

	except IndexError:
		return format("Atenção: Não foram encontrados resultados que atendem a seus parâmetros"), 422

# #Score de um determinado departamento em uma área.
def department_score(areaName, departmentName):
	try:
		df = openCSV('../data/'+ areaName +'-out-scores.csv', scoresHeader)
		result = df.loc[df['DepartmentName']==departmentName]
		result = result['Score']
		return saveCSV(result, areaName +'-out-scores'), 200

	except IOError:
		return format("Atenção: O arquivo solicitado não existe"), 404

	except IndexError:
		return format("Atenção: Não foram encontrados resultados que atendem a seus parâmetros"), 422

##############- Teachers section - ###################
# #Número de professores que publicam em uma determinada área (organizados por departamentos)
def num_teachers_by_area(areaName):
	try:
		df = openCSV('../data/'+ areaName +'-out-profs.csv', teachersHeader)
		return saveCSV(df, areaName +'-out-profs'), 200

	except IOError:
		return format("Atenção: O arquivo solicitado não existe"), 404

	except IndexError:
		return format("Atenção: Não foram encontrados resultados que atendem a seus parâmetros"), 422

# #Número de professores de um determinado departamento que publicam em uma área
def num_teachers_in_department_by_area(areaName, departmentName):
	try:
		df = openCSV('../data/'+ areaName +'-out-profs.csv', teachersHeader)
		result = df.loc[df['DepartmentName']==departmentName]
		result = result['Quantity']
		return saveCSV(result, areaName +'-out-profs'), 200

	except IOError:
		return format("Atenção: O arquivo solicitado não existe"), 404

	except IndexError:
		return format("Atenção: Não foram encontrados resultados que atendem a seus parâmetros"), 422

##############- Papers section - ###################
# #Todos os papers de uma área (ano, título, deptos e autores)
def papers_by_area(areaName):
	try:
		df = openCSV('../data/'+ areaName +'-out-papers.csv', papersHeader)
		return saveCSV(df, areaName +'-out-papers'), 200

	except IOError:
		return format("Atenção: O arquivo solicitado não existe"), 404

	except IndexError:
		return format("Atenção: Não foram encontrados resultados que atendem a seus parâmetros"), 422

# #Todos os papers de uma área em um determinado ano
def papers_by_area_in_year(areaName, year):
	try:
		df = openCSV('../data/'+ areaName +'-out-papers.csv', papersHeader)
		result = df.loc[df['Year']==int(year)]
		return saveCSV(result, areaName +'-out-papers'), 200

	except IOError:
		return format("Atenção: O arquivo solicitado não existe"), 404

	except IndexError:
		return format("Atenção: Não foram encontrados resultados que atendem a seus parâmetros"), 422

# #Todos os papers de um departamento em uma área
def papers_by_department_in_area(areaName, departmentName):
	try:
		df = openCSV('../data/'+ areaName +'-out-papers.csv', papersHeader)
		result = df.loc[df['DepartmentName']==departmentName]
		return saveCSV(result, areaName +'-out-papers'), 200

	except IOError:
		return format("Atenção: O arquivo solicitado não existe"), 404

	except IndexError:
		return format("Atenção: Não foram encontrados resultados que atendem a seus parâmetros"), 422


# #Todos os papers de um professor (dado o seu nome)
def papers_by_teacher(teacherName):
	try:
		df = openCSV('../data/profs/search/'+ teacherName +'.csv', papersHeader)
		return saveCSV(df, teacherName +'-out-papers'), 200

	except IOError:
		return format("Atenção: O arquivo solicitado não existe"), 404

	except IndexError:
		return format("Atenção: Não foram encontrados resultados que atendem a seus parâmetros"), 422